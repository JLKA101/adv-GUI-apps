from tkinter import *
from gtts import gTTS
import os

w =Tk()
w.title("Text to Speech App")
w.geometry("400x300")

def speak_text():
    text = entry_box.get("1.0", END)
    if text.strip() == "":
        status_lbl.config(text="Please enter some text.")
        return
    audio = gTTS(text=text, lang='en')
    audio.save("voice.mp3")
    os.system("voice.mp3")
    status_lbl.config(text="Speaking...")

title_lbl = Label(w, text="Text to Speech Converter", font=("Arial", 15, "bold"))
title_lbl.pack(pady=10)

entry_box = Text(w, width=150, height = 10)
entry_box.pack(pady=10)

speak_btn = Button(w, text="Speak", command = speak_text, bg="blue", fg="white")
speak_btn.pack(pady=10)

status_lbl = Label(w, text="")
status_lbl.pack()

w.mainloop()