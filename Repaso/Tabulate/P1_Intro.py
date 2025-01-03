from tabulate import tabulate

# Datos que queremos mostrar en la tabla

data = [
    ['Max', 26, 'Sistemas'],
    ['Gisela', 19, 'Alimentarias'],
    ['Amaya', 18, 'Enfermeria']
]

# Encabezados de las columnas

header = ['Name', 'Age', 'Profesion']

# Crear la tabla con formato "grid" (con bordes)
print(tabulate(data, headers=header, tablefmt="latex"))