class Match:
    """
    Classe modelisant un match entre deux joueurs

    """
    NUMERO_MATCH = 1

    def __init__(self, joueur1, joueur2, score_joueur1, score_joueur2):
        self.nom_match = "Match " + str(Match.NUMERO_MATCH)
        self.joueur1 = joueur1
        self.joueur2 = joueur2
        self.score_joueur1 = score_joueur1
        self.score_joueur2 = score_joueur2
        self.resultat = None

    def __str__(self) -> str:
        return f"{self.nom} : {self.joueur1} -- VS -- {self.joueur2}.\n" \
               f" Résultat : {self.resultat}"
        
