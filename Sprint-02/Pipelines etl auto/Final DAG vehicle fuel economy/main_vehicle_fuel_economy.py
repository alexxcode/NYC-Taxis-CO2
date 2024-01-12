import etl_vehicle_fuel_economy as etl

def main():
    url = 'https://drive.google.com/uc?export=download&id=1tEsF-bZYqqBM2gjcHxdbzVeip-90wHFM'
    bucket_name = 'us-west4-eduardopc-bcaeda57-bucket'
    raw_folder = 'Bases_raw/VehicleFuelEconomy'
    curated_folder = 'Bases_curadas/VehicleFuelEconomy'

    # Extracción y carga de datos en bruto
    datos = etl.cargar_datos(url)
    etl.guardar_datos(datos, bucket_name, raw_folder, 'VehicleFuelEconomy_raw.csv')

    # Transformación
    df_transformado = etl.transformar_datos(datos)

    # Carga de datos transformados
    etl.guardar_datos(df_transformado, bucket_name, curated_folder, 'VehicleFuelEconomy_curado.csv')

if __name__ == "__main__":
    main()
