import PyPDF2, os
os.chdir('F://automate_online-materials')
pdfFile = open('meetingminutes.pdf', 'rb')
pdfReader = PyPDF2.PdfFileReader(pdfFile)
pdfWriter = PyPDF2.PdfFileWriter()
for pageNum in range(pdfReader.numPages):
    pdfWriter.addPage(pdfReader.getPage(pageNum))
resultPdf = open('encryptedminutes.pdf' , 'wb')
pdfWriter.encrypt('swordfish')
pdfWriter.write(resultPdf)
resultPdf.close()
