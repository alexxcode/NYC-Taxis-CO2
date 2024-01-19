from etl_vehiculos import  *
import pandas as pd

def main():
    url = 'https://drive.google.com/uc?id=1TO-oi55hcf4FbBHWFhvIMsaLhdA1jLLs'
    bucket_name = 'nwy-bucket'
    raw_folder = 'Bases_raw/Vehicles'
 
    bigquery_dataset='dataset_bd'
    bigquery_table='Vehicles'

    # Extracción y carga de datos en bruto
    data_raw = descargar_y_cargar_datos(url)
    upload_to_bucket(data_raw, bucket_name, raw_folder, 'Vehicles_raw.csv')

    # Transformación
    data_transformed = transformar_datos(data_raw)

    # Predicción SARIMA
    # pivot_data = data_transformed.pivot_table(index='state', columns='year', values=['Auto', 'Bus', 'Truck', 'Motorcycle'], aggfunc='sum')
    # for vehicle_type in ['Auto', 'Bus', 'Truck', 'Motorcycle']:
    #     pivot_vehicle = pivot_data[vehicle_type]
    #     predicted_data = predict_vehicle_type_sarima(pivot_vehicle, vehicle_type)
    #     upload_to_bucket(predicted_data, bucket_name, curated_folder, f'Vehicles_{vehicle_type}_pred.csv')

    # move to query
    load_to_bigquery(data_transformed, bigquery_dataset, bigquery_table)


if __name__ == "__main__":
    main()
