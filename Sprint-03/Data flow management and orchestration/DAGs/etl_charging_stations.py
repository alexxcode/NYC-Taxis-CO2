import requests
import pandas as pd
import io
from google.cloud import storage
from google.cloud import bigquery


def create_directory_in_bucket(bucket_name, directory_name):
    storage_client = storage.Client()
    bucket = storage_client.bucket(bucket_name)
    blob = bucket.blob(directory_name + '/')
    blob.upload_from_string('', content_type='application/x-www-form-urlencoded;charset=UTF-8')

def cargar_datos(url):
    response = requests.get(url)
    if response.status_code == 200:
        csv_content = io.StringIO(response.text)
        data = pd.read_csv(csv_content, low_memory=False)
        return data
    else:
        raise Exception(f"Error al descargar los datos: {response.status_code}")

def transformar_datos(dataset):
    df = dataset[["Fuel Type Code", "Street Address", "City", "State", "Status Code", "Groups With Access Code", "Access Days Time", "BD Blends", "NG Fill Type Code", "NG PSI", "Latitude", "Longitude", "Open Date", "NG Vehicle Class", "E85 Blender Pump", "EV Connector Types", "CNG Storage Capacity"]]
    df.loc[:, 'Open Date'] = pd.to_datetime(df['Open Date'], errors='coerce')
    df.loc[:, 'Open Year'] = df['Open Date'].dt.year
    df.columns = df.columns.str.lower().str.replace(' ', '_')
    return df



def guardar_datos(df, bucket_name, directory_name, file_name):
    create_directory_in_bucket(bucket_name, directory_name)
    storage_client = storage.Client()
    bucket = storage_client.bucket(bucket_name)
    blob = bucket.blob(f"{directory_name}/{file_name}")
    blob.upload_from_string(df.to_csv(index=False), 'text/csv')

def load_to_bigquery(df, dataset_name, table_name):

    client = bigquery.Client()
    table_ref = client.dataset(dataset_name).table(table_name)

    job_config = bigquery.LoadJobConfig(
        write_disposition="WRITE_TRUNCATE",  # Reemplaza la tabla si ya existe
        autodetect=True  # Detecta automáticamente los esquemas de las columnas
    )

    job = client.load_table_from_dataframe(df, table_ref, job_config=job_config)

    try:
        job.result()  # Espera a que finalice el trabajo de carga
        print(f"Datos cargados en BigQuery en la tabla {table_ref.path}")
    except Exception as e:
        print(f"Error al cargar los datos: {e}")