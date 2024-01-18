import etl_vehicle_fuel_economy as etl

def main():
    url = 'https://drive.google.com/uc?export=download&id=1tEsF-bZYqqBM2gjcHxdbzVeip-90wHFM'
    bucket_name = 'nwy-bucket'
    raw_folder = 'Bases_raw/VehicleFuelEconomy'
    
    bigquery_dataset='dataset_bd'
    bigquery_table='VehicleFuelEconomy'

    # Extracción y carga de datos en bruto
    datos = etl.cargar_datos(url)
    etl.guardar_datos(datos, bucket_name, raw_folder, 'VehicleFuelEconomy_raw.csv')

    # Transformación
    df_transformado = etl.transformar_datos(datos)

    # Carga de datos transformados

    etl.load_to_bigquery(df_transformado, bigquery_dataset, bigquery_table)

if __name__ == "__main__":
    main()
