¡Claro! Vamos a aprender **`pandas`** paso a paso en 10 etapas. Empezamos desde el inicio, con conceptos básicos y poco a poco iremos avanzando hacia funcionalidades más complejas. 😊

### **Paso 1/10: Introducción y conceptos básicos de `pandas`**

#### ¿Qué es `pandas`?

`pandas` es una de las bibliotecas más populares y poderosas en Python para la **manipulación y análisis de datos**. Es muy útil para trabajar con **tablas de datos** (como las hojas de cálculo o bases de datos) y realizar operaciones como filtrado, agregación, y transformación de datos.

#### Características principales:
- **DataFrame**: Es la estructura de datos más importante en `pandas`. Es como una tabla de Excel con filas y columnas.
- **Series**: Es una estructura unidimensional similar a un arreglo de Python, pero con índices.
- **Manejo de datos faltantes**: Permite gestionar valores ausentes o `NaN` de forma sencilla.
- **Lectura y escritura de datos**: Puede leer y escribir archivos de diferentes formatos como CSV, Excel, SQL, entre otros.
- **Operaciones avanzadas**: Soporta operaciones matemáticas, estadísticas, agrupación de datos, y más.

#### Primer paso práctico: Instalación de `pandas` y primer script

1. **Instalar `pandas`**:
   Si aún no tienes `pandas` instalado, puedes hacerlo con el siguiente comando:
   ```bash
   pip install pandas
   ```

2. **Importar `pandas` en tu script**:
   Al igual que otras bibliotecas, `pandas` se importa en tu código de la siguiente manera:
   ```python
   import pandas as pd
   ```

3. **Crear un DataFrame desde un diccionario**:
   Un `DataFrame` es la estructura más importante de `pandas`. Puedes crearlo de muchas maneras, pero una forma común es desde un diccionario de Python.
   ```python
   import pandas as pd

   # Crear un diccionario de datos
   data = {
       'Nombre': ['Ana', 'Luis', 'Carlos'],
       'Edad': [23, 30, 25],
       'Ciudad': ['Madrid', 'Barcelona', 'Valencia']
   }

   # Crear un DataFrame a partir del diccionario
   df = pd.DataFrame(data)

   # Ver el contenido del DataFrame
   print(df)
   ```

   **Salida**:
   ```
      Nombre  Edad     Ciudad
   0     Ana    23      Madrid
   1    Luis    30   Barcelona
   2  Carlos    25    Valencia
   ```

Este es el primer paso: hemos creado un pequeño DataFrame, que es una tabla con columnas (`Nombre`, `Edad`, `Ciudad`) y filas con datos.

---

¿Listo para continuar con el **Paso 2/10: Cómo leer y escribir archivos CSV**? 😊

### **Paso 2/10: Cómo leer y escribir archivos CSV con `pandas`**

Uno de los principales usos de `pandas` es leer y escribir archivos en varios formatos. En este paso, aprenderemos cómo trabajar con **archivos CSV** (Comma Separated Values), que es uno de los formatos más comunes para almacenar datos tabulares.

---

#### 1. **Leer un archivo CSV en un DataFrame**

Para leer un archivo CSV y convertirlo en un DataFrame, utilizamos la función `pd.read_csv()`. Esta función carga el contenido del archivo CSV en un DataFrame, lo que nos permite manipular los datos de forma eficiente.

**Ejemplo:**
Supongamos que tienes un archivo llamado `personas.csv` con el siguiente contenido:

```
Nombre,Edad,Ciudad
Ana,23,Madrid
Luis,30,Barcelona
Carlos,25,Valencia
```

Puedes leer este archivo CSV de la siguiente manera:

```python
import pandas as pd

# Leer el archivo CSV
df = pd.read_csv("personas.csv")

# Mostrar el DataFrame
print(df)
```

**Salida**:
```
   Nombre  Edad     Ciudad
0     Ana    23      Madrid
1    Luis    30   Barcelona
2  Carlos    25    Valencia
```

#### 2. **Escribir un DataFrame a un archivo CSV**

Una vez que tienes los datos en un DataFrame, también puedes guardarlos de nuevo en un archivo CSV utilizando el método `to_csv()`.

**Ejemplo:**

```python
import pandas as pd

# Crear un DataFrame
data = {
    'Nombre': ['Ana', 'Luis', 'Carlos'],
    'Edad': [23, 30, 25],
    'Ciudad': ['Madrid', 'Barcelona', 'Valencia']
}
df = pd.DataFrame(data)

# Escribir el DataFrame a un archivo CSV
df.to_csv("nuevo_archivo.csv", index=False)  # `index=False` evita guardar el índice
```

El archivo `nuevo_archivo.csv` será creado con el siguiente contenido:

```
Nombre,Edad,Ciudad
Ana,23,Madrid
Luis,30,Barcelona
Carlos,25,Valencia
```

#### 3. **Leer CSV con opciones adicionales**

Puedes personalizar cómo `pandas` lee el archivo CSV, por ejemplo, especificando el delimitador, el manejo de valores nulos, la codificación, entre otros.

**Ejemplo con parámetros adicionales**:

```python
# Leer un CSV con un delimitador diferente (por ejemplo, punto y coma)
df = pd.read_csv("personas.csv", delimiter=";")
```

Algunos otros parámetros útiles son:
- `na_values`: Para definir qué valores se deben considerar como `NaN`.
- `header`: Para especificar en qué fila se encuentran los nombres de las columnas.

---

#### 4. **Verificar si el archivo CSV fue leído correctamente**

Puedes revisar los primeros o últimos registros de un DataFrame usando los métodos `head()` y `tail()`.

```python
# Mostrar las primeras 5 filas
print(df.head())

# Mostrar las últimas 5 filas
print(df.tail())
```

Estos métodos son útiles para asegurarte de que los datos fueron leídos correctamente.

---

Con este paso, ya sabes cómo leer y escribir archivos CSV utilizando `pandas`, lo que es fundamental para trabajar con conjuntos de datos en Python.  

¿Listo para continuar con el **Paso 3/10: Cómo seleccionar y filtrar datos en un DataFrame**? 😊

### **Paso 3/10: Cómo seleccionar y filtrar datos en un DataFrame**

