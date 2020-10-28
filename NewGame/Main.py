# Fichier contenant le code principal du jeu
# On importe les class Monster
import time
import random
from Equipements import *
from competences import *
from Monsters import * 
from Personnages import *
from Sorts import *
#On définit le nom du joueur

joueur1_name = input("Nom du joueur 1 : ")
joueur2_name = input("Nom du joueur 2 : ")

#Le joueur défini ça classe entre les 6 proposés

#Si le joueur tape autre chose que "1" ou "2" la boucle recommence L'equipier sera la classe non choisi
#Etant un bot l'equipier sera moins fort que le joueur
while True:
    perso_class = input("Tapez le chiffre qui correspond a votre classe:\n1- Normal.\n2- Mage Blan.c\n")
    if perso_class == "1":      #Si le joueur tape 1 il joue un assassin
        print("tu es donc un "+ Normal.nom+" !")
        joueur1_pv = Normal.pv
        joueur1_pm = Normal.pm
        joueur1_endurance = Normal.endurance
        joueur1_attaque  = Normal.attaque
        joueur1_attaque_magique = Normal.attaque_magique
        joueur1_defense  = Normal.defense
        joueur1_defense_magique = Normal.defense_magique
        joueur1_vitesse = Normal.vitesse
        joueur1_precision = Normal.precision
        joueur1_esquive = Normal.esquive

        joueur2_pv = MageBlanc.pv
        joueur2_pm = MageBlanc.pm
        joueur2_endurance = MageBlanc.endurance
        joueur2_attaque = MageBlanc.attaque
        joueur2_attaque_magique = MageBlanc.attaque_magique
        joueur2_defense = MageBlanc.defense
        joueur2_defense_magique = MageBlanc.defense_magique
        joueur2_vitesse = MageBlanc.vitesse
        joueur2_precision = MageBlanc.precision
        joueur2_esquive = MageBlanc.esquive

        break
    elif perso_class == "2":
        print("tu es donc un "+ MageBlanc.nom+" !")
        joueur1_pv = MageBlanc.pv
        joueur1_pm = MageBlanc.pm
        joueur1_endurance = MageBlanc.endurance
        joueur1_attaque = MageBlanc.attaque
        joueur1_attaque_magique = MageBlanc.attaque_magique
        joueur1_defense = MageBlanc.defense
        joueur1_defense_magique = MageBlanc.defense_magique
        joueur1_vitesse = MageBlanc.vitesse
        joueur1_precision = MageBlanc.precision
        joueur1_esquive = MageBlanc.esquive

        joueur2_pv = Normal.pv
        joueur2_pm = Normal.pm
        joueur2_endurance = Normal.endurance
        joueur2_attaque  = Normal.attaque
        joueur2_attaque_magique = Normal.attaque_magique
        joueur2_defense  = Normal.defense
        joueur2_defense_magique = Normal.defense_magique
        joueur2_vitesse = Normal.vitesse
        joueur2_precision = Normal.precision
        joueur2_esquive = Normal.esquive
        break
    else:
        print("J'ai pas compris tu es quoi ?")


#print("Je vois que tu as un ami avec toi, Comment s'appelle t'il?")
#equipier_name=input("Equipier: ")
#print("Bienvenue à toi "+equipier_name+". Tu es un "+equipier_classe+" c'est ça? Toi au moins ça se voit !")

