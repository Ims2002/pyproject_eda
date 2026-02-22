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
- Se toma la parte antes del primer punto (`'9.0' → 9`) y se convierte a entero.
- Útil para análisis agregados por versión principal sin preocuparse por subversiones.

### 2️⃣ Last_Updated_Year y Last_Updated_Month
- Extrae el **año** y el **mes** de la columna `Last_Updated`.
- Permite agrupar aplicaciones por fecha de actualización de manera fácil (`df.groupby(['Last_Updated_Year', 'Last_Updated_Month'])`).
- Facilita análisis temporales y gráficos de evolución mensual.

