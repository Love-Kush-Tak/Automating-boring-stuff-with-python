import csv, os
os.chdir('F://automate_online-materials')
exampleFile = open('example.csv')
exampleReader = csv.reader(exampleFile)
exampleData = list(exampleReader)
print(exampleData)
print(exampleReader)
