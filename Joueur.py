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

class Joueur:
    '''Classe mére de l'objet joueur'''
    def __init__(self,nom,role):
        self_name = nom
        self_class = role
        self_etat = "Normal"
        self_pv=100
        self_pm=100
        self_end=100
        self_atk_phy=100
        self_atk_mag=100
        self_def_phy=100
        self_def_mag=100
        self_vit=100
        self_pre=100
        self_esquive=100
        self_crit=0
        self_exp = 0
        self_lvl = 1
        self_order = 1

        def _get_nom(self):
            return self._nom

        def _set_nom(self,nom):
            self._nom = nom


class Archer(Joueur):
    ''' Classe héritée de Joueur
	Initialise les stats spécifique au role Mage Noir
	'''
    def __init__(self,nom,role="Archer"):
        Joueur.__init__(self, nom,role)
        self_pv= 100
        self_pm= 50
        self_end= 100
        self_atk_phy= 150
        self_atk_mag= 80
        self_def_phy= 80
        self_def_mag= 75
        self_vit= 120
        self_pre= 145
        self_esquive= 100
        self_crit= 0.20