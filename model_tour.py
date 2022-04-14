from model_match import Match

class Tour:
    """
    classe modelisant un tour du tournoi

    """
    NUMERO_TOUR = 1

    def __init__(self, date_heure_debut=None, date_heure_fin=None, liste_matchs=None):
        self.nom = "Round " + str(Tour.NUMERO_TOUR)
        self.date_heure_debut = date_heure_debut
        self.date_heure_fin = date_heure_fin
        self.liste_matchs = liste_matchs

    def __call__(self):    
        return [self.nom, self.heure_debut, self.heure_fin, self.liste_matchs]
