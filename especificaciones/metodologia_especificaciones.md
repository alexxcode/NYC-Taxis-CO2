## 9.  Objetivos de trabajo especificos seguidos para lograr los entregables propuestos 

### 1. Automatizar la Extracción, la limpieza y la carga de datos para la creación de una estructura de datos que permita conexiones hacia el tablero interactivo y el modelo de ML. 

### 2. Pronosticar el volumen de emisiones de CO2, de Ruido y el gasto esperado.
**Objetivo**: Medir la potencial reducción en las emisiones de CO2, de volumen de ruido y de gasto.
- **Variables**:
  - **Emisiones de CO2**: Medidas en toneladas de CO2 emitidas anualmente por cada tipo de vehículo.
  - **Consumo de Combustible**: Cantidad de combustible consumido por los vehículos convencionales, medido en litros o galones por año.
  - **Consumo de Electricidad**: Cantidad de electricidad consumida por los vehículos eléctricos, medida en kilovatios-hora (kWh) por año.
  - **Eficiencia del Combustible**: Kilómetros por litro para vehículos convencionales o kilómetros por kWh para vehículos eléctricos.
- **Metodología**:
  - **Recopilación de Datos**: Obtendremos datos sobre emisiones de CO2, consumo de combustible y electricidad de fuentes confiables, incluyendo registros de flotas de vehículos y bases de datos ambientales.
  - **Análisis Exploratorio de Datos (EDA)**: Realizaremos un EDA para entender la distribución, tendencias y correlaciones entre las variables.
  - **Construcción del Modelo pronostico**: Utilizaremos Python y sus librerías de análisis de datos, como Pandas y Scikit-learn, para construir un modelo de series de tiempo. Este modelo nos permitirá entender cómo el tipo de vehículo (eléctrico o convencional) y su eficiencia influencian las emisiones de CO2, de ruido y de gasto. y pronosticar el cambio al modificar la flota en un 20% hacia coches electricos

### 3. Análisis de Datos de Taxis Existentes (TLC Trip Records)

#### Objetivo:
- Identificar patrones y tendencias en los datos de viajes de taxis existentes.

#### Variables:

- Fecha y hora de recogida y entrega.
- Demanda de taxi durante horas pico.
- Distancia promedio de los viajes.
- Estructura de tarifas y rentabilidad.
- Zonas de alta demanda.

#### Metodología :

- Diversos análisis estadisticos 

### 4. Evaluación de la Viabilidad de Vehículos Eléctricos
#### Objetivo:
* Evaluar la viabilidad económica y operativa de la transición a vehículos eléctricos en la flota de taxis.

#### Variables:

* Rendimiento (consumo de combustible por milla).
* Distancia promedio de los viajes de taxis.
* gastos en combustible
* Impacto ambiental.

#### Metodología :

- Rendimiento:

Comparar el consumo de combustible por milla entre vehiculos electricos y convencionales

- Análisis de Costos Operativos:

Comparación de los costos de combustible de los vehículos convencionales frente a los eléctricos.

- Impacto Ambiental:

Calcularemos la reducción potencial en emisiones de CO2 y otros contaminantes con la adopción de vehículos eléctricos.


### 5. Análisis de Tráfico y Contaminación
- Objetivo: Establecer la correlación entre la actividad de taxis/viajes compartidos y los niveles de contaminación en NYC.
- Datos: taxi+_zone_lookup.csv, datos adicionales de calidad del aire y contaminación sonora.
- Metodología
* Mapeo de Rutas:
Utilizaremos herramientas GIS para analizar y visualizar rutas y densidades de taxis y viajes compartidos en NYC, aprovechando los datos geoespaciales de taxi_zones.dbf y taxi+_zone_lookup.csv.
Esto permitirá identificar áreas con alta concentración de tráfico de taxis y su posible relación con niveles de contaminación.
* Correlación y Regresión Estadística:
Utilizando Python y librerías como Pandas, NumPy y Scikit-learn, realizaremos análisis de regresión lineal integrando variables como el número de viajes (extraídos de taxi+_zone_lookup.csv), emisiones de contaminantes (derivados de Vehicle Fuel Economy Data.csv, ElectricCarData_Clean.csv, Light Duty Vehicles.csv)  niveles de ruido.
* Visualización de Datos:
Crearemos visualizaciones interactivas utilizando herramientas como Matplotlib, Seaborn o incluso Google Data Studio para presentar nuestros hallazgos de manera clara y comprensible.

- KPI Asociado
Porcentaje de Reducción en Emisiones de CO2: Calcularemos este KPI utilizando la fórmula ((Emisiones de CO2 en el año base - Emisiones de CO2 en el año actual) / Emisiones de CO2 en el año base) * 100. Las emisiones de CO2 se estimarán a partir de los datos de consumo de combustible y eficiencia energética de los vehículos en los conjuntos de datos proporcionados y posiblemente enriquecidos con datos adicionales recopilados.
Este enfoque integral nos permitirá establecer una correlación clara entre la actividad de taxis y viajes compartidos y los niveles de contaminación en Nueva York, apoyando la toma de decisiones para estrategias de reducción de contaminación y mejora de la calidad del aire en la ciudad.
.

