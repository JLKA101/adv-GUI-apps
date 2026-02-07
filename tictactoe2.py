import random
import tkinter
from tkinter import *
from functools import partial
from tkinter import messagebox
from copy import deepcopy #using two separate boards

w = Tk()
w.title("Tic Tac Toe V2.0")

sign = 0 #even = player X, odd = player O/computer

global board
board = [[" " for x in range(3)] for you in range(3)] #3x3 board

#l = label
#b = button
def winner(b, l):
    return(
        #checking rows
        (b[0][0] == l and b[0][1] == l and b[0][2] == l) or
        (b[1][0] == l and b[1][1] == l and b[1][2] == l) or
        (b[2][0] == l and b[2][1] == l and b[2][2] == l) or
        
        #checking columns
        (b[0][0] == l and b[1][0] == l and b[2][0] == l) or
        (b[0][1] == l and b[1][1] == l and b[2][1] == l) or
        (b[0][2] == l and b[1][2] == l and b[2][2] == l) or

        #checking diagonals
        (b[0][0] == l and b[1][1] == l and b[2][2] == l) or
        (b[0][2] == l and b[1][1] == l and b[2][0] == l)
    )

#i = row
#j = column
def get_text(i, j, gb, l1, l2):
    global sign

    if board[i][j] == "":
        if sign % 2 == 0:
            l1.config(state = DISABLED)
            l2.config(state = ACTIVE)
            #player 2 is X ^
            board[i][j] = "X"
        else:
            l2.config(state = DISABLED)
            l1.config(state = ACTIVE)
            board[i][j] = "O"

        sign += 1 #for turns
        button[i][j].config(text = board[i][j])
    
    if winner(board, "X"):
        gb.destroy()
        box = messagebox.showinfo("Winner", "Player 1 won the match!")

    elif winner(board, "O"):
        gb.destroy()
        box = messagebox.showinfo("Winner", "Player 2 won the match!")

    elif isfull():
        gb.destroy()
        box = messagebox.showinfo("Tie", "Tie!")

def isfree():
    return board[i][j] == ""

def isfull():
    flag = True
    for i in board:
        if i.count("") > 0:
            flag = False
    return flag


w.mainloop()