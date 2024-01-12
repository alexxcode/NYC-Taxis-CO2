import etl_alternative_fuel_vehicles as etl

def main():
    url = 'https://drive.google.com/uc?id=1p73YBd4tjQF2au4IAo99FY6nq-JJX2t-'
    bucket_name = 'us-west4-eduardopc-bcaeda57-bucket'
    raw_folder = 'Bases_raw/Alternative_Fuel_Vehicles'
    curated_folder = 'Bases_curadas/Alternative_Fuel_Vehicles'

    # Extracción
    data_raw = etl.extract_data(url)
    etl.load_data(data_raw, bucket_name, raw_folder, 'Alternative_Fuel_Vehicles_raw.csv')

    # Transformación
    data_transformed = etl.transform_data(data_raw)

    # Carga
    etl.load_data(data_transformed, bucket_name, curated_folder, 'Alternative_Fuel_Vehicles_transformados.csv')

if __name__ == "__main__":
    main()
