import random

class Joueur:
    '''Classe mére de l'objet joueur'''
    def __init__(self,name,role):
        self.name = name
        self.classe = role
        self.etat = "Normal"
        self.pv=100
        self.pm=100
        self.end=100
        self.atk_phy=100
        self.atk_mag=100
        self.def_phy=100
        self.def_mag=100
        self.vit=100
        self.pre=100
        self.esquive=100
        self.crit=0
        self.exp = 0
        self.lvl = 1
        self.order = 1

        def _get_name(self):
            return self._name

        def _set_name(self,name):
            self._name = name


class Archer(Joueur):
    ''' Classe héritée de Joueur
	Initialise les stats spécifique au role Archer '''
    def __init__(self,name,role="Archer"):
        Joueur.__init__(self, name, role)
        self.pv= 100
        self.pm= 50
        self.end= 100
        self.atk_phy= 150
        self.atk_mag= 80
        self.def_phy= 80
        self.def_mag= 75
        self.vit= 120
        self.pre= 145
        self.esquive= 100
        self.crit= 0.20