from tkinter import *

# Génération de la fenêtre
window = Tk(screenName="Conversion GUI")
window.geometry("500x250") # Taille de la fenêtre
window.title("Conversion Multi-bases") # Titre de la fenêtre

# Sauvegarde des variables pour les Radiobutton
a = IntVar()
b = IntVar()

bases = [2, 10, 16] # Stockage des bases

# Fonction de convertion
def convB1ToB2(carac = ["0","1","2","3","4","5","6","7","8","9","A","B","C","D","E","F"]):
	number = entry.get()
	base = bases[a.get()]
	baseOut = bases[b.get()]

	nb = 0
	nbOut = ""
	indice = 0

	for i in range(0,len(number)):

		indice -= 1
		for i in range(0, len(carac)):
			if number[indice] == carac[i] or carac[i] == carac[base-1]:
				nb += i*(base**((indice+1)*-1))
				break

	indice = 0
	while nb // baseOut**indice >= baseOut :
		indice += 1

	while indice != -1 :
		if nb//baseOut**indice <= baseOut :
			nbOut += str(carac[nb//baseOut**indice])
			nb -= baseOut**indice*(nb//baseOut**indice)
		else :
			nbOut += "0"
		indice -= 1
	
	label['text'] = f"Le résultat est : {nbOut}"

# Components :
Label(text="Nombre a convertir :").pack()
entry = Entry()
entry.pack()

Radiobutton(text="Binaire", value=0, variable=b).pack()
Radiobutton(text="Decimal", value=1, variable=b).pack()
Radiobutton(text="Hexa", value=2, variable=b).pack()

Label(text="Conversion vers :").pack()
Radiobutton(text="Binaire", value=0, variable=b).pack()
Radiobutton(text="Decimal", value=1, variable=b).pack()
Radiobutton(text="Hexa", value=2, variable=b).pack()

Button(text="Convertir", command=convB1ToB2).pack()

label = Label(text="Le résultat est : rien pour l'instant")
label.pack()

window.mainloop()