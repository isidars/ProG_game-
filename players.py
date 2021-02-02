

class Joueur:
    '''Classe mére de l'objet joueur
    initialisation du constructeur de la classe'''
    def __init__(self, name, role):
        self.name = name
        self.classe = role
        self.etat = "Normal"
        self.mpv = 100
        self.pv = self.mpv
        self.mpm = 100
        self.pm = self.mpm
        self.mend = 100
        self.end = self.mend
        self.attaque_phy = 100
        self.defense_phy = 100
        self.vitesse = 100
        self.exp = 0
        self.lvl = 1

    def Attaquer(self, cible):
        return self.attaque_phy-cible.defense_phy/2

class Archer(Joueur):
    def __init__(self, name, role='Archer'):
        self.name = name
        self.mpv = 150
        self.mpm = 50
        self.mend = 200
        self.attaque_phy = 150

class Mob(Joueur):
    def __init__(self, name):
        self.defense_phy = 100
        self.vitesse = 100
        self.exp = 0
        self.lvl = 1
        if name == 'gob':
            self.name = 'gob'
            self.mpv = 120
            self.attaque_phy = 90
            self.mend = 150