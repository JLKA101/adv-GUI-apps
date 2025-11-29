from tkinter import *
import random
w = Tk()
w.geometry("600x400")
w.title("rock, paper, scissors game")

title_lbl = Label(w, text="Rock, Paper, Scissors", font=("Arial", 20, "bold"), fg="#538467")
title_lbl.pack()

victory_lbl = Label(w, text="", font=("Arial", 15), fg="#6b9c7f")
victory_lbl.pack()

user_lbl = Label(w, text="", font=("Arial", 15), fg="#71a586")
user_lbl.pack()

comp_lbl = Label(w, text="", font=("Arial", 15), fg="#71a586")
comp_lbl.pack()

#functions above buttons
def check(player_choice):
    comp_options = ["rock", "paper", "scissors"]
    comp_choice = random.choice(comp_options)
    comp_lbl.config(text=f"Computer choice: {comp_choice}")
    user_lbl.config(text=f"Your choice: {player_choice}")
    if comp_choice == player_choice:
        result = "Tie."
    elif (player_choice == "rock" and comp_choice == "scissors") or (player_choice == "paper" and comp_choice == "rock") or (player_choice == "scissors" and comp_choice == "paper"):
        result = "You Win! :D"
    else:
        result = "You lose, computer wins :("
    victory_lbl.config(text=result)

rock_btn = Button(w, text="Rock", font=("Arial", 15), command=lambda: check("rock"), bd=5, bg="#9fc599", fg="#ffffff", activebackground="#84a67e", activeforeground="#f1f1f1", width= 10, height=1)
rock_btn.pack()

paper_btn = Button(w, text="Paper", font=("Arial", 15), command=lambda: check("paper"), bd=5, bg="#5f775b", fg="#ffffff", activebackground="#51664e", activeforeground="#f1f1f1", width= 10, height=1)
paper_btn.pack()

scissors_btn = Button(w, text="Scissors", font=("Arial", 15), command=lambda: check("scissors"), bd=5, bg="#4c5d48", fg="#ffffff", activebackground="#3c4b3a", activeforeground="#f1f1f1", width= 10, height=1)
scissors_btn.pack()

def reset():
    victory_lbl.config(text="")
    user_lbl.config(text="")
    comp_lbl.config(text="")

reset_btn = Button(w, text="Reset", font=("Arial", 15), command= reset, bd=5, bg="#3b4738", fg="#ffffff", activebackground="#293327", activeforeground="#f1f1f1", width= 10, height=1)
reset_btn.place(relx=0.5, rely= 0.8, anchor=CENTER)



w.mainloop()