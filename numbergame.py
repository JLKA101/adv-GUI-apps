from tkinter import *
from tkinter import messagebox
import random
w = Tk()
w.title("number guessing game :D")
w.geometry("400x220")
w.config(bg="#000000")

def reset():
    global num, attempts
    num = random.randint(1, 100)
    attempts = 0
    subtitle_lbl.config(text="Guess a number between 1 and 100!")
    user_input.delete(0, "end")

def check():
    global attempts
    guess = user_input.get()
    attempts += 1
    #check if guess is not digit
    if not guess.isdigit():
        messagebox.showerror("Error", "Invalid input. Please choose a number between 1 and 100.")
    guess = int(guess)
    if guess > 100 or guess < 1:
        messagebox.showerror("Error", "Invalid input. Please choose a number between 1 and 100.")
    if guess == num:
            if attempts == 1:
                      subtitle_lbl.config(text="Wow! First try?!")
            else:
                      subtitle_lbl.config(text=f"Well done! Took you {attempts} attempts.")
    elif guess > num:
                 subtitle_lbl.config(text=f"Guess lower. Attempts: {attempts}.")
    else:
                 subtitle_lbl.config(text=f"Guess higher. Attempts: {attempts}.")

title_lbl = Label(w, text="Guess the Number!", font=("Arial", 20, "bold"), bg="#000000", fg="#FFFFFF")
title_lbl.pack()

subtitle_lbl = Label(w, text="Guess a number between 1 and 100", font=("Arial", 15), bg="#000000", fg="#FFFFFF")
subtitle_lbl.pack()

user_input = Entry(w, width=20)
user_input.pack()

guess_btn = Button(w, text="Guess", font=("Arial", 15), command=check, bg="#FE6FCA", fg="#FFFFFF", bd=5, activebackground="#DF61B1", activeforeground="#FFFFFF")
guess_btn.pack()

reset_btn = Button(w, text="Reset", font=("Arial", 15), command=reset, bg="#FF46BB", fg="#FFFFFF", bd=5, activebackground="#D73A9E", activeforeground="#FFFFFF")
reset_btn.pack()

reset()

w.mainloop()