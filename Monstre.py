#	Monstre
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
#		niveau
#		pex
#		loot
#		ordre_action
import random


class BossGobelin:
    mob_class="Gobelin géant"
    mob_pv= 120
    mob_pm= 55
    mob_end= 130
    mob_atk_phy= 85
    mob_atk_mag= 40
    mob_def_phy= 55
    mob_def_mag= 40
    mob_vit= 85
    mob_pre= 100
    mob_esquive= 60
    mob_crit= 0.15
    mob_lvl= 10
    mob_pex= 500
    mob_loot=random.randrange(154, 179, 1)


class Troll:
    mob_class = "Troll"
    mob_pv = 140
    mob_pm = 40
    mob_end = 80
    mob_atk_phy = 110
    mob_atk_mag = 50
    mob_def_phy = 115
    mob_def_mag = 80
    mob_vit = 75
    mob_pre = 100
    mob_esquive = 60
    mob_crit = 0.15
    mob_lvl = 1
    mob_pex = 66
    mob_loot = random.randrange(12, 26, 1)