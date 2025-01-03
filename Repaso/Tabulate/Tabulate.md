¡Perfecto! Vamos a aprender a usar la librería `tabulate` paso a paso en 10 etapas. Empezaremos desde el principio para que puedas comprender cómo sacarle el máximo provecho a esta herramienta. 😊

---

### **Paso 1/10: Introducción a `tabulate` y su instalación**

#### ¿Qué es `tabulate`?
`tabulate` es una librería de Python diseñada para generar **tablas formateadas** de manera sencilla y legible. Es especialmente útil cuando necesitas presentar datos de manera clara, ya sea en la consola, en archivos de texto o incluso en formatos más complejos como HTML o LaTeX.

#### Características principales:
- **Fácil de usar** para generar tablas con cualquier tipo de datos.
- **Soporte para diferentes formatos de salida**: texto, Markdown, HTML, LaTeX, CSV, etc.
- **Alineación de datos**: permite alinear las columnas a la izquierda, derecha o centrado.

#### Instalación de `tabulate`:
Para empezar, debes instalar la librería si aún no lo has hecho. Puedes instalarla mediante pip:

```bash
pip install tabulate
```

#### Primer paso práctico:
Una vez instalado, puedes empezar a usar `tabulate`. A continuación, te muestro cómo importar la librería y crear tu primera tabla en la consola.

```python
from tabulate import tabulate

# Datos que queremos mostrar en la tabla
data = [
    ["Juan", 28, "Programador"],
    ["Ana", 24, "Diseñadora"],
    ["Luis", 30, "Ingeniero"]
]

# Encabezados de las columnas
headers = ["Nombre", "Edad", "Profesión"]

# Crear la tabla con formato "grid" (con bordes)
print(tabulate(data, headers=headers, tablefmt="grid"))
```

**Resultado en la consola**:

```
+---------+-------+------------+
| Nombre  | Edad  | Profesión  |
+---------+-------+------------+
| Juan    | 28    | Programador|
| Ana     | 24    | Diseñadora |
| Luis    | 30    | Ingeniero  |
+---------+-------+------------+
```

---

Este es el primer paso: aprender a instalar y usar `tabulate` para crear una tabla básica con datos.

¿Te gustaría que continuemos con el **Paso 2/10**? 😊

### **Paso 2/10: Usar diferentes formatos para las tablas con `tabulate`**

En este paso, aprenderemos cómo usar diferentes **formatos de tabla** con la librería `tabulate`. La librería soporta varios estilos de formato que te permiten presentar tus tablas de manera más flexible, ya sea para consola o para ser exportadas a otros formatos como HTML, LaTeX o Markdown.

#### **1. Formatos más comunes**

Al utilizar `tabulate`, puedes elegir entre varios tipos de formato para que las tablas se vean como deseas. Aquí te muestro algunos de los más utilizados:

##### **1.1 Formato "plain"** (sin bordes)

Este es el formato más simple, sin bordes ni líneas adicionales, solo los datos de la tabla.

```python
from tabulate import tabulate

data = [
    ["Juan", 28, "Programador"],
    ["Ana", 24, "Diseñadora"],
    ["Luis", 30, "Ingeniero"]
]

headers = ["Nombre", "Edad", "Profesión"]

# Mostrar la tabla en formato "plain"
print(tabulate(data, headers=headers, tablefmt="plain"))
```

**Resultado**:
```
Nombre    Edad  Profesión
------  ------  ------------
Juan      28    Programador
Ana       24    Diseñadora
Luis      30    Ingeniero
```

##### **1.2 Formato "grid"** (con bordes)

El formato "grid" agrega bordes a la tabla, lo que hace que se vea más estructurada.

```python
# Mostrar la tabla en formato "grid"
print(tabulate(data, headers=headers, tablefmt="grid"))
```

**Resultado**:
```
+---------+-------+------------+
| Nombre  | Edad  | Profesión  |
+---------+-------+------------+
| Juan    | 28    | Programador|
| Ana     | 24    | Diseñadora |
| Luis    | 30    | Ingeniero  |
+---------+-------+------------+
```

##### **1.3 Formato "pipe"** (similar a Markdown)

Este formato usa el estilo de Markdown, con líneas verticales `|` separando las columnas. Es útil si necesitas mostrar la tabla en un documento Markdown.

```python
# Mostrar la tabla en formato "pipe"
print(tabulate(data, headers=headers, tablefmt="pipe"))
```

**Resultado**:
```
| Nombre | Edad | Profesión  |
|--------|------|------------|
| Juan   | 28   | Programador|
| Ana    | 24   | Diseñadora |
| Luis   | 30   | Ingeniero  |
```

##### **1.4 Formato "html"** (para web)

Si estás trabajando en aplicaciones web, puedes generar la tabla en formato HTML para mostrarla en una página web.

```python
# Mostrar la tabla en formato HTML
print(tabulate(data, headers=headers, tablefmt="html"))
```

**Resultado**:
```html
<table>
<thead>
<tr><th>Nombre</th><th>Edad</th><th>Profesión</th></tr>
</thead>
<tbody>
<tr><td>Juan</td><td>28</td><td>Programador</td></tr>
<tr><td>Ana</td><td>24</td><td>Diseñadora</td></tr>
<tr><td>Luis</td><td>30</td><td>Ingeniero</td></tr>
</tbody>
</table>
```

##### **1.5 Formato "latex"** (para documentos LaTeX)

Este formato es ideal para generar tablas que luego se incluirán en documentos LaTeX.

