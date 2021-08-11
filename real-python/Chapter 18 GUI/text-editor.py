import tkinter as tk
from tkinter.constants import RAISED
from pathlib import Path
from tkinter.filedialog import askopenfilename, asksaveasfilename


def open_file():
    file_path = askopenfilename(
        filetypes=(
            ('text files', '*.txt',),
            ('All files', '*.*')
        )
    )

    if not file_path:
        return

    window.title(f"Simple Text Editor - {Path(file_path).name}")
    with open(file_path, "r") as output_file:
        text = output_file.read()
        txt_edit.insert(tk.END, text)
        pass


def save_as():
    file_path = asksaveasfilename(
        filetypes=(
            ('text files', '*.txt'),
            ('All files', '*.*')
        )
    )

    with open(file_path + ".txt", "w") as output_file:
        text = txt_edit.get("1.0", tk.END)
        output_file.write(text)


window = tk.Tk()
window.title("Simple Text Editor")
window.columnconfigure(1, minsize=800)
window.rowconfigure(0, minsize=800)

frm_button = tk.Frame(master=window, relief=RAISED, borderwidth=1)


txt_edit = tk.Text(window)

btn_open = tk.Button(master=frm_button, text="Open", command=open_file)
btn_save_as = tk.Button(master=frm_button, text="Save as", command=save_as)


frm_button.grid(row=0, column=0, sticky="ns")
txt_edit.grid(row=0, column=1, sticky="nsew")

btn_open.grid(row=0, column=0, padx=5, pady=5, sticky="ew")
btn_save_as.grid(row=1, column=0, padx=5, pady=5, sticky="ew")

window.mainloop()
