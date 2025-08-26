import tkinter as tk

def countdown(sekunden):
    if sekunden >= 0:
        Sekunden.config(text=f"Verbleibende Zeit: {sekunden} Sekunden")
        root.after(1000, countdown, sekunden-1)
    else:
        Sekunden.config(text="Guten Appetit!")

root = tk.Tk()
root.title("Ei-Timer GUI")
root.configure(bg="yellow")

label = tk.Label(root, text="Ei-Timer Version 1.4", bg="white", font=("Times New Roman", 16))
label.pack(pady=10)

head = tk.Label(root, text="Wie willst du dein Ei?")
head.pack(pady=10)

Sekunden = tk.Label(root, text="Verbleibende Zeit:")
Sekunden.pack(pady=10)

Durchgebraten = tk.Button(root, text="Durchgebraten", command=lambda: countdown(600)) # 10 Minuten
Durchgebraten.pack(pady=10)

Weich = tk.Button(root, text="Weich", command=lambda: countdown(360)) # 6 Minuten
Weich.pack(pady=10)

Ultraweich = tk.Button(root, text="Ultraweich", command=lambda: countdown(180)) # 3 Minuten
Ultraweich.pack(pady=10)

root.mainloop()








