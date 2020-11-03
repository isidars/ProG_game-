def choix_nom():
    print("Comment t'appel-tu donc ? ")
    nom = input()
    return nom


def verif_nom(nom):
    print("Alors comme ça tu t'appel " + nom + "?\n")
    verification_nom = str(input())
    return verification_nom

def combat(p1, p2):
    #Définition ordre de combat
if p1.vit > p2.vit:
    x = p1
    y = p2
else:
    x = p2
    y = p1


