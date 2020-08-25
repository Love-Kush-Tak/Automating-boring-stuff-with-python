import openpyxl
from openpyxl.styles import Font, NamedStyle
# create new file
wb = openpyxl.Workbook()
# read active sheet
sheet = wb['Sheet']

# give new name parameters 
italic24Font = NamedStyle(name="italic24Font")
italic24Font.font = Font(size=24, italic=True)
sheet['A1'].style = italic24Font
sheet['A1'] = 'Hello world!'
wb.save('styled.xlsx')
'''fontObj1 = Font(name='Times New Roman', bold=True)
styleObj1 = NamedStyle(font=fontObj1)
sheet['A2'].style/styleObj
sheet['A2'] = 'Bold Times New Roman'
wb.save('styles.xlsx')'''
styleObj1 = NamedStyle(name="Times New Roman")
styleObj1.font = Font(size=24, bold=True)
sheet['A2'].style = styleObj1
sheet['A2'] = 'Bold Times New Roman'
wb.save('styled.xlsx')
