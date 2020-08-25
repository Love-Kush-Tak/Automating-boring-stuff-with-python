import PyPDF2, os
os.chdir('F://automate_online-materials')
pdfReader = PyPDF2.PdfFileReader(open('encrypted.pdf', 'rb'))
print(pdfReader.isEncrypted)
pdfReader.decrypt('rosebud')
pageObj = pdfReader.getPage(0)
print(pageObj.extractText())
print(pdfReader.numPages)
#rosebud is the password for the pdf
