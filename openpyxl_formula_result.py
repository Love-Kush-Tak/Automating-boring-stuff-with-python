import openpyxl
wbFormulas = openpyxl.load_workbook('writeFormula.xlsx')
sheet = wbFormulas.active
print(sheet['A4'].value)
wbDataOnly = openpyxl.load_workbook('writeFormula.xlsx', data_only =True)
sheet1 = wbDataOnly.active
print(sheet1['A4'].value)
print(sheet1['A5'].value)
print(sheet1['B4'].value)
print(sheet1['A6'].value)
#openpyxl never evaluates formula
'''a Workbook object can show either
the formulas or the result of the formulas but not both. (But you can have
multiple Workbook objects loaded for the same spreadsheet file.)'''
