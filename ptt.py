# importing required modules 
import PyPDF2 

# creating a pdf file object
pdfFileObj = open('E:\\report_100000_1.pdf', 'rb')

# creating a pdf reader object
pdfReader = PyPDF2.PdfFileReader(pdfFileObj)

# printing number of pages in pdf file
print(pdfReader.numPages)

for i in range(0, 9):
    print(i)
    pageObj = pdfReader.getPage(i)
    page = pageObj.extractText()
    print(page)
    content=pageObj.getContents()
    print(content)
    raw_input("enter a key")

pdfFileObj.close()
