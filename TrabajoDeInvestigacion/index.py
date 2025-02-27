'''
Este proyecto de investifacion
es para conocer sobre un CRUD con archivos .xlsx

 CRUD es el acrónimo de Create (Crear), Read (Leer), Update (Actualizar) y Delete (Borrar). Este
concepto se utiliza para describir las cuatro operaciones básicas que pueden realizarse en la
mayoría de las bases de datos y sistemas de gestión de información.
    
Adicional: AGREGAR UN HISTORIAL EN TIEMPO REAL
'''

from tabulate import tabulate
import time

# from C_create import saludo
historial = []
while True:
    print()
    header_menu = ['Menu CRUD', 'Opcion']
    body_menu = [
        ['C-Nuevo Registro', 1],
        ['R-Leer Registro', 2],
        ['U-Actualizar Registro', 3],
        ['D-Eliminar Registro', 4],
        ['H-Historial', 5],
        ['Salir', 6]
        ]
    print(tabulate(body_menu, headers=header_menu, tablefmt='plain'))
    print()
    opcion = int(input('Elija el numero de lo que desea hacer:   '))
    if opcion == 1:
        # Codigo para C
        # saludo()
        historial.append([f' ####### creado', f'time {time.strftime("%H:%M:%S")}'])
        pass
    elif opcion == 2:
        # Codigo para R 
        historial.append([f' ####### Leido', f'time {time.strftime("%H:%M:%S")}'])
        pass
    elif opcion == 3:
        # Codigo para U
        historial.append([f' ####### Actualizado', f'time {time.strftime("%H:%M:%S")}'])
        pass
    elif opcion == 4:
        # Codigo para D
        historial.append([f' ####### Eliminado', f'time {time.strftime("%H:%M:%S")}'])
        pass
    elif opcion == 5:
        # Codigo para Historial
        for i in historial:
            print(i)
        pass
    elif opcion == 6:
        print('Salir del programa')
        break
    else:
        print('Opcion no valida')