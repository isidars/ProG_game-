

class Joueur:
    '''Classe mére de l'objet joueur
    initialisation du constructeur de la classe'''
    def __init__(self, name, role):
        self.name = name
        self.classe = role
        self.etat = "Normal"
        self.mpv = 100
        self.pv= self.mpv
        self.mpm = 100
        self.pm= self.mpm
        self.mendurance = 100
        self.endurance = self.mendurance
        self.attaque_physique = 100
        self.attaque_magique = 100
        self.defense_physique = 100
        self.defense_magique = 100
        self.vitesse = 100
        self.precision = 100
        self.esquive = 100
        self.critique = 0
        self.exp = 0
        self.lvl = 1