import pandas as pd
import requests
import zipfile
from urllib.parse import urljoin
from bs4 import BeautifulSoup
from google.cloud import storage
from google.cloud import bigquery
import io


def download_file(url, bucket, blob_path):
    response = requests.get(url, stream=True)
    if response.status_code == 200:
        blob = bucket.blob(blob_path)
        blob.upload_from_string(response.content)
    return blob_path

def unzip_blob(blob, bucket, extraction_folder):
    zipbytes = io.BytesIO(blob.download_as_bytes())
    with zipfile.ZipFile(zipbytes, 'r') as zip_ref:
        for zip_info in zip_ref.infolist():
            if zip_info.filename.endswith('.csv'):
                destination_blob_path = f"{extraction_folder}/{zip_info.filename}"
                destination_blob = bucket.blob(destination_blob_path)
                destination_blob.upload_from_string(zip_ref.read(zip_info))


def scrape_and_download(base_url, bucket_name, start_year=2000, 
                        raw_folder='Bases_raw/contaminacion_historico', 
                        processed_folder='Bases_processed/contaminacion_historico'):
    storage_client = storage.Client()
    bucket = storage_client.bucket(bucket_name)

    response = requests.get(base_url)
    soup = BeautifulSoup(response.text, 'html.parser')
    links = soup.find_all('a')

    for link in links:
        href = link.get('href')
        if href and 'annual_conc_by_monitor' in href and href.endswith('.zip'):
            year = href.split('_')[-1].split('.')[0]
            try:
                year = int(year)
                if year >= start_year:
                    download_url = urljoin(base_url, href)
                    zip_blob_path = f'{raw_folder}/{href}'
                    if not bucket.blob(zip_blob_path).exists():
                        print(f'Descargando y almacenando {href} en el bucket...')
                        download_file(download_url, bucket, zip_blob_path)
                        zip_blob = bucket.blob(zip_blob_path)
                        unzip_blob(zip_blob, bucket, processed_folder)
            except ValueError:
                pass

def transform_data(bucket_name, processed_folder):
    storage_client = storage.Client()
    bucket = storage_client.bucket(bucket_name)

    columns_to_keep = {
        'State Name': str, 'County Name': str, 'City Name': str, 
        'Date of Last Change': 'datetime64', 'Latitude': float, 'Longitude': float, 
        'Parameter Name': str, 'Metric Used': str, 'Year': int, 
        'Units of Measure': str, 'Arithmetic Mean': float
    }

    dfs = []
    blobs = bucket.list_blobs(prefix=processed_folder)
    for blob in blobs:
        if blob.name.endswith('.csv'):
            df = pd.read_csv(io.BytesIO(blob.download_as_bytes()))

            # Mantener solo las columnas necesarias y formatear los datos
            df = df[list(columns_to_keep.keys())]
            for column, dtype in columns_to_keep.items():
                df[column] = df[column].astype(dtype, errors='ignore')

            # Filtrar y colapsar el DataFrame
            filtered_df = df[(df['Parameter Name'].isin(["PM2.5 - Local Conditions", "Ozone"])) & (df['Metric Used'] == "Observed Values")]
            collapsed_df = filtered_df.pivot_table(
                index=['Year', 'State Name'],
                columns='Parameter Name',
                values='Arithmetic Mean',
                aggfunc='mean'
            ).reset_index()
            collapsed_df.columns.name = None
            collapsed_df = collapsed_df.rename(columns={"PM2.5 - Local Conditions": "PM2_5 Mean", "Ozone": "Ozone Mean"})
            dfs.append(collapsed_df)

    combined_df = pd.concat(dfs, ignore_index=True)
    return combined_df

def save_transformed_data(data, bucket_name, curated_folder, file_name):
    storage_client = storage.Client()
    bucket = storage_client.bucket(bucket_name)
    blob = bucket.blob(f'{curated_folder}/{file_name}')
    blob.upload_from_string(data.to_csv(index=False), 'text/csv')

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
        