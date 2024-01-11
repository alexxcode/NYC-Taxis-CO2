from etl_ruido import extract_data, transform_data, upload_to_bucket

def main():
    bucket_name = 'us-west4-eduardopc-bcaeda57-bucket'
    raw_folder = 'Bases_raw/Ruido'
    curated_folder = 'Bases_curadas/Ruido'

    # Extracción
    df_raw = extract_data()

    # Carga de datos en bruto
    upload_to_bucket(df_raw, bucket_name, raw_folder, 'Ruido_raw.csv')

    # Transformación
    df_transformed = transform_data(df_raw)

    # Carga de datos transformados
    upload_to_bucket(df_transformed, bucket_name, curated_folder, 'Ruido_curado.csv')

if __name__ == "__main__":
    main()
