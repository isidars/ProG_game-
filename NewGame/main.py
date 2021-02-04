from players import *

print("""Salut étranger, tu nous rejoins toi aussi pour la gloire et l'argent je suppose..
Ce n'est pas bien grave, nous avons besoin de main d'oeuvre de toute manière,
Je te fait le topo, alors nous sommes attaqués par qulques sale bête mais personne n'est au village..
Aide nous et tu sera récompensé !

Tout d'abord, comment t'appel-tu ?
""")
pseudo = []
pseudo_c = input("Pseudo : ")
pseudo.append(pseudo_c)

print("Et bien enchanté", pseudo[0], "!\nQuel sorte de combattant souhaiterais-tu être ? Attention, tu ne pourra pas en changer une fois t'y être engagé.")
print("""Alors il y a différentes sortes, voici : 
1. Guerrier
2. Archer
3. Mage noir
4. Mage blanc
5. Assassin
6. Tank""")

rep = 0
while rep > 6 or rep < 1:
    try:
        rep = int(input(">> "))
    except:
        print("Veuillez entré une spécialité valide..")
#-----------------------CHOIX CLASSE---------------------------
"""if rep == 1:
    pseudo[0] = Guerrier(pseudo[0])"""
if rep == 2:
    j1 = Archer(pseudo[0])
"""elif rep == 3:
    pseudo[0] = MageN(pseudo[0])
elif rep == 4:
    pseudo[0] = MageB(pseudo[0])
elif rep == 5:
    pseudo[0] = Assassin(pseudo[0])
elif rep == 6:
    pseudo[0] = Tank(pseudo[0])"""
#--------------------FIRST COMBAT--------------------------------


#print("Il y a 3 monstres qui attaquent le village !! Aide nous!")
mob = Mob('gob')
mob2 = Mob('gob')
mob3 = Mob('troll')
mob.Reinit()
mob2.Reinit()
mob3.Reinit()
j1.Reinit()
list = (j1, mob, mob2, mob3)

j1.Combattre(list)
#print("{} attaque {}, il lui reste {}pv".format(pseudo[0].name, mob.name, pseudo[0].Attaquer(mob)))
