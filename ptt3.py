import pdftotext
import io

pdf = pdftotext.PDF()


memory_file = io.BytesIO("E:\\books\\CSSMasterclassBook.pdf").read()

pdf=pdftotext.PDF(memory_file)
# Iterate over all the pages
for page in pdf:
    print(page)