```python
# Mostrar la tabla en formato LaTeX
print(tabulate(data, headers=headers, tablefmt="latex"))
```

**Resultado**:
```latex
\begin{tabular}{|l|l|l|}
\hline
Nombre & Edad & Profesión \\
\hline
Juan & 28 & Programador \\
Ana & 24 & Diseñadora \\
Luis & 30 & Ingeniero \\
\hline
\end{tabular}
```

#### **2. Resumen**

- **plain**: Formato sin bordes, solo los datos.
- **grid**: Agrega bordes a la tabla.
- **pipe**: Estilo Markdown, muy útil para documentación.
- **html**: Para mostrar en páginas web.
- **latex**: Para usar en documentos LaTeX.

---

Este paso te ha enseñado cómo cambiar el formato de las tablas para adaptarlas a diferentes necesidades. En el siguiente paso, exploraremos cómo **personalizar la alineación de las columnas**.

¿Listo para continuar con el **Paso 3/10**? 😊

### **Paso 3/10: Personalización de la alineación de las columnas**

En este paso, vamos a aprender cómo **alinear los datos de las columnas** de la tabla. `tabulate` te permite ajustar la alineación de las celdas para que los datos se vean más ordenados y sean más fáciles de leer.

#### **1. Tipos de alineación**

Existen tres tipos principales de alineación que puedes aplicar a las columnas:

- **Alineación a la izquierda** (`'left'`)
- **Alineación al centro** (`'center'`)
- **Alineación a la derecha** (`'right'`)

#### **2. Sintaxis para la alineación**

Cuando llamas a la función `tabulate()`, puedes utilizar el parámetro `stralign` para definir cómo se alinearán las columnas. También puedes usar el parámetro `numalign` para alinear las columnas que contengan números.

#### **3. Ejemplo con alineación personalizada**

Vamos a crear una tabla y alinear las columnas de diferentes maneras.

```python
from tabulate import tabulate

# Datos de ejemplo
data = [
    ["Juan", 28, "Programador"],
    ["Ana", 24, "Diseñadora"],
    ["Luis", 30, "Ingeniero"]
]

# Encabezados de la tabla
headers = ["Nombre", "Edad", "Profesión"]

# Alinear las columnas:
# - Nombre alineado a la izquierda
# - Edad alineada a la derecha
# - Profesión alineada al centro
print(tabulate(data, headers=headers, tablefmt="grid", stralign="left", numalign="right"))
```

**Resultado**:
```
+---------+-------+------------+
| Nombre  | Edad  | Profesión  |
+---------+-------+------------+
| Juan    |    28 | Programador|
| Ana     |    24 | Diseñadora |
| Luis    |    30 | Ingeniero  |
+---------+-------+------------+
```

En este caso:
- La columna **Nombre** se alinea a la izquierda.
- La columna **Edad** se alinea a la derecha (porque es un número).
- La columna **Profesión** se mantiene centrada de manera predeterminada, pero también se puede especificar su alineación si lo deseas.

#### **4. Alineación individual por columna**

Si deseas alinear cada columna de forma diferente, puedes usar un diccionario con las claves `'stralign'` y `'numalign'` para especificar el comportamiento de cada columna.

```python
# Alinear cada columna de manera diferente
alignment = {'Nombre': 'left', 'Edad': 'right', 'Profesión': 'center'}

print(tabulate(data, headers=headers, tablefmt="grid", colalign=[alignment[col] for col in headers]))
```

**Resultado**:
```
+---------+-------+------------+
| Nombre  | Edad  | Profesión  |
+---------+-------+------------+
| Juan    |    28 | Programador|
| Ana     |    24 | Diseñadora |
| Luis    |    30 | Ingeniero  |
+---------+-------+------------+
```

#### **5. Resumen**

- **Alineación de texto**: Puedes alinear el texto de las columnas a la izquierda, derecha o al centro.
- **Alineación de números**: Usa `numalign="right"` para alinear los números a la derecha.
- **Columna por columna**: Puedes personalizar la alineación para cada columna individualmente, si lo deseas.

---

Este paso te ha enseñado a cómo alinear las columnas de manera adecuada para hacer que los datos se vean más organizados y fáciles de leer.

En el siguiente paso, exploraremos cómo **mostrar tablas con datos provenientes de diccionarios**.

¿Te gustaría continuar con el **Paso 4/10**? 😊

### **Paso 4/10: Crear tablas usando diccionarios**

En este paso, vamos a aprender cómo crear tablas usando **diccionarios** en lugar de listas. Los diccionarios son estructuras de datos que contienen claves y valores, lo que puede hacer que tu código sea más legible y fácil de mantener, especialmente cuando trabajas con conjuntos de datos más complejos.

#### **1. Uso de diccionarios con `tabulate`**

En lugar de representar los datos como listas de listas, puedes usar un diccionario donde las claves sean los nombres de las columnas y los valores sean las filas de datos.

#### **2. Sintaxis para usar diccionarios en `tabulate`**

```python
from tabulate import tabulate

# Datos como diccionario
data_dict = [
    {"Nombre": "Juan", "Edad": 28, "Profesión": "Programador"},
    {"Nombre": "Ana", "Edad": 24, "Profesión": "Diseñadora"},
    {"Nombre": "Luis", "Edad": 30, "Profesión": "Ingeniero"}
]

# Crear la tabla a partir del diccionario
headers = ["Nombre", "Edad", "Profesión"]
print(tabulate(data_dict, headers=headers, tablefmt="grid"))
```

