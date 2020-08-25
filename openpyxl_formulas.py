import openpyxl
wb = openpyxl.Workbook()
sheet = wb.active
sheet['A1'] = 200
sheet['A2'] = 250
sheet['A3'] = 272
sheet['A4'] = '=SUM(A1:A3)'
wb.save('writeFormula.xlsx')
