# Modificar datos del data Frame

import pandas as pd
import random

# Leer un cvs
df = pd.read_csv("Inventory_v2.csv")

# Agregar una nueva columna con un valor constante
df['Costo'] = 3000
# Agregar una columna basada en una operacion
df['Valor'] = df['Costo']*random.randint(1,3000)

# Agregar filas con append()
menu = 'product.partNumber,location.locationIdentifier,inventoryType,quantity,quantityUnits,value,valueCurrency,reservationOrders,daysOfSupply,shelfLife,reorderLevel,expectedLeadTime,quantityUpperThreshold,quantityLowerThreshold,daysOfSupplyUpperThreshold,daysOfSupplyLowerThreshold,expiringThreshold,plannerCode,velocityCode,inventoryParentType,class,segment,Costo,Valor'
menu = menu.split(',')
index = []
# for i, j in enumerate(menu):
#     index.append(i)  xdxdxd, no se porq hice esto, si puedo tener el index con un contador xddxd
fila = []
count = 0
for i in menu:
    # element = input(f'Agrega un elemento para {menu[count]}: ')
    element = '444444'
    fila.append([menu[count], element])
    count += 1
df = df.append(fila, ignore_index=True)
print(df)

'''
No me salio, pipipi
'''

