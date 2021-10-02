from pathlib import Path
from PyPDF2 import PdfFileReader

pdf_path = (
 Path.home() /
 "python-basics-exercises" /
 "ch14-interact-with-pdf-files" /
 "practice_files" /
 "zen.pdf"
 )

pdf = PdfFileReader(str(pdf_path))

print(pdf.getNumPages())
first_page = pdf.getPage(0)
print(first_page.extractText())
