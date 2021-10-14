from sys import argv, exit

# on test le nombre d'arguments reçus
if len(argv) != 3:
    print("Usage: python dna.py data.csv sequence.txt")
    exit(1)
# on test si ces arguments contiennent des fichiers avec une extension
if argv[1].find(".") == -1 or argv[2].find(".") == -1:
    print("Usage: python dna.py data.csv sequence.txt")
    exit(1)
# on test le type de fichiers reçus
else:
    typeFile = argv[1].split('.')
    if typeFile[1] != "csv":
        print("Usage: python dna.py data.csv sequence.txt")
        exit(1)
    typeFile = argv[2].split('.')
    if typeFile[1] != "txt":
        print("Usage: python dna.py data.csv sequence.txt")
        exit(1)

# on ouvre le fichier .csv en lecture
fdata = open(argv[1], "r")

# on récupère les données du fichier et on les place dans une liste appelée tableD
tableD = []
for x in fdata:
    tableD.append(x.replace("\n", '').split(","))
fdata.close()  # on ferme le fichier .csv

# on ouvre le chier .txt en lecture
fdna = open(argv[2], "r")

# on place ces données dans un string appelé dna
dna = fdna.readline()
fdna.close()  # on ferme le fichier .txt

# on crée un dictionnaire vide afin de récupérer le nombre de match qu'il y a eu entre les séquences d'adn contenu dans tableD et dna
match = {}
# on crée un second dictionnaire afin de comptabiliser le nombre de séquence d'adn qui colle avec une personne contenu dans tableD
nameMatch = {}

# pour chaque séquence d'adn contenu dans tableD
for i in range(1, len(tableD[0])):
    match[tableD[0][i]] = 0
    n = len(tableD[0][i])

    # pour chaque séquence d'adn contenu dans dna
    for j in range(len(dna)):
        if tableD[0][i] == dna[j:n]:
            match[tableD[0][i]] += 1
        n += 1

    # si le nombre de match d'une sequence d'adn est différent de 0
    if match[tableD[0][i]] != 0:

        # alors pour chaque personne ayant le même nombre de la même séquence d'adn
        for j in range(1, len(tableD)):
            if int(tableD[j][i]) == match[tableD[0][i]]:

                # on lui compte une correspondance en plus
                try:
                    nameMatch[tableD[j][0]] += 1
                except KeyError:
                    nameMatch[tableD[j][0]] = 1

# on vérifie si une personne a obtenus une correspondance parfaite avec la séquence d'adn contenu dans le fichier .txt
matchOrNot = 0
for name, nbMatch in nameMatch.items():
    if nbMatch == (len(tableD[0]) - 1):
        matchOrNot = 1
        print(name)

# si il n'y a pas eu de correspondance on affiche "No match"
if matchOrNot == 0:
    print("No match")
