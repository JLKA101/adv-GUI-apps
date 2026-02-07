from tkinter import *
from tkinter import messagebox
mainw = Tk()
mainw.title("Tic Tac Toe V1.0")
turn = 1
result = ""
def Win():
    global result

    #cget = configure get
    #b1/2/3 etc. = buttons 1/2/3 etc.

    #ROW 1
    if b1.cget("text") == b2.cget("text") == b3.cget("text") == "X":
        result = "Player 1 wins!"
    elif b1.cget("text") == b2.cget("text") == b3.cget("text") == "O":
        result = "Player 2 wins!"

    #ROW 2
    elif b4.cget("text") == b5.cget("text") == b6.cget("text") == "X":
        result = "Player 1 wins!"
    elif b4.cget("text") == b5.cget("text") == b6.cget("text") == "O":
        result = "Player 2 wins!"

    #ROW 3
    elif b7.cget("text") == b8.cget("text") == b9.cget("text") == "X":
        result = "Player 1 wins!"
    elif b7.cget("text") == b8.cget("text") == b9.cget("text") == "O":
        result = "Player 2 wins!"


    #COLUMN 1
    elif b1.cget("text") == b4.cget("text") == b7.cget("text") == "X":
        result = "Player 1 wins!"
    elif b1.cget("text") == b4.cget("text") == b7.cget("text") == "O":
        result = "Player 2 wins!"

    #COLUMN 2
    elif b2.cget("text") == b5.cget("text") == b8.cget("text") == "X":
        result = "Player 1 wins!"
    elif b2.cget("text") == b5.cget("text") == b8.cget("text") == "O":
        result = "Player 2 wins!"

    #COLUMN 3
    elif b3.cget("text") == b6.cget("text") == b9.cget("text") == "X":
        result = "Player 1 wins!"
    elif b3.cget("text") == b6.cget("text") == b9.cget("text") == "O":
        result = "Player 2 wins!"


    #DIAGONAL 1
    elif b1.cget("text") == b5.cget("text") == b9.cget("text") == "X":
        result = "Player 1 wins!"
    elif b1.cget("text") == b5.cget("text") == b9.cget("text") == "O":
        result = "Player 2 wins!"

    #DIAGONAL 2
    elif b3.cget("text") == b5.cget("text") == b7.cget("text") == "X":
        result = "Player 1 wins!"
    elif b3.cget("text") == b5.cget("text") == b7.cget("text") == "O":
        result = "Player 2 wins!"

    elif all(btn.cget('text') != '' for btn in [b1,b2,b3,b4,b5,b6,b7,b8,b9]):
        result = "It's a Tie!"
    else:
        return
    

    messagebox.showinfo("Result: ", str(result))
    mainw.destroy()


def b1Click():
    global turn
    myText = b1.cget("text")
    if myText == "":
        if turn == 1:
            b1.configure(text = "X")
            turn = 2
        else:
            b1.configure(text = "O")
            turn = 1
    lbl.configure(text="Player " + str(turn) + "'s Turn")
    Win()

def b2Click():
    global turn
    myText = b2.cget("text")
    if myText == "":
        if turn == 1:
            b2.configure(text = "X")
            turn = 2
        else:
            b2.configure(text = "O")
            turn = 1
    lbl.configure(text="Player " + str(turn) + "'s Turn")
    Win()

def b3Click():
    global turn
    myText = b3.cget("text")
    if myText == "":
        if turn == 1:
            b3.configure(text = "X")
            turn = 2
        else:
            b3.configure(text = "O")
            turn = 1
    lbl.configure(text="Player " + str(turn) + "'s Turn")
    Win()

def b4Click():
    global turn
    myText = b4.cget("text")
    if myText == "":
        if turn == 1:
            b4.configure(text = "X")
            turn = 2
        else:
            b4.configure(text = "O")
            turn = 1
    lbl.configure(text="Player " + str(turn) + "'s Turn")
    Win()

def b5Click():
    global turn
    myText = b5.cget("text")
    if myText == "":
        if turn == 1:
            b5.configure(text = "X")
            turn = 2
        else:
            b5.configure(text = "O")
            turn = 1
    lbl.configure(text="Player " + str(turn) + "'s Turn")
    Win()

def b6Click():
    global turn
    myText = b6.cget("text")
    if myText == "":
        if turn == 1:
            b6.configure(text = "X")
            turn = 2
        else:
            b6.configure(text = "O")
            turn = 1
    lbl.configure(text="Player " + str(turn) + "'s Turn")
    Win()

def b7Click():
    global turn
    myText = b7.cget("text")
    if myText == "":
        if turn == 1:
            b7.configure(text = "X")
            turn = 2
        else:
            b7.configure(text = "O")
            turn = 1
    lbl.configure(text="Player " + str(turn) + "'s Turn")
    Win()

def b8Click():
    global turn
    myText = b8.cget("text")
    if myText == "":
        if turn == 1:
            b8.configure(text = "X")
            turn = 2
        else:
            b8.configure(text = "O")
            turn = 1
    lbl.configure(text="Player " + str(turn) + "'s Turn")
    Win()

def b9Click():
    global turn
    myText = b9.cget("text")
    if myText == "":
        if turn == 1:
            b9.configure(text = "X")
            turn = 2
        else:
            b9.configure(text = "O")
            turn = 1
    lbl.configure(text="Player " + str(turn) + "'s Turn")
    Win()

b1 = Button(mainw, text="", width=5, command=b1Click)
b1.grid(row=0, column=0, padx=5, pady=5)

b2 = Button(mainw, text="", width=5, command=b2Click)
b2.grid(row=0, column=1, padx=5, pady=5)

b3 = Button(mainw, text="", width=5, command=b3Click)
b3.grid(row=0, column=2, padx=5, pady=5)

b4 = Button(mainw, text="", width=5, command=b4Click)
b4.grid(row=1, column=0, padx=5, pady=5)

b5 = Button(mainw, text="", width=5, command=b5Click)
b5.grid(row=1, column=1, padx=5, pady=5)

b6 = Button(mainw, text="", width=5, command=b6Click)
b6.grid(row=1, column=2, padx=5, pady=5)

b7 = Button(mainw, text="", width=5, command=b7Click)
b7.grid(row=2, column=0, padx=5, pady=5)

b8 = Button(mainw, text="", width=5, command=b8Click)
b8.grid(row=2, column=1, padx=5, pady=5)

b9 = Button(mainw, text="", width=5, command=b9Click)
b9.grid(row=2, column=2, padx=5, pady=5)


lbl = Label(mainw, text="Player" + str(turn) + "'s Turn")
lbl.grid(row=3, column=1, padx=10, pady=10)

mainw.mainloop()