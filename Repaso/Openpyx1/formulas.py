from openpyxl import Workbook

workbook = Workbook()
sheet1 = workbook.active
sheet1.title = "Hoja1"
sheet2 = workbook.create_sheet("Hoja2")

sheet1["A1"] = 10
sheet2["A2"] = 20

# Escribir la formula
sheet2["A3"] = "=Hoja1!A1+Hoja2!A2"

workbook.save("operacion.xlsx")
print("Operado")