import openpyxl, os
os.chdir('F://automate_online-materials')
wb = openpyxl.load_workbook('produceSales.xlsx')
sheet = wb.active
sheet.freeze_panes ='A2'
wb.save('freezeExample.xlsx')
