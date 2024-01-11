import requests
import pandas as pd
import io
from google.cloud import storage

def create_directory_in_bucket(bucket_name, directory_name):
    storage_client = storage.Client()
    bucket = storage_client.bucket(bucket_name)
    blob = bucket.blob(directory_name + '/')
    blob.upload_from_string('', content_type='application/x-www-form-urlencoded;charset=UTF-8')

def extract_data():
    csv_url = 'https://citsci-noise-server.ornith.cornell.edu/noise/download/csv?lang=en'
    response = requests.get(csv_url)
    if response.status_code == 200:
        csv_content = io.StringIO(response.text)
        df = pd.read_csv(csv_content)
        return df
    else:
        raise Exception("Error al descargar los datos")

def transform_data(df):
    df['Start date/time in UTC'] = pd.to_datetime(df['Start date/time in UTC'])
    df['Start date UTC'] = df['Start date/time in UTC'].dt.normalize()
    df['Start time UTC'] = df['Start date/time in UTC'].dt.time
    df['Timezone'] = df['Timezone'].str.replace('America/New_York', 'New York')
    df = df[df['Timezone'] == 'New York']
    df = df.rename(columns={'Emoji descriptions':'Noise_Source'})
    df['Mood_scale'] = df['Mood'].apply(lambda x: {1: "Extremely Happy", 2: "Happy", 3: "Neutral", 4: "Somewhat Sad", 5: "Very Sad"}.get(x, "Unknown"))
    df = df[(df['Noise_Source'].str.contains('taxi')) | (df['Noise_Source'].str.contains('automobile'))]
    df = df.sort_values(by='Start date/time in UTC', ascending=False).reset_index(drop=True)
    df.drop(['Emoji', 'Noise_Source', 'Mood'], axis=1, inplace=True)
    df['Nominated as noise refuge'] = df['Nominated as noise refuge'].fillna(False)
    df['Start date/time in UTC'] = pd.to_datetime(df['Start date/time in UTC'])
    df['Start date UTC'] = pd.to_datetime(df['Start date UTC'])
    df['Start time UTC'] = pd.to_datetime(df['Start time UTC'], format='%H:%M:%S').dt.time
    df['Duration (s)'] = df['Duration (s)'].astype(int)
    df['Observer ID'] = df['Observer ID'].astype(int)
    df['Latitude'] = df['Latitude'].astype(float)
    df['Longitude'] = df['Longitude'].astype(float)
    df['Mean volume (dBA)'] = df['Mean volume (dBA)'].astype(int)
    df['Could control noise exposure'] = df['Could control noise exposure'].astype(bool)
    df['Indoors'] = df['Indoors'].astype(bool)
    df['Nominated as noise refuge'] = df['Nominated as noise refuge'].astype(bool)
    df['timestamp'] = pd.to_datetime(df['Start date/time in UTC'])
    df['hour_of_day'] = df['timestamp'].dt.hour
    df['day_of_month'] = df['timestamp'].dt.day
    df['month'] = df['timestamp'].dt.month
    df['day_of_week'] = df['timestamp'].dt.dayofweek + 1
    return df

def upload_to_bucket(df, bucket_name, directory_name, file_name):
    create_directory_in_bucket(bucket_name, directory_name)
    storage_client = storage.Client()
    bucket = storage_client.bucket(bucket_name)
    blob = bucket.blob(f"{directory_name}/{file_name}")
    blob.upload_from_string(df.to_csv(index=False), content_type='text/csv')
