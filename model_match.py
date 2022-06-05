class Match:
    """
    Classe modelisant un match entre deux joueurs

    """

    def __init__(self, nom=None, joueur1=None, joueur2=None, score_joueur1=0, score_joueur2=0, numero=None, vainqueur=None):
        self.joueur1 = joueur1
        self.joueur2 = joueur2
        self.score_joueur1 = score_joueur1
        self.score_joueur2 = score_joueur2
        self.vainqueur = None
        self.numero = numero
        self.nom_match = "Match " + str(self.numero)

    def __call__(self):
        return [[self.joueur1, self.score_joueur1 ], [self.joueur2, self.score_joueur2]]


    def __str__(self) -> str:
        return f"{self.nom_match} : {self.joueur1[0]} {self.joueur1[1]} -- VS -- {self.joueur2[0]} {self.joueur2[1]}.\n"

    def afficher_match(self, numero_match):
        print( f"*****  Match {numero_match} *****\n"
               f"Premier Joueur: {self.joueur1[0]} {self.joueur1[1]} \n"
               f"Second Joueur : {self.joueur2[0]} {self.joueur2[1]}\n"
               f"Score {self.joueur1[0]} {self.joueur1[1]}: {self.score_joueur1}\n"
               f"Score {self.joueur2[0]} {self.joueur2[1]}: {self.score_joueur2}")
        if self.score_joueur1 > self.score_joueur2:
            print(f"Vainqueur : {self.joueur1[0]} {self.joueur1[1]}\n")
        elif  self.score_joueur1 < self.score_joueur2:
            print(f"Vainqueur : {self.joueur2[0]} {self.joueur2[1]}\n")
        else:
            print("Vainqueur : Match Nul\n")
               
    
    def match_serialized(self):
        infos_match = {}
        infos_match["nom"] = self.nom_match
        infos_match["joueur1"] = self.joueur1
        infos_match["score_joueur1"] = self.score_joueur1
        infos_match["joueur2"] = self.joueur2
        infos_match["score_joueur2"] = self.score_joueur2
        infos_match["vainqueur"] = self.vainqueur

        return infos_match