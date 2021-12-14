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