class Match:
    """
    Classe modelisant un match entre deux joueurs

    """
    NUMERO_MATCH = 1

    def __init__(self, joueur1=None, joueur2=None, resultat_joueur1=None, resultat_joueur2=None):
        self.nom_match = "Match " + str(Match.NUMERO_MATCH)
        self.joueur1 = joueur1
        self.joueur2 = joueur2
        self.resultat_joueur1 = resultat_joueur1
        self.resultat_joueur2 = resultat_joueur2
        self.vainqueur = "En attente de vainqueur... Le match n'est pas terminé"

        if self.resultat_joueur1 > self.resultat_joueur2:
            self.vainqueur = self.joueur1
        elif self.resultat_joueur1 < self.resultat_joueur2:
            self.vainqueur = self.joueur2

    def __call__(self):
        return ([self.joueur1, self.resultat_joueur1],[self.joueur2, self.resultat_joueur2])


    def __str__(self) -> str:
        return f"{self.nom_match} : {self.joueur1[0]} {self.joueur1[1]} -- VS -- {self.joueur2[0]} {self.joueur2[1]}.\n" \
               f"Victoire de {self.vainqueur}"
               
        
