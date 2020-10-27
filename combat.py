#déclaration de la fonction combat
choix_action(attaque;magie;objet)
choix_cible(joueur1;joueur2;joueurs;mob)
req_choix_cible
req_choix_action

def choix_action
    {
    si req_choix_action = attaque
        attaque(choix_cible)
    sinon si req_choix_action = magie
        magie(choix_cible)
    sinon
        objet()
    }


def combat:
    {
    tant que x joueur ou mob à de la vie le combat se déroule
            {
            si Vit_joueur < mob = true
                mob attaque(joueur)
                req_choix_action
                req_choix_cible
                choix_action(choix_cible)
            sinon
                req_choix_action
                req_choix_cible
                choix_action(choix_cible)
                mob attaque(joueur)
            }
    fin boucle
    }