Ahora que sabes cómo leer y escribir archivos CSV, es momento de aprender a **seleccionar y filtrar datos** dentro de un DataFrame. `pandas` ofrece una variedad de maneras de acceder a los datos y filtrar la información que necesitas.

---

#### 1. **Seleccionar columnas**

Puedes seleccionar una o varias columnas de un DataFrame de diferentes maneras:

**Ejemplo: Seleccionar una columna**:
```python
import pandas as pd

# Crear un DataFrame
data = {
    'Nombre': ['Ana', 'Luis', 'Carlos'],
    'Edad': [23, 30, 25],
    'Ciudad': ['Madrid', 'Barcelona', 'Valencia']
}
df = pd.DataFrame(data)

# Seleccionar una columna
edad_columna = df['Edad']
print(edad_columna)
```

**Salida**:
```
0    23
1    30
2    25
Name: Edad, dtype: int64
```

**Ejemplo: Seleccionar múltiples columnas**:
```python
# Seleccionar varias columnas
columnas_seleccionadas = df[['Nombre', 'Ciudad']]
print(columnas_seleccionadas)
```

**Salida**:
```
   Nombre     Ciudad
0     Ana      Madrid
1    Luis   Barcelona
2  Carlos    Valencia
```

---

#### 2. **Seleccionar filas por índice**

Puedes acceder a las filas de un DataFrame utilizando el índice o la posición de las filas. 

**Ejemplo: Seleccionar una fila por índice**:
```python
# Seleccionar una fila por su índice
fila_0 = df.loc[0]  # Índice 0
print(fila_0)
```

**Salida**:
```
Nombre       Ana
Edad          23
Ciudad    Madrid
Name: 0, dtype: object
```

**Ejemplo: Seleccionar varias filas por índice**:
```python
# Seleccionar varias filas por índice
filas_0_1 = df.loc[0:1]  # Selecciona las filas de índice 0 a 1
print(filas_0_1)
```

**Salida**:
```
   Nombre  Edad     Ciudad
0     Ana    23      Madrid
1    Luis    30   Barcelona
```

---

#### 3. **Filtrar datos por condiciones**

Una de las funciones más poderosas de `pandas` es la capacidad de **filtrar datos** basados en condiciones. Puedes aplicar condiciones a las columnas y filtrar el DataFrame de acuerdo a esos criterios.

**Ejemplo: Filtrar filas donde la edad sea mayor que 24**:
```python
# Filtrar filas donde la edad sea mayor que 24
filtro_edad = df[df['Edad'] > 24]
print(filtro_edad)
```

**Salida**:
```
   Nombre  Edad     Ciudad
1    Luis    30   Barcelona
2  Carlos    25    Valencia
```

**Ejemplo: Filtrar por múltiples condiciones (Edad mayor que 24 y Ciudad igual a Barcelona)**:
```python
# Filtrar con múltiples condiciones
filtro_multiple = df[(df['Edad'] > 24) & (df['Ciudad'] == 'Barcelona')]
print(filtro_multiple)
```

**Salida**:
```
   Nombre  Edad     Ciudad
1    Luis    30   Barcelona
```

---

#### 4. **Filtrar datos usando `query()`**

`pandas` también tiene un método llamado `query()` que permite realizar filtrados de una manera más expresiva, similar a las consultas SQL.

**Ejemplo: Usar `query()` para filtrar**:
```python
# Filtrar usando el método query()
filtro_query = df.query('Edad > 24 and Ciudad == "Barcelona"')
print(filtro_query)
```

**Salida**:
```
   Nombre  Edad     Ciudad
1    Luis    30   Barcelona
```

---

#### 5. **Seleccionar filas y columnas con `loc[]` y `iloc[]`**

- **`loc[]`**: Se utiliza para seleccionar filas y columnas **por etiqueta**.
- **`iloc[]`**: Se utiliza para seleccionar filas y columnas **por índice numérico**.

**Ejemplo con `loc[]`**:
```python
# Seleccionar una fila y una columna por etiqueta
dato = df.loc[1, 'Nombre']  # Fila 1, columna 'Nombre'
print(dato)
```

**Salida**:
```
Luis
```

**Ejemplo con `iloc[]`**:
```python
# Seleccionar una fila y una columna por índice
dato = df.iloc[1, 0]  # Fila 1, columna 0 (que es 'Nombre')
print(dato)
```

**Salida**:
```
Luis
```

---

Con estos métodos, ahora sabes cómo seleccionar y filtrar datos en un DataFrame usando condiciones, índices, etiquetas, y funciones como `query()`. Esto te da gran flexibilidad para explorar y manipular tus datos.

---

¿Listo para continuar con el **Paso 4/10: Cómo agregar, eliminar y modificar datos en un DataFrame**? 😊

### **Paso 4/10: Cómo agregar, eliminar y modificar datos en un DataFrame**

En este paso, aprenderás cómo **agregar nuevas filas y columnas**, **eliminar** datos, y **modificar** los valores dentro de un DataFrame en `pandas`. Estas son tareas comunes cuando trabajas con conjuntos de datos.

---

#### 1. **Agregar nuevas columnas**

Puedes agregar columnas nuevas a un DataFrame simplemente asignando un valor o una serie de valores a una nueva columna.

**Ejemplo: Agregar una nueva columna con valores constantes**:
```python
import pandas as pd

# Crear un DataFrame
data = {
    'Nombre': ['Ana', 'Luis', 'Carlos'],
    'Edad': [23, 30, 25],
    'Ciudad': ['Madrid', 'Barcelona', 'Valencia']
}
df = pd.DataFrame(data)

# Agregar una nueva columna con un valor constante
df['Salario'] = 3000
print(df)
```

**Salida**:
```
   Nombre  Edad     Ciudad  Salario
0     Ana    23      Madrid     3000
1    Luis    30   Barcelona     3000
2  Carlos    25    Valencia     3000
```

**Ejemplo: Agregar una columna basada en una operación**:
```python
# Agregar una nueva columna basada en una operación
df['Edad en 5 años'] = df['Edad'] + 5
print(df)
```

