import requests
import pandas as pd
import io
from google.cloud import storage

def create_directory_in_bucket(bucket_name, directory_name):
    storage_client = storage.Client()
    bucket = storage_client.bucket(bucket_name)
    blob = bucket.blob(directory_name + '/')
    blob.upload_from_string('', content_type='application/x-www-form-urlencoded;charset=UTF-8')

def cargar_datos(url):
    response = requests.get(url, stream=True)
    if response.status_code == 200:
        data = pd.read_csv(io.BytesIO(response.content), encoding='utf-8')
        return data
    else:
        raise Exception(f"Error al descargar el archivo CSV: {response.status_code}")

def transformar_datos(df):
    df.columns = df.columns.str.lower().str.replace(' ', '_')
    return df

def guardar_datos(df, bucket_name, directory_name, file_name):
    create_directory_in_bucket(bucket_name, directory_name)
    storage_client = storage.Client()
    bucket = storage_client.bucket(bucket_name)
    blob = bucket.blob(f"{directory_name}/{file_name}")
    blob.upload_from_string(df.to_csv(index=False), 'text/csv')
