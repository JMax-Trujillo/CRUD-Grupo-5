import xlsxwriter

workbook = xlsxwriter.Workbook('mi_archive.xlsx')

worksheet = workbook.add_worksheet()

worksheet.write('A1', 'HelloWorld')
worksheet.write('A2', 42)

workbook.close()

print('Archivo Excel creado')