**Salida**:
```
   Nombre  Edad     Ciudad  Salario  Edad en 5 años
0     Ana    23      Madrid     3000              28
1    Luis    30   Barcelona     3000              35
2  Carlos    25    Valencia     3000              30
```

---

#### 2. **Agregar nuevas filas**

Para agregar nuevas filas, puedes usar el método `append()` o `loc[]`.

**Ejemplo: Agregar una fila con `append()`**:
```python
# Agregar una nueva fila usando append()
nueva_fila = {'Nombre': 'Marta', 'Edad': 27, 'Ciudad': 'Sevilla', 'Salario': 3200, 'Edad en 5 años': 32}
df = df.append(nueva_fila, ignore_index=True)
print(df)
```

**Salida**:
```
   Nombre  Edad     Ciudad  Salario  Edad en 5 años
0     Ana    23      Madrid     3000              28
1    Luis    30   Barcelona     3000              35
2  Carlos    25    Valencia     3000              30
3   Marta    27     Sevilla     3200              32
```

**Ejemplo: Agregar una fila con `loc[]`**:
```python
# Agregar una fila con loc[]
df.loc[len(df)] = ['Juan', 28, 'Bilbao', 3500, 33]
print(df)
```

**Salida**:
```
   Nombre  Edad     Ciudad  Salario  Edad en 5 años
0     Ana    23      Madrid     3000              28
1    Luis    30   Barcelona     3000              35
2  Carlos    25    Valencia     3000              30
3   Marta    27     Sevilla     3200              32
4    Juan    28     Bilbao     3500              33
```

---

#### 3. **Eliminar columnas o filas**

Puedes eliminar tanto columnas como filas usando los métodos `drop()` y `del`.

**Ejemplo: Eliminar una columna**:
```python
# Eliminar una columna con drop()
df = df.drop('Salario', axis=1)
print(df)
```

**Salida**:
```
   Nombre  Edad     Ciudad  Edad en 5 años
0     Ana    23      Madrid              28
1    Luis    30   Barcelona              35
2  Carlos    25    Valencia              30
3   Marta    27     Sevilla              32
4    Juan    28     Bilbao              33
```

**Nota**: El parámetro `axis=1` especifica que se elimina una columna. Si fuera `axis=0`, se eliminarían filas.

**Ejemplo: Eliminar una fila por índice**:
```python
# Eliminar una fila por índice
df = df.drop(2, axis=0)  # Eliminar la fila con índice 2
print(df)
```

**Salida**:
```
   Nombre  Edad     Ciudad  Edad en 5 años
0     Ana    23      Madrid              28
1    Luis    30   Barcelona              35
3   Marta    27     Sevilla              32
4    Juan    28     Bilbao              33
```

---

#### 4. **Modificar datos existentes**

Para modificar valores en un DataFrame, puedes usar la indexación estándar de `pandas`.

**Ejemplo: Modificar el valor de una celda**:
```python
# Modificar el valor de una celda
df.loc[1, 'Edad'] = 31  # Cambiar la edad de Luis a 31
print(df)
```

**Salida**:
```
   Nombre  Edad     Ciudad  Edad en 5 años
0     Ana    23      Madrid              28
1    Luis    31   Barcelona              36
3   Marta    27     Sevilla              32
4    Juan    28     Bilbao              33
```

---

#### 5. **Modificar varias celdas a la vez**

Si necesitas modificar varias celdas a la vez, puedes usar asignaciones con operaciones:

**Ejemplo: Modificar varias celdas**:
```python
# Modificar todas las edades sumando 1
df['Edad'] = df['Edad'] + 1
print(df)
```

**Salida**:
```
   Nombre  Edad     Ciudad  Edad en 5 años
0     Ana    24      Madrid              29
1    Luis    32   Barcelona              37
3   Marta    28     Sevilla              33
4    Juan    29     Bilbao              34
```

---

Con estos métodos, ahora sabes cómo **agregar** y **eliminar** tanto filas como columnas, y cómo **modificar** valores dentro de un DataFrame de manera eficiente.

---

¿Listo para continuar con el **Paso 5/10: Cómo agrupar y agregar datos en un DataFrame**? 😊

### **Paso 5/10: Cómo agrupar y agregar datos en un DataFrame**

En este paso, aprenderás a **agrupar** datos en un DataFrame y realizar **operaciones de agregación**. El agrupamiento es útil cuando deseas realizar cálculos sobre subconjuntos de datos basados en una o más columnas, como sumas, promedios, o contar elementos en categorías.

---

#### 1. **Agrupar datos con `groupby()`**

La función `groupby()` de `pandas` permite agrupar filas de un DataFrame por una o más columnas, para luego aplicar operaciones de agregación a cada grupo.

**Ejemplo: Agrupar por una columna y contar**:

Supongamos que tienes el siguiente DataFrame:

```python
import pandas as pd

# Crear un DataFrame de ejemplo
data = {
    'Nombre': ['Ana', 'Luis', 'Carlos', 'Marta', 'Juan'],
    'Ciudad': ['Madrid', 'Barcelona', 'Madrid', 'Sevilla', 'Madrid'],
    'Edad': [23, 30, 25, 27, 28],
}
df = pd.DataFrame(data)

# Agrupar por la columna 'Ciudad' y contar cuántas personas hay en cada ciudad
grupo_ciudad = df.groupby('Ciudad').size()
print(grupo_ciudad)
```

**Salida**:
```
Ciudad
Barcelona    1
Madrid       3
Sevilla      1
dtype: int64
```

El método `size()` cuenta cuántas filas hay en cada grupo (en este caso, cuántas personas hay en cada ciudad).

---

#### 2. **Aplicar funciones de agregación**

Una vez que tienes los grupos, puedes aplicar funciones de agregación como `sum()`, `mean()`, `min()`, `max()`, entre otras, para obtener resultados resumidos para cada grupo.

**Ejemplo: Calcular la edad promedio por ciudad**:
```python
# Agrupar por 'Ciudad' y calcular el promedio de la edad
promedio_edad = df.groupby('Ciudad')['Edad'].mean()
print(promedio_edad)
```

**Salida**:
```
Ciudad
Barcelona    30.0
Madrid       25.3
Sevilla      27.0
Name: Edad, dtype: float64
```

