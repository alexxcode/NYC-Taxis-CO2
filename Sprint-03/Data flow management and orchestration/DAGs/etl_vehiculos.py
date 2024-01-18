import requests
import pandas as pd
import io
from google.cloud import storage
#import statsmodels.api as sm
#from statsmodels.tsa.stattools import adfuller
from google.cloud import bigquery

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

# def predict_vehicle_type_sarima(data, vehicle_type):
#     predictions = {}
#     for state in data.index:
#         state_data = data.loc[state].dropna()
#         if len(state_data) > 2:
#             diff_state_data = state_data.diff().dropna()
#             result_diff = adfuller(diff_state_data)
#             if result_diff[1] < 0.05:
#                 model = sm.tsa.statespace.SARIMAX(state_data, 
#                                                   order=(1, 1, 1), 
#                                                   seasonal_order=(1, 1, 1, 12),
#                                                   enforce_stationarity=False, 
#                                                   enforce_invertibility=False)
#                 results = model.fit(disp=False)
#                 forecast = results.get_forecast(steps=2).predicted_mean
#                 predictions[state] = {2019: forecast.iloc[0], 2020: forecast.iloc[1]}
#             else:
#                 predictions[state] = {2019: None, 2020: None}
#         else:
#             predictions[state] = {2019: None, 2020: None}
#     return pd.DataFrame(predictions).T


def upload_to_bucket(df, bucket_name, directory_name, file_name):
    create_directory_in_bucket(bucket_name, directory_name)
    storage_client = storage.Client()
    bucket = storage_client.bucket(bucket_name)
    blob = bucket.blob(f"{directory_name}/{file_name}")
    blob.upload_from_string(df.to_csv(index=False), content_type='text/csv')

def load_to_bigquery(df, dataset_name, table_name):

    client = bigquery.Client()
    table_ref = client.dataset(dataset_name).table(table_name)

    job_config = bigquery.LoadJobConfig(
        write_disposition="WRITE_TRUNCATE",  # Reemplaza la tabla si ya existe
        autodetect=True  # Detecta automáticamente los esquemas de las columnas
    )

    job = client.load_table_from_dataframe(df, table_ref, job_config=job_config)

    try:
        job.result()  # Espera a que finalice el trabajo de carga
        print(f"Datos cargados en BigQuery en la tabla {table_ref.path}")
    except Exception as e:
        print(f"Error al cargar los datos: {e}")