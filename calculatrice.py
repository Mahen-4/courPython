import tkinter as tk


def addition():
    resultat = int(num1.get()) + int(num2.get())
    res = tk.Label(fenetre, text=resultat)
    res.pack()

def soustraction():
    resultat = int(num1.get()) - int(num2.get())
    res = tk.Label(fenetre, text=resultat)
    res.pack()

def multiplication():
    resultat = int(num1.get()) * int(num2.get())
    res = tk.Label(fenetre, text=resultat)
    res.pack()

def division():
    resultat = int(num1.get()) / int(num2.get())
    res = tk.Label(fenetre, text=resultat)
    res.pack()

fenetre = tk.Tk()
fenetre.title("Calculatrice")

etiquette = tk.Label(fenetre, text="Calculatrice")
etiquette.pack()


num1 = tk.Entry(fenetre)
num1.pack()

# mail
num2 = tk.Entry(fenetre)
num2.pack()


button = tk.Button(fenetre, text="+", command= addition)
button.pack()
button = tk.Button(fenetre, text="-", command= soustraction)
button.pack()
button = tk.Button(fenetre, text="*", command= multiplication)
button.pack()
button = tk.Button(fenetre, text="/", command= division)
button.pack()
fenetre.geometry("400x300")
fenetre.mainloop()