---

#### 3. **Usar múltiples funciones de agregación**

Puedes aplicar varias funciones de agregación a una o más columnas al mismo tiempo utilizando `agg()`. Esto es útil cuando quieres calcular más de una métrica por grupo, como el promedio y la suma.

**Ejemplo: Calcular múltiples métricas (promedio y suma) para la edad por ciudad**:
```python
# Agrupar por 'Ciudad' y calcular el promedio y la suma de las edades
resumen_edad = df.groupby('Ciudad')['Edad'].agg(['mean', 'sum'])
print(resumen_edad)
```

**Salida**:
```
           mean  sum
Ciudad               
Barcelona   30.0   30
Madrid      25.3   76
Sevilla     27.0   27
```

En este ejemplo, hemos calculado tanto el promedio (`mean`) como la suma (`sum`) de las edades por cada ciudad.

---

#### 4. **Filtrar grupos**

Después de realizar un agrupamiento, a veces es útil filtrar los grupos que cumplen ciertas condiciones. Esto se puede hacer con `filter()`.

**Ejemplo: Filtrar ciudades con más de una persona**:
```python
# Filtrar grupos (ciudades) que tengan más de una persona
ciudades_con_mas_de_1_persona = df.groupby('Ciudad').filter(lambda x: len(x) > 1)
print(ciudades_con_mas_de_1_persona)
```

**Salida**:
```
   Nombre    Ciudad  Edad
0     Ana     Madrid    23
2  Carlos     Madrid    25
4    Juan     Madrid    28
1    Luis  Barcelona    30
```

Este ejemplo muestra solo las ciudades que tienen más de una persona.

---

#### 5. **Agrupar por múltiples columnas**

También puedes agrupar por varias columnas. Esto crea grupos jerárquicos y te permite hacer análisis más complejos.

**Ejemplo: Agrupar por dos columnas (Ciudad y Edad)**:
```python
# Agrupar por 'Ciudad' y 'Edad' y contar cuántas veces se repite cada combinación
grupo_ciudad_edad = df.groupby(['Ciudad', 'Edad']).size()
print(grupo_ciudad_edad)
```

**Salida**:
```
Ciudad     Edad
Barcelona  30      1
Madrid     23      1
           25      1
           28      1
Sevilla    27      1
dtype: int64
```

---

#### 6. **Realizar transformaciones después de agrupar**

Además de agregación, `groupby()` permite realizar transformaciones, que son operaciones que retornan un DataFrame del mismo tamaño que el original.

**Ejemplo: Normalizar las edades dentro de cada ciudad (restar el promedio de la ciudad)**:
```python
# Normalizar la edad (restar el promedio de la ciudad)
df['Edad_normalizada'] = df.groupby('Ciudad')['Edad'].transform(lambda x: x - x.mean())
print(df)
```

**Salida**:
```
   Nombre    Ciudad  Edad  Edad_normalizada
0     Ana     Madrid    23              -2.0
1    Luis  Barcelona    30               0.0
2  Carlos     Madrid    25              -0.5
3   Marta    Sevilla    27               0.0
4    Juan     Madrid    28               1.0
```

---

Con estos métodos, ahora puedes **agrupar datos** en un DataFrame y realizar **agregaciones** y **transformaciones**. Esto es extremadamente útil cuando necesitas analizar grandes conjuntos de datos y resumir información por categorías.

---

¿Listo para continuar con el **Paso 6/10: Cómo manejar valores faltantes (NaN) en un DataFrame**? 😊

### **Paso 6/10: Cómo manejar valores faltantes (NaN) en un DataFrame**

En este paso, aprenderás cómo trabajar con **valores faltantes (NaN)** en un DataFrame. Los valores faltantes son comunes en los datos del mundo real, y `pandas` ofrece varias maneras de **detectarlos**, **reemplazarlos** o **eliminarlos**.

---

#### 1. **Detectar valores faltantes**

Para detectar los valores faltantes en un DataFrame, `pandas` proporciona las funciones `isna()` o `isnull()`. Ambas funciones devuelven un DataFrame de valores booleanos (`True` para valores faltantes, `False` para los valores presentes).

**Ejemplo: Detectar valores faltantes**:
```python
import pandas as pd

# Crear un DataFrame con valores faltantes
data = {
    'Nombre': ['Ana', 'Luis', 'Carlos', 'Marta', 'Juan'],
    'Edad': [23, None, 25, None, 28],
    'Ciudad': ['Madrid', 'Barcelona', None, 'Sevilla', 'Madrid']
}
df = pd.DataFrame(data)

# Detectar valores faltantes
valores_faltantes = df.isna()
print(valores_faltantes)
```

**Salida**:
```
   Nombre   Edad  Ciudad
0   False  False   False
1   False   True   False
2   False  False    True
3   False   True   False
4   False  False   False
```

En este ejemplo, las posiciones con `True` indican que hay un valor faltante en esa celda.

---

#### 2. **Contar valores faltantes**

Para contar cuántos valores faltantes hay en cada columna, puedes usar `isna()` seguido de `sum()`.

**Ejemplo: Contar valores faltantes por columna**:
```python
# Contar los valores faltantes por columna
faltantes_por_columna = df.isna().sum()
print(faltantes_por_columna)
```

**Salida**:
```
Nombre    0
Edad      2
Ciudad    1
dtype: int64
```

Esto indica que la columna `Edad` tiene 2 valores faltantes, y `Ciudad` tiene 1 valor faltante.

---

#### 3. **Eliminar filas o columnas con valores faltantes**

Puedes eliminar las filas o columnas que contienen valores faltantes utilizando `dropna()`. 

- **Eliminar filas con valores faltantes**:
```python
# Eliminar filas con al menos un valor faltante
df_sin_faltantes = df.dropna(axis=0)
print(df_sin_faltantes)
```

**Salida**:
```
   Nombre  Edad    Ciudad
0     Ana  23.0     Madrid
4    Juan  28.0     Madrid
```

El parámetro `axis=0` especifica que estamos eliminando filas. Si quieres eliminar columnas con valores faltantes, usa `axis=1`.

