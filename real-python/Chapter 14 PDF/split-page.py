import copy
from pathlib import Path
from PyPDF2 import PdfFileReader, PdfFileWriter

pdf_path = (
 Path.home() /
 "rotated.pdf"
)

pdf_reader = PdfFileReader(str(pdf_path))
pdf_writer = PdfFileWriter()



for page in pdf_reader.pages:
    left_side = copy.deepcopy(page)
    current_coords = left_side.mediaBox.upperRight
    new_coords = (current_coords[0] / 2, current_coords[1])

    right_side = copy.deepcopy(page)
    right_side.mediaBox.upperLeft = new_coords
    left_side.mediaBox.upperRight = new_coords

    pdf_writer.addPage(left_side)
    pdf_writer.addPage(right_side)

with Path("split.pdf").open(mode="wb") as output:
    pdf_writer.write(output)