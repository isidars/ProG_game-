

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
        dgts = self.attaque_phy - cible.defense_phy / 2
        cible.pv -= dgts
        return cible.pv

    def Reinit(self):
        self.pv = self.mpv
        self.pm = self.mpm
        self.end = self.mend

    def Combattre(self, joueur):
        #Creation fonction affichage joueurs lors d'un combat
        def AffJoueur():
            for i in range(len(joueur)):
                while joueur[i].pv > 0:
                    print("[{}] {}pv".format(joueur[i].name, joueur[i].pv))

        #Affichage des joueurs au début du combat
                AffJoueur()
                while joueur[i].pv > 0:
                    x = 0
                    while x > 4 or x < 1:
                        try:
                            x = int(input("Renseigner l'action à faire :\n1.Attaquer\n2.Magie\n3.Objet\n4.Fuite"))
                     except:
                           print("Veuillez choisir une action valide")
                        x = 0

                if x == 1:
                    print("Quel joueur voulez-vous toucher ?\n", joueur)
                    target = 999999
                    print(joueur)
                    while target < 0 and target > len(joueur):
                        try:
                            target = int(input(">>"))
                        except:
                            print("Veuillez renseigner un ennemie valide")
                    self.Attaquer(joueur[target])
            else:
                print(joueur[i].name, " est mort")

class Archer(Joueur):
    def __init__(self, name, role='Archer'):
        Joueur.__init__(self, name, role='Archer')
        self.desc = "L'archer utilise ces capacités et compétence pour infliger de gros dégats à distance," \
                    "\nIl est cependant assez fragile!"
        self.mpv = 150
        self.mpm = 50
        self.mend = 200
        self.attaque_phy = 150

class MageBlanc(Joueur):
    def __init__(self, name, role='MageB'):
        Joueur.__init__(self, name, role='MageB')
        self.desc = "Le Mage Blanc utilise ces compétences magique pour soigné et soutenir ces alliés," \
                    "\nIl est faible mais sera d'une grande d'aide contre les ennemies puissants!"
        self.mpv = 120
        self.mpm = 120
        self.mend = 100
        self.attaque_phy = 80
#        self.attaque_mag = 100
        self.defense_phy = 80
#        self.defense_mag = 115
        self.vitesse = 85

class Mob(Joueur):
    def __init__(self, name, role='Monstre'):
        Joueur.__init__(self, name, role='Monstre')
        if name == 'gob':
            self.desc = "Le gobelin est une créature commune du fait de son mode de reproduction a l'instar des chiens," \
                        "ils naissent par portées de 3 à 10 individus.\nIl est faible et en est conscient, d'habitude il préfère rester en horde!"
            self.mpv = 130
            self.mpm = 70
            self.mend = 120
            self.attaque_phy = 80
            self.defense_phy = 100
        if name == 'troll':
            self.desc = "Le troll est une ignoble créature, aussi impitoyable que moche! souvent solitaire, certain savent faire preuve de cohésion" \
                        " pour dévoiler tout leur potentiel. \nIl dispose d'une résistance physique particulèrement remarquable.."
            self.mpv = 200
            self.mpm = 50
            self.mend = 150
            self.attaque_phy = 150
            self.defense_phy = 180