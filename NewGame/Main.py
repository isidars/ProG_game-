# Fichier contenant le code principal du jeu
# On importe les class Monster et Personnage
from NewGame.Monster import *
from NewGame.Personnage import *
#On définit le nom du joueur
print("Enchanté "+Personnage.perso_name+", ravie de te connaitre!\nCe n'est pas l'heure des présentation défend toi !")

#Le joueur est attaqué par 1er monstre
print("Vous êtes attaqué par un monstre, c'est un "+Monster.monster_name+"!\nIl a "+str(Monster.monster_life)+" point de vie.\nBonne chance !\n")

#tant que le joueur ou le monstre on de la vie le combat continue
while Monster.monster_life > 0 and Personnage.perso_life > 0:
    #le monstre attaque en 1er
    print("Le "+Monster.monster_name+" vous attaque !\nVous perdez "+str(Monster.monster_attak-Personnage.perso_shield)+" point de vie.")
    #le joueur perd des point de vie
    Personnage.perso_life = Personnage.perso_life - Monster.monster_attak + Personnage.perso_shield
    print(Personnage.perso_name + ":" + str(Personnage.perso_life) + "/" + str(Personnage.perso_life_max) + " point de vie.")
    print(Monster.monster_name+": "+str(Monster.monster_life)+"/"+str(Monster.monster_life_max)+" point de vie\n\n")
    if Personnage.perso_life <= 0:
        break
    #le joueur peux effectuer 2 actions, se soigner ou attaquer
    print("à vous de jouer!")
    action=input("Que voulez vous faire?\n- 1 pour attaquer\n- 2 pour se soigner\n")

    #Le joueur attaque le calcule est calculer (dégat=attaque-defense)
    if action == "1":
        print("Vous attaquez le "+Monster.monster_name+". Vous infligez "+str(Personnage.perso_attak-Monster.monster_shield)+" dégats")
        Monster.monster_life = Monster.monster_life - Personnage.perso_attak + Monster.monster_shield
    elif action == "2":
        print("Vous vous soignez de "+str(Personnage.perso_attak)+" point de vie")
        Personnage.perso_life = Personnage.perso_life + Personnage.perso_attak

        if Personnage.perso_life > Personnage.perso_life_max:
            Personnage.perso_life = Personnage.perso_life_max
    else:
        print("En voulant faire quelque chose vous tombez par terre ! Vous ne pouvez rien faire !")
    print(Personnage.perso_name+": "+str(Personnage.perso_life)+"/"+str(Personnage.perso_life_max)+" pdv")
    print(Monster.monster_name+": "+str(Monster.monster_life)+"/"+str(Monster.monster_life_max)+" pdv\n\n")
if Personnage.perso_life <= 0:
    print("NOOOON!!! Vous etes mort -_-\"")
if Monster.monster_life <= 0:
    print("Oue oue oue vous avez gagnez sur un coup de chance !")