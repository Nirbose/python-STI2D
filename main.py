from tkinter import *
from components import *

window = Tk(screenName="Conversion GUI") # Librairies
window.geometry("500x250") # Dimention
window.title("Conversion Multi-bases") # Titre de la fenêtre

a = IntVar()
b = IntVar()

view = Components() # Truc sympa pour que cela soit propre

bases = [2, 10, 16] # Stockage des bases

def conversion():
    # Calcule de conversion
    pass

def render():
    # Rendu sur la fenêtre
    print(a.get())
    print(b.get())
    
def convB1ToB2(carac = ["0","1","2","3","4","5","6","7","8","9","A","B","C","D","E","F"]):
	number = entry.get()
	base = bases[a.get()]
	baseOut = bases[b.get()]

	if base <= 1 or baseOut <= 1 :
		return "Error : base cannot be less than 1"

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

view.label("Nombre a convertir :")
entry = view.input()
view.radio(text="Binaire", value=0, variable=a)
view.radio(text="Decimal", value=1, variable=a)
view.radio(text="Hexa", value=2, variable=a)

view.label("Conversion vers :")
view.radio("Binaire", 0, b)
view.radio("Decimal", 1, b)
view.radio("Hexa", 2, b)

view.btn("Convertir", convB1ToB2)

label = view.label("Le résultat est : rien pour l'instant")

window.mainloop()