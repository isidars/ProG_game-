#	Monstre
#		Nom
#		pv
#		pm
#		enduranceurance
#		attaque
#		attaque.magiqueique
#		defense
#		defense.magiqueique
#		vitesseesse
#		présicion
#		esquive
#		taux.critiqueique
#		état(normal,empoissoné,paralysé,brulé)
#		niveau
#		pex
#		loot
#		ordre.action
import random

class Mob:
    def __init__(self, name, lvl):
        self.name = name
        self.etat = "Normal"
        self.pv = 100
        self.mpv = 100
        self.pm = 100
        self.mpm = 100
        self.endurance = 100
        self.mendurance = 100
        self.attaque_physique = 100
        self.attaque_magique = 100
        self.defense_physique = 100
        self.defense_magique = 100
        self.vitesse = 100
        self.precision = 100
        self.esquive = 100
        self.critique = 0
        self.pex = lvl * random.randrange(10, 15, 1)
        self.lvl = lvl


class GobelinGeant(Mob):
    def __init__(self, name="Gobelin geant", lvl=1):
        Mob.__init__(self, name, lvl)
        self.mpv = 120
        self.mpm = 55
        self.mendurance = 130
        self.attaque_physique = 85
        self.attaque_magique = 40
        self.defense_physique = 55
        self.defense_magique = 40
        self.vitesse = 85
        self.precision = 100
        self.esquive = 100
        self.critique = 0.15
        self.loot = random.randrange(16, 25, 1)


class Troll(Mob):
    def __init__(self, name="Troll", lvl=1):
        Mob.__init__(self, name, lvl)
        self.mpv = 140
        self.ppm = 40
        self.mendurance = 75
        self.attaque_physique = 115
        self.attaque_magique = 50
        self.defense_physique = 120
        self.defense_magique = 80
        self.vitesse = 70
        self.precision = 100
        self.esquive = 50
        self.critique = 0.15
        self.loot = random.randrange(24, 37, 1)


class TrollG(Mob):
    def __init__(self, name="TrollG", lvl=1):
        Mob.__init__(self, name, lvl)
        self.mpv = 200
        self.ppm = 40
        self.mendurance = 75
        self.attaque_physique = 200
        self.attaque_magique = 50
        self.defense_physique = 500
        self.defense_magique = 80
        self.vitesse = 70
        self.precision = 100
        self.esquive = 50
        self.critique = 0.15
        self.loot = random.randrange(24, 37, 1)