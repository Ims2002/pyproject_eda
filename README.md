# 📊 Análisis Exploratorio del Dataset de Aplicaciones Android

## 🎯 Objetivo del Proyecto

El objetivo de este proyecto es realizar un **Análisis Exploratorio de Datos (EDA)** sobre un dataset de aplicaciones Android para entender:

- La distribución de aplicaciones gratuitas y de pago.
- La relación entre precio, valoración y descargas.
- Qué categorías monetizan más.
- Cómo influyen la versión de Android y el tipo de contenido.
- Qué patrones existen entre calidad percibida y modelo de negocio.

---

## 📁 Dataset

El dataset contiene información sobre aplicaciones móviles, incluyendo:

- `App`
- `Category`
- `Rating`
- `Reviews`
- `Installs`
- `Type` (Free / Paid)
- `Price_$`
- `Content_Rating`
- `Genres`
- `Last_Updated`
- `Android_Version`

Durante el proceso se realizaron tareas de limpieza y generación de variables adicionales como:

- `Android_Version_Major`
- `Last_Updated_Year`
- `Last_Updated_Month`
- `Rating_Group`

---

## ❓ Preguntas de Análisis

El análisis busca responder preguntas como:

1. ¿Qué proporción de apps son gratuitas vs de pago?
2. ¿Qué categorías concentran más aplicaciones?
3. ¿Qué géneros son los más frecuentes?
4. ¿Qué categorías tienen mayor proporción de apps de pago?
5. ¿Las apps mejor valoradas son más caras?
6. ¿Influye la versión mínima de Android en el número de descargas?
7. ¿Existe relación entre categoría y tipo de contenido?

---

## 🔎 Pasos del Análisis

### 1️⃣ Distribución de precios
Se analiza la frecuencia de precios en la columna `Price_$` para entender la estructura del mercado.

### 2️⃣ Proporción Free vs Paid
Se calcula el porcentaje de aplicaciones gratuitas frente a las de pago.

### 3️⃣ Distribución por categoría
Se visualiza el número de aplicaciones por categoría para detectar sectores dominantes.

### 4️⃣ Top 10 géneros
Se representa la distribución porcentual de los géneros más frecuentes mediante un gráfico circular.

### 5️⃣ Heatmap Categoría vs Versión Android
Se analiza cuántas aplicaciones por categoría requieren cada versión principal de Android.

### 6️⃣ Precio medio de apps de pago por género
Se identifican los géneros con mayor precio medio entre aplicaciones de pago.

### 7️⃣ Descargas promedio por versión Android
Se calcula el porcentaje de descargas promedio agrupadas por versión principal de Android.

### 8️⃣ Precio medio según grupo de rating (apps de pago)
Se analiza si existe relación entre valoración (`Rating_Group`) y precio.

### 9️⃣ Crosstabs relevantes
Se estudian relaciones categóricas mediante tablas cruzadas normalizadas:

- `Category vs Type`
- `Category vs Content_Rating`

---

## 📌 Conclusiones Principales

- La mayoría del mercado está dominado por aplicaciones gratuitas, con esto identificamos que por lo general el mercado esta copado por aplicaciones gratuitas que sacan rentabilidad mediante anuncios o micropagos.
- Algunas categorías presentan mayor proporción de aplicaciones de pago, asi podemos identificar cuales son las categorías por las que la gente está más dispuesta apagar.
- No necesariamente las apps mejor valoradas son las más caras, mas bien es al contrario ya que las aplicaciones con un precio mayor son las que peor Rating tienen en promedio.
- Las versiones más recientes de Android concentran mayor número de descargas promedio, este dato va creciendo con el paso de las versiones.
- Existen diferencias claras en clasificación de contenido según categoría, los adolescentes se suelen centrar en aplicaciones de entretenimiento por ejemplo.

---

# Cleaning del Dataset de Aplicaciones

La función `clean(df: pd.DataFrame)` se encarga de **preprocesar y estandarizar el dataset** para que sea consistente y listo para análisis o visualización.  

## Pasos del preprocesamiento

