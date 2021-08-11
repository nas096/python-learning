import copy
from pathlib import Path
from PyPDF2 import PdfFileReader, PdfFileWriter

pdf_path = (
 Path.home() /
 "python-basics-exercises" /
 "ch14-interact-with-pdf-files" /
 "practice_files" /
 "split_and_rotate.pdf"
)

pdf_reader = PdfFileReader(str(pdf_path))
pdf_writer = PdfFileWriter()

for n in range(pdf_reader.getNumPages()):
    page = pdf_reader.getPage(n)
    page.rotateCounterClockwise(90)
    pdf_writer.addPage(page)

with Path(Path.home() / "rotated.pdf").open(mode="wb") as output:
    pdf_writer.write(output)



