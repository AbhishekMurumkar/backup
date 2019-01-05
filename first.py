import pyPdf
filename="E:\\books\\Recepies for AngularJS.pdf"
pdf = pyPdf.PdfFileReader(open(filename, "rb"))
print(pdf.numPages)
for i in range(0,9):
    print(i)
    page=pdf.getPage(i)
    print(page.extractText())