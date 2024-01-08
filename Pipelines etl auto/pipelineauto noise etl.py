import requests
import pandas as pd
import io
from google.cloud import storage

def extract_data(url):
    response = requests.get(url)
    if response.status_code == 200:
        return io.StringIO(response.text)
    else:
        raise Exception("Error al descargar los datos")

def transform_data(csv_content):
    df = pd.read_csv(csv_content)

    # Transformaciones básicas
    df['Start date/time in UTC'] = pd.to_datetime(df['Start date/time in UTC'])
    df['Start date UTC'] = df['Start date/time in UTC'].dt.normalize()
    df['Start time UTC'] = df['Start date/time in UTC'].dt.time
    df['Timezone'] = df['Timezone'].str.replace('America/New_York', 'New York')
    df = df[df['Timezone'] == 'New York']

    # Mapeo de Mood a nombres descriptivos
    def best_name(Mood):
        mood_map = {
            1: "Extremely Happy",
            2: "Happy",
            3: "Neutral",
            4: "Somewhat Sad",
            5: "Very Sad"
        }
        return mood_map.get(Mood, "Unknown")

    df['Mood_scale'] = df['Mood'].apply(best_name)
    df['Noise_Source'] = df['Emoji descriptions']  # Renombrar columna para consistencia
    df = df[(df['Noise_Source'].str.contains('taxi')) | (df['Noise_Source'].str.contains('automobile'))]
    df = df.sort_values(by='Start date/time in UTC', ascending=False).reset_index(drop=True)

    # Transformaciones adicionales para alinearse con el segundo script
    df.drop(['Emoji', 'Noise_Source', 'Mood'], axis=1, inplace=True)
    df['Nominated as noise refuge'] = df['Nominated as noise refuge'].fillna(False)
    df['Could control noise exposure'] = df['Could control noise exposure'].astype(bool)
    df['Indoors'] = df['Indoors'].astype(bool)
    df['Nominated as noise refuge'] = df['Nominated as noise refuge'].astype(bool)
    df['Duration (s)'] = df['Duration (s)'].astype(int)
    df['Observer ID'] = df['Observer ID'].astype(int)
    df['Latitude'] = df['Latitude'].astype(float)
    df['Longitude'] = df['Longitude'].astype(float)
    df['Mean volume (dBA)'] = df['Mean volume (dBA)'].astype(float)

    # Añadiendo columnas de tiempo adicionales
    df['hour_of_day'] = df['Start date/time in UTC'].dt.hour
    df['day_of_month'] = df['Start date/time in UTC'].dt.day
    df['month'] = df['Start date/time in UTC'].dt.month
    df['day_of_week'] = df['Start date/time in UTC'].dt.dayofweek + 1

    return df

def load_to_gcp(df, bucket_name, destination_blob_name):
    storage_client = storage.Client()
    bucket = storage_client.bucket(bucket_name)
    csv_data = df.to_csv(index=False)
    blob = bucket.blob(destination_blob_name)
    blob.upload_from_string(csv_data, 'text/csv')

def main():
    URL = "https://citsci-noise-server.ornith.cornell.edu/noise/download/csv?lang=en"
    BUCKET_NAME = "your_gcp_bucket_name"
    DESTINATION_BLOB_NAME = "your_destination_blob_name.csv"

    try:
        csv_content = extract_data(URL)
        transformed_data = transform_data(csv_content)
        load_to_gcp(transformed_data, BUCKET_NAME, DESTINATION_BLOB_NAME)
        print("ETL completado con éxito y cargado en GCP")
    except Exception as e:
        print(f"Error en el pipeline ETL: {e}")

if __name__ == "__main__":
    main()
