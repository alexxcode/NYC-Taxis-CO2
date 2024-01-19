import pandas as pd

# Rutas de los archivos CSV
ruta_emisiones = 'Bases_api/modelo_electricoVsgasolina_edmunds/regresion_edmunds_emisiones.csv'
ruta_ruido = 'Bases_api/modelo_electricoVsgasolina_edmunds/regresion_edmunds_ruido.csv'

# Función para cargar los datos
def cargar_datos_emisiones():
    return pd.read_csv(ruta_emisiones)

def cargar_datos_ruido():
    return pd.read_csv(ruta_ruido)

# Función para buscar información de coeficientes
def buscar_coeficiente(df, nombre_coeficiente):
    resultado = df[df['variable'] == nombre_coeficiente]
    if not resultado.empty:
        return resultado.iloc[0].to_dict()
    else:
        return None

# Variables globales para almacenar los datos cargados
datos_emisiones = cargar_datos_emisiones()
datos_ruido = cargar_datos_ruido()
