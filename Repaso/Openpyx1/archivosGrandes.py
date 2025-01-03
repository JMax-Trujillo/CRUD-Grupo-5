from openpyxl import Workbook
import random as rd

workbook = Workbook(write_only=True)
sheet1 = workbook.create_sheet("Hoja1")

for i in range(10000):
    sheet1.append([f'key: {i}', f'description: {rd.randint(1,10000)}', rd.randint(-10000, 10000)*24.4])

workbook.save("Write.xlsx")
print("ok")