#	Monstre
#		Nom
#		pv
#		pm
#		endurance
#		attaque
#		attaque.magique
#		defense
#		defense.magique
#		vitesse
#		présicion
#		esquive
#		taux.critique
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
        self.pm = 100
        self.end = 100
        self.atk_phy = 100
        self.atk_mag = 100
        self.def_phy = 100
        self.def_mag = 100
        self.vit = 100
        self.pre = 100
        self.esquive = 100
        self.crit = 0
        self.pex = lvl * random.randrange(10, 15, 1)
        self.lvl = lvl


class GobelinGeant(Mob):
    def __init__(self, name="Gobelin geant", lvl=1):
        Mob.__init__(self, name, lvl)
        self.pv = 120
        self.pm = 55
        self.end = 130
        self.atk_phy = 85
        self.atk_mag = 40
        self.def_phy = 55
        self.def_mag = 40
        self.vit = 85
        self.pre = 100
        self.esquive = 100
        self.crit = 0.15
        self.loot = random.randrange(16, 25, 1)


class Troll(Mob):
    def __init__(self, name="Troll", lvl=1):
        Mob.__init__(self, name, lvl)
        self.pv = 140
        self.pm = 40
        self.end = 75
        self.atk_phy = 115
        self.atk_mag = 50
        self.def_phy = 120
        self.def_mag = 80
        self.vit = 70
        self.pre = 100
        self.esquive = 50
        self.crit = 0.15
        self.loot = random.randrange(24, 37, 1)