import etl_taxi_zones as etl

def main():
    url = 'https://drive.google.com/uc?id=14cnXFjTL_SzUhgfE95TySVqBAAQksvVl'
    bucket_name = 'us-west4-eduardopc-bcaeda57-bucket'
    raw_folder = 'Bases_raw/TaxiZones'
    curated_folder = 'Bases_curadas/TaxiZones'

    # Extracción
    datos = etl.cargar_datos(url)

    # Carga de datos en bruto
    etl.guardar_datos(datos, bucket_name, raw_folder, 'TaxiZones_raw.csv')

    # Transformación
    df_transformado = etl.transformar_datos(datos)

    # Carga de datos transformados
    etl.guardar_datos(df_transformado, bucket_name, curated_folder, 'TaxiZones_curado.csv')

if __name__ == "__main__":
    main()
