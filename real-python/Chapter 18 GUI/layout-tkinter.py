import tkinter as tk

window = tk.Tk()
# 1
# frame1 = tk.Frame(master=window, bg="red", width=100, height=100)
# frame1.pack()


# frame2 = tk.Frame(master=window, bg="yellow", width=50, height=50)
# frame2.pack()

# frame3 = tk.Frame(master=window, bg="blue", width=25, height=25)
# frame3.pack()


# 2
# frame1 = tk.Frame(master=window, bg="red",  height=100)
# frame1.pack(fill=tk.X)


# frame2 = tk.Frame(master=window, bg="yellow",  height=50)
# frame2.pack(fill=tk.X)


# frame3 = tk.Frame(master=window, bg="blue",  height=25)
# frame3.pack(fill=tk.X)


# 3
# frame1 = tk.Frame(master=window, bg="red", width=200, height=100)
# frame1.pack(fill=tk.X, side=tk.LEFT, expand=True)


# frame2 = tk.Frame(master=window, bg="yellow", width=100, height=100)
# frame2.pack(fill=tk.X, side=tk.LEFT, expand=True)


# frame3 = tk.Frame(master=window, bg="blue", width=50, height=100)
# frame3.pack(fill=tk.X, side=tk.LEFT, expand=True)


# 4
# frame = tk.Frame(master=window, width=200, height=200)
# frame.pack()

# label1 = tk.Label(master=frame, text="I'm at (0,0)", bg="red")
# label1.place(x=0, y=0)

# label2 = tk.Label(master=frame, text="I'm at (75,75)", bg="yellow")
# label2.place(x=75, y=75)

# 5

# for i in range(3):
#     for j in range(3):
#         frame = tk.Frame(
#             master=window,
#             relief=tk.RAISED,
#             borderwidth=1)
#         frame.grid(row=i, column=j)
#         label = tk.Label(master=frame, text=f"Row{i}\n Column{j}")
#         label.pack()


# 6
for i in range(3):
    for j in range(3):
        frame = tk.Frame(
            master=window,
            relief=tk.RAISED,
            borderwidth=1)
        frame.grid(row=i, column=j, padx=5, pady=5)
        label = tk.Label(master=frame, text=f"Row {i}\nColumn {j}")
        label.pack(padx=5, pady=5)


# 7

# window.columnconfigure(0, minsize=250)
# window.rowconfigure([0, 1], minsize=100)

# label1 = tk.Label(master=window, text="A")
# label1.grid(row=0, column=0)

# label2 = tk.Label(master=window, text="B")
# label2.grid(row=1, column=0)

# 8

# window.columnconfigure(0, minsize=250)
# window.rowconfigure([0, 1], minsize=100)

# label1 = tk.Label(master=window, text="A")
# label1.grid(row=0, column=0, sticky="ne")

# label2 = tk.Label(master=window, text="B")
# label2.grid(row=1, column=0, sticky="sw")

# 9

# window.rowconfigure(0, minsize=50)
# window.columnconfigure([0, 1, 2, 3], minsize=50)

# label1 = tk.Label(master=window, text="1", fg="white", bg="black")
# label1.grid(row=0, column=0)

# label2 = tk.Label(master=window, text="2", fg="white", bg="black")
# label2.grid(row=0, column=1, sticky="we")

# label3 = tk.Label(master=window, text="3", fg="white", bg="black")
# label3.grid(row=0, column=2, sticky="ns")

# label4 = tk.Label(master=window, text="4", fg="white", bg="black")
# label4.grid(row=0, column=3, sticky="nesw")


window.mainloop()
