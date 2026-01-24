from tkinter import *
from tkinter.filedialog import *
w = Tk()
w.title("simple memorizer :)")

def openFile():
    fin = askopenfile(title="Open File")
    if fin is not None:
        listbox.delete(0, END)
        #read from files
        items = fin.readlines()
        #insert items in list
        for item in items:
            listbox.insert(END, item.strip())
        
def saveFile():
    #save file as a text file
    fout = asksaveasfile(defaultextension=".txt")
    if fout is not None:
        for item in listbox.get(0, END):
            print(item.strip(), file=fout)
        #delete items from listbox
        listbox.delete(0, END)

def addItem():
    #add items to list
    listbox.insert(END, item.get())
    item.delete(0, END)

def deleteItem():
    #delete items from listbox
    index = listbox.curselection()
    #recognise index numbers to delete stuff
    if index:
        listbox.delete(index)

fOpen = Button(w, text="OPEN", command = openFile, width = 15)
lDelete = Button(w, text="DELETE", command=deleteItem, width=15)
fSave = Button(w, text="SAVE", command = saveFile, width=15)

fOpen.pack(side=LEFT, padx=5, pady=5)
lDelete.pack(side=RIGHT, padx=5, pady=5)
fSave.pack(padx=5, pady=5)

lAdd = Button(w, text="ADD", command=addItem, width=15)
item = Entry(w, width=35)

item.pack(padx=5, pady=5)
lAdd.pack(padx=5, pady=5)

frame = Frame(w)

scroll = Scrollbar(frame, orient="vertical")
scroll.pack(side=RIGHT, fill=Y)

listbox = Listbox(frame, width=70, yscrollcommand=scroll.set, bg="red")

for i in range(1, 101):
    listbox.insert(END, "LIST" + str(i))

listbox.pack(side=LEFT, padx=5)
scroll.config(command=listbox.yview)

frame.pack(side=RIGHT)

w.mainloop()