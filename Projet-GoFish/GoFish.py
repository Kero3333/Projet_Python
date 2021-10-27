import csv
import re
import tkinter as tk
from tkinter.constants import ANCHOR, END

# on définit la fenêtre
fenetre = tk.Tk()
fenetre.title("Go Fish")
fenetre.configure(background = 'white')
fenetre.resizable(0, 0)

# fonction qui sert à définir ce qui se passe lorsque la touche entrer est pressée
def keyEnterPressed(event):
    valider()

# fonction qui définit ce que le programme doit faire si le bouton valider est cliqué
def valider():
    choix=list.get(ANCHOR)  # on récupère l'objet qui a été selectionner dans la listbox

    # on récupère les différents choix ainsi que le tableau contenant les données sur la pêche
    global btnValider, saisonChoix, typePeche, fish, caractFish

    btnValider.click += 1  # on ajoute 1 au compteur de clique du bouton

    # lorsque l'on est à la première question du programme 
    if btnValider.click == 1:
        saisonChoix = choix  # on récupère le choix de la saison
        # on réactualise la question ainsi que les choix contenus dans la listbox
        list.delete(0, END)
        label.config(text = "Appuyez sur la touche correspondant au mode de pêche que vous souhaitez :" )
        choixTypePeche = ["pêche en mer", "pêche au bord"]
        for i in range(len(choixTypePeche)):
            list.insert(END, choixTypePeche[i])

    # lorsque l'on est à la deuxième question du programme        
    elif btnValider.click == 2:
        typePeche = choix
        list.delete(0, END)
        # on réactualise la question ainsi que les choix contenus dans la listbox, selon le choix de la saison éffectué et celui du type de pêche choisit
        if saisonChoix == "été":            
            if typePeche == "pêche en mer":
                label.config(text = "Voici les poissons que vous pouvez pêcher en mer l'été :")               
                for i in range(1,len(caractFish)):
                    if re.search("ete" , caractFish[i][2]) or re.search("Toute l'annee" , caractFish[i][2]):
                        if caractFish[i][7] != "\n":
                            list.insert(END, caractFish[i][0])
            
            if typePeche == "pêche au bord":
                label.config(text = "Voici les poissons que vous pouvez pêcher au bord l'été :")
                for i in range(1,len(caractFish)):
                    if re.search("ete" , caractFish[i][2]) or re.search("Toute l'annee" , caractFish[i][2]):
                        if caractFish[i][6] != "\n":
                            list.insert(END, caractFish[i][0])

        if saisonChoix == "printemps":            
            if typePeche == "pêche en mer":
                label.config(text = "Voici les poissons que vous pouvez pêcher en mer le printemps :")
                for i in range(1,len(caractFish)):
                    if re.search("printemps" , caractFish[i][2]) or re.search("Toute l'annee" , caractFish[i][2]):
                        if caractFish[i][7] != "\n":
                            list.insert(END, caractFish[i][0])
            if typePeche == "pêche au bord":
                label.config(text = "Voici les poissons que vous pouvez pêcher au bord le printemps :")
                for i in range(1,len(caractFish)):
                    if re.search("printemps" , caractFish[i][2]) or re.search("Toute l'annee" , caractFish[i][2]):
                        if caractFish[i][6] != "\n":
                            list.insert(END, caractFish[i][0])

        if saisonChoix == "hiver":            
            if typePeche == "pêche en mer":
                label.config(text = "Voici les poissons que vous pouvez pêcher en mer l'hiver :")
                for i in range(1,len(caractFish)):
                    if re.search("hiver" , caractFish[i][2]) or re.search("Toute l'annee" , caractFish[i][2]):
                        if caractFish[i][7] != "\n":
                            list.insert(END, caractFish[i][0])
            if typePeche == "pêche au bord":
                label.config(text = "Voici les poissons que vous pouvez pêcher au bord l'hiver :")
                for i in range(1,len(caractFish)):
                    if re.search("hiver" , caractFish[i][2]) or re.search("Toute l'annee" , caractFish[i][2]):
                        if caractFish[i][6] != "\n":
                            list.insert(END, caractFish[i][0])

        if saisonChoix == "automne":           
            if typePeche == "pêche en mer":
                label.config(text = "Voici les poissons que vous pouvez pêcher en mer l'automne :")
                for i in range(1,len(caractFish)):
                    if re.search("automne" , caractFish[i][2]) or re.search("Toute l'annee" , caractFish[i][2]):
                        if caractFish[i][7] != "\n":
                            list.insert(END, caractFish[i][0])
            if typePeche == "pêche au bord":
                label.config(text = "Voici les poissons que vous pouvez pêcher au bord en automne :")
                for i in range(1,len(caractFish)):
                    if re.search("automne" , caractFish[i][2]) or re.search("Toute l'annee" , caractFish[i][2]):
                        if caractFish[i][6] != "\n":
                            list.insert(END, caractFish[i][0])

    # lorque l'on est à la troisième question du programme
    elif btnValider.click == 3:
        fish = choix
        list.grid_forget()  # on fait disparaître la listbox

        # on affiche les caratéristiques du poisson choisit
        for i in range(1,len(caractFish)):
            if fish == caractFish[i][0]:
                nbFish = i
        if typePeche == "pêche en mer":
            label.config(text = f"  \n \n Vous voulez pêcher le poisson {caractFish[nbFish][0]} vous aurez besoin \n comme appât : {caractFish[nbFish][4]} \n comme leurre/technique : {caractFish[nbFish][5]} \n les coins de pêche sont : {caractFish[nbFish][7]} \n Attention la taille minimal autorisée est : {caractFish[nbFish][3]} cm")
        if typePeche == "pêche au bord":
            label.config(text = f" \n \n Vous voulez pêcher le poisson {caractFish[nbFish][0]} vous aurez besoin \n comme appât : {caractFish[nbFish][4]} \n comme leurre/technique : {caractFish[nbFish][5]} \n les coins de pêche sont : {caractFish[nbFish][6]} \n Attention la taille minimal autorisée est : {caractFish[nbFish][3]} cm")
        btnValider.grid_forget()
              
# on définit la listbox dans lequel on affiche les choix possibles
list = tk.Listbox(fenetre)
list.grid(row=1, column=0)

# on crée le bouton valider
btnValider = tk.Button(fenetre, height = 1, width = 10, text = "Valider", command = valider)
btnValider.grid(row = 2, column = 0)
btnValider.click = 0 #  on initialise le nombre de click du boutton à 0

# on crée la fonction de la touche enter
fenetre.bind('<Return>', keyEnterPressed)

# on récupère les données contenus dans le fichier Poisson.csv
caractFish = []
with open("Poissons.csv", "r") as f:
    for data in f:
        caractFish.append(data.split(','))

# on affiche les saisons
saison=["été","printemps","hiver","automne"]
for i in range(len(saison)):
    list.insert(END, saison[i])

# on affiche la première question
label = tk.Label(fenetre, text = "Appuyez sur la touche correspondant a la saison actuel :",bg = 'white', fg = 'black', font = 10)
label.grid(row = 0, column = 0)

# on initialise les variables qui vont servir à enregistrer les choix effectuer par l'utilisateur
saisonChoix, typePeche, fish = "", "", ""

# on génère notre fenêtre
fenetre.mainloop()