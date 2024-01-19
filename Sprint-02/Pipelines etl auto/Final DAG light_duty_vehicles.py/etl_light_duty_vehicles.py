import pandas as pd
import requests
from io import StringIO
from google.cloud import storage

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
    df.columns = df.columns.str.lower().str.replace(' ', '_')
    selected_columns = ['vehicle_id', 'fuel_id', 'fuel_configuration_id', 'manufacturer_id',
                        'category_id', 'model', 'model_year', 'alternative_fuel_economy_city',
                        'alternative_fuel_economy_highway', 'alternative_fuel_economy_combined',
                        'conventional_fuel_economy_city', 'conventional_fuel_economy_highway',
                        'conventional_fuel_economy_combined', 'engine_cylinder_count']
    df = df[selected_columns]
    df = df.dropna(subset=['fuel_configuration_id'])
    columns_with_nulls = ['alternative_fuel_economy_city', 'alternative_fuel_economy_highway',
                          'alternative_fuel_economy_combined', 'conventional_fuel_economy_city',
                          'conventional_fuel_economy_highway', 'conventional_fuel_economy_combined',
                          'engine_cylinder_count']
    df[columns_with_nulls] = df[columns_with_nulls].fillna(0).astype(int)
    integer_columns = ['fuel_configuration_id', 'alternative_fuel_economy_city',
                       'alternative_fuel_economy_highway', 'alternative_fuel_economy_combined',
                       'conventional_fuel_economy_city', 'conventional_fuel_economy_highway',
                       'conventional_fuel_economy_combined', 'engine_cylinder_count']
    df[integer_columns] = df[integer_columns].astype(int)
    return df

def load_data(df, bucket_name, directory_name, file_name):
    create_directory_in_bucket(bucket_name, directory_name)
    storage_client = storage.Client()
    bucket = storage_client.bucket(bucket_name)
    blob = bucket.blob(f"{directory_name}/{file_name}")
    blob.upload_from_string(df.to_csv(index=False), content_type='text/csv')