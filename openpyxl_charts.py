import openpyxl
wb = openpyxl.Workbook()
sheet = wb.active
for i in range(1,11):
    sheet['A' + str(i)] = i**3

refObj = openpyxl.chart.Reference(sheet, min_row=1, min_col=1, max_row=10, max_col =1)
seriesObj = openpyxl.chart.Series(refObj, title='First series')
chartObj = openpyxl.chart.BarChart()
'''chartObj.append(seriesObj)
chartObj.drawing.top = 50
chartObj.drawing.left = 100
chartObj.drawing.width = 300
chartObj.drawing.height = 200'''
chartObj.append(seriesObj)
sheet.add_chart(chartObj)
wb.save('sampleChart.xlsx')
