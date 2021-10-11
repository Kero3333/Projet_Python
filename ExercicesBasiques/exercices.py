def main():
    # premier exercice
    exercice1()
    # second exercice
    exercice2()
    # troisième exercice
    exercice3()


def exercice1():
    # on récupère le premier entier ainsi que le second entier
    entier1 = int(input("veuillez saisir un premier entier\n"))
    entier2 = int(input("veuillez saisir un second entier\n"))
    # on affiche le produit des deux entiers
    print(f"Voici le produit de ces deux entiers : {entier1 * entier2}")


def exercice2():
    # on récupère le premier entier ainsi que le second entier
    entier1 = int(input("veuillez saisir un premier entier\n"))
    entier2 = int(input("veuillez saisir un second entier\n"))
    # on affiche les deux entiers
    print(f"la valeur du premier entier est de {entier1} et le second entier est de {entier2}")
    # on intevertit les valeurs
    tmp = entier1  # on initialise une variable temporaire avec entier1
    entier1 = entier2  # on stock la valeur de entier2 dans entier1
    entier2 = tmp  # on assigne tmp à l'entier2
    # on affiche les deux entiers après l'échange de leurs valeurs respective
    print(f"la valeur du premier entier après échange est de {entier1} et celui du second entier est de {entier2}")


def exercice3():

    # on récupère les trois entiers
    tabVal = []  # on initialise un tableau vide
    # on ajoute les trois entiers à ce tableau
    tabVal.append(int(input("veuillez saisir un premier entier\n")))
    tabVal.append(int(input("veuillez saisir un second entier\n")))
    tabVal.append(int(input("veuillez saisir un troisième entier\n")))
    # on fait le tri entre les 3 valeur saisis
    grandEntier = tabVal[0]  # on initialise la variable grandEntier à la première valeur saisi par défault
    for i in [1, 2]:  # on parcours le tableau à partir du second élément de celui-ci
        if tabVal[i] > grandEntier:  # si la valeur d'un élément du tableau est supérieur à la valeur de la variable grandEntier
            grandEntier = tabVal[i]  # alors grandEntier prend la valeur de l'élément du tableau
    # on affiche la variable grandEntier
    print(f"Voici le plus grand entier saisi : {grandEntier}")


# on appelle la fonction main
main()