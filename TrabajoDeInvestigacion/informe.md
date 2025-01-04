# Liberias

## OpenPyXL

OpenPyXL es una biblioteca de Python diseñada para trabajar con archivos de Excel (formatos `.xlsx` y `.xlsm`). Esta herramienta es ideal para tareas como la creación, edición, lectura y manipulación de hojas de cálculo de Excel de manera programática. Es ampliamente utilizada en proyectos que requieren manejar datos estructurados en hojas de cálculo, ya que elimina la necesidad de abrir Excel manualmente y permite automatizar procesos.

---

### Instalación

Para instalar OpenPyXL, necesitas tener Python instalado en tu computadora. Una vez que esté configurado, sigue estos pasos:

1. **Abre una terminal o línea de comandos**.
2. **Ejecuta el siguiente comando** para instalar OpenPyXL usando `pip` (el administrador de paquetes de Python):  
   ```bash
   pip install openpyxl
   ```

3. **Verifica la instalación** asegurándote de que no aparezcan errores durante el proceso. Si deseas confirmar que la instalación fue exitosa, puedes comprobar la versión instalada ejecutando:  
   ```bash
   pip show openpyxl
   ```

---

### ¿Para qué sirve OpenPyXL?

OpenPyXL es una herramienta versátil y poderosa que permite interactuar con hojas de cálculo de Excel directamente desde un script de Python. A continuación, se enumeran algunas de las tareas comunes que facilita:

1. **Automatización de tareas repetitivas**:  
   - Crear reportes periódicos con datos actualizados.
   - Generar plantillas de Excel de forma automática.

2. **Manipulación de datos estructurados**:  
   - Leer datos desde hojas de cálculo para integrarlos en aplicaciones.
   - Editar valores existentes o actualizar celdas específicas.

3. **Creación de archivos de Excel**:  
   - Diseñar hojas de cálculo con múltiples pestañas, celdas formateadas, fórmulas y gráficos.

4. **Análisis de datos**:  
   - Extraer información clave de grandes volúmenes de datos almacenados en hojas de cálculo.

5. **Compatibilidad multiplataforma**:  
   - Permite trabajar con archivos Excel sin necesidad de tener el software instalado.

## Pandas

Pandas es una biblioteca de Python ampliamente utilizada para la manipulación y el análisis de datos. Proporciona estructuras de datos flexibles como **DataFrames** y **Series**, que facilitan trabajar con datos tabulares y series temporales. Aunque Pandas tiene aplicaciones en múltiples formatos de datos, es especialmente útil cuando se trabaja con hojas de cálculo Excel (`.xlsx`).

---

### Instalación

Para instalar Pandas, sigue estos pasos:

1. **Abre una terminal o línea de comandos**.
2. **Ejecuta el siguiente comando** para instalar Pandas usando `pip`:  
   ```bash
   pip install pandas
   ```

3. Si necesitas trabajar específicamente con archivos Excel, también deberás instalar una biblioteca complementaria, como **openpyxl** (para leer y escribir archivos `.xlsx`):  
   ```bash
   pip install openpyxl
   ```

4. **Verifica la instalación** ejecutando:  
   ```bash
   pip show pandas
   ```

---

### ¿Para qué sirve Pandas?

Pandas se destaca por su capacidad para procesar y analizar datos de forma eficiente. Al trabajar con archivos Excel (`.xlsx`), Pandas es una herramienta excepcional debido a las siguientes razones:

1. **Lectura de archivos Excel**:  
   Pandas permite importar datos de hojas de cálculo Excel directamente en un DataFrame, lo que facilita su manipulación y análisis. Puedes cargar archivos con múltiples hojas, seleccionar hojas específicas y definir el rango de datos que deseas procesar.

2. **Manipulación de datos**:  
   Una vez que los datos están en un DataFrame, puedes:
   - Filtrar filas y columnas específicas.
   - Realizar operaciones matemáticas y estadísticas.
   - Limpiar datos eliminando valores nulos o duplicados.
   - Transformar datos mediante funciones personalizadas.

3. **Escritura de datos en Excel**:  
   Pandas permite guardar DataFrames como archivos Excel, creando nuevas hojas de cálculo o actualizando archivos existentes. Esto es ideal para generar reportes automatizados o compartir datos procesados.

4. **Edición avanzada**:  
   - Agregar o eliminar hojas dentro de un archivo.
   - Insertar datos procesados en una hoja específica.
   - Personalizar formatos, como cambiar los nombres de las columnas o reordenarlas.

## Tabulate

**Tabulate** es una biblioteca de Python que permite generar tablas con datos tabulares en texto plano de forma fácil y estética. Es especialmente útil cuando necesitas mostrar información estructurada en la consola, como resultados de consultas, reportes o datos procesados. Funciona con listas, diccionarios, y pandas DataFrames, y te permite personalizar el formato para que la salida sea legible y profesional.

---

### Instalación

Para instalar Tabulate, sigue estos pasos:

1. Abre una terminal o línea de comandos.
2. Ejecuta el siguiente comando para instalar Tabulate usando `pip`:  
   ```bash
   pip install tabulate
   ```

3. Verifica la instalación asegurándote de que no aparezcan errores. Puedes comprobar la versión instalada ejecutando:  
   ```bash
   pip show tabulate
   ```

**Grid (cuadrícula)**:  
   ```
   +----+------------+----------+-------+
   | ID | Producto   | Cantidad | Precio|
   +----+------------+----------+-------+
   | 1  | Manzanas   | 50       | 0.5   |
   | 2  | Plátanos   | 30       | 0.25  |
   | 3  | Peras      | 20       | 0.75  |
   +----+------------+----------+-------+
   ```

Con **Tabulate**, puedes transformar la experiencia de usuario en aplicaciones de consola, haciendo que los datos sean claros y fáciles de interpretar en cualquier operación CRUD.