**Resultado**:
```
+---------+-------+------------+
| Nombre  | Edad  | Profesión  |
+---------+-------+------------+
| Juan    | 28    | Programador|
| Ana     | 24    | Diseñadora |
| Luis    | 30    | Ingeniero  |
+---------+-------+------------+
```

#### **3. ¿Cómo funciona esto?**

- **Claves del diccionario**: Cada clave en el diccionario (`"Nombre"`, `"Edad"`, `"Profesión"`) se convierte en una columna de la tabla.
- **Valores del diccionario**: Cada valor correspondiente a las claves es una fila de datos que será colocada en su respectiva columna.

#### **4. Ventajas de usar diccionarios**:

- **Mayor legibilidad**: Los nombres de las columnas se obtienen directamente de las claves del diccionario, lo que hace que el código sea más fácil de leer y mantener.
- **Mayor flexibilidad**: Puedes acceder a los valores de las columnas mediante sus claves, lo que resulta en un código más flexible y robusto.

#### **5. Ejemplo de una tabla con diccionario y alineación personalizada**:

Podemos combinar diccionarios con alineación personalizada. Por ejemplo, queremos que la columna de "Edad" esté alineada a la derecha y "Profesión" centrada.

```python
# Alinear "Edad" a la derecha y "Profesión" al centro
alignment = {'Edad': 'right', 'Profesión': 'center'}

print(tabulate(data_dict, headers=headers, tablefmt="grid", colalign=[alignment.get(col, 'left') for col in headers]))
```

**Resultado**:
```
+---------+-------+------------+
| Nombre  | Edad  | Profesión  |
+---------+-------+------------+
| Juan    |    28 | Programador|
| Ana     |    24 | Diseñadora |
| Luis    |    30 | Ingeniero  |
+---------+-------+------------+
```

En este ejemplo:
- Las claves del diccionario (`"Nombre"`, `"Edad"`, `"Profesión"`) determinan las columnas.
- Usamos `colalign` para alinear la columna "Edad" a la derecha y "Profesión" al centro.

#### **6. Resumen**

- Puedes usar diccionarios en lugar de listas para crear tablas con `tabulate`.
- Las **claves** del diccionario se usan como encabezados de columna.
- Los **valores** del diccionario se colocan como filas.
- Es posible personalizar la alineación de las columnas de manera sencilla.

---

Este paso te ha mostrado cómo crear tablas usando diccionarios, lo cual mejora la legibilidad y flexibilidad del código.

En el siguiente paso, exploraremos cómo **filtrar y seleccionar solo algunas columnas o filas** para mostrar en la tabla.

¿Listo para continuar con el **Paso 5/10**? 😊

### **Paso 5/10: Filtrar y seleccionar columnas o filas específicas**

En este paso, vamos a aprender a **filtrar** y **seleccionar columnas o filas específicas** en nuestras tablas generadas con `tabulate`. Esto es útil cuando quieres mostrar solo una parte de los datos, por ejemplo, si tienes un conjunto de datos grande pero solo te interesa mostrar ciertos valores.

#### **1. Seleccionar columnas específicas**

Cuando tienes una tabla con varias columnas, puedes elegir mostrar solo algunas de ellas.

##### **Ejemplo: Mostrar solo ciertas columnas**

Supongamos que tienes una tabla con información sobre personas, pero solo deseas mostrar los nombres y las edades.

```python
from tabulate import tabulate

# Datos como diccionario
data_dict = [
    {"Nombre": "Juan", "Edad": 28, "Profesión": "Programador"},
    {"Nombre": "Ana", "Edad": 24, "Profesión": "Diseñadora"},
    {"Nombre": "Luis", "Edad": 30, "Profesión": "Ingeniero"}
]

# Seleccionar solo las columnas "Nombre" y "Edad"
filtered_data = [{"Nombre": row["Nombre"], "Edad": row["Edad"]} for row in data_dict]

# Mostrar la tabla filtrada
headers = ["Nombre", "Edad"]
print(tabulate(filtered_data, headers=headers, tablefmt="grid"))
```

**Resultado**:
```
+---------+-------+
| Nombre  | Edad  |
+---------+-------+
| Juan    | 28    |
| Ana     | 24    |
| Luis    | 30    |
+---------+-------+
```

En este ejemplo, hemos creado una nueva lista `filtered_data` que solo contiene las columnas "Nombre" y "Edad", eliminando "Profesión" de la tabla.

#### **2. Seleccionar filas específicas**

También puedes filtrar las filas de la tabla. Por ejemplo, tal vez solo quieras mostrar las personas que tienen más de 25 años.

##### **Ejemplo: Filtrar filas por una condición**

```python
# Filtrar las filas para mostrar solo las personas con más de 25 años
filtered_rows = [row for row in data_dict if row["Edad"] > 25]

# Mostrar la tabla filtrada
print(tabulate(filtered_rows, headers=headers, tablefmt="grid"))
```

**Resultado**:
```
+---------+-------+------------+
| Nombre  | Edad  | Profesión  |
+---------+-------+------------+
| Juan    | 28    | Programador|
| Luis    | 30    | Ingeniero  |
+---------+-------+------------+
```

En este ejemplo, solo se muestran las personas cuya edad es mayor a 25 años (Juan y Luis).

#### **3. Filtrar tanto filas como columnas**

Es posible combinar ambos filtros. Por ejemplo, quieres mostrar solo las personas mayores de 25 años, pero solo las columnas "Nombre" y "Edad".

