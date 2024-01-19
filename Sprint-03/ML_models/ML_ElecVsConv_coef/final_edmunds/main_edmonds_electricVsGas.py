from fastapi import FastAPI, HTTPException
import apifunctions_edmonds as fe
import uvicorn

app = FastAPI()

@app.get("/emisiones/{coeficiente}")
def obtener_emisiones(coeficiente: str):
    resultado = fe.buscar_coeficiente(fe.datos_emisiones, coeficiente)
    if resultado:
        return resultado
    else:
        raise HTTPException(status_code=404, detail="Coeficiente no encontrado")

@app.get("/ruido/{coeficiente}")
def obtener_ruido(coeficiente: str):
    resultado = fe.buscar_coeficiente(fe.datos_ruido, coeficiente)
    if resultado:
        return resultado
    else:
        raise HTTPException(status_code=404, detail="Coeficiente no encontrado")
#definir el puerto en el que se va a escuchar la api
if __name__ == "__main__":
    uvicorn.run(app, host="0.0.0.0", port=8000)