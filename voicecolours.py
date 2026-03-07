from tkinter import *
import speech_recognition as sr
from tkinter import messagebox

w = Tk()
w.title("Voice Colours")
w.geometry("500x200")

lbl = Label(w, text="Say a color name (red, blue green, etc.)")
lbl.pack()

def Listen():
    r = sr.Recognizer()
    with sr.Microphone() as source:
        r.adjust_for_ambient_noise(source)
        audio = r.listen(source)
        audio = r.listen(source)
        try:
            text = r.recognize_google(audio)
            w.config(bg=text)   
        except:
            messagebox.showinfo("Voice not recognised", "Please try speaking a colour name again.")

btn = Button(w, text="Listen", width=15, bg="#475C95", fg="#FFFFFF", command=Listen)
btn.pack()


w.mainloop()