```python
# Filtrar las filas por edad > 25 y seleccionar solo las columnas "Nombre" y "Edad"
filtered_data = [{"Nombre": row["Nombre"], "Edad": row["Edad"]} for row in data_dict if row["Edad"] > 25]

# Mostrar la tabla filtrada
print(tabulate(filtered_data, headers=["Nombre", "Edad"], tablefmt="grid"))
```

**Resultado**:
```
+---------+-------+
| Nombre  | Edad  |
+---------+-------+
| Juan    | 28    |
| Luis    | 30    |
+---------+-------+
```

#### **4. Resumen**

- **Filtrar columnas**: Puedes crear una nueva lista de diccionarios que contenga solo las columnas que te interesan.
- **Filtrar filas**: Puedes usar una condición (como `if row["Edad"] > 25`) para mostrar solo las filas que cumplen con la condición.
- **Combinación de filtros**: Es posible aplicar ambos filtros simultáneamente para seleccionar las columnas y filas que deseas.

---

Este paso te ha enseñado cómo **filtrar y seleccionar columnas y filas** específicas, lo cual te permite trabajar con subconjuntos de tus datos.

En el siguiente paso, exploraremos cómo **trabajar con datos numéricos** y mostrar estadísticas o realizar cálculos con `tabulate`.

¿Te gustaría continuar con el **Paso 6/10**? 😊

### **Paso 6/10: Trabajar con datos numéricos y mostrar estadísticas**

En este paso, aprenderemos cómo trabajar con **datos numéricos** en las tablas generadas con `tabulate`, y cómo puedes **mostrar estadísticas** o realizar cálculos, como sumas o promedios, sobre las columnas numéricas.

#### **1. Mostrar cálculos simples (sumas, promedios, etc.)**

Puedes realizar cálculos sobre las columnas de datos numéricos antes de mostrar la tabla. Aquí te mostraré cómo hacerlo.

##### **Ejemplo 1: Sumar los valores de una columna numérica**

Supongamos que tienes una tabla con las edades de varias personas y quieres mostrar la **suma total de las edades**.

```python
from tabulate import tabulate

# Datos como diccionario
data_dict = [
    {"Nombre": "Juan", "Edad": 28, "Profesión": "Programador"},
    {"Nombre": "Ana", "Edad": 24, "Profesión": "Diseñadora"},
    {"Nombre": "Luis", "Edad": 30, "Profesión": "Ingeniero"}
]

# Calcular la suma de las edades
total_edad = sum(row["Edad"] for row in data_dict)

# Mostrar la tabla
headers = ["Nombre", "Edad", "Profesión"]
print(tabulate(data_dict, headers=headers, tablefmt="grid"))

# Mostrar el cálculo de la suma
print(f"\nSuma total de edades: {total_edad}")
```

**Resultado**:
```
+---------+-------+------------+
| Nombre  | Edad  | Profesión  |
+---------+-------+------------+
| Juan    | 28    | Programador|
| Ana     | 24    | Diseñadora |
| Luis    | 30    | Ingeniero  |
+---------+-------+------------+

Suma total de edades: 82
```

Aquí, hemos mostrado cómo calcular la **suma de las edades** y luego mostrarla en la consola.

##### **Ejemplo 2: Calcular el promedio de una columna numérica**

Otra operación común es calcular el **promedio** de una columna numérica. Esto es útil, por ejemplo, para obtener la edad promedio de un grupo de personas.

```python
# Calcular el promedio de las edades
promedio_edad = sum(row["Edad"] for row in data_dict) / len(data_dict)

# Mostrar la tabla y el cálculo
print(tabulate(data_dict, headers=headers, tablefmt="grid"))
print(f"\nPromedio de edades: {promedio_edad:.2f}")
```

**Resultado**:
```
+---------+-------+------------+
| Nombre  | Edad  | Profesión  |
+---------+-------+------------+
| Juan    | 28    | Programador|
| Ana     | 24    | Diseñadora |
| Luis    | 30    | Ingeniero  |
+---------+-------+------------+

Promedio de edades: 26.00
```

En este ejemplo, hemos calculado el **promedio de las edades** y lo hemos mostrado con dos decimales.

#### **2. Agregar filas con estadísticas a la tabla**

También puedes agregar una **fila adicional** a la tabla con las estadísticas que hayas calculado, como la suma o el promedio. Esto se puede hacer agregando una nueva fila a la lista de datos antes de generar la tabla.

```python
# Agregar una fila con el cálculo del promedio
data_dict.append({"Nombre": "Promedio", "Edad": promedio_edad, "Profesión": ""})

# Mostrar la tabla con la fila de promedio
print(tabulate(data_dict, headers=headers, tablefmt="grid"))
```

**Resultado**:
```
+-----------+-------+------------+
| Nombre    | Edad  | Profesión  |
+-----------+-------+------------+
| Juan      | 28    | Programador|
| Ana       | 24    | Diseñadora |
| Luis      | 30    | Ingeniero  |
| Promedio  | 26.0  |            |
+-----------+-------+------------+
```

Aquí hemos agregado una fila con el **promedio de edades** al final de la tabla.

#### **3. Trabajar con otras estadísticas (mínimo, máximo, etc.)**

También puedes calcular otras estadísticas, como el valor **mínimo** o **máximo** de una columna.

```python
# Calcular el valor mínimo y máximo de las edades
edad_minima = min(row["Edad"] for row in data_dict)
edad_maxima = max(row["Edad"] for row in data_dict)

# Mostrar las estadísticas
print(f"Edad mínima: {edad_minima}")
print(f"Edad máxima: {edad_maxima}")
```

