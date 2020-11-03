# -*-coding:utf-8 -*

from assassin import *

player1 = input("Choisissez un nom pour le Player 1 : ")

choix_role1 = True

while choix_role1 :
    
    choix1 = input(""" 
Tank 
Guerrier
Archer
Mage blanc
Mage noir
Assassin

Choisissez un role : """)
    
    try:
        
        if choix1 == "Tank" or choix1 == "tank":
            choix_role1 = False
            print("Tank choisi ")
        elif choix1 == "Guerrier" or choix1 == "guerrier":
            choix_role1 = False
            print("Guerrier choisi ")
        elif choix1 == "Archer" or choix1 == "archer":
            choix_role1 = False
            print("Archer choisi ")
        elif choix1 == "Mage blanc" or choix1 == "mage blanc":
            choix_role1 = False
            print("Mage blanc choisi ")
        elif choix1 == "Mage noir" or choix1 == "mage noir":
            choix_role1 = False
            print("Mage noir choisi ")
        elif choix1 == "Assassin" or choix1 == "assassin":
            choix_role1 = False
            print("Assassin choisi ")
        else:
            print("Erreur, choisissez un role parmis la liste")
    except :
        print("Erreur, choisissez un role parmis la liste")
    
    
print(player1 + " est pret pour le combat " )

player2 = input("Choisissez un nom pour le Player 2 : ")
choix_role2 = True
while choix_role2 :
    
    choix2 = input(""" 
Tank 
Guerrier
Archer
Mage blanc
Mage noir
Assassin

Choisissez un role : """)
    
    try:
        
        if choix2 == "Tank" or choix2 == "tank":
            choix_role2 = False
            print("Tank choisi ")
        elif choix2 == "Guerrier" or choix2 == "guerrier":
            choix_role2 = False
            print("Guerrier choisi ")
        elif choix2 == "Archer" or choix2 == "archer":
            choix_role2 = False
            print("Archer choisi ")
        elif choix2 == "Mage blanc" or choix2 == "mage blanc":
            choix_role2 = False
            print("Mage blanc choisi ")
        elif choix2 == "Mage noir" or choix2 == "mage noir":
            choix_role2 = False
            print("Mage noir choisi ")
        elif choix2 == "Assassin" or choix2 == "assassin":
            choix_role2 = False
            print("Assassin choisi ")
        else:
            print("Erreur, choisissez un role parmis la liste")
    except :
        print("Erreur, choisissez un role parmis la liste")


print(player2 + " est pret pour le combat " )
print(" Debut du combat avec " + player1 + " avec le role " + choix1 )
print(" Debut du combat avec " + player2 + " avec le role " + choix2 )  