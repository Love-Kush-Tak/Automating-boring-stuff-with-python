import csv,os
os.chdir('F://automate_online-materials')
exampleFile = open('example.csv')
exampleReader = csv.reader(exampleFile)
for row in exampleReader:
    print('row #' + str(exampleReader.line_num) + ' ' + str(row))
