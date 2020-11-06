from Fonction import *
from Joueur import *
from Monstre import *
mob =""
nom =""
choix_role =10
joueur = Joueur(name=nom, role=choix_role)


print("Bonjour, jeune homme. Tu viens d'arrivé ?")
nom = choix_nom()
verification_nom = verif_nom(nom)

while verification_nom.lower() == "non":
    nom = choix_nom()
    verif_nom = verif_nom(nom)


print("D'accord, et quel type de combattant est-tu étranger ?")
print("""
1. Tank;
2. Archer;
3. Guerrier;
4. Mage Blanc;
5. Mage Noir;
6. Assassin;
""")

while choix_role > 6:
    try:
        choix_role = int(input())
    except ValueError:
        print("Vous n'avez pas entrée le bonne indice de rôle")


if choix_role == 1:
    joueur = Tank(nom)
elif choix_role == 2:
    joueur = Archer(nom)
elif choix_role == 3:
    joueur = Guerrier(nom)
elif choix_role == 4:
    joueur = MageBlanc(nom)
elif choix_role == 5:
    joueur = MageNoir(nom)
elif choix_role == 6:
    joueur = Assassin(nom)


print("Tu est donc '" + joueur.classe + "'. Tu rencontre un mob attention ! Ils sont très dangereux")
mob = Troll()

combat(joueur, mob)


