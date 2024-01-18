from etl_contaminacion_historico import *
from google.cloud import storage

def create_gcs_directory(bucket_name, directory_name):
    storage_client = storage.Client()
    bucket = storage_client.bucket(bucket_name)
    directory_path = directory_name if directory_name.endswith('/') else directory_name + '/'
    blob = bucket.blob(directory_path)
    if not blob.exists():
        blob.upload_from_string('')

def main():

    bucket_name = 'nwy-bucket'
   
    bigquery_dataset='dataset_bd'
    bigquery_table='contaminacion_historico'

    base_url = 'https://aqs.epa.gov/aqsweb/airdata/download_files.html'
   
    raw_folder = 'Bases_raw/contaminacion_historico'
    processed_folder = 'Bases_processed/contaminacion_historico'


    create_gcs_directory(bucket_name, raw_folder)
    create_gcs_directory(bucket_name, processed_folder)


    scrape_and_download(base_url, bucket_name)
    transformed_data = transform_data(bucket_name, processed_folder)


    load_to_bigquery(transformed_data, bigquery_dataset, bigquery_table)

if __name__ == "__main__":
    main()
