from tkinter import *
import random
from tkinter import messagebox

w = Tk()
w.title("unscramble the word!")
w.geometry("500x350")

og_words = ["bouquets", "hibiscus", "photosynthesis", "chlorophyll", "mitochondria"]
scramble_words = ["qsubouet", "uishcbis", "toohpysseshnit", "lyoorlchpl", "motrihocandi"]

num_letters = random.randrange(0, len(scramble_words), 1)
score = 0
total = 0
str_score = ""

def check():
    global og_words, scramble_words, score, total, num_letters
    guess = user_input.get()
    total += 1
    if guess == og_words[num_letters]:
        messagebox.showinfo("Correct","Congrats! Correct answer (that was hard wasn't it).")
        score += 1
    else:
        messagebox.showinfo("Incorrect","Wrong answer. Keep guessing!")
    str_score = "SCORE: "+str(score)+"/"+str(total)
    score_lbl.config(text=str_score)


def new_word():
    global scramble_words
    nw = random.choice(scramble_words)
    word_lbl.config(text=nw)
    user_input.delete(0, "end")
    

#reset
#config of stuff

def default():
    global scramble_words, num_letters
    word_lbl.config(text=scramble_words[num_letters])

def reset():
    global score, total
    default()
    score = 0
    total = 0
    str_score = "SCORE: "+str(score)+"/"+str(total)
    score_lbl.config(text=str_score)
    user_input.delete(0, "end")
    """choose = random.choice(scramble_words)"""

title_lbl = Label(w, text="Word Unscramble Game", font=("Arial", 20, "bold"), fg="#41779B")
title_lbl.pack(pady=15)

word_lbl = Label(w, text="", font=("Arial", 15), fg="#5A8698")
word_lbl.pack(pady=5)

score_lbl = Label(w, text="", font=("Arial", 13, "italic"), fg="#5A8698")
score_lbl.pack()

user_input = Entry(w, width=25)
user_input.pack(pady=10)

guess_btn = Button(w, text="Guess", font=("Arial", 12), command = check, fg="#FFFFFF", bg="#3C4C6E")
guess_btn.pack(pady=10)

#new_btn = Button(w, text="New Word", font=("Arial", 12), command = default, fg="#FFFFFF", bg="#3C4C6E")
#new_btn.pack(pady=5)

restart_btn = Button(w, text="Reset", font=("Arial", 12), command=reset, fg="#FFFFFF", bg="#3C4C6E")
restart_btn.pack(pady=5)

result_lbl = Label(w, text="", font=("Arial", 10, "italic"), fg="#415C9B")
title_lbl.pack(pady=10)

default()
"""    if len(user_input.get()) == 0:
        messagebox.showerror("Error", "Please input a value in the entry box.")"""
w.mainloop()