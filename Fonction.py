def choix_nom():
    print("Comment t'appel-tu donc ? ")
    nom = input()
    return nom


def verif_nom(nom):
    print("Alors comme ça tu t'appel " + nom + "?\n")
    verification_nom = str(input())
    return verification_nom
