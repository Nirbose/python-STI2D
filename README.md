# Les fichiers
Il vous ait conseillé de prendre le fichier `main.py` et non ceux dans le dossier `/v2`, sinon il faut comprendre se qui s'y trouve à l'interieure pour pouvoir utiliser le programme.

# Informations
Dans un premier temps nous importons la librairie `tkinter` qui nous permet de créer une interface graphique grace à `from tkinter import *`.

ensuite, nous sauvegardons des variables :
```py
# Sauvegarde des variables pour les Radiobutton
a = IntVar()
b = IntVar()

# Stockage des bases de conversion (base 2, base 10, base 16)
bases = [2, 10, 16]
```

fonction qui permet de convertir un nombre en base 2, base 10 ou base 16 :
```py
def convB1ToB2(carac = ["0","1","2","3","4","5","6","7","8","9","A","B","C","D","E","F"]):
	number = entry.get()
	base = bases[a.get()]
	baseOut = bases[b.get()]

	nb = 0
	nbOut = ""
	indice = 0

    # on boucle pour tester le nombre
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
```

Nous finissons par l'affichage.

## Execution du code
Télécharger le ZIP [ici](https://github.com/Nirbose/python-STI2D/archive/refs/heads/main.zip)!

Pour l'executer il vous faut taper la commande `py main.py` ou clicker sur `F5` si votre IDE le supporte.