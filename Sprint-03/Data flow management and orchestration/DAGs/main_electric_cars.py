import etl_electric_cars as etl

def main():
    url = 'https://drive.google.com/uc?export=download&id=1upo7PZvkAo-ryNKxYgeUT48Ovycpkmkt'
    bucket_name = 'nwy-bucket'
    raw_folder = 'Bases_raw/ElectricCars'

    bigquery_dataset='dataset_bd'
    bigquery_table='ElectricCars'

    # Extracción
    datos = etl.cargar_datos(url)

    # Carga de datos en bruto
    etl.guardar_datos(datos, bucket_name, raw_folder, 'ElectricCars_raw.csv')

    # Transformación
    df_transformado = etl.transformar_datos(datos)

    # move to query
    etl.load_to_bigquery(df_transformado, bigquery_dataset, bigquery_table)

if __name__ == "__main__":
    main()
