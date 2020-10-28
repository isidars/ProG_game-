#	Joueur
#		Nom
#		pv
#		pm
#		endurance
#		attaque
#		attaque_magique
#		defense
#		defense_magique
#		vitesse
#		présicion
#		esquive
#		taux_critique
#		état(normal,empoissoné,paralysé,brulé)
#		experience
#		niveau
#		ordre_action
import random


class Archer:
    joueur_class="Archer"
    joueur_pv= 100
    joueur_pm= 50
    joueur_end= 100
    joueur_atk_phy= 150
    joueur_atk_mag= 80
    joueur_def_phy= 80
    joueur_def_mag= 75
    joueur_vit= 120
    joueur_pre= 145
    joueur_esquive= 100
    joueur_crit= 0.20
    joueur_lvl= 1
    joueur_exp= 0