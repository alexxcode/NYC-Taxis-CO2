import etl_charging_stations as etl

def main():
    url = 'https://drive.google.com/uc?export=download&id=16fbavFKfcFqb85akQgFY1ED_gqqihwRf'
    bucket_name = 'nwy-bucket'
    raw_folder = 'Bases_raw/ChargingStations'
    curated_folder = 'Bases_curadas/ChargingStations'

    bigquery_dataset='dataset_bd'
    bigquery_table='ChargingStations'

    # Extracción y carga de datos en bruto
    datos = etl.cargar_datos(url)
    etl.guardar_datos(datos, bucket_name, raw_folder, 'ChargingStations_raw.csv')

    # Transformación
    df_transformado = etl.transformar_datos(datos)

    # move to query
    etl.load_to_bigquery(df_transformado, bigquery_dataset, bigquery_table)

if __name__ == "__main__":
    main()
    
