import pandas as pd

# Seleccionar un csv para pasar a data frame
df = pd.read_csv("Catalog_v2.csv")

nameCode = df[["name", "code"]]
# print(nameCode)

fila_0 = df.loc[0:2]

filtro_multiple = df[df["code"] == "All"]

filtro_query = df.query('name == "Miramar "')

dato = df.loc[54, 'name']

dato_indice = df.iloc[24,5]
print(dato_indice)