**Resultado**:
```
Edad mínima: 24
Edad máxima: 30
```

#### **4. Resumen**

- **Suma y promedio**: Puedes calcular la suma y el promedio de columnas numéricas.
- **Estadísticas adicionales**: También puedes calcular otras estadísticas como mínimo, máximo, etc.
- **Agregar estadísticas a la tabla**: Es posible agregar una fila con estadísticas calculadas, como el promedio o la suma.

---

Este paso te ha mostrado cómo trabajar con **datos numéricos** y calcular estadísticas como sumas, promedios, y otros valores. Ahora sabes cómo realizar estos cálculos y mostrarlos de forma clara en tu tabla.

En el siguiente paso, exploraremos cómo **ordenar** los datos de la tabla según una o más columnas.

¿Te gustaría continuar con el **Paso 7/10**? 😊

### **Paso 7/10: Ordenar datos por una o más columnas**

En este paso, aprenderemos cómo **ordenar los datos** de la tabla según una o más columnas. Esto es útil cuando deseas mostrar la información de forma ordenada, como ordenar por edades, nombres alfabéticamente, o cualquier otro criterio relevante.

#### **1. Ordenar por una columna**

Puedes ordenar los datos de la tabla usando la función `sorted()` de Python. El parámetro `key` se usa para especificar la columna por la que deseas ordenar.

##### **Ejemplo 1: Ordenar por una columna (Edad)**

Vamos a ordenar los datos por la columna "Edad" de forma ascendente (de menor a mayor).

```python
from tabulate import tabulate

# Datos como diccionario
data_dict = [
    {"Nombre": "Juan", "Edad": 28, "Profesión": "Programador"},
    {"Nombre": "Ana", "Edad": 24, "Profesión": "Diseñadora"},
    {"Nombre": "Luis", "Edad": 30, "Profesión": "Ingeniero"}
]

# Ordenar por la columna "Edad" de forma ascendente
sorted_data = sorted(data_dict, key=lambda x: x["Edad"])

# Mostrar la tabla ordenada
headers = ["Nombre", "Edad", "Profesión"]
print(tabulate(sorted_data, headers=headers, tablefmt="grid"))
```

**Resultado**:
```
+---------+-------+------------+
| Nombre  | Edad  | Profesión  |
+---------+-------+------------+
| Ana     | 24    | Diseñadora |
| Juan    | 28    | Programador|
| Luis    | 30    | Ingeniero  |
+---------+-------+------------+
```

Aquí hemos utilizado `sorted()` para ordenar las filas según la edad en orden ascendente.

#### **2. Ordenar por varias columnas**

También puedes ordenar los datos por **varias columnas**. Por ejemplo, quieres ordenar primero por la edad y luego por el nombre de forma alfabética.

##### **Ejemplo 2: Ordenar por varias columnas (Edad, luego Nombre)**

```python
# Ordenar por "Edad" (ascendente) y luego por "Nombre" (alfabéticamente)
sorted_data_multiple = sorted(data_dict, key=lambda x: (x["Edad"], x["Nombre"]))

# Mostrar la tabla ordenada
print(tabulate(sorted_data_multiple, headers=headers, tablefmt="grid"))
```

**Resultado**:
```
+---------+-------+------------+
| Nombre  | Edad  | Profesión  |
+---------+-------+------------+
| Ana     | 24    | Diseñadora |
| Juan    | 28    | Programador|
| Luis    | 30    | Ingeniero  |
+---------+-------+------------+
```

En este caso, hemos usado una **tupla** dentro de la función `lambda` para ordenar primero por "Edad" y luego por "Nombre". Python ordenará las filas de acuerdo con estos dos criterios.

#### **3. Ordenar de forma descendente**

Si deseas ordenar en orden **descendente** (de mayor a menor), puedes usar el parámetro `reverse=True`.

##### **Ejemplo 3: Ordenar por "Edad" de forma descendente**

```python
# Ordenar por "Edad" de forma descendente
sorted_data_desc = sorted(data_dict, key=lambda x: x["Edad"], reverse=True)

# Mostrar la tabla ordenada
print(tabulate(sorted_data_desc, headers=headers, tablefmt="grid"))
```

**Resultado**:
```
+---------+-------+------------+
| Nombre  | Edad  | Profesión  |
+---------+-------+------------+
| Luis    | 30    | Ingeniero  |
| Juan    | 28    | Programador|
| Ana     | 24    | Diseñadora |
+---------+-------+------------+
```

Aquí hemos ordenado las edades de mayor a menor usando `reverse=True`.

#### **4. Resumen**

- **Ordenar por una columna**: Puedes ordenar los datos usando la función `sorted()` y especificar la columna con el parámetro `key`.
- **Ordenar por varias columnas**: Si deseas ordenar por más de una columna, puedes usar una **tupla** en el parámetro `key`.
- **Ordenar en orden descendente**: Usa `reverse=True` para invertir el orden y ordenar de mayor a menor.

---

Este paso te ha enseñado cómo **ordenar** los datos de una tabla por una o más columnas, y cómo hacerlo tanto en orden ascendente como descendente.

En el siguiente paso, veremos cómo **dar formato** a la tabla, como cambiar el estilo, agregar bordes o personalizar los colores.

¿Te gustaría continuar con el **Paso 8/10**? 😊

### **Paso 8/10: Dar formato a la tabla (estilos, bordes, colores)**

