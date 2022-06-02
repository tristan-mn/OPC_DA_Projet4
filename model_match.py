

class Match:
    """
    Classe modelisant un match entre deux joueurs

    """

    def __init__(self, joueur1=None, joueur2=None, score_joueur1=0, score_joueur2=0, numero=None):
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
    
    def match_serialized(self):
        infos_match = {}
        infos_match["nom"] = self.nom_match
        infos_match["joueur1"] = self.joueur1
        infos_match["score_joueur1"] = self.score_joueur1
        infos_match["joueur2"] = self.joueur2
        infos_match["score_joueur2"] = self.score_joueur2
        infos_match["vainqueur"] = self.vainqueur

        return infos_match
