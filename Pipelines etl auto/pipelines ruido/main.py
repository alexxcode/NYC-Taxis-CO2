from etl import descargar_datos_si_necesario, transformar_datos, cargar_datos

def main():
    # Llamar a la función para descargar o verificar los datos
    datos_blob = descargar_datos_si_necesario()

    # Extraer el contenido del blob (archivo CSV) si es necesario
    csv_data = datos_blob.download_as_text()
    
    # 2. Transformación
    try:
        datos_transformados = transformar_datos(pd.read_csv(io.StringIO(csv_data)))
        print("Datos transformados con éxito.")
    except Exception as e:
        print(f"Error en la transformación: {e}")
        return

    # 3. Carga
    try:
        cargar_datos(datos_transformados, 'ruido.csv', 'us-west4-eduardopc-bcaeda57-bucket')
        print("Datos cargados con éxito en 'ruido.csv' en el bucket 'us-west4-eduardopc-bcaeda57-bucket'.")
    except Exception as e:
        print(f"Error en la carga: {e}")
        return

    # 4. Ejecución del modelo ARIMA
    try:
        # Tu código para el modelo ARIMA aquí (puedes importarlo desde otro archivo si es necesario)
        print("Modelo ARIMA ejecutado con éxito.")
    except Exception as e:
        print(f"Error en el modelo ARIMA: {e}")
        return

# Llamar al método principal
if __name__ == "__main__":
    main()