En este paso, aprenderemos a **dar formato** a la tabla generada con `tabulate`, como agregar bordes, cambiar colores, o darle estilo a las celdas. Aunque `tabulate` no tiene soporte directo para colores y estilos avanzados, podemos aplicar ciertos formatos como bordes y alineación. Sin embargo, para una mayor personalización (como colores o fuentes), se recomienda usar bibliotecas adicionales como `xlsxwriter`, pero aún así te mostraré cómo mejorar la presentación con lo que ofrece `tabulate`.

#### **1. Personalizar el formato de la tabla**

El parámetro `tablefmt` en `tabulate` te permite elegir entre varios estilos de tablas. Algunos de los más comunes son:

- `plain`: tabla sin bordes ni líneas.
- `grid`: tabla con bordes.
- `pipe`: tabla estilo Markdown.
- `html`: tabla en formato HTML.

##### **Ejemplo 1: Cambiar el estilo de la tabla**

```python
from tabulate import tabulate

# Datos como diccionario
data_dict = [
    {"Nombre": "Juan", "Edad": 28, "Profesión": "Programador"},
    {"Nombre": "Ana", "Edad": 24, "Profesión": "Diseñadora"},
    {"Nombre": "Luis", "Edad": 30, "Profesión": "Ingeniero"}
]

# Mostrar la tabla con formato de cuadrícula
headers = ["Nombre", "Edad", "Profesión"]
print(tabulate(data_dict, headers=headers, tablefmt="grid"))
```

**Resultado (usando `grid`)**:
```
+---------+-------+------------+
| Nombre  | Edad  | Profesión  |
+---------+-------+------------+
| Juan    | 28    | Programador|
| Ana     | 24    | Diseñadora |
| Luis    | 30    | Ingeniero  |
+---------+-------+------------+
```

Al cambiar el formato de la tabla usando `tablefmt="grid"`, la tabla tiene bordes alrededor de cada celda.

##### **Ejemplo 2: Usar formato de tabla Markdown**

```python
# Mostrar la tabla en formato Markdown
print(tabulate(data_dict, headers=headers, tablefmt="pipe"))
```

**Resultado (usando `pipe`)**:
```
| Nombre | Edad | Profesión  |
|--------|------|------------|
| Juan   | 28   | Programador|
| Ana    | 24   | Diseñadora |
| Luis   | 30   | Ingeniero  |
```

El formato `pipe` es útil si deseas mostrar la tabla en un formato compatible con Markdown.

#### **2. Alinear el contenido de las celdas**

Puedes ajustar la alineación del contenido en las celdas de la tabla. Por defecto, los números se alinean a la derecha y las cadenas de texto a la izquierda. Sin embargo, puedes cambiar esto usando el parámetro `numalign` (para los números) y `stralign` (para las cadenas).

##### **Ejemplo 3: Cambiar la alineación de las columnas**

```python
# Alinear las columnas de forma personalizada
print(tabulate(data_dict, headers=headers, tablefmt="grid", stralign="center", numalign="right"))
```

**Resultado**:
```
+---------+-------+------------+
| Nombre  | Edad  | Profesión  |
+---------+-------+------------+
|  Juan   |  28   | Programador|
|  Ana    |  24   | Diseñadora |
|  Luis   |  30   | Ingeniero  |
+---------+-------+------------+
```

En este caso, hemos centrado las columnas de texto (`stralign="center"`) y alineado los números a la derecha (`numalign="right"`).

#### **3. Personalizar bordes**

Puedes usar el parámetro `tablefmt` con el valor `grid` para mostrar bordes, pero no es posible personalizar el grosor o color de los bordes en `tabulate`. Si necesitas más personalización, como cambiar el color de las celdas o agregar bordes específicos, necesitarías usar otra biblioteca como `xlsxwriter`.

#### **4. Crear tablas con colores (limitado)**

Aunque `tabulate` no permite establecer colores directamente, puedes **agregar colores** si exportas los datos a HTML y luego trabajas con estilos CSS.

##### **Ejemplo 4: Exportar la tabla a HTML con estilos básicos**

```python
# Mostrar la tabla en formato HTML con etiquetas <style>
html_table = tabulate(data_dict, headers=headers, tablefmt="html")

# Imprimir la tabla en HTML
print(html_table)
```

**Resultado (en formato HTML)**:
```html
<table>
<thead>
<tr><th>Nombre  </th><th>Edad  </th><th>Profesión</th></tr>
</thead>
<tbody>
<tr><td>Juan    </td><td>28     </td><td>Programador</td></tr>
<tr><td>Ana     </td><td>24     </td><td>Diseñadora </td></tr>
<tr><td>Luis    </td><td>30     </td><td>Ingeniero  </td></tr>
</tbody>
</table>
```

Puedes agregar estilos CSS al código HTML generado para darle color y personalizar la apariencia.

#### **5. Resumen**

- **Personalización del formato**: Usando el parámetro `tablefmt`, puedes elegir entre varios estilos como `grid`, `pipe` o `html`.
- **Alineación**: Puedes controlar la alineación del texto y los números en las celdas usando `stralign` y `numalign`.
- **HTML y CSS**: Para una personalización más avanzada, puedes exportar la tabla a HTML y agregar estilos CSS.

---

Este paso te ha mostrado cómo **dar formato** a las tablas generadas con `tabulate`, desde cambiar el estilo de las tablas hasta ajustar la alineación y exportar a HTML.

En el siguiente paso, veremos cómo **trabajar con grandes conjuntos de datos**, como paginar o dividir grandes tablas en partes más manejables.

¿Te gustaría continuar con el **Paso 9/10**? 😊

