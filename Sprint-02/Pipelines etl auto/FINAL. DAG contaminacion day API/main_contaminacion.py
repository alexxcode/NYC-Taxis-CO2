# main_contaminacion.py
from etl_contaminacion import extract_data, transform_data, aggregate_monthly_with_boroughs, upload_to_bucket
from datetime import datetime
from google.cloud import storage

def create_gcs_directory(bucket_name, directory_name):
    """Crea un 'directorio' en un bucket de Google Cloud Storage."""
    storage_client = storage.Client()
    bucket = storage_client.bucket(bucket_name)

    # Crear un objeto Blob con un nombre de ruta que termine en '/'
    directory_path = directory_name if directory_name.endswith('/') else directory_name + '/'
    blob = bucket.blob(directory_path)

    # Subir un objeto vacío, lo que crea un 'directorio'
    blob.upload_from_string('')

create_gcs_directory('us-west4-eduardopc-bcaeda57-bucket', 'Bases_raw/contaminacion/')
create_gcs_directory('us-west4-eduardopc-bcaeda57-bucket', 'Bases_curadas/contaminacion/')

# Parámetros de la API y zonas
api_key = 'e49a90e730e178434b65ddc9689cbf9d'
zones_names = [
    'Upper East Side, Manhattan', 'Williamsburg, Brooklyn', 'Astoria, Queens', 
    'Riverdale, Bronx', 'St. George, Staten Island'
]
start_date = '2020-11-27'
end_date = datetime.now().date().strftime("%Y-%m-%d")

# Nombre del bucket y carpetas de destino
bucket_name = 'us-west4-eduardopc-bcaeda57-bucket'
raw_folder = 'Bases_raw/contaminacion'
curated_folder = 'Bases_curadas/contaminacion'

# Extracción
df_raw = extract_data(api_key, zones_names, start_date, end_date)

# Carga de los datos en bruto
upload_to_bucket(df_raw, bucket_name, raw_folder, 'datos_contaminacion_raw.csv')

# Transformación y agregación
df_transformed = transform_data(df_raw)
df_monthly = aggregate_monthly_with_boroughs(df_transformed)

# Carga de los datos transformados
upload_to_bucket(df_monthly, bucket_name, curated_folder, 'datos_contaminacion_curados.csv')
