from etl_taxis import *

def main():
    url = "https://www.nyc.gov/site/tlc/about/tlc-trip-record-data.page"
    bucket_name = 'nwy-bucket'
    raw_folder = 'Bases_raw/Taxis'

    bigquery_dataset='dataset_bd'
    bigquery_table='Taxis'

    # Extracción y carga de datos en bruto
    datos = cargar_datos(url)

    guardar_datos(datos, bucket_name, raw_folder, 'Taxis_raw.csv')

    # Transformación
    df_transformed = transform_data(datos)



    load_to_bigquery(df_transformed, bigquery_dataset, bigquery_table)


if __name__ == "__main__":
    main()
