from pathlib import Path
from PyPDF2 import PdfFileMerger, PdfFileReader, PdfFileWriter

pdf_path = (
 Path.home() /
 "python-basics-exercises" /
 "ch14-interact-with-pdf-files" /
 "practice_files"
)

merge1_file = pdf_path / "merge1.pdf"

merge2_file = pdf_path / "merge2.pdf"

pdf_merger = PdfFileMerger()

merge_list = [merge1_file, merge2_file]

for i in merge_list:
    pdf_merger.append(str(i))
"""
with Path(Path.home() / "concatenated.pdf").open(mode="wb") as output:
    pdf_merger.write(output)
"""

merge3_file = pdf_path / "merge3.pdf"
concatenated_file = Path.home() / "concatenated.pdf"

pdf_merger.merge(1, str(merge3_file))

with Path(Path.home() / "merged.pdf").open(mode="wb") as output:
    pdf_merger.write(output)
