import openpyxl
wb = openpyxl.Workbook()
sheet = wb.active
sheet['A1'] = 'Tall row'
sheet['B2'] = 'Wide column'
sheet.row_dimensions[1].height = 70
sheet.column_dimensions['B'].width = 20
wb.save('dimensions.xlsx')
'''The row height can be
set to an integer or float value between 0 and 409'''
'''This value represents the
height measured in points, where one point equals 1/72 of an inch'''
