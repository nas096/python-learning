import copy
from pathlib import Path
from PyPDF2 import PdfFileReader, PdfFileWriter

pdf_path = (
 Path.home() /
 "python-basics-exercises" /
 "ch14-interact-with-pdf-files" /
 "practice_files" /
 "scrambled.pdf"
)

pdf_reader = PdfFileReader(str(pdf_path))
pdf_writer = PdfFileWriter()
def get_page_text(page):
    return page.extractText()
pages_list = list(pdf_reader.pages)
pages_list.sort(key=get_page_text)
for page in pages_list:
    if page["/Rotate"] == 90:
        page.rotateClockwise(-90)
    
    if page["/Rotate"] == 180:
        page.rotateCounterClockwise(-180)

    if page["/Rotate"] == 270:
        page.rotateCounterClockwise(-270)

    if page["/Rotate"] == -90:
        page.rotateCounterClockwise(-90)

    if page["/Rotate"] == -180:
        page.rotateCounterClockwise(-180) 
    pdf_writer.addPage(page)


with Path("scrambled.pdf").open(mode="wb") as output:
    pdf_writer.write(output)


