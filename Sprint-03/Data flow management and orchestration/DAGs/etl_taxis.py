import pandas as pd
import requests
from bs4 import BeautifulSoup
from google.cloud import storage
from google.cloud import bigquery
import io


def create_directory_in_bucket(bucket_name, directory_name):
    storage_client = storage.Client()
    bucket = storage_client.bucket(bucket_name)
    blob = bucket.blob(directory_name + '/')
    blob.upload_from_string('', content_type='application/x-www-form-urlencoded;charset=UTF-8')

def download_parquet_links(links_list):
    # Create a variable to store the links
    parquet_links = links_list

    return parquet_links



def cargar_datos(url):   
    response = requests.get(url)
    
    if response.status_code == 200:
        soup = BeautifulSoup(response.content, "html.parser") # Contenido de la pagina
        parquet_files = [] 

        selected_years = ['2021', '2022', '2023'] 
         

        for link in soup.find_all('a',href=True): # Busco todos los elementos que sean links
         if link['href'].endswith('.parquet'): # Si el elemento termina en .parquet, añado el elemento a la lista parquet_files
            if any(year in link['href'] for year in selected_years):
                parquet_files.append(link['href'])

        yellow_taxis = []
        green_taxis = []
        #fhv_taxis = []
       # fhvhv_taxis = []

        for link in parquet_files:
            if 'yellow_tripdata' in link: # Todos los links que contengan 'yellow_tripdata' en su texto
                yellow_taxis.append(link)
            elif 'green_tripdata' in link: # Todos los links que contengan 'green_tripdata' en su texto
                green_taxis.append(link)
         #   elif 'fhv_tripdata' in link: # Todos los links que contengan 'fhv_tripdata' en su texto
          #      fhv_taxis.append(link)
          #  elif 'fhvhv_tripdata' in link: # Todos los links que contengan 'fhvhv_tripdata' en su texto
           #     fhvhv_taxis.append(link)

        yellow_taxis = sorted(yellow_taxis, reverse=True)
        green_taxis = sorted(green_taxis, reverse=True)
      #  fhv_taxis = sorted(fhv_taxis, reverse=True)
      #  fhvhv_taxis = sorted(fhvhv_taxis, reverse=True)


        # Define variables to store the links
        yellow_links = download_parquet_links(yellow_taxis)
        green_links = download_parquet_links(green_taxis)
      #  fhv_links = download_parquet_links(fhv_taxis)
      #  fhvhv_links = download_parquet_links(fhvhv_taxis)

        # Read the parquet files
        taxi1 = pd.read_parquet(yellow_links[-1])
        taxi1['kind'] = 'yellow'

        taxi2 = pd.read_parquet(green_links[-1])
        taxi2['kind'] = 'green'

      #  taxi3 = pd.read_parquet(fhv_links[-1])
      #  taxi3['kind'] = 'yellow'

       # taxi4 = pd.read_parquet(fhvhv_links[-1])
      #  taxi4['kind'] = 'green'


        dftaxis= pd.concat([taxi1, taxi2 ], ignore_index=True) #taxi3, taxi4

        return dftaxis
    else:
        raise Exception(f"Error al descargar los datos: {response.status_code}")
    
def guardar_datos(df, bucket_name, directory_name, file_name):
    create_directory_in_bucket(bucket_name, directory_name)
    storage_client = storage.Client()
    bucket = storage_client.bucket(bucket_name)
    blob = bucket.blob(f"{directory_name}/{file_name}")
    blob.upload_from_string(df.to_csv(index=False), 'text/csv')

def listar_boroughs_y_locationIDs(df):
    # Filtrar el conjunto de datos para incluir solo las filas que corresponden a los cinco distritos.
    boroughs = ['Bronx', 'Brooklyn', 'Manhattan', 'Queens', 'Staten Island', 'EWR']
    df = df[df['borough'].isin(boroughs)]

    # Agrupar los datos por distrito y crear una lista de los valores únicos en la columna LocationID para cada distrito.
    borough_to_locationIDs = {}
    for borough in boroughs:
        locationIDs = df[df['borough'] == borough]['locationid'].unique().tolist()
        borough_to_locationIDs[borough] = locationIDs

    return borough_to_locationIDs

def transform_data(df):

    columnas_eliminar = ["airport_fee","congestion_surcharge",
                     "improvement_surcharge","tolls_amount","mta_tax","extra","store_and_fwd_flag"]
    df = df.drop(columnas_eliminar,axis=1)
    
    from google.cloud import bigquery

    # Establecer las variables de entorno para el proyecto y el conjunto de datos de BigQuery.
    project_id = "nyc-taxis-co2"
    dataset_id = "dataset_bd"
    table_id = "TaxiZones"

    # Crear un cliente de BigQuery.
    client = bigquery.Client()

    # Leer la tabla de BigQuery.
    dfzone = client.query("SELECT * FROM `{}.{}.{}`".format(project_id, dataset_id, table_id)).to_dataframe()

    borough_to_locationIDs = listar_boroughs_y_locationIDs(dfzone)

    # Mapear los valores de las columnas PULocationID y DOLocationID a los distritos correspondientes
    borough_to_locationIDs = listar_boroughs_y_locationIDs(dfzone)
    locationID_to_borough = {}
    for borough, locationIDs in borough_to_locationIDs.items():
        for locationID in locationIDs:
            locationID_to_borough[locationID] = borough

    # Agregar una nueva columna al dataframe que contenga los nombres de los distritos correspondientes a los valores de PULocationID y DOLocationID
    df['borough'] = df.apply(lambda row: locationID_to_borough.get(row['PULocationID'], 'Unknown'), axis=1)

    


    return df


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