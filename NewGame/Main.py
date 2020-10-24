# Fichier contenant le code principal du jeu
# On importe les class Monster
import time
import random
from Monster import Monster

#On définit le nom du joueur
print("Bienvenue nouvel aventurier ! Euh... Comment tu t'appelles enfaite?")
perso_name = input("Nom:")
print("Enchanté "+perso_name+", ravie de te connaitre!\nEt Euh.... tu es quoi au juste?")

#Le joueur défini ça classe entre paladin ou assassin.
perso_class=""

#Si le joueur tape autre chose que "1" ou "2" la boucle recommence L'equipier sera la classe non choisi
#Etant un bot l'equipier sera moins fort que le joueur
while perso_class != "1" or perso_class != "2":
    perso_class = input("Tapez le chiffre qui correspond a votre classe:\n1- Assassin.\n2- Paladin\n")
    if perso_class == "1":      #Si le joueur tape 1 il joue un assassin
        from Personnage import Assassin, Paladin
        print("Ah oui je vois tu es donc un "+ Assassin.perso_class+". Faut dire vu ton accoutrement je l'aurais jamais deviné!")
        perso_life=Assassin.perso_life
        perso_life_max=Assassin.perso_life_max
        perso_attak=Assassin.perso_attak
        perso_shield=Assassin.perso_shield

        equipier_classe=Paladin.perso_classe
        equipier_life = Paladin.perso_life
        equipier_life_max = Paladin.perso_life_max
        equipier_attak = Paladin.perso_attak-3
        equipier_shield = Paladin.perso_shield-3

        break
    elif perso_class == "2":
        from NewGame.Personnage import Paladin, Assassin
        print("Ah oui je vois tu es donc un "+ Paladin.perso_classe+". Faut dire vu ton accoutrement je l'aurais jamais deviné!")
        perso_life=Paladin.perso_life
        perso_life_max=Paladin.perso_life_max
        perso_attak=Paladin.perso_attak
        perso_shield=Paladin.perso_shield

        equipier_classe= Assassin.perso_class
        equipier_life = Assassin.perso_life
        equipier_life_max = Assassin.perso_life_max
        equipier_attak = Assassin.perso_attak-3
        equipier_shield = Assassin.perso_shield-3
        break
    else:
        print("J'ai pas compris tu es quoi ?")
#On défini le nom du coéquipier
print("Je vois que tu as un ami avec toi, Comment s'appelle t'il?")
equipier_name=input("Equipier: ")
print("Bienvenue à toi "+equipier_name+". Tu es un "+equipier_classe+" c'est ça? Toi au moins ça se voit !")

#Le joueur est attaqué par un 1er monstre
print("Eeh c'est quoi ce gros oiseaux qui vole vers nous? ")
time.sleep(1)
print("UN "+Monster.monster_name.upper()+"!!!! FUYEZ!!!!")
time.sleep(1)
print("Vous êtes attaqué par un monstre, c'est un "+Monster.monster_name+"!\nIl a "+str(Monster.monster_life)+" point de vie.\nBonne chance !\n")
time.sleep(1)
#tant que le joueur ou le monstre on de la vie le combat continue
rejouer = "1"
while rejouer != "2":
    while Monster.monster_life > 0 and perso_life > 0:
        #le monstre attaque en 1er
        print("Le "+Monster.monster_name+" vous attaque ! Vous perdez "+str(Monster.monster_attak-perso_shield)+" point de vie.")

        #le joueur perd des point de vie
        perso_life = perso_life - Monster.monster_attak + perso_shield

        #Ce if c'est pour évité les valeur negative si le joueur meurt
        if perso_life < 0:
            perso_life = 0

        #on indique au joueur ou on en est dans les points de vie
        print("{0}:{1}/{2} point de vie.".format(perso_name, str(perso_life), str(perso_life_max)))
        print(Monster.monster_name+": "+str(Monster.monster_life)+"/"+str(Monster.monster_life_max)+" point de vie\n\n")

        #à cette partie seul le joueur perd des point de vie donc si il est 0 on sort de la boucle
        if perso_life <= 0:
            break

        #le joueur peux effectuer 2 actions, se soigner ou attaquer
        print("à vous de jouer!")
        action = input("Que voulez vous faire?\n- 1 pour attaquer\n- 2 pour se soigner\n")

        #Le joueur attaque le calcule est calculer (dégat=attaque-defense)
        if action == "1":
            print("Vous attaquez le "+Monster.monster_name+". Vous infligez "+str(perso_attak-Monster.monster_shield)+" dégats")
            Monster.monster_life = Monster.monster_life - perso_attak + Monster.monster_shield

       #Le joueur se soigne en utilisant sa variable d'attaque(à modifié plus tard)
        elif action == "2":
            print("Vous vous soignez de "+str(perso_attak-5)+" point de vie")
            perso_life = perso_life + perso_attak

            #si les point de vie du personnage ne peuvent pas depasser les point de vie max
            if perso_life > perso_life_max:
                perso_life = perso_life_max

       #Si le joueur ecris autre chose que "1" ou "2" il passe son tour
        else:
            print("En voulant faire quelque chose vous tombez par terre ! Vous ne pouvez rien faire !")

        #à l'équipier d'attaquer le bot a 2 choix attaquer le monstre ou soigné le joueur
        equipier_rand=random.choice(["1","2"])

        if equipier_rand == "1":
            print(equipier_name+" attaque le "+Monster.monster_name+"."+equipier_name+" inflige "+str((equipier_attak-Monster.monster_shield))+" dégats")
            Monster.monster_life=Monster.monster_life-(equipier_attak-Monster.monster_shield)
        if equipier_rand == "2":
            print(equipier_name+" vous force a boire une boisson revigourante.")
            print(perso_name+" est soigné de "+ str(equipier_attak-5))
            perso_life=perso_life+(equipier_attak-5)

        #Ce if c'est juste pour evitez une valeur negative quand on affiche les point de vie apres
        if perso_life < 0:
            perso_life = 0
        if Monster.monster_life < 0:
            Monster.monster_life = 0
        #On indique au joueur ou en sont les point de vie
        print(perso_name+": "+str(perso_life)+"/"+str(perso_life_max)+" pdv")
        print(Monster.monster_name+": "+str(Monster.monster_life)+"/"+str(Monster.monster_life_max)+" pdv\n\n")
    rejouer="2"
    #Si le joueur atteint 0 pdv il a perdu
    if perso_life <= 0:
        print("NOOOON!!! Vous etes mort -_-\". Voulez vous recommencer?")
        again=""
        while again != "oui" and again!= "non":
            again = input("oui/non?")
            if again == "non":
                print("Au revoir! Merci d'avoir joué!")
                rejouer = "2"
            elif again == "oui":
                rejouer = "1"
                Monster.monster_life = Monster.monster_life_max
                perso_life = perso_life_max
            else:
                print("J'ai pas compris. oui ou non?")



#Si le monstre atteint 0 pdv le joueur gagne
if Monster.monster_life <= 0:
    print("Oue oue oue vous avez gagnez sur un coup de chance !")