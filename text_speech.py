from gtts import gTTS
from playsound import playsound
import tkinter as tk
import os


def reproduce(entry):
    ent_text = entry.get()
    language = "es"
    output = gTTS(text=ent_text, lang=language, slow=False)
    
    with open('output.mp3', 'wb') as f:
        output.write_to_fp(f)

    playsound('output.mp3')

    os.remove('output.mp3')


# Create GUI
window = tk.Tk()
window.geometry("350x350")

frm_sentence = tk.Frame(master=window, pady=20)
lbl_sentence = tk.Label(
    master= frm_sentence, 
    text="Text something:", 
    font=("Courier", 14),
    )
ent_sentence = tk.Entry(master=frm_sentence)
btn = tk.Button(master=window, text="Play", font=("Courier", 12), command=lambda: reproduce(ent_sentence))

frm_sentence.pack()
lbl_sentence.pack()
ent_sentence.pack()
btn.pack()

window.mainloop()
