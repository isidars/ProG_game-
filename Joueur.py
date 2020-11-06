import random

class Joueur:
    '''Classe mére de l'objet joueur'''
    def __init__(self, name, role):
        self.name = name
        self.classe = role
        self.etat = "Normal"
        self.mpv=100
        self.pv= self.mpv
        self.mpm=100
        self.pm= self.mpm
        self.mendurance=100
        self.endurance=self.mendurance
        self.attaque_physique=100
        self.attaque_magique=100
        self.defense_physique=100
        self.defense_magique=100
        self.vitesse=100
        self.precision=100
        self.esquive=100
        self.critique=0
        self.exp = 0
        self.lvl = 1


class Archer(Joueur):
    ''' Classe héritée de Joueur
	Initialise les stats spécifique au role Archer '''
    def __init__(self, name, role="Archer"):
        Joueur.__init__(self, name, role)
        self.mpm= 50
        self.attaque_physique= 150
        self.attaque_magique= 80
        self.defense_physique= 80
        self.defense_magique= 75
        self.vitesse= 120
        self.precision= 145
        self.esquive= 100
        self.critique= 0.20


class MageNoir(Joueur):
    def __init__(self, name, role="Mage Noir"):
        Joueur.__init__(self, name, role)
        self.pm= 120
        self.endurance= 80
        self.attaque= 80
        self.attaque_magique= 120
        self.defense= 80
        self.defense_magique= 120