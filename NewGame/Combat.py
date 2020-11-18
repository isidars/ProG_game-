#Phase de combat
import Personnages
import Monstre

init=0
Monstre1=Monstre.Mob1()
Perso1=Personnages.Paladin()

print ("Un",Monstre1.Name,"vient d'apparaitre!")
print ("Début du combat:")
print ("Votre vitesse est de:",Perso1.VIT)
print ("La Vitesse de",Monstre1.Name,"est de:" ,Monstre1.VIT)

#Savoir qui commence:
if int(Perso1.VIT) >= int(Monstre1.VIT) :
		print ("vous avez l'initiative!")
		init=1
else:
		print (Monstre1.Name,"a l'initiative!")

def Etat_Combat():

	print ("################	",Perso1.Name," PV:",Perso1.PV,"	################################	",Monstre1.Name," PV:",Monstre1.PV,"	################")
	print ("#		Endurance:",Perso1.EDRC,"   --  PM:     ",Perso1.PM,"		##		Endurance:",Monstre1.EDRC,"   --  PM:     ",Monstre1.PM,"		#")
	print ("#		Attaque:  ",Perso1.ATK,"   --  Atq Mag:",Perso1.ATK_MAG,"		##		Attaque:  ",Monstre1.ATK,"   --  Atq Mag:",Monstre1.ATK_MAG,"		#")
	print ("#		Defense:  ",Perso1.DEF,"   --  Def Mag:",Perso1.DEF_MAG,"		##		Defense:  ",Monstre1.DEF,"   --  Def Mag:",Monstre1.DEF_MAG,"		#")
	print ("#  	 Vitesse:",Perso1.VIT,"  --  Précision:",Perso1.PREC,"  --  Esquive:",Perso1.ESQV,"	##  	 Vitesse:",Monstre1.VIT,"  --  Précision:",Monstre1.PREC,"  --  Esquive:",Monstre1.ESQV,"	#")
	print ("#################################################################################################################################")

def Etat_Competences():

	print ("###################		Selectionnez une action: 	#################")
	print ("########    Compétences:    ####################    Magie:    ###################")
	print ("#		1:",Personnages.PaladinComp[0],"		##	A:",Personnages.PaladinMagie[0],"			#")
	print ("#		2:",Personnages.PaladinComp[1],"		##	B:",Personnages.PaladinMagie[1],"			#")
	print ("#		3:",Personnages.PaladinComp[2],"		##	C:",Personnages.PaladinMagie[2],"		#")
	print ("#		4:",Personnages.PaladinComp[3],"		##")

Etat_Combat()
Etat_Competences()

Action = input('Quel action voulez-vous faire?')

print (Action)