- **Eliminar columnas con valores faltantes**:
```python
# Eliminar columnas con valores faltantes
df_sin_columnas_faltantes = df.dropna(axis=1)
print(df_sin_columnas_faltantes)
```

**Salida**:
```
   Nombre
0     Ana
1    Luis
2  Carlos
3   Marta
4    Juan
```

---

#### 4. **Reemplazar valores faltantes**

En lugar de eliminar los valores faltantes, en muchos casos es útil **reemplazarlos** por un valor específico, como la media, la mediana, o un valor constante.

- **Reemplazar con un valor constante**:
```python
# Reemplazar valores faltantes con un valor constante (por ejemplo, 0 o 'Desconocido')
df_reemplazado = df.fillna({'Edad': 0, 'Ciudad': 'Desconocido'})
print(df_reemplazado)
```

**Salida**:
```
   Nombre  Edad       Ciudad
0     Ana   23.0        Madrid
1    Luis    0.0    Barcelona
2  Carlos   25.0  Desconocido
3   Marta    0.0      Sevilla
4    Juan   28.0        Madrid
```

- **Reemplazar con la media de la columna**:
```python
# Reemplazar los valores faltantes en 'Edad' con la media de la columna
media_edad = df['Edad'].mean()
df['Edad'] = df['Edad'].fillna(media_edad)
print(df)
```

**Salida**:
```
   Nombre  Edad     Ciudad
0     Ana   23.0     Madrid
1    Luis   26.5  Barcelona
2  Carlos   25.0  Desconocido
3   Marta   26.5     Sevilla
4    Juan   28.0     Madrid
```

---

#### 5. **Interpolación de valores faltantes**

La interpolación es un proceso que permite **estimar los valores faltantes** en función de los valores circundantes. `pandas` proporciona el método `interpolate()` para realizar interpolación en series o DataFrames.

**Ejemplo: Interpolación lineal de valores faltantes**:
```python
# Interpolar los valores faltantes en la columna 'Edad'
df['Edad'] = df['Edad'].interpolate()
print(df)
```

**Salida**:
```
   Nombre  Edad     Ciudad
0     Ana   23.0     Madrid
1    Luis   24.0  Barcelona
2  Carlos   25.0  Desconocido
3   Marta   26.0     Sevilla
4    Juan   28.0     Madrid
```

---

#### 6. **Verificar si hay valores nulos después del reemplazo o eliminación**

Después de manejar los valores faltantes, es importante verificar si los cambios han sido efectivos. Puedes usar `isna().sum()` nuevamente para comprobar que ya no hay valores faltantes.

```python
# Verificar si hay valores faltantes después de reemplazar
print(df.isna().sum())
```

**Salida**:
```
Nombre    0
Edad      0
Ciudad    0
dtype: int64
```

---

Con estos métodos, ahora sabes cómo **detectar**, **contar**, **eliminar**, **reemplazar** y **convertir** valores faltantes en un DataFrame. Trabajar con valores faltantes es una habilidad esencial cuando limpias y preparas datos para el análisis.

---

¿Listo para continuar con el **Paso 7/10: Cómo combinar y fusionar DataFrames**? 😊
### **Paso 7/10: Cómo combinar y fusionar DataFrames**

En este paso, aprenderás cómo **combinar** o **fusionar** múltiples DataFrames. Estas técnicas son útiles cuando trabajas con varios conjuntos de datos relacionados y necesitas unirlos para realizar un análisis más completo.

---

#### 1. **Concatenar DataFrames con `concat()`**

La función `concat()` de `pandas` te permite unir varios DataFrames, ya sea apilándolos **verticalmente** (uno encima del otro) o **horizontalmente** (uno al lado del otro).

- **Concatenar verticalmente (por filas)**:
  
Si tienes varios DataFrames con las mismas columnas y quieres unirlos, usa `concat()` para apilarlos verticalmente.

```python
import pandas as pd

# Crear dos DataFrames
df1 = pd.DataFrame({'Nombre': ['Ana', 'Luis'], 'Edad': [23, 30]})
df2 = pd.DataFrame({'Nombre': ['Carlos', 'Marta'], 'Edad': [25, 27]})

# Concatenar verticalmente (por filas)
df_concat = pd.concat([df1, df2], axis=0, ignore_index=True)
print(df_concat)
```

**Salida**:
```
   Nombre  Edad
0     Ana    23
1    Luis    30
2  Carlos    25
3   Marta    27
```

El parámetro `axis=0` indica que la concatenación es vertical (por filas). El `ignore_index=True` asegura que los índices se reinicien de manera consecutiva.

- **Concatenar horizontalmente (por columnas)**:

Si tienes DataFrames con diferentes columnas y deseas unirlos por las columnas, usa `axis=1`.

```python
# Crear dos DataFrames con diferentes columnas
df3 = pd.DataFrame({'Nombre': ['Ana', 'Luis'], 'Ciudad': ['Madrid', 'Barcelona']})
df4 = pd.DataFrame({'Edad': [23, 30], 'Salario': [2500, 3000]})

# Concatenar horizontalmente (por columnas)
df_concat_horizontal = pd.concat([df3, df4], axis=1)
print(df_concat_horizontal)
```

**Salida**:
```
   Nombre     Ciudad  Edad  Salario
0     Ana      Madrid    23     2500
1    Luis   Barcelona    30     3000
```

---

#### 2. **Fusionar DataFrames con `merge()`**

La función `merge()` es similar a las uniones de bases de datos SQL. Te permite combinar DataFrames basados en columnas comunes (llamadas **clave de fusión**), lo cual es muy útil cuando necesitas combinar información de diferentes fuentes.

- **Fusionar por una columna común (simulando un `JOIN` en SQL)**:

Si tienes dos DataFrames y quieres fusionarlos usando una columna en común, puedes usar `merge()`. Es similar a un `INNER JOIN` de SQL por defecto.

```python
# Crear dos DataFrames con una columna común
df5 = pd.DataFrame({'ID': [1, 2, 3], 'Nombre': ['Ana', 'Luis', 'Carlos']})
df6 = pd.DataFrame({'ID': [2, 3, 4], 'Edad': [30, 25, 28]})

# Fusionar por la columna 'ID'
df_merge = pd.merge(df5, df6, on='ID')
print(df_merge)
```

