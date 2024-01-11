# etl_vehiculos.py

import requests
import pandas as pd
import io
from google.cloud import storage
import statsmodels.api as sm
from statsmodels.tsa.stattools import adfuller

def create_directory_in_bucket(bucket_name, directory_name):
    storage_client = storage.Client()
    bucket = storage_client.bucket(bucket_name)
    blob = bucket.blob(directory_name + '/')
    blob.upload_from_string('', content_type='application/x-www-form-urlencoded;charset=UTF-8')

def descargar_y_cargar_datos(url):
    response = requests.get(url)
    if response.status_code == 200:
        csv_content = io.StringIO(response.text)
        data = pd.read_csv(csv_content)
        return data
    else:
        raise Exception("Error al descargar los datos")

def transformar_datos(data):
    data_since_1980 = data[data['year'] >= 1980]
    data_since_1980['year'].replace({2017: 1917}, inplace=True)
    return data_since_1980

def predict_vehicle_type_sarima(data, vehicle_type):
    predictions = []
    for state in data.index:
        state_data = data.loc[state].dropna()
        if len(state_data) > 2:
            diff_state_data = state_data.diff().dropna()
            result_diff = adfuller(diff_state_data)
            if result_diff[1] < 0.05:
                model = sm.tsa.statespace.SARIMAX(state_data, 
                                                  order=(1, 1, 1), 
                                                  seasonal_order=(1, 1, 1, 12),
                                                  enforce_stationarity=False, 
                                                  enforce_invertibility=False)
                results = model.fit(disp=False)
                forecast = results.get_forecast(steps=2).predicted_mean
                for year, value in zip([2019, 2020], forecast):
                    predictions.append({'state': state, 'year': year, vehicle_type: value})
            else:
                for year in [2019, 2020]:
                    predictions.append({'state': state, 'year': year, vehicle_type: None})
        else:
            for year in [2019, 2020]:
                predictions.append({'state': state, 'year': year, vehicle_type: None})
    return pd.DataFrame(predictions)

def upload_to_bucket(df, bucket_name, directory_name, file_name):
    create_directory_in_bucket(bucket_name, directory_name)
    storage_client = storage.Client()
    bucket = storage_client.bucket(bucket_name)
    blob = bucket.blob(f"{directory_name}/{file_name}")
    blob.upload_from_string(df.to_csv(index=False), content_type='text/csv')

def integrate_predictions(transformed_data, predicted_data):
    integrated_data = pd.merge(transformed_data, predicted_data, on=['state', 'year'], how='left')
    return integrated_data
