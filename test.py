Classes :
Role : spécialité du joueur
Tank => Francis
Guerrier (DPS CAC) => Adrien
Archer (DPS Dis) => Melvin
Mage blanc (healer, soutien) => Remy
Mage noir (DPS magique) => Mathieu
Assassin(DPS CAC, Dist) => Jerome

100 normal
120	bien
80 moins bien

Equilibrage = nbr stat * 100 = 1000

------------------------------------------------------------------------------------------
Demander nom joueur 1
Demander spécialité joueur en proposant la liste, une courte description des roles et les stats
Demander nom joueur 2
Demander spécialité joueur en proposant la liste, une courte description des roles et les stats
Boucle tant que joueurs et monstre en vie
	determiner l'ordre d'action par rapport à la vitesse
	Si montre
		si vie en dessous de 25% et sort existe
			soin du monstre
		sinon
			comparaison des pv des joueurs
				random (attaque magie) attaque le plus faible
				resultat esquive
				infliger dégats
				si tout les joueurs sont morts
					fin du combat
	sinon si joueur
		Proposez choix 
			choix = compétence physique
				Si endurance suffisante
					resultat esquive
					infliger dégats
					si montre mort
						victoire
				sinon échec action
					affichage message erreur
					retour choix action
			choix = sort
				Si PM suffisant
					ingliger les dégats
					si montre mort
						victoire
				sinon échec action
					affichage message erreur
					retour choix action
			choix = objet
				affichage des objets dispo
				appliquer effets objet (fin du tour)
				si montre mort
						victoire
			choix = fuite
				affichage TROLL
				plus perte de tour
			Choix = erreur
				retour choix action
				
			
	