### 1️⃣ Estandarización de categorías
- Todas las categorías se pasan a **mayúsculas** para uniformidad.
- Se recodifican categorías específicas según reglas del proyecto:
  - `'LIFESTYLE' → 'HEALTH'`
  - `'FINANCE' → 'BUSINESS'`
  - `'TOOLS' → 'PRODUCTIVITY'`
  - `'ENTERTAINMENT' → 'GAME'`

### 2️⃣ Limpieza de la columna `Installs`
- Se eliminan caracteres innecesarios: `+`, `,` y la palabra `'installs'`.
- Se eliminan espacios en blanco al inicio o final.
- Se descartan filas con valor `'unknown'`.
- Se convierte la columna a **tipo entero (`int`)**.

### 3️⃣ Manejo de valores nulos
- Se eliminan filas con valores nulos en **`Last_Updated`** (corresponden ~3% del dataset).  
- Para **`Rating`**, los valores nulos se reemplazan por la **media de la columna**, redondeada a 1 decimal.
- Para **`Genres`**, los valores nulos se rellenan con `'UNKNOWN'` y se convierten a mayúsculas.
- Para **`Price_$`**, los valores nulos se rellenan con `0.0` (asumiendo que las apps son gratuitas).

### 4️⃣ Sincronización de `Type` y `Price_$`
- Todas las apps con `Type == 'Free'` tienen el precio forzado a **0** para consistencia.

### 5️⃣ Conversión de tipos y creación de columnas de tiempo
- `Last_Updated` se convierte a **datetime**.

### 6️⃣ Eliminación de columnas irrelevantes
- Se elimina **`Size_MB`**, ya que todos los valores son iguales y no aportan información útil para el análisis.

### 7️⃣ Resultado
- El DataFrame resultante está **limpio, consistente y listo para análisis, visualización o generación de features adicionales**.

---

💡 Este preprocesamiento asegura que:

- No haya inconsistencias en categorías o tipos.  
- Las columnas numéricas estén correctamente formateadas.  
- Los valores nulos sean tratados de forma lógica.  
- Se puedan hacer análisis temporales sin errores de formato.


# Generación de Features del Dataset de Aplicaciones

La función `build_features(df: pd.DataFrame)` crea **features derivadas** a partir del dataset limpio para facilitar análisis, agregaciones y visualizaciones.  

Se aplica **después de la limpieza** (`clean(df)`), sobre un DataFrame consistente.

## Features generadas

### 1️⃣ Android_Version_Major
- Extrae la versión principal de Android a partir de la columna `Android_Version`.
- Se toma la parte antes del primer espacio (`'9.0 and up' → 9.0'`) y se convierte a float.
- Útil para análisis agregados por versión principal sin preocuparse por subversiones.

### 2️⃣ Last_Updated_Year y Last_Updated_Month
- Extrae el **año** y el **mes** de la columna `Last_Updated`.
- Permite agrupar aplicaciones por fecha de actualización de manera fácil (`df.groupby(['Last_Updated_Year', 'Last_Updated_Month'])`).
- Facilita análisis temporales y gráficos de evolución mensual.

### 3️⃣ Rating_Group
- Agrupa la variable numérica `Rating` en categorías ordinales.
- Convierte una variable continua en una variable categórica más interpretable.
- Permite realizar análisis segmentados por nivel de calidad.

Rangos definidos:

| Rating | Grupo |
|--------|--------|
| 0 – 2.5 | Low |
| 2.5 – 3.5 | Mid |
| 3.5 – 4.5 | High |
| 4.5 – 5 | Top |

- Facilita visualizaciones como countplots, crosstabs y análisis de descargas o precio por nivel de valoración.




## 🔎 Validación de columnas requeridas

En el módulo `utils.py` se define la función `assert_columns`, cuyo objetivo es validar que el `DataFrame` contiene todas las columnas necesarias antes de continuar con el pipeline de procesamiento.

### Implementación

```python
import pandas as pd

def assert_columns(df: pd.DataFrame, required: list[str]) -> None:
    missing = [c for c in required if c not in df.columns]
    if missing:
        raise ValueError(f'Missing columns: {missing}')