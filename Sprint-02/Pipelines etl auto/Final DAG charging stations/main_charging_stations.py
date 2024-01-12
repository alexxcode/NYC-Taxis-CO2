import etl_charging_stations as etl

def main():
    url = 'https://drive.google.com/uc?export=download&id=16fbavFKfcFqb85akQgFY1ED_gqqihwRf'
    bucket_name = 'us-west4-eduardopc-bcaeda57-bucket'
    raw_folder = 'Bases_raw/ChargingStations'
    curated_folder = 'Bases_curadas/ChargingStations'

    # Extracción y carga de datos en bruto
    datos = etl.cargar_datos(url)
    etl.guardar_datos(datos, bucket_name, raw_folder, 'ChargingStations_raw.csv')

    # Transformación
    df_transformado = etl.transformar_datos(datos)

    # Carga de datos transformados
    etl.guardar_datos(df_transformado, bucket_name, curated_folder, 'ChargingStations_curado.csv')

if __name__ == "__main__":
    main()
