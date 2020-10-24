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
        from Personnage import Assassin #, Paladin
        print("Ah oui je vois tu es donc un "+ Assassin.perso_class+". Faut dire vu ton accoutrement je l'aurais jamais deviné!")
        perso_life            = Assassin.perso_life
        perso_life_max        = Assassin.perso_life_max
        perso_physical_attack = Assassin.perso_physical_attack
        perso_magical_attack  = Assassin.perso_magical_attack
        perso_physical_shield = Assassin.perso_physical_shield
        perso_magical_shield  = Assassin.perso_magical_shield
        perso_speed           = Assassin.perso_speed
        perso_dodge           = Assassin.perso_dodge

      #  equipier_classe=Paladin.perso_classe
      #  equipier_life = Paladin.perso_life
      #  equipier_life_max = Paladin.perso_life_max
      #  equipier_attak = Paladin.perso_attak-3
      #  equipier_shield = Paladin.perso_shield-3

        break
    elif perso_class == "2":
        from NewGame.Personnage import Paladin#, Assassin
        print("Ah oui je vois tu es donc un "+ Paladin.perso_classe+". Faut dire vu ton accoutrement je l'aurais jamais deviné!")
        perso_life            = Paladin.perso_life
        perso_life_max        = Paladin.perso_life_max
        perso_physical_attack = Paladin.perso_magical_attack
        perso_magical_attack  = Paladin.perso_magical_attack
        perso_physical_shield = Paladin.perso_physical_shield
        perso_magical_shield  = Paladin.perso_magical_shield
        perso_speed           = Paladin.perso_speed
        perso_dodge           = Paladin.perso_dodge

        #equipier_classe= Assassin.perso_class
        #equipier_life = Assassin.perso_life
        #equipier_life_max = Assassin.perso_life_max
        #equipier_attak = Assassin.perso_attak-3
        #equipier_shield = Assassin.perso_shield-3
        break
    else:
        print("J'ai pas compris tu es quoi ?")
#On défini le nom du coéquipier
#print("Je vois que tu as un ami avec toi, Comment s'appelle t'il?")
#equipier_name=input("Equipier: ")
#print("Bienvenue à toi "+equipier_name+". Tu es un "+equipier_classe+" c'est ça? Toi au moins ça se voit !")

