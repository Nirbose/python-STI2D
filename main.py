from tkinter import *

# Génération de la fenêtre
window = Tk(screenName="Conversion GUI")
window.geometry("500x250") # Taille de la fenêtre
window.title("Conversion Multi-bases") # Titre de la fenêtre

# Sauvegarde des variables pour les Radiobutton
a = IntVar()
b = IntVar()

bases = [2, 10, 16] # Stockage des bases

# Frame espaces
Fleft = Frame(window)
Fleft.pack(side=LEFT)

Frigth = Frame(window)
Frigth.pack(side=RIGHT)

Fbottom = Frame(window)
Fbottom.pack(side=BOTTOM)

# Fonction de convertion
def convB1ToB2():
    nbOut = int(str(entry.get()), bases[a.get()])

    if bases[b.get()] == 2:
        nbOut = bin(nbOut)[2:]

    elif bases[b.get()] == 16:
        nbOut = hex(nbOut)[2:]

    label['text'] = f"Le résultat est : {nbOut}"

# Components :
Label(text="Nombre a convertir :").pack()
entry = Entry()
entry.pack()

Label(Fleft, text="Base de depart").pack()
Radiobutton(Fleft, text="Binaire", value=0, variable=a, indicator = 0, width=15).pack()
Radiobutton(Fleft, text="Decimal", value=1, variable=a, indicator = 0, width=15).pack()
Radiobutton(Fleft, text="Hexa", value=2, variable=a, indicator = 0, width=15).pack()

Label(Frigth, text="Base d'arrivee").pack()
Radiobutton(Frigth, text="Binaire", value=0, variable=b, indicator = 0, width=15).pack()
Radiobutton(Frigth, text="Decimal", value=1, variable=b, indicator = 0, width=15).pack()
Radiobutton(Frigth, text="Hexa", value=2, variable=b, indicator = 0, width=15).pack()

Button(Fbottom, text="Convertir", command=convB1ToB2, width=25).pack()
Button(Fbottom, text="EXIT", foreground="red", command=window.destroy, width=25).pack()

label = Label(text="Le résultat est : rien pour l'instant")
label.pack()

window.mainloop()
