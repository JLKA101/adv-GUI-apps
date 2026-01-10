from tkinter import *
from tkinter.ttk import *

w = Tk()
w.title("Multiplication Table")

title_lbl = Label(w, text="Multiplication Table Generator")
title_lbl.grid(row=0, column=0, columnspan=3, pady=25)

select_lbl = Label(w, text="Select a Number: ")
select_lbl.grid(row=1, column=0, padx=10)

#Combobox creation
nums = IntVar()
dropdown = Combobox(w, textvariable=nums, width=8, state="readonly")
dropdown["values"] = tuple(range(101))
dropdown.grid(row=1, column=1)

#Creating Radiobuttons
val = IntVar()
r10 = Radiobutton(w, text="10", variable=val, value=10)
r20 = Radiobutton(w, text="20", variable=val, value=20)
r30 = Radiobutton(w, text="30", variable=val, value=30)
val.set(10)
r10.grid(row=1, column=2)
r20.grid(row=2, column=2, padx=30)
r30.grid(row=3, column=2, padx=30)




w.mainloop()