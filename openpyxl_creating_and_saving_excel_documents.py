#Creating and Saving Excel document
import openpyxl
wb = openpyxl.Workbook()
print(wb.get_sheet_names())
sheet = wb.active
print(sheet.title)
sheet.title = 'Spam Bacon Eggs Sheet'
print(wb.get_sheet_names())
'''Any time you modify the Workbook object or its sheets and cells, the
spreadsheet file will not be saved until you call the save() workbook method.'''
#Modifying sheets and saving it as different spreadsheet file
wb = openpyxl.load_workbook('example.xlsx')
sheet = wb.active
sheet.title ='Sapm Spam Spam'
wb.save('example_copy.xlsx')
#creating and removing sheets








