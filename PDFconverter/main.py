from pdf2docx import Converter
pdf_path="sample.pdf"
docx_path="sample.docx"

cv=Converter(pdf_path)
cv.convert(docx_path)
cv.close()  #hafizadan silme çok yer kaplamasını önleme
