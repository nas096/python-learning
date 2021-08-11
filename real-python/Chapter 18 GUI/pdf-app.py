from PyPDF2 import PdfFileReader, PdfFileWriter
import easygui as gui


input_path = gui.fileopenbox(
    default="*.pdf",
    title="Open a PDF file to extract text")
if input_path == None:
    exit()
starting_page = gui.integerbox(
    msg="Enter a starting page: ",
    title="Your starting page")
if starting_page == None:
    exit()
while starting_page < 0:

    if starting_page <= 0:
        gui.msgbox(msg="Input Invalid, Please enter a valid page number")
        starting_page = gui.integerbox(
            msg="Enter a starting page: ",
            title="Your starting page")

ending_page = gui.integerbox(
    msg="Enter a ending page: ",
    title="Your ending page")
if ending_page == None:
    exit()

while ending_page < 0:

    if ending_page <= 0:
        gui.msgbox(msg="Input Invalid, Please enter a valid page number")
        ending_page = gui.integerbox(
            msg="Enter a ending page:",
            title="Your ending page")

save_path = gui.filesavebox(
    msg="Choose your save place",
    title="Your save place")

if save_path == None:
    exit()

while save_path == input_path:
    gui.msgbox("You can't overwrite the input file")
    save_path = gui.filesavebox(
        msg="Choose your save place",
        title="Your save place")


reader = PdfFileReader(input_path)
writer = PdfFileWriter()

for page in reader.pages[starting_page:ending_page+1]:
    writer.addPage(page)


with open(save_path + ".pdf", "wb") as output:
    writer.write(output)