**Salida**:
```
   ID Nombre  Edad
0   2   Luis    30
1   3 Carlos    25
```

En este ejemplo, `merge()` fusiona los DataFrames `df5` y `df6` por la columna `ID`. Como por defecto el `merge()` realiza un `INNER JOIN`, solo las filas con valores comunes en la columna `ID` serán incluidas.

- **Fusionar con diferentes claves**:

Si las columnas que deseas usar para la fusión tienen nombres diferentes en cada DataFrame, puedes especificarlo usando los parámetros `left_on` y `right_on`.

```python
# Fusionar con claves diferentes
df_merge_diferente_clave = pd.merge(df5, df6, left_on='ID', right_on='ID')
print(df_merge_diferente_clave)
```

---

#### 3. **Especificar el tipo de fusión**

El parámetro `how` en `merge()` te permite especificar el tipo de unión que deseas, similar a las opciones en SQL (`INNER JOIN`, `LEFT JOIN`, `RIGHT JOIN`, `OUTER JOIN`).

- **Inner join (por defecto)**: Solo se incluyen las filas que tienen coincidencias en ambas tablas.

```python
# Realizar un INNER JOIN
df_inner = pd.merge(df5, df6, on='ID', how='inner')
```

- **Left join**: Mantiene todas las filas del DataFrame de la izquierda y las filas coincidentes del DataFrame de la derecha.

```python
# Realizar un LEFT JOIN
df_left = pd.merge(df5, df6, on='ID', how='left')
```

- **Right join**: Mantiene todas las filas del DataFrame de la derecha y las filas coincidentes del DataFrame de la izquierda.

```python
# Realizar un RIGHT JOIN
df_right = pd.merge(df5, df6, on='ID', how='right')
```

- **Outer join**: Incluye todas las filas de ambos DataFrames, rellenando con `NaN` donde no haya coincidencias.

```python
# Realizar un OUTER JOIN
df_outer = pd.merge(df5, df6, on='ID', how='outer')
```

---

#### 4. **Fusionar múltiples DataFrames**

Puedes fusionar más de dos DataFrames de forma secuencial utilizando `merge()` varias veces.

```python
# Crear otro DataFrame
df7 = pd.DataFrame({'ID': [1, 2, 4], 'Salario': [2500, 3000, 3500]})

# Fusionar tres DataFrames
df_merge_multiple = pd.merge(df5, df6, on='ID', how='inner')
df_merge_multiple = pd.merge(df_merge_multiple, df7, on='ID', how='inner')
print(df_merge_multiple)
```

**Salida**:
```
   ID Nombre  Edad  Salario
0   2   Luis    30     3000
1   3 Carlos    25     3500
```

---

Con estos métodos, ahora puedes **combinar** y **fusionar** múltiples DataFrames de diversas maneras: **verticalmente**, **horizontalmente**, y usando **operaciones de unión** complejas basadas en claves comunes.

---

¿Listo para continuar con el **Paso 8/10: Cómo ordenar y filtrar datos en un DataFrame**? 😊

### **Paso 8/10: Cómo ordenar y filtrar datos en un DataFrame**

En este paso, aprenderás a **ordenar** y **filtrar** los datos de un DataFrame según tus necesidades. Estas son operaciones clave cuando necesitas obtener una vista más específica de tus datos o realizar análisis basados en ciertos criterios.

---

#### 1. **Ordenar datos con `sort_values()`**

`sort_values()` te permite ordenar un DataFrame en función de una o varias columnas, ya sea de forma ascendente o descendente.

- **Ordenar por una columna**:

Si quieres ordenar los datos por una columna específica, simplemente usa el nombre de la columna.

```python
import pandas as pd

# Crear un DataFrame
data = {
    'Nombre': ['Ana', 'Luis', 'Carlos', 'Marta', 'Juan'],
    'Edad': [23, 30, 25, 27, 28],
    'Salario': [2500, 3000, 3500, 3200, 2800]
}
df = pd.DataFrame(data)

# Ordenar por la columna 'Edad' de manera ascendente
df_ordenado_edad = df.sort_values(by='Edad')
print(df_ordenado_edad)
```

**Salida**:
```
   Nombre  Edad  Salario
0     Ana    23     2500
2  Carlos    25     3500
3   Marta    27     3200
4    Juan    28     2800
1    Luis    30     3000
```

Por defecto, `sort_values()` ordena de forma **ascendente**.

- **Ordenar en orden descendente**:

Puedes ordenar en orden descendente pasando el parámetro `ascending=False`.

```python
# Ordenar por la columna 'Edad' de manera descendente
df_ordenado_edad_desc = df.sort_values(by='Edad', ascending=False)
print(df_ordenado_edad_desc)
```

**Salida**:
```
   Nombre  Edad  Salario
1    Luis    30     3000
4    Juan    28     2800
3   Marta    27     3200
2  Carlos    25     3500
0     Ana    23     2500
```

- **Ordenar por múltiples columnas**:

Si deseas ordenar por varias columnas, pasa una lista de nombres de columnas.

```python
# Ordenar por 'Edad' y luego por 'Salario'
df_ordenado_multiple = df.sort_values(by=['Edad', 'Salario'], ascending=[True, False])
print(df_ordenado_multiple)
```

**Salida**:
```
   Nombre  Edad  Salario
0     Ana    23     2500
2  Carlos    25     3500
3   Marta    27     3200
4    Juan    28     2800
1    Luis    30     3000
```

---

#### 2. **Filtrar datos con condiciones**

Puedes filtrar los datos en un DataFrame utilizando **condiciones booleanas**. Esto te permite seleccionar solo las filas que cumplan con ciertos criterios.

- **Filtrar por una sola condición**:

Por ejemplo, si deseas obtener solo las filas donde la **edad sea mayor a 25**, puedes hacerlo de la siguiente manera:

```python
# Filtrar filas donde la edad sea mayor a 25
df_filtrado_edad = df[df['Edad'] > 25]
print(df_filtrado_edad)
```

**Salida**:
```
   Nombre  Edad  Salario
1    Luis    30     3000
4    Juan    28     2800
```

- **Filtrar con múltiples condiciones**:

