from dosListas import lista_Ciclo_2

from openpyxl import Workbook

def create_02():
    workbook = Workbook()
    sheet = workbook.active

    sheet.append(["ID", "User", "Ciclo"])
    key = 1
    for i in lista_Ciclo_2:
        temp = []
        temp.append(key)
        temp.append(lista_Ciclo_2[key-1][1])
        temp.append(lista_Ciclo_2[key-1][0])
        key += 1
        sheet.append(temp)

    # Guardar el archivo excel
    workbook.save("Ciclo_02.xlsx")
    print("todo OK")

    print(lista_Ciclo_2[0])
    print(lista_Ciclo_2[0][0])
    print(lista_Ciclo_2[0][1])  
    
