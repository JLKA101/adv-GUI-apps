from tkinter import *
import speech_recognition as sr
from tkinter import messagebox
from tkinter.filedialog import asksaveasfile

w = Tk()
w.title("Speech Recognition")
w.geometry("1000x400")

h1 = Label(w, text="Voice Notepad", font=("Arial", 30, "bold"))
h1.grid(row=0, column=1, padx=20, pady=20)

output_text = Text(w, height=6, width=40, font=("Arial", 12))
output_text.grid(row=1, column=1, padx=20, pady=20)

def Translate():
    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("Speak anything")
        r.adjust_for_ambient_noise(source)
        audio = r.listen(source)
        try:
            text = r.recognize_google(audio)
        except:
            text = "Sorry, could not recognise your voice."
    output_text.delete(1.0, END) #text keeps updating - this deletes
    output_text.insert(END, text) #this inserts new text

def Save():
    fOut = asksaveasfile(defaultextension=".txt") #notepad file format
    if fOut:
        fOut.write(output_text.get(1.0, END)) #saves output in file
        fOut.close()
        messagebox.showinfo("Saved", "Filed saved successfully.")
    else:
        messagebox.showinfo("Warning", "Text not saved.")

translate_btn = Button(w, text="Start recording", font=("Arial", 15, "bold"), command=Translate, width=20, bg="#4CAF50", fg="white")
translate_btn.grid(row=1, column=0, pady=20, padx=20)

save_btn = Button(w, text="Save text", font=("Arial", 12, "bold"), command=Save, width=20, bg="#5789A8", fg="white")
save_btn.grid(row=1, column=2, pady=10)

w.mainloop()