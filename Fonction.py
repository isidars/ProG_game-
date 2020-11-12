import random
def choix_nom():
    print("Comment t'appel-tu donc ? ")
    nom = input()
    return nom


def verif_nom(nom):
    print("Alors comme ça tu t'appel " + nom + "?\n")
    verification_nom = str(input("Oui/Non?"))
    return verification_nom

def attaque(lanceur, cible):
    d1 = (cible.mpv / 20 / 100) * (lanceur.attaque_physique / 4 - cible.defense_physique / 6)

    if (cible.defense_physique / 2) > lanceur.attaque_physique:
        if d1 <= 0:
            d1 = 25 / 100
        d2 = random.randrange(1, 10, 1) * d1

    if d1 <= 0:
        d1 = 20 / 100
    d2 = (lanceur.attaque_physique/6 - cible.defense_physique/8) + random.randrange(1, 6, 1)

    if d2 <= 0:
        d2 = random.randrange(1, 6, 1)

    d = d1 * d2
    return d

def action(x, jou_obj, j_cible):
    if int(x) == 1:
        print("vous allez attaquer")
    elif int(x) == 2:
        choix_objet(jou_obj, j_cible)
    elif int(x) == 3:
        print("Louperr")
    elif int(x) ==0:
        print("Vous devez choisir l'indice correspondant aux actions dans les propositions")
    else:
        print("Vous devez choisir l'indice correspondant aux actions dans les propositions")


def combat(p1, p2):
    #Définition ordre de combat
    prio_tour = [p1, p2]
    tour = 0
    p1_pv = p1.mpv
    p2_pv = p2.mpv
    if p1.vitesse < p2.vitesse:
        prio_tour = [p2, p1]
    while p1_pv > 1 and p2_pv > 1:
        tour += 1

        if prio_tour[0] == p1:
            try:
                x = int(input("Quel action voulez-vous choisir ?\n1.Attaque.\n2.Objet\n3.Fuite\n:"))
            except:
                print("Vous devez choisir une action.\n:")

            action(x, p1, p2)
            if x == 1:
                p2_pv -= attaque(p1, p2)
                print("Vous avez infligé {} dégats".format(round(attaque(p1, p2), 2)))

        if p2_pv > 0:
            p1_pv -= attaque(p2, p1)
            print("Vous avez reçu {} dégats".format(round(attaque(p2, p1), 2)))

        print("Pour le tour {0} il vous reste {1}pv, et il reste {2}pv au monstre".format(tour, round(p1_pv, 2), round(p2_pv, 2)))