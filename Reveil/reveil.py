import time as t
import threading
from os import system

# fonction qui va lancer l'alarme avec pour paramètre la date de lancement ainsi que le lien de la vidéo à lancer


def alarm(time, video):
    # tant que l'alarme n'a pas sonnée
    ring = False
    while ring == False:
        # si la date récupérée est la même que celle à cet instant
        if time == t.strftime('%H:%M %d/%m/%Y'):
            ring = True
            # alors on envoie la commande suivante dans le terminal de l'ordinateur pour lancer la vidéo sur firefox
            system(f"firefox --private-window {video}")
            # on modifie le fichier qui sauvgarde les programmations d'alarmes
            updateFile(time)

# fonction qui permet de modifier le lien youtube reçus avec pour paramètre le lien de la vidéo


def washing(linkY):
    # on remplace "watch?v=" par "embed/" afin que la video prenne l'entierté du navigateur et
    # on ajoute "?autoplay=1" à la fin du lien afin que la vidéo se lance toute seule
    freshLink = (linkY.replace("watch?v=", "embed/"))+"?autoplay=1\n"
    return freshLink

# fonction qui sauvegarde les programmations d'alarme


def saveAlarm(alarmToSave, linkVideoToSave):
    # on ouvre le fichier et on y ajoute la date ainsi que le lien de la vidéo
    with open('saveAlarm.csv', 'a') as f:
        f.write(alarmToSave + "," + linkVideoToSave)

# fonction qui modifie le fichier de sauvegarde


def updateFile(theTime):
    # on crée un fichier dans lequelle on va copier le contenus du fichier de sauvegarde
    with open('saveAlarmC.csv', 'w') as fc:
        with open('saveAlarm.csv', 'r') as f:
            for line in f:
                fc.write(line)
    # on réécrit dans le fichier de sauvegarde les données en omettant la programmation qui a été réaliser
    with open('saveAlarm.csv', 'w') as f:
        with open('saveAlarmC.csv', 'r') as fc:
            for line in fc:
                date = line.split(',')
                if theTime != date[0]:
                    f.write(line)


# fonction qui initialise les alarmes en fonction des programmations enregistrées dans le fichier de sauvegarde


def initAlarm():
    # on crée deux listes contenant chacun respectivement les dates et les liens de vidéos
    dates = []
    videos = []
    # on essaie d'ouvrir le fichier, si il y arrive
    try:
        # alors on relance les thread des différents alarmes
        with open('saveAlarm.csv', 'r') as f:
            for line in f:
                date, video = line.split(',')
                dates.append(date)
                videos.append(video)
        for nbAlarm in range(len(dates)):
            anAlarm = threading.Thread(target=alarm, args=(dates[nbAlarm], videos[nbAlarm],))
            anAlarm.start()
    # si on a pas réussi à l'ouvrir alors on fait rien
    except FileNotFoundError:
        pass


# on appelle la fonction iniAlarm() afin de vérifier si il n'y a pas d'alarme qui a été programée avant l'arrêt du programme
initAlarm()

while True:

    # on demande si l'utilisateur souhaite voir l'heure ou programmer une alarme
    choice = input("Time   Alarm : ")
    # si il choisit de voir l'heure alors on la lui affiche
    if choice.lower() == "time":
        print(t.strftime('%H:%M %d/%m/%Y'))
    # si il choisit de programmer unn alarme
    elif choice.lower() == "alarm":
        # alors on lui demande pour quelle date ainsi que, quelle video en gage de sonnerie il souhaitera lancer
        talarm = input("Donnez la date et l'heure pour laquelle vous souhaitez programmer le réveil (HH:MM JJ/MM/AAAA)")
        linkVideo = input("Quelle video souhaitez-vous lancer lorsque l'alarme sonnera (mettez le lien d'une video de youtube) ? ")
        # on modifie le lien youtube afin que la vidéo s'affiche le mieux possible sur l'écran
        newLink = washing(linkVideo)
        # on enregistre la programmation de l'alarme dans un fichier .csv
        saveAlarm(talarm, newLink)
        # on lance un thread correspondant à cette alarme
        anAlarm = threading.Thread(target=alarm, args=(talarm, newLink,))
        anAlarm.start()
