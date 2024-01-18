import etl_light_duty_vehicles as etl

def main():
    url = 'https://drive.google.com/uc?id=18hzPaVttvyo8QyuC-jVSrN1-jkCnCIpW'
    bucket_name = 'nwy-bucket'
    raw_folder = 'Bases_raw/Light_Duty_Vehicles'
    
    bigquery_dataset='dataset_bd'
    bigquery_table='Light_Duty_Vehicles'

    # Extracción
    data_raw = etl.extract_data(url)
    etl.load_data(data_raw, bucket_name, raw_folder, 'Light_Duty_Vehicles_raw.csv')

    # Transformación
    data_transformed = etl.transform_data(data_raw)

    # Carga
    etl.load_to_bigquery(data_transformed, bigquery_dataset, bigquery_table)



if __name__ == "__main__":
    main()
