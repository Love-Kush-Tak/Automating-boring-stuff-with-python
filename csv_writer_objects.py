import csv
outputFile = open('output.csv', 'w', newline='')
outputWriter= csv.writer(outputFile)
outputWriter.writerow(['spam', 'eggs', 'bacon', 'ham'])
outputWriter.writerow(['Hello, world', 'eggs', 'bacon', 'ham'])
outputWriter.writerow([1, 2, 3.1415, 4])
outputFile2 = open('output.csv')
outputReader = csv.reader(outputFile2)
outputData = list(outputReader)
print(outputData)
outputFile.close()
outputFile3 = open('output.csv')
outputReader = csv.reader(outputFile3)
outputData = list(outputReader)
print(outputData)
