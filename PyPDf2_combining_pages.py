import PyPDF2, os
os.chdir('F://Highways_intern')
#Get all the PDF filenames
pdfFiles = []
for filename in os.listdir('.'):
    if filename.endswith('.pdf'):
        pdfFiles.append(filename)
#pdfFiles.sort(key = str.lower)
pdfWriter = PyPDF2.PdfFileWriter()
#Loop through all the pdf files
print(pdfFiles)
for filename in pdfFiles:
    pdfFileObj = open(filename, 'rb')
    print(pdfFileObj)
    pdfReader = PyPDF2.PdfFileReader(pdfFileObj)
    #Loop through all the pages (except the first) and add them
    for pageNum in range(1, pdfReader.numPages):
        pageObj = pdfReader.getPage(pageNum)
        pdfWriter.addPage(pageObj)

#Save the resulting PDF to a file
pdfOutput = open('allminutes.pdf', 'wb')
pdfWriter.write(pdfOutput)
pdfOutput.close()









    
    