#Le joueur est attaqué par un 1er monstre
print("Eeh c'est quoi ce gros oiseaux qui vole vers nous? ")
time.sleep(1)
print("UN "+Monsters.name.upper()+"!!!! FUYEZ!!!!")
time.sleep(1)
print("Attrape ça ce sont des herbes médicinal! elle pourrait te servir si tu viens à être en mauvaise position")
time.sleep(1)
print("vous recever une bourse contenant 5 herbes médicinal et 10 piece d'or, ces plantes vous soigne de 20 point de vie")
print("Vous êtes attaqué par un monstre, c'est un "+Monsters.name+"!\nIl a "+str(Monsters.pv)+" point de vie.\nBonne chance !\n")
time.sleep(1)
#tant que le joueur ou le monstre on de la vie le combat continue
rejouer = "1"
while rejouer != "2":
    medicinal_plante = 5
    while Monsters.nom > 0 and joueur1_pv > 0 and joueur_2 > 0:
        #le monstre à 2 choix attaque physique ou magique
        monster_choice=random.choice(["physique","magique"])
        if monster_choice == "physique":
            print(Monsters.nom+" vous lance une attaque physique!")
            #On définie le taux d'esquive du joueur
            chance_esquive =int( 50 * (joueur1_esquive/Monsters.vitesse))
            if chance_esquive < 10:
                chance_esquive = 10
            elif chance_esquive > 75:
                chance_esquive = 75

            #maintenant que nous avons notre % de chance d'esquive on définie si l'attaque reussi
            test_attack=random.randint(1,100)
            # Le joueur à de la chance il esquive le coup
            if test_attack < chance_esquive:
                print(joueur1_name+" esquive l'attaque ! Il ne subit aucun dommage !")
            # le joueur a pas de chance il prend des degats mais reduit grace a sa défense
            else:
                print(Monsters.name+" Vous à touché vous subissez "+ str(Monsters.attaque-joueur1_defense)+" point de dégats")
                joueur1_pv = joueur1_pv - (Monsters.attaque- joueur1_defense)
       #Le monstre choisi l'attaque magique
        elif monster_choice == "magique" and count_spell_monster >= 3:
            print("Le "+Monsters.name+" crache du feu !!")
            count_spell_monster = 0
            chance_esquive =int(50*(joueur1_esquive/Monsters.vitesse)*0.8)
            if chance_esquive < 10:
                chance_esquive = 10
            elif chance_esquive > 75:
                chance_esquive = 75
            # maintenant que nous avons notre % de chance d'esquive on définie si l'attaque reussi
            test_attack = random.randint(1, 100)
            # Le joueur à de la chance il esquive le coup
            if test_attack < chance_esquive:
                print(joueur1_name + " esquive l'attaque ! Il ne subit aucun dommage !")
            # le joueur a pas de chance il prend des degats mais reduit grace a sa défense
            else:
                print(Monsters.name + " Vous à touché vous subissez " + str(
                            Monsters.attaque_magique - joueur1_defense_magique) + " point de dégats")
                joueur1_pv = joueur1_pv - (Monsters.attaque_magique - joueur1_defense_magique)



        #Ce if c'est pour évité les valeur negative si le joueur meurt
        if joueur1_pv < 0:
            joueur1_pv = 0

        #on indique au joueur ou on en est dans les points de vie
        print("{0}:{1}/{2} point de vie.".format(joueur1_name, str(joueur1_pv), str(joueur1_pv_max)))
        print(Monsters.name + ":"+ str(Monsters.pv) +"/" + str(Monsters.pv_max))

        #à cette partie seul le joueur perd des point de vie donc si il est 0 on sort de la boucle
        if joueur1_pv <= 0:
            break


        #le joueur peux effectuer 3 actions, se soigner ou attaquer
        print("à vous de jouer!")
        action = input("Que voulez vous faire?\n- 1 pour attaquer\n- 2 pour lancer un sort\n- 3 pour utiliser un objet\n")

        #Le joueur attaque le calcule est calculer (dégat=attaque-defense)
        if action == "1":
            print("Vous lancer votre attaque!")
            #on calcule le pourcentage de chance que le monstre esquive
            chance_esquive = int(50*(Monsters.esquive/joueur1_vitesse))
            if chance_esquive > 50:
                chance_esquive = 50
            test_attack=random.randint(1,100)
            if test_attack < chance_esquive:
                print("Ho non le monstre à esquivé!")
            else:
                print("Vous infligez "+str(joueur1_attaque-Monsters.defense)+" dégats")
                Monsters.pv = Monsters.pv - (joueur1_attaque - Monsters.defense)

       #Le joueur dispose de plusieur en fonction de son niveau
        elif action == "2":
            print("Quels sort voulez vous utilisé?\n-1 Eclair    - 3\n-2           - 4")
            spell_choice=input()
            if spell_choice == "1":
                print("Vous lancer un eclair!")
            else:
                print("vous ne pouvez lancer que l'eclair alors vous decider de faire un eclair quand meme")
            chance_esquive = int(50 * (Monsters.esquive / joueur1_vitesse)*0.5)
            if chance_esquive > 50:
                chance_esquive = 50
            test_attack = random.randint(1, 100)
            if test_attack < chance_esquive:
                print("Ho non le monstre à esquivé!")
            else:
                print("Vous infligez " + str(joueur1_attaque_magique - Monsters.defense_magique) + " dégats")
                Monsters.pv = Monsters.pv - (
                            joueur1_attaque_magique - Monsters.defense_magique)
        #Le joueur peut utilisé des objets
        elif action == "3":
            if medicinal_plante > 0:
                print("Vous utilisé une plante médicinal vous gagné 20 point de vie")
                joueur1_pv = joueur1_pv + 20
                medicinal_plante = medicinal_plante - 1
                print("il vous reste "+str(medicinal_plante)+" plante(s) médicinal")
            else:
                print("vous n'avez plus de plante médicinal vous perdez votre tour a chercher l'inexistant ...")
            #si les point de vie du personnage ne peuvent pas depasser les point de vie max
            if joueur1_pv > joueur1_pv_max:
                joueur1_pv = joueur1_pv_max


       #Si le joueur tape autre chose que "1" "2" ou "3" il passe son tour
        else:
            print("En voulant faire quelque chose vous tombez par terre ! Vous ne pouvez rien faire !")

        #Ce if c'est juste pour evitez une valeur negative quand on affiche les point de vie apres
        if joueur1_pv < 0:
            joueur1_pv = 0
        if Monsters.pv < 0:
            Monsters.pv = 0
        #On indique au joueur ou en sont les point de vie
        print(joueur1_name+": "+str(joueur1_pv)+"/"+str(joueur1_pv_max)+" pdv")
        print(Monsters.name+": "+str(Monsters.pv)+"/"+str(Monsters.pv_max)+" pdv\n\n")
    rejouer="2"

    #Si le joueur atteint 0 pdv il a perdu
    if joueur1_pv <= 0:
        print("NOOOON!!! Vous etes mort -_-\". Voulez vous recommencer?")
        again=""
        while again != "oui" and again!= "non":
            again = input("oui/non?")
            if again == "non":
                print("Au revoir! Merci d'avoir joué!")
                rejouer = "2"
            elif again == "oui":
                rejouer = "1"
                Monsters.pv = Monsters.pv_max
                joueur1_pv = joueur1_pv_max
                print("Aller c'est repartie")
            else:
                print("J'ai pas compris. oui ou non?")

#Si le monstre atteint 0 pdv le joueur gagne
if Monsters.pv <= 0:
    piece_dor_win=random.randint(50,1000)
    piece_dor=piece_dor + piece_dor_win
    print("Felicitation vous gagné "+str(piece_dor_win)+" piece d'or.")
    print("Vous avez "+str(piece_dor)+".")