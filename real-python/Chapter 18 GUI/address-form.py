import tkinter as tk
from tkinter.constants import SUNKEN


window = tk.Tk()
window.title("Address Entry Form")

frame = tk.Frame(
    master=window,
    relief=SUNKEN,
    borderwidth=3)
frame.pack()
# frame.columnconfigure([0, 1], weight=1, minsize=500)
# frame.rowconfigure([0, 1, 2, 3, 4, 5, 6, 7], weight=1, minsize=500)
lbl_firstName = tk.Label(master=frame, text="First Name: ")
ent_firstName = tk.Entry(master=frame, width=50)
lbl_firstName.grid(row=0, column=0, sticky="e")
ent_firstName.grid(row=0, column=1, sticky="w")

lbl_lastName = tk.Label(master=frame, text="Last Name: ")
ent_lastName = tk.Entry(master=frame, width=50)
lbl_lastName.grid(row=1, column=0, sticky="e")
ent_lastName.grid(row=1, column=1, sticky="w")

lbl_addressLine1 = tk.Label(master=frame, text="Address Line 1: ")
ent_addressLine1 = tk.Entry(master=frame, width=50)
lbl_addressLine1.grid(row=2, column=0, sticky="e")
ent_addressLine1.grid(row=2, column=1, sticky="w")

lbl_addressLine2 = tk.Label(master=frame, text="Address Line 2: ")
ent_addressLine2 = tk.Entry(master=frame, width=50)
lbl_addressLine2.grid(row=3, column=0, sticky="e")
ent_addressLine2.grid(row=3, column=1, sticky="w")

lbl_city = tk.Label(master=frame, text="City: ")
ent_city = tk.Entry(master=frame, width=50)
lbl_city.grid(row=4, column=0, sticky="e")
ent_city.grid(row=4, column=1, sticky="w")

lbl_stateProvince = tk.Label(master=frame, text="State/Province: ")
ent_stateProvince = tk.Entry(master=frame, width=50)
lbl_stateProvince.grid(row=5, column=0, sticky="e")
ent_stateProvince.grid(row=5, column=1, sticky="w")

lbl_postalCode = tk.Label(master=frame, text="Postal Code: ")
ent_postalCode = tk.Entry(master=frame, width=50)
lbl_postalCode.grid(row=6, column=0, sticky="e")
ent_postalCode.grid(row=6, column=1, sticky="w")

lbl_country = tk.Label(master=frame, text="Country: ")
ent_country = tk.Entry(master=frame, width=50)
lbl_country.grid(row=7, column=0, sticky="e")
ent_country.grid(row=7, column=1, sticky="w")


btn_submit = tk.Button(master=window, text="Submit")
btn_submit.pack(fill=tk.Y, side=tk.RIGHT, padx=10, pady=4, ipadx=10, ipady=2)
btn_clear = tk.Button(master=window, text="Clear")
btn_clear.pack(fill=tk.Y, side=tk.RIGHT, padx=5, pady=4, ipadx=10, ipady=2)

window.mainloop()