### **Paso 9/10: Trabajar con grandes conjuntos de datos (paginación y división de tablas)**

Cuando trabajas con grandes conjuntos de datos, las tablas pueden volverse difíciles de manejar o visualizar en su totalidad. En este paso, aprenderemos cómo **paginarlas** (dividirlas en varias partes) o **mostrar solo una parte** de la tabla para hacerla más manejable.

#### **1. Paginación de datos**

La paginación es útil cuando tienes muchas filas y deseas mostrar solo un subconjunto de los datos en cada "página". Puedes dividir las filas en "páginas" y mostrar solo un número limitado de filas por página.

##### **Ejemplo 1: Crear una función de paginación**

Imaginemos que tienes una lista de 100 registros y deseas mostrar solo 10 registros por página.

```python
from tabulate import tabulate

# Datos de ejemplo
data_dict = [{"Nombre": f"Persona {i}", "Edad": 20 + (i % 5), "Profesión": "Estudiante"} for i in range(1, 101)]

# Función para paginar
def mostrar_pagina(data, pagina, filas_por_pagina):
    # Calcular los índices de las filas para la página solicitada
    inicio = (pagina - 1) * filas_por_pagina
    fin = pagina * filas_por_pagina
    datos_pagina = data[inicio:fin]

    # Mostrar la tabla para esa página
    print(tabulate(datos_pagina, headers=["Nombre", "Edad", "Profesión"], tablefmt="grid"))

# Mostrar la página 1
print("Página 1:")
mostrar_pagina(data_dict, 1, 10)

# Mostrar la página 2
print("\nPágina 2:")
mostrar_pagina(data_dict, 2, 10)
```

**Resultado (para la página 1 y 2)**:
```
Página 1:
+-------------+-------+------------+
| Nombre     | Edad  | Profesión  |
+-------------+-------+------------+
| Persona 1  | 20    | Estudiante |
| Persona 2  | 21    | Estudiante |
| Persona 3  | 22    | Estudiante |
| Persona 4  | 23    | Estudiante |
| Persona 5  | 24    | Estudiante |
| Persona 6  | 20    | Estudiante |
| Persona 7  | 21    | Estudiante |
| Persona 8  | 22    | Estudiante |
| Persona 9  | 23    | Estudiante |
| Persona 10 | 24    | Estudiante |
+-------------+-------+------------+

Página 2:
+-------------+-------+------------+
| Nombre     | Edad  | Profesión  |
+-------------+-------+------------+
| Persona 11 | 20    | Estudiante |
| Persona 12 | 21    | Estudiante |
| Persona 13 | 22    | Estudiante |
| Persona 14 | 23    | Estudiante |
| Persona 15 | 24    | Estudiante |
| Persona 16 | 20    | Estudiante |
| Persona 17 | 21    | Estudiante |
| Persona 18 | 22    | Estudiante |
| Persona 19 | 23    | Estudiante |
| Persona 20 | 24    | Estudiante |
+-------------+-------+------------+
```

En este ejemplo, hemos creado una función `mostrar_pagina` que divide los datos en páginas, con un número específico de filas por página. Al llamar a esta función con diferentes números de página, puedes ver los datos de forma paginada.

#### **2. Mostrar solo una parte de la tabla**

A veces, en lugar de mostrar una tabla completa, puede que solo quieras mostrar las primeras `n` filas o un subconjunto de las columnas.

##### **Ejemplo 2: Mostrar las primeras `n` filas**

Puedes utilizar el índice para acceder a las primeras `n` filas de los datos y mostrarlas en la tabla.

```python
# Mostrar solo las primeras 5 filas
print(tabulate(data_dict[:5], headers=["Nombre", "Edad", "Profesión"], tablefmt="grid"))
```

**Resultado**:
```
+-------------+-------+------------+
| Nombre     | Edad  | Profesión  |
+-------------+-------+------------+
| Persona 1  | 20    | Estudiante |
| Persona 2  | 21    | Estudiante |
| Persona 3  | 22    | Estudiante |
| Persona 4  | 23    | Estudiante |
| Persona 5  | 24    | Estudiante |
+-------------+-------+------------+
```

En este ejemplo, mostramos solo las primeras 5 filas usando el índice de Python `data_dict[:5]`.

#### **3. Mostrar solo ciertas columnas**

También puedes **seleccionar ciertas columnas** para mostrar, de modo que no necesitas mostrar toda la tabla si solo te interesa una parte de los datos.

##### **Ejemplo 3: Mostrar solo ciertas columnas**

```python
# Mostrar solo las columnas "Nombre" y "Edad"
print(tabulate([{"Nombre": row["Nombre"], "Edad": row["Edad"]} for row in data_dict], headers=["Nombre", "Edad"], tablefmt="grid"))
```

**Resultado**:
```
+-------------+-------+
| Nombre     | Edad  |
+-------------+-------+
| Persona 1  | 20    |
| Persona 2  | 21    |
| Persona 3  | 22    |
| Persona 4  | 23    |
| Persona 5  | 24    |
+-------------+-------+
```

Aquí, hemos usado una lista de diccionarios con solo las columnas que nos interesan (en este caso, "Nombre" y "Edad").

#### **4. Resumen**

- **Paginación de datos**: Divide los datos en "páginas" y muestra solo un número limitado de filas por página.
- **Mostrar parte de la tabla**: Puedes mostrar solo un subconjunto de las filas usando índices (por ejemplo, las primeras `n` filas).
- **Mostrar ciertas columnas**: Puedes seleccionar qué columnas mostrar en lugar de la tabla completa, personalizando lo que se presenta.

