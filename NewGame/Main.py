# Fichier contenant le code principal du jeu
# On importe les class Monster et Personnage
from NewGame.Monster import *
from NewGame.Personnage import *

#On définit le nom du joueur
print("Enchanté "+Personnage.perso_name+", ravie de te connaitre!\nCe n'est pas l'heure des présentation défend toi !")

#Le joueur est attaqué par un 1er monstre
print("Vous êtes attaqué par un monstre, c'est un "+Monster.monster_name+"!\nIl a "+str(Monster.monster_life)+" point de vie.\nBonne chance !\n")

#tant que le joueur ou le monstre on de la vie le combat continue
while Monster.monster_life > 0 and Personnage.perso_life > 0:
    #le monstre attaque en 1er
    print("Le "+Monster.monster_name+" vous attaque ! Vous perdez "+str(Monster.monster_attak-Personnage.perso_shield)+" point de vie.")

    #le joueur perd des point de vie
    Personnage.perso_life = Personnage.perso_life - Monster.monster_attak + Personnage.perso_shield

    #Ce if c'est pour évité les valeur negative si le joueur meurt
    if Personnage.perso_life < 0:
        Personnage.perso_life = 0

    #on indique au joueur ou on en est dans les points de vie
    print(Personnage.perso_name + ":" + str(Personnage.perso_life) + "/" + str(Personnage.perso_life_max) + " point de vie.")
    print(Monster.monster_name+": "+str(Monster.monster_life)+"/"+str(Monster.monster_life_max)+" point de vie\n\n")

    #à cette partie seul le joueur perd des point de vie donc si il est 0 on sort de la boucle
    if Personnage.perso_life <= 0:
        break

    #le joueur peux effectuer 2 actions, se soigner ou attaquer
    print("à vous de jouer!")
    action = input("Que voulez vous faire?\n- 1 pour attaquer\n- 2 pour se soigner\n")

    #Le joueur attaque le calcule est calculer (dégat=attaque-defense)
    if action == "1":
        print("Vous attaquez le "+Monster.monster_name+". Vous infligez "+str(Personnage.perso_attak-Monster.monster_shield)+" dégats")
        Monster.monster_life = Monster.monster_life - Personnage.perso_attak + Monster.monster_shield

   #Le joueur se soigne en utilisant sa variable d'attaque(à modifié plus tard)
    elif action == "2":
        print("Vous vous soignez de "+str(Personnage.perso_attak)+" point de vie")
        Personnage.perso_life = Personnage.perso_life + Personnage.perso_attak

        #si les point de vie du personnage ne peuvent pas depasser les point de vie max
        if Personnage.perso_life > Personnage.perso_life_max:
            Personnage.perso_life = Personnage.perso_life_max

   #Si le joueur ecris autre chose que "1" ou "2" il passe son tour
    else:
        print("En voulant faire quelque chose vous tombez par terre ! Vous ne pouvez rien faire !")

    #Ce if c'est juste pour evitez une valeur negative quand on affiche les point de vie apres
    if Personnage.perso_life < 0:
        Personnage.perso_life = 0
    if Monster.monster_life < 0:
        Monster.monster_life = 0
    #On indique au joueur ou en sont les point de vie
    print(Personnage.perso_name+": "+str(Personnage.perso_life)+"/"+str(Personnage.perso_life_max)+" pdv")
    print(Monster.monster_name+": "+str(Monster.monster_life)+"/"+str(Monster.monster_life_max)+" pdv\n\n")

#Si le joueur atteint 0 pdv il a perdu
if Personnage.perso_life <= 0:
    print("NOOOON!!! Vous etes mort -_-\"")

#Si le monstre atteint 0 pdv le joueur gagne
if Monster.monster_life <= 0:
    print("Oue oue oue vous avez gagnez sur un coup de chance !")