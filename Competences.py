import random

class FlecheEnflamme:
	comp_class="Flèche enflammée"
	comp_desc="lancer une flèche embrasée contre l'adversaire et peut le brûler"
	comp_effet=random.randrange(8, 14, 1)
	comp_conso=30


class Concentration:
	comp_class="Concentration"
	comp_desc="vous plonger dans un état de transe et permettre une defense optimal"
	comp_effet=random.randrange(8, 12, 1)
	com_conso=15



#print("Vous avez donc choisi d'utiliser '" + Concentration.comp_class + "' ce qui aura pour effet de " + Concentration.comp_desc + ". ce qui vous rajoutera " + str(Concentration.comp_effet))
#print("Vous avez donc choisi d'utiliser '" + Rush.comp_class + "' ce qui aura pour effet de " + Rush.comp_desc)
