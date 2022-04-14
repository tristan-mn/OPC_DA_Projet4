class Match:
    """
    Classe modelisant un match entre deux joueurs

    """
    NUMERO_MATCH = 1

    def __init__(self, joueur1=None, joueur2=None, score_joueur1=0, score_joueur2=0, vainqueur=None):
        self.nom_match = "Match " + str(Match.NUMERO_MATCH)
        self.joueur1 = joueur1
        self.joueur2 = joueur2
        self.score_joueur1 = score_joueur1
        self.score_joueur2 = score_joueur2

        #if self.resultat_joueur1 > self.resultat_joueur2:
            #self.vainqueur = self.joueur1
        #elif self.resultat_joueur1 < self.resultat_joueur2:
            #self.vainqueur = self.joueur2

    def __call__(self):
        return ([self.joueur1, self.score_joueur1 ], [self.joueur2, self.score_joueur2])


    def __str__(self) -> str:
        return f"{self.nom_match} : {self.joueur1[0]} {self.joueur1[1]} -- VS -- {self.joueur2[0]} {self.joueur2[1]}.\n"
