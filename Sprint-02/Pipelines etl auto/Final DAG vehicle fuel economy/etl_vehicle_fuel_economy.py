import requests
import pandas as pd
import io
import numpy as np
from google.cloud import storage

def create_directory_in_bucket(bucket_name, directory_name):
    storage_client = storage.Client()
    bucket = storage_client.bucket(bucket_name)
    blob = bucket.blob(directory_name + '/')
    blob.upload_from_string('', content_type='application/x-www-form-urlencoded;charset=UTF-8')

def cargar_datos(url):
    response = requests.get(url)
    if response.status_code == 200:
        csv_content = io.StringIO(response.text)
        data = pd.read_csv(csv_content)
        return data
    else:
        raise Exception(f"Error al descargar los datos: {response.status_code}")

def transformar_datos(df):
    df.insert(0, 'ID', range(1, len(df) + 1))
    selected_columns = ['guzzler', 'combA08U', 'lv2', 'trany', 'co2', 'UHighway', 'rangeCity', 'fuelType1', 'Model', 'ID', 'cityE', 'sCharger', 'combE', 'tCharger', 'cityA08', 'Year', 'co2A', 'trans_dscr', 'cityCD', 'youSaveSpend', 'phevBlended', 'fuelType2', 'range', 'ghgScore', 'cylinders', 'city08', 'rangeHwy', 'fuelCostA08', 'phevComb', 'VClass', 'drive', 'comb08U', 'Manufacturer', 'pv2', 'UCity', 'createdOn', 'atvType', 'fuelCost08']
    df = df[selected_columns]

    columns_to_convert = ['Model', 'fuelType1', 'fuelType2', 'drive', 'VClass', 'phevBlended', 'guzzler']
    for column in columns_to_convert:
        df[column] = df[column].astype(str)

    df['Manufacturer'] = df['Manufacturer'].replace('General Motors', 'GMC')
    df.loc[df['fuelType2'] == 'Electricity', 'co2A'] = 0
    columns_to_replace_zero_with_nan = ['co2', 'co2A', 'ghgScore', 'range', 'rangeCity', 'rangeHwy', 'cityA08', 'cityCD', 'cityE', 'combE', 'comb08U', 'combA08U', 'fuelCostA08', 'lv2', 'pv2', 'phevComb']
    df[columns_to_replace_zero_with_nan] = df[columns_to_replace_zero_with_nan].replace(0, np.nan)

    return df

def guardar_datos(df, bucket_name, directory_name, file_name):
    create_directory_in_bucket(bucket_name, directory_name)
    storage_client = storage.Client()
    bucket = storage_client.bucket(bucket_name)
    blob = bucket.blob(f"{directory_name}/{file_name}")
    blob.upload_from_string(df.to_csv(index=False), 'text/csv')
