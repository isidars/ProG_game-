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

print("Et bien enchanté", pseudo[0], "!")
pseudo[0] = Archer(pseudo[0])
mob = 'gob'
mob = Mob(mob)
print(pseudo[0].name)
print(pseudo[0].Attaquer(mob))

