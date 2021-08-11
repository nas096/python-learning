import easygui as gui
from PyPDF2 import PdfFileReader, PdfFileWriter

input_path = gui.fileopenbox(
    title="Select a PDF to rotate...",
    default="*.pdf"

)

if input_path is None:
    exit()

# 3. Let the user select one of the degree to rotate the PDfs

choice = ("90", "180", "270")
degrees = gui.buttonbox(
    msg="Rotate the PDF clockwise by how many degrees?",
    title="Choose rotation...",
    choices=choice
)

degrees = int(degrees)

# Display a file selection dialog for saving the rotated PDf

save_title = "Save the rotated PDF as ..."
file_type = "*.pdf"
output_path = gui.filesavebox(title=save_title, default=file_type)

# When we set the `default` to PDF, the file is automatically saved with the .pdf extension

# 5. If the user tries to save the same name as the input file:
while input_path == output_path:
    gui.msgbox(msgbox="Cannot overwrite original file!")

    output_path = gui.filesavebox(title=save_title, default=file_type)

if output_path is None:
    exit()

# 7. Perform the Page rotation
# - Open the selected PDF.
input_file = PdfFileReader(input_path)
output_pdf = PdfFileWriter()

# - Rotate all of the pages.

for page in input_file.pages:
    page = page.rotateClockwise(degrees)
    output_pdf.addPage(page)

# - Save the rotated PDF to the selected file.

with open(output_path + ".pdf", "wb") as output_file:
    output_pdf.write(output_file)
