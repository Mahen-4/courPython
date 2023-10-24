import time

def ajouterFruit(): 
    quitter = False   
    while(quitter == False):
        getFruit = input("Quel est ton fruit préférer ")
        getFruitColor = input("Quel est la couleur de ce fruit ")
        fruit = {"nomFruit": getFruit, "couleurFruit": getFruitColor}
        fruitPref.append(fruit)
        getContinue = input("si tu veu ajouter d'autre fruit appui entrer sinon appuie sur Q ")
        if (getContinue == 'Q'):
            quitter = True

def messageDeSalutation():
    print("Salutation " + getPrenom + " " +getNom.upper())
    time.sleep(1)

def start():
    time.sleep(3)
    quitter = False
    while(quitter == False):
        print("--------------- Bienvenue sur le menu ---------------")
        print("Recevoir un message de salutation - A")
        print("Voir la liste de ces fruits préferer - B")
        print("Quitter - C")
        getOption = input("Ton choix : ")
        match getOption:
            case "A":
                messageDeSalutation()
            case "B":
                for fruit in fruitPref: 
                    print(fruit)
                time.sleep(1)
            case "C":
                quitter = True

getPrenom = input("Quel est ton prenom ? ")
getNom = input("Quel est ton nom ? ")
getAge = input("Quel age as tu ? ")
getTaille = input("Quel est ta taille (en cm) ? ")
fruitPref = []
ajouterFruit()
start()



