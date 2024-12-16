# pip install pdf2docx
from pdf2docx import Converter
pdf_file = 'coding.pdf'
docx_file = 'coding.docx'
cv = Converter(pdf_file)
cv.convert(docx_file)
cv.close()