---

Este paso te ha enseñado cómo **trabajar con grandes conjuntos de datos** dividiéndolos en páginas, mostrando solo un subconjunto de las filas o columnas, y manteniendo la tabla manejable.

En el siguiente paso, veremos cómo **guardar las tablas en diferentes formatos**, como CSV o HTML, para que puedas usarlas fuera de Python.

¿Te gustaría continuar con el **Paso 10/10**? 😊

### **Paso 10/10: Guardar la tabla en diferentes formatos (CSV, HTML, etc.)**

En este último paso, aprenderemos cómo **guardar los datos de la tabla** en diferentes formatos de archivo como CSV, HTML, y otros, para que puedas usarlos fuera de Python y compartirlos fácilmente.

#### **1. Guardar en formato CSV**

El formato **CSV** (Comma-Separated Values) es uno de los más comunes para almacenar datos tabulares. Puedes guardar la tabla como un archivo CSV para abrirlo en Excel, Google Sheets u otros programas de hojas de cálculo.

##### **Ejemplo 1: Guardar en formato CSV**

```python
import csv

# Datos como diccionario
data_dict = [
    {"Nombre": "Juan", "Edad": 28, "Profesión": "Programador"},
    {"Nombre": "Ana", "Edad": 24, "Profesión": "Diseñadora"},
    {"Nombre": "Luis", "Edad": 30, "Profesión": "Ingeniero"}
]

# Escribir en un archivo CSV
with open('tabla_datos.csv', 'w', newline='', encoding='utf-8') as csvfile:
    writer = csv.DictWriter(csvfile, fieldnames=["Nombre", "Edad", "Profesión"])
    writer.writeheader()  # Escribe las cabeceras
    writer.writerows(data_dict)  # Escribe las filas

print("Archivo CSV guardado como 'tabla_datos.csv'.")
```

**Resultado**:
El archivo `tabla_datos.csv` tendrá el siguiente contenido:

```
Nombre,Edad,Profesión
Juan,28,Programador
Ana,24,Diseñadora
Luis,30,Ingeniero
```

Este archivo CSV puede abrirse fácilmente en Excel o cualquier otro editor de texto.

#### **2. Guardar en formato HTML**

Si deseas mostrar la tabla en una página web o guardarla en formato HTML, puedes usar el formato `html` de `tabulate` y guardarlo en un archivo HTML.

##### **Ejemplo 2: Guardar en formato HTML**

```python
# Crear una tabla HTML con 'tabulate'
html_table = tabulate(data_dict, headers=["Nombre", "Edad", "Profesión"], tablefmt="html")

# Guardar en un archivo HTML
with open("tabla_datos.html", "w", encoding="utf-8") as file:
    file.write(html_table)

print("Archivo HTML guardado como 'tabla_datos.html'.")
```

**Resultado**:
El archivo `tabla_datos.html` tendrá el siguiente contenido:

```html
<table>
<thead>
<tr><th>Nombre</th><th>Edad</th><th>Profesión</th></tr>
</thead>
<tbody>
<tr><td>Juan</td><td>28</td><td>Programador</td></tr>
<tr><td>Ana</td><td>24</td><td>Diseñadora</td></tr>
<tr><td>Luis</td><td>30</td><td>Ingeniero</td></tr>
</tbody>
</table>
```

Este archivo HTML puede ser abierto en cualquier navegador y mostrar la tabla de forma visual.

#### **3. Guardar en formato Markdown**

Si deseas exportar la tabla para usarla en un archivo **Markdown** (por ejemplo, en un archivo README), puedes usar el formato `pipe` de `tabulate`, que es compatible con Markdown.

##### **Ejemplo 3: Guardar en formato Markdown**

```python
# Crear la tabla en formato Markdown
markdown_table = tabulate(data_dict, headers=["Nombre", "Edad", "Profesión"], tablefmt="pipe")

# Guardar en un archivo Markdown
with open("tabla_datos.md", "w", encoding="utf-8") as file:
    file.write(markdown_table)

print("Archivo Markdown guardado como 'tabla_datos.md'.")
```

**Resultado**:
El archivo `tabla_datos.md` tendrá el siguiente contenido en formato Markdown:

```
| Nombre | Edad | Profesión  |
|--------|------|------------|
| Juan   | 28   | Programador|
| Ana    | 24   | Diseñadora |
| Luis   | 30   | Ingeniero  |
```

Este archivo puede ser visualizado correctamente en cualquier visor de Markdown.

#### **4. Resumen**

- **Guardar en CSV**: Usando la librería `csv` de Python, puedes guardar los datos de la tabla como un archivo CSV, que puede abrirse en programas como Excel.
- **Guardar en HTML**: Usando el formato `html` de `tabulate`, puedes guardar la tabla como un archivo HTML para visualización en navegadores web.
- **Guardar en Markdown**: Usando el formato `pipe` de `tabulate`, puedes guardar la tabla en un archivo Markdown para su uso en plataformas como GitHub.

---

Este paso te ha mostrado cómo **guardar las tablas** en diferentes formatos como CSV, HTML y Markdown, lo que facilita el uso y la distribución de tus datos.

¡Felicidades! Has completado el recorrido de 10 pasos para aprender a usar `tabulate`. Ahora tienes las herramientas necesarias para **crear, personalizar y guardar tablas** de manera eficiente en diferentes formatos.

¿Te gustaría realizar algún ejercicio práctico o tienes alguna pregunta adicional? 😊