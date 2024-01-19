import etl_electric_cars as etl

def main():
    url = 'https://drive.google.com/uc?export=download&id=1upo7PZvkAo-ryNKxYgeUT48Ovycpkmkt'
    bucket_name = 'us-west4-eduardopc-bcaeda57-bucket'
    raw_folder = 'Bases_raw/ElectricCars'
    curated_folder = 'Bases_curadas/ElectricCars'

    # Extracción
    datos = etl.cargar_datos(url)

    # Carga de datos en bruto
    etl.guardar_datos(datos, bucket_name, raw_folder, 'ElectricCars_raw.csv')

    # Transformación
    df_transformado = etl.transformar_datos(datos)

    # Carga de datos transformados
    etl.guardar_datos(df_transformado, bucket_name, curated_folder, 'ElectricCars_curado.csv')

if __name__ == "__main__":
    main()