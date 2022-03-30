class Tour:
    """
    classe modelisant un tour du tournoi

    """
    def __init__(self,nom ,heure_debut ,heure_fin , liste_matchs):
        self.nom = nom
        self.heure_debut = heure_debut
        self.heure_fin = heure_fin
        self.liste_matchs = liste_matchs
        return [nom, heure_debut, heure_fin, liste_matchs]