#Le joueur est attaqué par un 1er monstre
print("Eeh c'est quoi ce gros oiseaux qui vole vers nous? ")
time.sleep(1)
print("UN "+Monster.monster_name.upper()+"!!!! FUYEZ!!!!")
time.sleep(1)
print("Attrape ça ce sont des herbes médicinal! elle pourrait te servir si tu viens à être en mauvaise position")
time.sleep(1)
print("vous recever une bourse contenant 5 herbes médicinal et 10 piece d'or, ces plantes vous soigne de 20 point de vie")
print("Vous êtes attaqué par un monstre, c'est un "+Monster.monster_name+"!\nIl a "+str(Monster.monster_life)+" point de vie.\nBonne chance !\n")
time.sleep(1)
#tant que le joueur ou le monstre on de la vie le combat continue
rejouer = "1"
while rejouer != "2":
    count_spell_monster = 2
    piece_dor = 10
    medicinal_plante = 5
    while Monster.monster_life > 0 and perso_life > 0:
        #le monstre à 2 choix attaque physique ou magique
        count_spell_monster= count_spell_monster + 1
        monster_choice=random.choice(["physique","magique"])
        if monster_choice == "physique":
            print(Monster.monster_name+" vous lance une attaque physique!")

            #On définie le taux d'esquive du joueur
            perso_luck_dodge =int( 50 * (perso_dodge/Monster.monster_speed))
            if perso_luck_dodge < 10:
                perso_luck_dodge = 10
            elif perso_luck_dodge > 75:
                perso_luck_dodge = 75

            #maintenant que nous avons notre % de chance d'esquive on définie si l'attaque reussi
            test_attack=random.randint(1,100)
            # Le joueur à de la chance il esquive le coup
            if test_attack < perso_luck_dodge:
                print(perso_name+" esquive l'attaque ! Il ne subit aucun dommage !")
            # le joueur a pas de chance il prend des degats mais reduit grace a sa défense
            else:
                print(Monster.monster_name+" Vous à touché vous subissez "+ str(Monster.monster_physical_attack-perso_physical_shield)+" point de dégats")
                perso_life = perso_life - (Monster.monster_physical_attack - perso_physical_shield)
       #Le monstre choisi l'attaque magique
        elif monster_choice == "magique" and count_spell_monster >= 3:
            print("Le "+Monster.monster_name+" crache du feu !!")
            count_spell_monster = 0
            perso_luck_dodge =int(50*(perso_dodge/Monster.monster_speed)*0.8)
            if perso_luck_dodge < 10:
                perso_luck_dodge = 10
            elif perso_luck_dodge > 75:
                perso_luck_dodge = 75
            # maintenant que nous avons notre % de chance d'esquive on définie si l'attaque reussi
            test_attack = random.randint(1, 100)
            # Le joueur à de la chance il esquive le coup
            if test_attack < perso_luck_dodge:
                print(perso_name + " esquive l'attaque ! Il ne subit aucun dommage !")
            # le joueur a pas de chance il prend des degats mais reduit grace a sa défense
            else:
                print(Monster.monster_name + " Vous à touché vous subissez " + str(
                            Monster.monster_magical_attack - perso_magical_shield) + " point de dégats")
                perso_life = perso_life - (Monster.monster_magical_attack - perso_magical_shield)



        #Ce if c'est pour évité les valeur negative si le joueur meurt
        if perso_life < 0:
            perso_life = 0

        #on indique au joueur ou on en est dans les points de vie
        print("{0}:{1}/{2} point de vie.".format(perso_name, str(perso_life), str(perso_life_max)))
        print(Monster.monster_name + ":"+ str(Monster.monster_life) +"/" + str(Monster.monster_life_max))

        #à cette partie seul le joueur perd des point de vie donc si il est 0 on sort de la boucle
        if perso_life <= 0:
            break


        #le joueur peux effectuer 3 actions, se soigner ou attaquer
        print("à vous de jouer!")
        action = input("Que voulez vous faire?\n- 1 pour attaquer\n- 2 pour lancer un sort\n- 3 pour utiliser un objet\n")

        #Le joueur attaque le calcule est calculer (dégat=attaque-defense)
        if action == "1":
            print("Vous lancer votre attaque!")
            #on calcule le pourcentage de chance que le monstre esquive
            monster_luck_dodge = int(50*(Monster.monster_dodge/perso_speed))
            if monster_luck_dodge > 50:
                monster_luck_dodge = 50
            test_attack=random.randint(1,100)
            if test_attack < monster_luck_dodge:
                print("Ho non le monstre à esquivé!")
            else:
                print("Vous infligez "+str(perso_physical_attack-Monster.monster_physical_shield)+" dégats")
                Monster.monster_life = Monster.monster_life - (perso_physical_attack - Monster.monster_physical_shield)

       #Le joueur dispose de plusieur en fonction de son niveau
        elif action == "2":
            print("Quels sort voulez vous utilisé?\n-1 Eclair    - 3\n-2           - 4")
            spell_choice=input()
            if spell_choice == "1":
                print("Vous lancer un eclair!")
            else:
                print("vous ne pouvez lancer que l'eclair alors vous decider de faire un eclair quand meme")
            monster_luck_dodge = int(50 * (Monster.monster_dodge / perso_speed)*0.5)
            if monster_luck_dodge > 50:
                monster_luck_dodge = 50
            test_attack = random.randint(1, 100)
            if test_attack < monster_luck_dodge:
                print("Ho non le monstre à esquivé!")
            else:
                print("Vous infligez " + str(perso_magical_attack - Monster.monster_magical_shield) + " dégats")
                Monster.monster_life = Monster.monster_life - (
                            perso_magical_attack - Monster.monster_magical_shield)
        #Le joueur peut utilisé des objets
        elif action == "3":
            if medicinal_plante > 0:
                print("Vous utilisé une plante médicinal vous gagné 20 point de vie")
                perso_life = perso_life + 20
                medicinal_plante = medicinal_plante - 1
                print("il vous reste "+str(medicinal_plante)+" plante(s) médicinal")
            else:
                print("vous n'avez plus de plante médicinal vous perdez votre tour a chercher l'inexistant ...")
            #si les point de vie du personnage ne peuvent pas depasser les point de vie max
            if perso_life > perso_life_max:
                perso_life = perso_life_max


       #Si le joueur tape autre chose que "1" "2" ou "3" il passe son tour
        else:
            print("En voulant faire quelque chose vous tombez par terre ! Vous ne pouvez rien faire !")

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
                print("Aller c'est repartie")
            else:
                print("J'ai pas compris. oui ou non?")

#Si le monstre atteint 0 pdv le joueur gagne
if Monster.monster_life <= 0:
    piece_dor_win=random.randint(50,1000)
    piece_dor=piece_dor + piece_dor_win
    print("Felicitation vous gagné "+str(piece_dor_win)+" piece d'or.")
    print("Vous avez "+str(piece_dor)+".")