import pandas as pd
import requests
from io import StringIO
from google.cloud import storage
from google.cloud import bigquery
import json

def create_directory_in_bucket(bucket_name, directory_name):
    storage_client = storage.Client()
    bucket = storage_client.bucket(bucket_name)
    blob = bucket.blob(directory_name + '/')
    blob.upload_from_string('', content_type='application/x-www-form-urlencoded;charset=UTF-8')

def extract_data(url):
    response = requests.get(url)
    if response.status_code == 200:
        return pd.read_csv(StringIO(response.content.decode('utf-8')))
    else:
        raise Exception(f"Error al descargar los datos: {response.status_code}")

def transform_data(df):
    df['name'] = df['Manufacturer'] + ' ' + df['Model']
    columns_to_drop = ["Notes", "Number of Passengers", "PHEV Total Range"]
    df = df.drop(columns=columns_to_drop)
    columns_to_fillna = ['Alternative Fuel Economy City', 'Alternative Fuel Economy Highway',
                         'Alternative Fuel Economy Combined', 'Conventional Fuel Economy City',
                         'Conventional Fuel Economy Highway', 'Conventional Fuel Economy Combined']
    df[columns_to_fillna] = df[columns_to_fillna].fillna(0).astype(int)
    int_columns = ['Alternative Fuel Economy City', 'Alternative Fuel Economy Highway',
                   'Alternative Fuel Economy Combined', 'Conventional Fuel Economy City',
                   'Conventional Fuel Economy Highway', 'Conventional Fuel Economy Combined']
    df[int_columns] = df[int_columns].astype(int)
    df.columns = df.columns.str.lower().str.replace(' ', '_')
    return df

def load_data(df, bucket_name, directory_name, file_name):
    create_directory_in_bucket(bucket_name, directory_name)
    storage_client = storage.Client()
    bucket = storage_client.bucket(bucket_name)
    blob = bucket.blob(f"{directory_name}/{file_name}")
    blob.upload_from_string(df.to_csv(index=False), content_type='text/csv')





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

