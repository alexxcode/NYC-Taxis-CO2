import pandas as pd
import hashlib
import requests
import io
from google.cloud import storage

def calcular_hash(data):
    # Calcular el hash MD5 de los datos
    md5_hash = hashlib.md5()
    md5_hash.update(data.encode())
    return md5_hash.hexdigest()

def descargar_datos_si_necesario(bucket_name='us-west4-eduardopc-bcaeda57-bucket'):
    storage_client = storage.Client()
    bucket = storage_client.bucket(bucket_name)
    blob = bucket.blob('datos_descargados.csv')

    if blob.exists():
        # Calcular el hash del archivo existente en el bucket
        existing_blob_data = blob.download_as_text()
        existing_blob_hash = calcular_hash(existing_blob_data)
    else:
        existing_blob_hash = None

    # Realizar la solicitud para descargar los datos
    csv_url = 'https://citsci-noise-server.ornith.cornell.edu/noise/download/csv?lang=en'
    response_csv = requests.get(csv_url)

    if response_csv.status_code == 200:
        csv_data = response_csv.text
        new_blob_hash = calcular_hash(csv_data)

        if existing_blob_hash != new_blob_hash:
            # Si los hashes son diferentes, descargar y cargar los datos
            df = pd.read_csv(io.StringIO(csv_data))
            csv_data = df.to_csv(index=False)
            blob.upload_from_string(csv_data, 'text/csv')
            print("Datos descargados y cargados en el bucket.")
        else:
            print("Los datos en el bucket son los mismos que en la fuente. No es necesario descargarlos nuevamente.")
    else:
        raise Exception("Error al descargar los datos")

    return blob

def transformar_datos(df):
    # Convertir a datetime
    df['Start date/time in UTC'] = pd.to_datetime(df['Start date/time in UTC'])
    df['Start date UTC'] = df['Start date/time in UTC'].dt.normalize()
    df['Start time UTC'] = df['Start date/time in UTC'].dt.time

    # Cambio en la especificación de la zona horaria
    df['Timezone'] = df['Timezone'].str.replace('America/New_York', 'New York')

    # Filtrado y renombramiento
    df = df[df['Timezone'] == 'New York']
    df = df.rename(columns={'Emoji descriptions':'Noise_Source'})
    df['Mood_scale'] = df['Mood'].apply(lambda Mood: "Extremely Happy" if Mood == 1 else 
                                        "Happy" if Mood == 2 else 
                                        "Neutral" if Mood == 3 else 
                                        "Somewhat Sad" if Mood == 4 else 
                                        "Very Sad" if Mood == 5 else "Unknown")
    df.drop(['Emoji', 'Mood'], axis=1, inplace=True)
    df['Nominated as noise refuge'] = df['Nominated as noise refuge'].fillna(False)

    # Tipo de datos
    df = df.astype({'Duration (s)': int, 'Observer ID': int, 
                    'Latitude': float, 'Longitude': float, 
                    'Mean volume (dBA)': int, 
                    'Could control noise exposure': bool, 
                    'Indoors': bool, 'Nominated as noise refuge': bool})

    # Nuevas columnas de tiempo
    df['timestamp'] = pd.to_datetime(df['Start date/time in UTC'])
    df['hour_of_day'] = df['timestamp'].dt.hour
    df['day_of_month'] = df['timestamp'].dt.day
    df['month'] = df['timestamp'].dt.month
    df['day_of_week'] = df['timestamp'].dt.dayofweek + 1

    return df

def cargar_datos(df, nombre_archivo='ruido.csv', bucket_name='us-west4-eduardopc-bcaeda57-bucket'):
    storage_client = storage.Client()
    bucket = storage_client.bucket(bucket_name)
    blob = bucket.blob(nombre_archivo)
    csv_data = df.to_csv(index=False)
    blob.upload_from_string(csv_data, 'text/csv')

