import pandas as pd
from pathlib import Path

# Obtener la ruta del directorio actual
current_dir = Path(__file__).parent

# Construir las rutas de los archivos CSV
predicted_co2_yellow_path = current_dir / 'predicted_co2_emissions_yellow_paraPowerBi.csv'
predicted_noise_yellow_path = current_dir / 'predicted_noise_yellow_paraPowerBi.csv'
predicted_ahorro_yellow_path = current_dir / 'predict_ahorro_yellow_PowerBi.csv'

# Cargar los archivos CSV
predicted_co2_yellow = pd.read_csv(predicted_co2_yellow_path)
predicted_noise_yellow = pd.read_csv(predicted_noise_yellow_path)
predicted_ahorro_yellow = pd.read_csv(predicted_ahorro_yellow_path)

def is_valid_date(year, month):
    return 2023 <= year <= 2024 and (year != 2024 or month <= 5)

def should_exclude_borough(borough):
    return borough in ['Unknown', 'EWR']

def format_result(row):
    return {
        "Predicted": round(row['Predicted'], 2),
        "Reducted": round(row['Reducted'], 2),
        "Difference": round(row['Difference'], 2)
    }

def calculate_co2_reduction(year, month, change_percentage):
    if not is_valid_date(year, month):
        return {"error": "Invalid date. Only data from 2023-06 to 2024-05 is available."}

    df_filtered = predicted_co2_yellow[(predicted_co2_yellow['year'] == year) & (predicted_co2_yellow['month'] == month)]
    df_filtered = df_filtered[~df_filtered['borough'].apply(should_exclude_borough)]
    change_factor = change_percentage / 100
    df_filtered['Reducted'] = df_filtered['predicted_co2_emissions'] * (1 - change_factor)
    df_filtered['Difference'] = df_filtered['predicted_co2_emissions'] - df_filtered['Reducted']
    df_filtered['Predicted'] = df_filtered['predicted_co2_emissions']
    return {row['borough']: format_result(row) for _, row in df_filtered.iterrows()}

def calculate_noise_reduction(year, month, change_percentage):
    if not is_valid_date(year, month):
        return {"error": "Invalid date. Only data from 2023-06 to 2024-05 is available."}

    df_filtered = predicted_noise_yellow[(predicted_noise_yellow['year'] == year) & (predicted_noise_yellow['month'] == month)]
    df_filtered = df_filtered[~df_filtered['borough'].apply(should_exclude_borough)]
    change_factor = change_percentage / 100
    df_filtered['Reducted'] = df_filtered['predicted_noise'] * (1 - change_factor)
    df_filtered['Difference'] = df_filtered['predicted_noise'] - df_filtered['Reducted']
    df_filtered['Predicted'] = df_filtered['predicted_noise']
    return {row['borough']: format_result(row) for _, row in df_filtered.iterrows()}

def calculate_cost_savings(year, month, change_percentage, efficiency_index=1/3):
    if not is_valid_date(year, month):
        return {"error": "Invalid date. Only data from 2023-06 to 2024-05 is available."}

    df_filtered = predicted_ahorro_yellow[(predicted_ahorro_yellow['year'] == year) & (predicted_ahorro_yellow['month'] == month)]
    df_filtered = df_filtered[~df_filtered['borough'].apply(should_exclude_borough)]
    change_factor = change_percentage / 100
    df_filtered['Reducted'] = df_filtered['predicted_cost'] - (abs(df_filtered['predicted_cost'] * change_factor) / efficiency_index)
    df_filtered['Difference'] = df_filtered['predicted_cost'] - df_filtered['Reducted']
    df_filtered['Predicted'] = df_filtered['predicted_cost']
    return {row['borough']: format_result(row) for _, row in df_filtered.iterrows()}
