import etl_taxi_zones as etl

def main():
    url = 'https://drive.google.com/uc?id=14cnXFjTL_SzUhgfE95TySVqBAAQksvVl'
    bucket_name = 'nwy-bucket'
    raw_folder = 'Bases_raw/TaxiZones'
  
    bigquery_dataset='dataset_bd'
    bigquery_table='TaxiZones'

    # Extracción
    datos = etl.cargar_datos(url)

    # Carga de datos en bruto
    etl.guardar_datos(datos, bucket_name, raw_folder, 'TaxiZones_raw.csv')

    # Transformación
    df_transformado = etl.transformar_datos(datos)

    # move to query
    etl.load_to_bigquery(df_transformado, bigquery_dataset, bigquery_table)

if __name__ == "__main__":
    main()
