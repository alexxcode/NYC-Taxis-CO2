import pandas as pd
import statsmodels.api as sm
import os

# ETL - Extracción
def extract_data(file_path):
    return pd.read_excel(file_path)

# ETL - Transformación
def transform_data(data):
    data['Es_Electrico'] = (data['Fuel'] == 'Electric').astype(int)
    data['Vehicle Type'] = data['Vehicle Type'].replace({'Sedán': 'Sedan'})
    
    vehicle_types = ['Minivan', 'Pick-up', 'SUV', 'Sedan']
    for v_type in vehicle_types:
        data[f'Vehicle Type_{v_type}'] = (data['Vehicle Type'] == v_type).astype(int)
    
    X = data[['Es_Electrico', 'Year', 'Base Price (USD)', 'Range (mi)'] + [f'Vehicle Type_{v_type}' for v_type in vehicle_types]]
    X = sm.add_constant(X)
    
    y_emisiones = data['CO2 Emissions (g/mi)']
    y_ruido = data['Sound Emission (dB)']
    
    modelo_emisiones_stats_robust = sm.OLS(y_emisiones, X).fit(cov_type='HC3')
    modelo_ruido_stats_robust = sm.OLS(y_ruido, X).fit(cov_type='HC3')
    
    return modelo_emisiones_stats_robust, modelo_ruido_stats_robust

# ETL - Carga
def load_results(output_dir, modelo_emisiones_stats, modelo_ruido_stats):
    if not os.path.exists(output_dir):
        os.makedirs(output_dir)
    
    def model_results_to_df(model_results):
        params = model_results.params
        std_err = model_results.bse
        p_values = model_results.pvalues

        df = pd.DataFrame({
            'Coef': params,
            'Std Err': std_err,
            'P>|t|': p_values
        })

        df['Significativo'] = df['P>|t|'] < 0.05

        return df

    df_emisiones = model_results_to_df(modelo_emisiones_stats)
    df_ruido = model_results_to_df(modelo_ruido_stats)

    emisiones_csv_path = f'{output_dir}/regresion_edmunds_emisiones.csv'
    ruido_csv_path = f'{output_dir}/regresion_edmunds_ruido.csv'

    df_emisiones.to_csv(emisiones_csv_path)
    df_ruido.to_csv(ruido_csv_path)

    return emisiones_csv_path, ruido_csv_path

# Extracción de datos
data = extract_data("edmunds_data.xlsx")

# Transformación de datos y cálculo de modelos
modelo_emisiones_stats, modelo_ruido_stats = transform_data(data)

# Carga de resultados
output_dir = 'Bases_api/modelo_electricoVsgasolina_edmunds'
emisiones_csv_path, ruido_csv_path = load_results(output_dir, modelo_emisiones_stats, modelo_ruido_stats)

# Visualización de rutas de archivos finales
print("Ruta del archivo de emisiones:", emisiones_csv_path)
print("Ruta del archivo de ruido:", ruido_csv_path)
