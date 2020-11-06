def choix_nom():
    print("Comment t'appel-tu donc ? ")
    nom = input()
    return nom


def verif_nom(nom):
    print("Alors comme ça tu t'appel " + nom + "?\n")
    verification_nom = str(input("Oui/Non?"))
    return verification_nom

def attaque(lanceur, cible):
    d = (lanceur.mpv / 20) / 100 * (lanceur.attaque_phy/2 - cible.defense/3)
    print(d)


def choix_objet(nom_obj, joueur_cible):


def combat(p1, p2):
    #Définition ordre de combat
    prio_tour = [p1, p2]
    if p1.vitesse < p2.vitesse:
        prio_tour = [p2, p1]
    while p1.pv >= 0 or p2.pv >= 0:
        tour = 0
        def choix_action(x, jou_obj, j_cible):
            if x == 1:
                attaque(jou_obj, j_cible)
            elif x == 2:
                choix_objet(jou_obj, j_cible)
            elif x == 3:

            else:
                "Vous devez choisir une l'indice correspondant aux actions dans les propositions"
        tour += 1


