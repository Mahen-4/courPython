import tkinter as tk
import re

print(tk.TkVersion)
regex = r'\b[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Z|a-z]{2,7}\b'

def getData():
   
        if champTextPseudo.get() and champTextMail.get() and champTextMdp.get():
            print("Pseudo : " + champTextPseudo.get())
            print("Mail : " + champTextMail.get())
            print("Mot de passe : " + champTextMdp.get())
        else:
            print("Tous les champs sont requis")

fenetre = tk.Tk()
fenetre.title("Launcher")

etiquette = tk.Label(fenetre, text="Inscription")
etiquette.pack()

# pseudo
pseudoLabel = tk.Label(fenetre, text="Pseudo")
champTextPseudo = tk.Entry(fenetre)
pseudoLabel.pack()
champTextPseudo.pack()

# mail
mailLabel = tk.Label(fenetre, text="mail")
champTextMail = tk.Entry(fenetre)
mailLabel.pack()
champTextMail.pack()

# mdp
mdpLabel = tk.Label(fenetre, text="mdp")
champTextMdp = tk.Entry(fenetre, show="*")
mdpLabel.pack()
champTextMdp.pack()


button = tk.Button(fenetre, text="Inscription", command= getData)
button.pack()

fenetre.geometry("400x300")
fenetre.mainloop()