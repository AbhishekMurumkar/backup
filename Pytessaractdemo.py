from wand.image import Image as Img
import pytesseract
with Img(filename='E:\\python\\test.PNG', resolution=300) as img:
    img.compression_quality = 99
    img.save(filename='image_name.jpg')

# If you don't have tesseract executable in your PATH, include the following:
pytesseract.pytesseract.tesseract_cmd = r'C:\Program Files (x86)\Tesseract-OCR\tesseract'
# Example tesseract_cmd = r'C:\Program Files (x86)\Tesseract-OCR\tesseract'

# Simple image to string
text=pytesseract.image_to_string(Img.open('image_name.jpg'))
print(text)

# French text image to string
#print(pytesseract.image_to_string(Image.open('test-european.jpg'), lang='fra'))

# Get bounding box estimates
#print(pytesseract.image_to_boxes(Image.open('E:\\python\\test.PNG')))

# Get verbose data including boxes, confidences, line and page numbers
table=pytesseract.image_to_data(Img.open('E:\\python\\test.PNG'))
text=text.replace("\n"," ")
text=text.replace("\n\n","")
print(text)

# Get information about orientation and script detection
#print(pytesseract.image_to_osd(Image.open('E:\\python\\test.PNG')))

# In order to bypass the internal image conversions, just use relative or absolute image path
# NOTE: If you don't use supported images, tesseract will return error
#print(pytesseract.image_to_string('E:\\python\\test.PNG'))

# get a searchable PDF
pdf = pytesseract.image_to_pdf_or_hocr('E:\\python\\test.PNG', extension='pdf')