import etl_light_duty_vehicles as etl

def main():
    url = 'https://drive.google.com/uc?id=18hzPaVttvyo8QyuC-jVSrN1-jkCnCIpW'
    bucket_name = 'us-west4-eduardopc-bcaeda57-bucket'
    raw_folder = 'Bases_raw/Light_Duty_Vehicles'
    curated_folder = 'Bases_curadas/Light_Duty_Vehicles'

    # Extracción
    data_raw = etl.extract_data(url)
    etl.load_data(data_raw, bucket_name, raw_folder, 'Light_Duty_Vehicles_raw.csv')

    # Transformación
    data_transformed = etl.transform_data(data_raw)

    # Carga
    etl.load_data(data_transformed, bucket_name, curated_folder, 'Light_Duty_Vehicles_transformados.csv')

if __name__ == "__main__":
    main()
