from etl_ruido import *

def main():

    bucket_name = 'nwy-bucket'
    raw_folder = 'Bases_raw/Ruido'
  

    bigquery_dataset='dataset_bd'
    bigquery_table='Noise'

    # Extracción
    df_raw = extract_data()

    # Carga de datos en bruto
    upload_to_bucket(df_raw, bucket_name, raw_folder, 'Ruido_raw.csv')

    # Transformación
    df_transformed = transform_data(df_raw)

    # Carga de datos transformados
    #upload_to_bucket(df_transformed, bucket_name, curated_folder, 'Ruido_curado.csv')

    load_to_bigquery(df_transformed, bigquery_dataset, bigquery_table)

if __name__ == "__main__":
    main()

