import time
import tkinter as tk

root = tk.Tk()
root.title("Ei-Timer GUI")
root.configure(bg="lightyellow")

Head = tk.Label(root, text="Ei-Timer Version 1.7", bg="white", font="Sans-Serif 16")
Head.pack(pady=10)

label = tk.Label(root,text="Wie willst du dein EI?\nWähle aus:")
label.pack(pady=10)

Durchgebraten = tk.Button(root, text="Durchgebraten")
Durchgebraten.pack(pady=10)

Weich = tk.Button(root, text="Weich")
Weich.pack(pady=10)

Ultraweich =tk.Button(root, text="Ultraweich")
Ultraweich.pack(pady=10)

Sekunden = tk.Label(root, text="Verbleibende Zeit:")
Sekunden.pack(pady=10)

def countdown(sekunden):
    if sekunden >=0:
        Sekunden.config(root, text=f"Verbleibende Zeit: {sekunden} Sekunden")
        root.after(1000, countdown, sekunden-1)


if Durchgebraten == pressed():
    countdown(600) # 10 Minuten
elif Weich == True:
    countdown(360) # 6 Minuten
elif Ultraweich == True:
    countdown(180)
root.mainloop()



