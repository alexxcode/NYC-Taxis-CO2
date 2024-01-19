# main_contaminacion.py
from etl_contaminacion import *
from datetime import datetime
from google.cloud import storage


def main():

    bucket_name = 'nwy-bucket'
    raw_folder = 'Bases_raw/contaminacion'
    bigquery_dataset='dataset_bd'
    bigquery_table='contaminacion_monthly'


    create_gcs_directory(bucket_name, 'Bases_raw/contaminacion/')

    # Parámetros de la API y zonas
    api_key = 'e49a90e730e178434b65ddc9689cbf9d'
    zones_names = [
        'Upper East Side, Manhattan', 'Williamsburg, Brooklyn', 'Astoria, Queens', 
        'Riverdale, Bronx', 'St. George, Staten Island'
    ]
    start_date = '2020-11-27'
    end_date = datetime.now().date().strftime("%Y-%m-%d")


    # Extracción
    df_raw = extract_data(api_key, zones_names, start_date, end_date)

    # Carga de los datos en bruto
    upload_to_bucket(df_raw, bucket_name, raw_folder, 'datos_contaminacion_raw.csv')

    # Transformación y agregación
    df_transformed = transform_data(df_raw)
    df_monthly = aggregate_monthly_with_boroughs(df_transformed)

    # Carga de los datos transformados
    load_to_bigquery(df_monthly, bigquery_dataset, bigquery_table)


if __name__ == "__main__":
    main()