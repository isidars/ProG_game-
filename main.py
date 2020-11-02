from Fonction import *
from Joueur import *
joueur = Joueur()
nom =""

print("Bonjour, jeune homme. Tu viens d'arrivé ?")
nom = choix_nom()
verification_nom = verif_nom(nom)

while verification_nom == "Non" or verification_nom == "non":
    nom = choix_nom()
    verif_nom = verif_nom(nom)


print("D'accord, et quel type de combattant est-tu étranger ?")
choix_role = input("""1. Tank;
2. Archer;
3. Guerrier;
4. Mage Blanc;
5. Mage Noir;
6. Assassin; \n""")

if choix_role==1:
    joueur = Joueur(name=nom)
elif choix_role==2:
    joueur = Archer(name=nom)
elif choix_role==3:
    joueur = Joueur(name=nom)
elif choix_role==4:
    joueur = Joueur(name=nom)
elif choix_role==5:
    joueur = Joueur(name=nom)
elif choix_role==6:
    joueur = Joueur(name=nom)


print()

