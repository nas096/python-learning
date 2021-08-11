from pathlib import Path
from PyPDF2 import PdfFileReader, PdfFileWriter

pdf_path = (
 Path.home() /
 "python-basics-exercises" /
 "ch14-interact-with-pdf-files" /
 "practice_files" /
 "Pride_and_Prejudice.pdf"
)

input_pdf = PdfFileReader(str(pdf_path))
pdf_writer = PdfFileWriter()

last_page = input_pdf.getPage(233)

pdf_writer.addPage(last_page)
with Path(Path.home() / "last_page.pdf").open(mode="wb") as output_file:
	pdf_writer.write(output_file)

pdf = PdfFileReader(str(pdf_path))
