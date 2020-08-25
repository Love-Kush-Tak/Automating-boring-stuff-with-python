import PyPDF2, os
os.chdir('F://automate_online-materials')
minutesFile = open('meetingminutes.pdf', 'rb')
pdfReader = PyPDF2.PdfFileReader(minutesFile)
page = pdfReader.getPage(0)
page.rotateClockwise(90)
pdfWriter = PyPDF2.PdfFileWriter()
pdfWriter.addPage(page)
resultFile = open('rotatedPage.pdf', 'wb')
pdfWriter.write(resultFile)
resultFile.close()
minutesFile.close()