Puedes combinar varias condiciones utilizando los operadores lógicos `&` (AND) o `|` (OR). Recuerda que cada condición debe ir entre paréntesis.

Por ejemplo, si quieres seleccionar filas donde la **edad sea mayor a 25** **y el salario sea mayor a 2800**:

```python
# Filtrar con múltiples condiciones (Edad > 25 y Salario > 2800)
df_filtrado_multiple = df[(df['Edad'] > 25) & (df['Salario'] > 2800)]
print(df_filtrado_multiple)
```

**Salida**:
```
   Nombre  Edad  Salario
1    Luis    30     3000
3   Marta    27     3200
```

- **Filtrar con `isin()`**:

La función `isin()` te permite filtrar filas que tengan valores específicos en una columna. Es útil cuando quieres seleccionar varias opciones de una columna.

```python
# Filtrar filas donde el 'Nombre' sea 'Ana' o 'Carlos'
df_filtrado_nombre = df[df['Nombre'].isin(['Ana', 'Carlos'])]
print(df_filtrado_nombre)
```

**Salida**:
```
   Nombre  Edad  Salario
0     Ana    23     2500
2  Carlos    25     3500
```

---

#### 3. **Filtrar usando `query()`**

`query()` permite filtrar filas de manera más legible usando una expresión similar a SQL. Esto puede ser útil si prefieres escribir condiciones más complejas de forma sencilla.

```python
# Filtrar usando query
df_filtrado_query = df.query('Edad > 25 and Salario > 2800')
print(df_filtrado_query)
```

**Salida**:
```
   Nombre  Edad  Salario
1    Luis    30     3000
3   Marta    27     3200
```

---

#### 4. **Seleccionar columnas específicas**

Si solo deseas trabajar con algunas columnas de un DataFrame, puedes seleccionar esas columnas directamente.

```python
# Seleccionar solo las columnas 'Nombre' y 'Edad'
df_seleccionado = df[['Nombre', 'Edad']]
print(df_seleccionado)
```

**Salida**:
```
   Nombre  Edad
0     Ana    23
1    Luis    30
2  Carlos    25
3   Marta    27
4    Juan    28
```

---

Con estas operaciones, ahora sabes cómo **ordenar** y **filtrar** datos en un DataFrame, lo que te permitirá trabajar con subconjuntos específicos de datos para análisis más detallados.

---

¿Listo para continuar con el **Paso 9/10: Cómo aplicar funciones y transformaciones en un DataFrame**? 😊

### **Paso 9/10: Cómo aplicar funciones y transformaciones en un DataFrame**

En este paso, aprenderás a aplicar **funciones** y **transformaciones** a los datos de un DataFrame. Esto es útil cuando necesitas realizar operaciones en columnas o filas de manera eficiente, como por ejemplo aplicar una función matemática o transformar los datos de acuerdo con ciertos criterios.

---

#### 1. **Aplicar funciones a las columnas con `apply()`**

La función `apply()` te permite aplicar una función a lo largo de las columnas o filas de un DataFrame. Esto es útil cuando necesitas realizar operaciones personalizadas sobre tus datos.

- **Aplicar una función a una columna**:

Si deseas aplicar una función a una columna específica, puedes hacerlo de la siguiente manera:

```python
import pandas as pd

# Crear un DataFrame
data = {
    'Nombre': ['Ana', 'Luis', 'Carlos', 'Marta', 'Juan'],
    'Edad': [23, 30, 25, 27, 28],
    'Salario': [2500, 3000, 3500, 3200, 2800]
}
df = pd.DataFrame(data)

# Definir una función que incremente el salario en un 10%
def aumento_salario(x):
    return x * 1.10

# Aplicar la función a la columna 'Salario'
df['Salario_Aumento'] = df['Salario'].apply(aumento_salario)
print(df)
```

**Salida**:
```
   Nombre  Edad  Salario  Salario_Aumento
0     Ana    23     2500            2750.0
1    Luis    30     3000            3300.0
2  Carlos    25     3500            3850.0
3   Marta    27     3200            3520.0
4    Juan    28     2800            3080.0
```

En este caso, hemos creado una nueva columna `Salario_Aumento` donde el salario original se ha incrementado en un 10%.

- **Aplicar una función a todas las columnas (con `axis=1`)**:

Si deseas aplicar una función a las filas completas (a través de todas las columnas), puedes usar `axis=1`.

```python
# Definir una función que calcule el salario promedio de cada fila
def salario_promedio(row):
    return (row['Salario'] + row['Salario_Aumento']) / 2

# Aplicar la función a todas las filas
df['Salario_Promedio'] = df.apply(salario_promedio, axis=1)
print(df)
```

**Salida**:
```
   Nombre  Edad  Salario  Salario_Aumento  Salario_Promedio
0     Ana    23     2500            2750.0             2625.0
1    Luis    30     3000            3300.0             3150.0
2  Carlos    25     3500            3850.0             3675.0
3   Marta    27     3200            3520.0             3360.0
4    Juan    28     2800            3080.0             2940.0
```

---

#### 2. **Aplicar funciones a columnas con `map()`**

La función `map()` es útil cuando deseas aplicar una función a una **columna específica** de forma más eficiente, especialmente cuando trabajas con valores de tipo `string`.

- **Aplicar una función que transforme los datos**:

Por ejemplo, si quieres transformar los nombres de una columna a mayúsculas:

```python
# Convertir los nombres a mayúsculas usando map
df['Nombre_Mayus'] = df['Nombre'].map(lambda x: x.upper())
print(df)
```

**Salida**:
```
   Nombre  Edad  Salario  Salario_Aumento  Salario_Promedio Nombre_Mayus
0     Ana    23     2500            2750.0             2625.0          ANA
1    Luis    30     3000            3300.0             3150.0         LUIS
2  Carlos    25     3500            3850.0             3675.0        CARLOS
3   Marta    27     3200            3520.0             3360.0         MARTA
4    Juan    28     2800            3080.0             2940.0         JUAN
```

---

#### 3. **Transformar datos con `applymap()`**

Si necesitas aplicar una función a **todos los elementos** de un DataFrame, puedes usar `applymap()`. Esto es útil cuando quieres hacer transformaciones generales en todo el DataFrame.

