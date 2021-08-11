import tkinter as tk


def fahrenheit_to_celcius():
    fahrenheit = int(ent_temperature.get())
    convert = (fahrenheit - 32) * (5/9)
    lbl_results["text"] = f"{convert:.1f} \u2103"


window = tk.Tk()
window.title('Temperature Converter')
window.resizable(width=False, height=False)
frm_entry = tk.Frame(window)


ent_temperature = tk.Entry(master=frm_entry, width=10)
lbl_fahrenheit = tk.Label(master=frm_entry, text="\u2109")

ent_temperature.grid(row=0, column=0, sticky="e")
lbl_fahrenheit.grid(row=0, column=1, sticky="w")

btn_converter = tk.Button(master=window,
                          text="\u2192",
                          command=fahrenheit_to_celcius)

lbl_results = tk.Label(master=window, text="0 \u2103")

frm_entry.grid(row=0, column=0, padx=10)
btn_converter.grid(row=0, column=1, pady=10)
lbl_results.grid(row=0, column=2, padx=10)

window.mainloop()
