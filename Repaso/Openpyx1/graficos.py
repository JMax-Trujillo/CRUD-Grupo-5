from openpyxl import Workbook
from openpyxl.chart import BarChart, Reference

workbook = Workbook()
sheet = workbook.active

# Escribir datos para el grafico
sheet.append(["Mes", "Enero", "Febrero", "Marzo"])
sheet.append(["Ventas", 1500, 2000, 1250])

# Inicializar un grafico de barras
chart = BarChart()
data = Reference(sheet, min_col=1, min_row=1, max_col=4, max_row=2)


'''
FALTAAAAAAA... aqui me dio flojera seguir
'''