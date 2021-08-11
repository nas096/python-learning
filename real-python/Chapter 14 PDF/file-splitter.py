from PyPDF2 import PdfFileReader, PdfFileWriter
from pathlib import Path
class PdfFileSplitter:
    """This can be used to split a pdf into two new PDFs"""

    def __init__(self, file):
        self.writer1 = None
        self.pdf_reader = PdfFileReader(str(Path(file)))
        self.writer2 = None

    def split(self, breakpoint):
        self.writer1 = PdfFileWriter()
        self.writer2 = PdfFileWriter()
        for page in self.pdf_reader.pages[:breakpoint]:
            self.writer1.addPage(page)

        for page in self.pdf_reader.pages[breakpoint:]:
            self.writer2.addPage(page)
        pass
    def writer(self, filename):
        with Path(f"{filename}_1.pdf").open(mode="wb") as output1:
            self.writer1.write(output1)

        with Path(f"{filename}_2.pdf").open(mode="wb") as output2:
            self.writer2.write(output2)
    
    pass

pdf_path = (
 Path.home() /
 "python-basics-exercises" /
 "ch14-interact-with-pdf-files" /
 "practice_files" /
 "Pride_and_Prejudice.pjjjdf"
)

pdf_splitter = PdfFileSplitter(pdf_path)
pdf_splitter.split(breakpoint=150)
pdf_splitter.writer("pride_pdf")