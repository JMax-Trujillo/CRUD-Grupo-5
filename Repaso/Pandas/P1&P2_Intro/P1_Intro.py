import pandas as pd

# Crear un Data Frame, osea es como un diccionario y dentro varias listas
data = {
    'Name': ['Max', 'Gisela', 'Amaya'],
    'Age': [26, 19, 18],
    'City': ['Paramonga', 'Pativilca', 'Barranca']
}

# Crear un DataFrame a partir del diccionario
df = pd.DataFrame(data)

# Ver el contenido
print(df)

print('*'*25)

# Leer el archivo CSV
newDF = pd.read_excel("data.xlsx")

# Mostrar el Data Frame
print(newDF)

# Escribir el dataFrame a archivo CVS
# df.to_html("df.html", index=False) # El index False evita que se guarde con el indice

# df.to_json("df.json", indent=False)

# df.to_csv("df.csv", index=False)
print(df.head()) # Ver las 5 priemras filas
print(df.tail()) # Ver las 5 ultimas filas
