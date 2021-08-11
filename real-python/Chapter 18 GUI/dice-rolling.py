import tkinter as tk
import random


def dice():
    rolled_number = random.randint(0, 6)
    lbl_rolled_number["text"] = f"{rolled_number}"


window = tk.Tk()

window.columnconfigure(0, minsize=50, weight=1)
window.rowconfigure([0, 1], minsize=50, weight=1)


btn_roll = tk.Button(text="Roll", command=dice, master=window)
btn_roll.grid(row=0, column=0, sticky="nsew")


lbl_rolled_number = tk.Label(text="0", master=window)
lbl_rolled_number.grid(row=1, column=0, sticky="nsew")

window.mainloop()