```python
# Aplicar una función que convierta todos los valores en el DataFrame a su valor absoluto
df_numero_abs = df[['Edad', 'Salario', 'Salario_Aumento']].applymap(abs)
print(df_numero_abs)
```

**Salida**:
```
   Edad  Salario  Salario_Aumento
0    23     2500            2750.0
1    30     3000            3300.0
2    25     3500            3850.0
3    27     3200            3520.0
4    28     2800            3080.0
```

---

#### 4. **Filtrar con `loc[]` y `iloc[]`**

Si deseas filtrar las filas o columnas utilizando condiciones más complejas, puedes usar `loc[]` (para etiquetas) o `iloc[]` (para posiciones).

- **Filtrar usando `loc[]`**:

```python
# Filtrar filas donde la edad sea mayor a 25, y seleccionar las columnas 'Nombre' y 'Salario'
df_filtrado_loc = df.loc[df['Edad'] > 25, ['Nombre', 'Salario']]
print(df_filtrado_loc)
```

**Salida**:
```
   Nombre  Salario
1    Luis     3000
3   Marta     3200
4    Juan     2800
```

- **Filtrar usando `iloc[]`**:

```python
# Filtrar las primeras 3 filas y las primeras 2 columnas
df_filtrado_iloc = df.iloc[:3, :2]
print(df_filtrado_iloc)
```

**Salida**:
```
   Nombre  Edad
0     Ana    23
1    Luis    30
2  Carlos    25
```

---

Con estas herramientas, puedes **aplicar funciones** de manera flexible a los datos de un DataFrame, ya sea a nivel de columna, fila o todo el DataFrame, lo que te permitirá transformar y personalizar los datos según lo necesites.

---

¿Listo para continuar con el **Paso 10/10: Cómo guardar y exportar datos en Pandas**? 😊

### **Paso 10/10: Cómo guardar y exportar datos en Pandas**

En este paso final, aprenderás cómo **guardar** y **exportar** tus datos de un DataFrame a diferentes formatos de archivo, como **CSV**, **Excel**, **JSON**, y más. Estas son operaciones esenciales cuando deseas compartir o almacenar tus datos después de haber realizado el análisis.

---

#### 1. **Guardar un DataFrame en un archivo CSV**

El formato **CSV** (Comma-Separated Values) es uno de los formatos más comunes para almacenar datos tabulares, y Pandas facilita la exportación de un DataFrame a este formato.

```python
# Guardar el DataFrame en un archivo CSV
df.to_csv('datos.csv', index=False)  # index=False evita guardar el índice
```

**Explicación**:
- El parámetro `index=False` evita que el índice del DataFrame se guarde como una columna adicional en el archivo CSV. Si deseas incluir el índice, simplemente omite este parámetro.

**Resultado**:
- El archivo `datos.csv` se guardará en el directorio de trabajo actual.

---

#### 2. **Guardar un DataFrame en un archivo Excel**

También puedes guardar un DataFrame como un archivo **Excel** usando `to_excel()`. Asegúrate de tener instalada la librería `openpyxl` o `xlsxwriter` para escribir archivos de Excel.

```python
# Guardar el DataFrame en un archivo Excel
df.to_excel('datos.xlsx', index=False)
```

**Explicación**:
- Como en el caso del CSV, el parámetro `index=False` previene que el índice sea guardado como una columna extra.
- Este archivo se guardará con la extensión `.xlsx`.

---

#### 3. **Guardar un DataFrame en un archivo JSON**

Si necesitas exportar los datos a un formato **JSON** (JavaScript Object Notation), que es útil para datos estructurados, puedes hacerlo de manera fácil con `to_json()`.

```python
# Guardar el DataFrame en un archivo JSON
df.to_json('datos.json')
```

**Explicación**:
- El formato JSON es ampliamente utilizado para la transmisión de datos en aplicaciones web.
- Por defecto, `to_json()` guarda el archivo en un formato estructurado que es fácilmente legible para otros lenguajes de programación.

---

#### 4. **Guardar un DataFrame en otros formatos**

Pandas también soporta la exportación a otros formatos, como **HTML**, **SQL** o **Parquet**. Aquí hay algunos ejemplos:

- **Guardar en formato HTML**:

```python
# Guardar el DataFrame en un archivo HTML
df.to_html('datos.html')
```

- **Guardar en una base de datos SQL**:

```python
from sqlalchemy import create_engine

# Crear una conexión a una base de datos SQLite
engine = create_engine('sqlite:///datos.db')

# Guardar el DataFrame en una tabla de la base de datos
df.to_sql('tabla_datos', engine, index=False, if_exists='replace')
```

**Explicación**:
- `to_sql()` guarda el DataFrame en una tabla de una base de datos SQL. El parámetro `if_exists='replace'` reemplaza la tabla si ya existe, pero puedes cambiarlo a `'append'` para agregar los datos a la tabla existente.

---

#### 5. **Leer los datos guardados**

Para asegurarte de que tus datos se han guardado correctamente, puedes volver a leer el archivo y cargarlo en un nuevo DataFrame.

- **Leer un archivo CSV**:

```python
df_leido_csv = pd.read_csv('datos.csv')
print(df_leido_csv)
```

- **Leer un archivo Excel**:

```python
df_leido_excel = pd.read_excel('datos.xlsx')
print(df_leido_excel)
```

- **Leer un archivo JSON**:

```python
df_leido_json = pd.read_json('datos.json')
print(df_leido_json)
```

---

#### Resumen

Al final de este recorrido de 10 pasos, ahora sabes cómo:

- Crear y manipular DataFrames en Pandas.
- Realizar operaciones de selección, filtrado y transformación de datos.
- Ordenar y agrupar datos.
- Aplicar funciones personalizadas a los datos.
- Exportar los resultados a formatos comunes como CSV, Excel y JSON.

---

¡Felicidades! Has aprendido los fundamentos de **Pandas** y ahora puedes empezar a aplicar estas habilidades en tus propios proyectos de análisis de datos. 🎉

¿Hay algo más en lo que pueda ayudarte con Pandas o cualquier otro tema? 😊
