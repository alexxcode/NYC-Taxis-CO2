from fastapi import FastAPI
from funciones_fc_yellow import calculate_co2_reduction, calculate_noise_reduction, calculate_cost_savings

app = FastAPI()

@app.get("/co2_reduction", summary="Calcula la reducción en la emision de CO2 (g) por Borough según porcentaje de cambio. Taxi-Yellow")
def get_co2_reduction(year: int, month: int, change_percentage: float):
    """Calcula la reducción de CO2 para un año y mes específicos. Valores posibles 2023-6 a 2024-5 ."""
    return calculate_co2_reduction(year, month, change_percentage)

@app.get("/noise_reduction", summary="Calcula la reducción de volumen de ruido (db)) por Borough según porcentaje de cambio. Taxi-Yellow")
def get_noise_reduction(year: int, month: int, change_percentage: float):
    """Calcula la reducción de ruido para un año y mes específicos. Valores posibles 2023-6 a 2024-5."""
    return calculate_noise_reduction(year, month, change_percentage)

@app.get("/cost_savings", summary="Calcula el ahorro en costos anuales de gasolina por Borough según porcentaje de cambio. Taxi-Yellow")
def get_cost_savings(year: int, month: int, change_percentage: float):
    """Calcula el ahorro en costos para un año y mes específicos. Valores posibles 2023-6 a 2024-5."""
    return calculate_cost_savings(year, month, change_percentage)

if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8000)
