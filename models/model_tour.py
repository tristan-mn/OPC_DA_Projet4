from .model_match import Match


class Tour:
    """
    classe modelisant un tour du tournoi

    """

    def __init__(
        self,
        nom=None,
        date_heure_debut=None,
        date_heure_fin=None,
        liste_matchs=None,
        numero_round=None,
    ):
        self.numero_round = numero_round
        self.nom = "Round " + str(self.numero_round)
        self.date_heure_debut = date_heure_debut
        self.date_heure_fin = date_heure_fin
        self.liste_matchs = liste_matchs

    def __call__(self):
        return [self.nom,
                self.date_heure_debut,
                self.date_heure_fin,
                self.liste_matchs]

    def afficher_tour(self):
        print(
            f"****************************\n"
            f"*********  {self.nom} **********\n"
            f"*****************************\n"
            f"Debut: {self.date_heure_debut} \n"
            f"Fin : {self.date_heure_fin} \n"
            f"*****************************\n"
        )
        self.afficher_matchs()

    def afficher_matchs(self):
        print("Matchs:")
        numero_match = 0
        matchs_unserialized = []
        if len(self.liste_matchs) > 0:
            for match in self.liste_matchs:
                match_unserialized = Match(**match)
                matchs_unserialized.append(match_unserialized)

            for match in matchs_unserialized:
                numero_match += 1
                match.afficher_match(numero_match=numero_match)
        else:
            print("Il n'y a pas encore de Matchs")

    def serialized(self):
        tour_infos = {}
        tour_infos["nom"] = self.nom
        tour_infos["date_heure_debut"] = self.date_heure_debut
        tour_infos["date_heure_fin"] = self.date_heure_fin
        tour_infos["liste_matchs"] = self.liste_matchs
        return tour_infos
