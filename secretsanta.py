from tkinter import *
from gtts import gTTS
import os
import random
from PIL import Image, ImageTk

w = Tk()
w.geometry("500x500")
w.title("secret santa :3")
w.config(bg="red")

msgs  = ["Merry Christmas! I hope you have a great day!", "Happy New Year! Any resolutions?",  "Have a relaxing Christmas holiday :)", "May your Christmas be filled with the warmth of family and friends."]
imgs = ["images/realbaubles.png", "images/realholly.png", "images/realstocking.png"]

def send():
    msg.config(text=random.choice(msgs))
    imag = Image.open(random.choice(imgs))
    imag = imag.resize((250, 250))
    photo = ImageTk.PhotoImage(imag)
    img_lbl.config(image=photo)
    img_lbl.image = photo

title_lbl = Label(w, text="Secret Santa Surprise!", font=("Verdana", 15, "bold"), fg="white", bg="red")
title_lbl.pack(pady=10)

msg = Label(w, text="", font=("Helvetica", 12), fg="white", bg="#ff0000")
msg.pack(pady=10)

img_lbl = Label(w)
img_lbl.pack(pady=10)

send_btn = Button(w, text="Send",width=25, command=send)
send_btn.pack(pady=10)

w.mainloop()
#####|##\###
####\|##\/##
#####/##|###
###/ _  _\##
#/    __  |#
#|    ^   |#
############

"""("Comic Sans MS", 18)
("Arial Rounded MT Bold", 16)
("Verdana", 14)
("Helvetica", 14)
("Calibri", 14)
("Segoe UI", 14)
("Impact", 18)
("Courier New", 14, "bold")
("Comic Sans MS", 16, "bold")
("Georgia", 14, "italic")
("Times New Roman", 16)"""