# etl_contaminacion.py
import requests
from datetime import datetime
from geopy.geocoders import Nominatim
import pandas as pd
from google.cloud import storage

def extract_data(api_key, zones_names, start_date, end_date):
    geolocator = Nominatim(user_agent="my_geocoder", timeout=10)
    start_date_datetime = datetime.strptime(start_date, "%Y-%m-%d")
    start_date_unix = int(start_date_datetime.timestamp())
    end_date_datetime = datetime.strptime(end_date, "%Y-%m-%d")
    end_date_unix = int(end_date_datetime.timestamp())
    dfs = []

    for zone in zones_names:
        location = geolocator.geocode(f"{zone}, New York, USA")
        if location:
            lat, lon = location.latitude, location.longitude
            url = f"http://api.openweathermap.org/data/2.5/air_pollution/history?lat={lat}&lon={lon}&start={start_date_unix}&end={end_date_unix}&appid={api_key}"
            response = requests.get(url)
            data = response.json()

            clean_data = {'date': [], 'co': [], 'pm2.5': [], 'pm10': [], 'zone': []}
            for entry in data['list']:
                clean_data['date'].append(datetime.fromtimestamp(entry['dt']).strftime('%Y-%m-%d %H:%M:%S'))
                clean_data['co'].append(entry['components']['co'])
                clean_data['pm2.5'].append(entry['components']['pm2_5'])
                clean_data['pm10'].append(entry['components']['pm10'])
                clean_data['zone'].append(zone)

            df = pd.DataFrame(clean_data)
            dfs.append(df)
        else:
            print(f"No se pudo encontrar la ubicación para {zone}")

    df_final = pd.concat(dfs, ignore_index=True)
    return df_final

def transform_data(df):
    df['co'] = pd.to_numeric(df['co'], errors='coerce')
    df['pm2.5'] = pd.to_numeric(df['pm2.5'], errors='coerce')

    borough_mapping = {
        'Upper East Side, Manhattan': 'Manhattan',
        'Williamsburg, Brooklyn': 'Brooklyn',
        'Astoria, Queens': 'Queens',
        'Riverdale, Bronx': 'Bronx',
        'St. George, Staten Island': 'Staten Island'
    }
    df['borough'] = df['zone'].map(borough_mapping)
    df.drop('zone', axis=1, inplace=True)

    return df

def aggregate_monthly_with_boroughs(df):
    df['date'] = pd.to_datetime(df['date'])
    df.set_index('date', inplace=True)
    df_monthly = df.groupby(['borough', pd.Grouper(freq='MS')])[['co', 'pm2.5', 'pm10']].mean().reset_index()

    return df_monthly

def upload_to_bucket(df, bucket_name, destination_folder, file_name):
    storage_client = storage.Client()
    bucket = storage_client.bucket(bucket_name)
    blob = bucket.blob(f"{destination_folder}/{file_name}")
    
    # Convertir el DataFrame a un archivo CSV en memoria
    output = df.to_csv(index=False)
    
    # Subir el archivo al bucket de Cloud Storage
    blob.upload_from_string(output, content_type='text/csv')
    print(f"Archivo {file_name} cargado en {destination_folder} del bucket {bucket_name}.")
