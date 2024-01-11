# main_vehiculos.py

import etl_vehiculos as etl

def main():
    url = 'https://drive.google.com/uc?id=1TO-oi55hcf4FbBHWFhvIMsaLhdA1jLLs'
    bucket_name = 'us-west4-eduardopc-bcaeda57-bucket'
    raw_folder = 'Bases_raw/Vehiculos'
    curated_folder = 'Bases_curadas/Vehiculos'

    # Extracción y carga de datos en bruto
    data_raw = etl.descargar_y_cargar_datos(url)
    etl.upload_to_bucket(data_raw, bucket_name, raw_folder, 'Vehiculos_raw.csv')

    # Transformación
    data_transformed = etl.transformar_datos(data_raw)

    # Predicción e integración
    pivot_data = data_transformed.pivot_table(index='state', columns='year', values=['Auto', 'Bus', 'Truck', 'Motorcycle'], aggfunc='sum')
    for vehicle_type in ['Auto', 'Bus', 'Truck', 'Motorcycle']:
        pivot_vehicle = pivot_data[vehicle_type]
        predicted_data = etl.predict_vehicle_type_sarima(pivot_vehicle, vehicle_type)
        
        # Integra las predicciones
        integrated_data = etl.integrate_predictions(data_transformed, predicted_data)

        # Carga los datos integrados al bucket
        etl.upload_to_bucket(integrated_data, bucket_name, curated_folder, f'Vehiculos_{vehicle_type}_integrated.csv')

if __name__ == "__main__":
    main()
