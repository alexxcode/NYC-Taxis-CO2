from etl_contaminacion_historico import scrape_and_download, transform_data, save_transformed_data
from google.cloud import storage

def create_gcs_directory(bucket_name, directory_name):
    storage_client = storage.Client()
    bucket = storage_client.bucket(bucket_name)
    directory_path = directory_name if directory_name.endswith('/') else directory_name + '/'
    blob = bucket.blob(directory_path)
    if not blob.exists():
        blob.upload_from_string('')

def main():
    base_url = 'https://aqs.epa.gov/aqsweb/airdata/download_files.html'
    bucket_name = 'us-west4-eduardopc-bcaeda57-bucket'
    raw_folder = 'Bases_raw/contaminacion_historico'
    processed_folder = 'Bases_processed/contaminacion_historico'
    curated_folder = 'Bases_curadas/contaminacion_historico'
    output_filename = "pollution_year_state.csv"

    create_gcs_directory(bucket_name, raw_folder)
    create_gcs_directory(bucket_name, processed_folder)
    create_gcs_directory(bucket_name, curated_folder)

    scrape_and_download(base_url, bucket_name)
    transformed_data = transform_data(bucket_name, processed_folder)
    save_transformed_data(transformed_data, bucket_name, curated_folder, output_filename)

if __name__ == "__main__":
    main()
