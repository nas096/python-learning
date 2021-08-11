import tkinter as tk
import random
color_list = ["red", "orange", "yellow", "blue", "green", "indigo", "violet"]


def choose_color():
    random_color = random.choice(color_list)
    btn_click_me["background"] = random_color
    pass


window = tk.Tk()

btn_click_me = tk.Button(text="Click me", master=window,
                         fg="black", command=choose_color)
btn_click_me.pack()
window.mainloop()
