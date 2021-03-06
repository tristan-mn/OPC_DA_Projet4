from tinydb import TinyDB, where


tournois_database = TinyDB("tournois.json", indent=4)


class Tournoi:
    """
    classe modelisant un tournoi

    """

    def __init__(
        self,
        nom,
        lieu,
        date,
        temps,
        description,
        tours=[],
        tours_joues=0,
        nombre_tours=4,
        joueurs=None,
    ):
        self.nom = nom
        self.lieu = lieu
        self.date = date
        self.temps = temps
        self.description = description
        self.tours_joues = tours_joues
        self.tours = tours
        self.nombre_tours = nombre_tours
        self.joueurs = joueurs
        self.infos_tournoi = [
            self.nom,
            self.lieu,
            self.date,
            self.temps,
            self.description,
            self.nombre_tours,
            self.joueurs,
            self.tours,
        ]

    def __call__(self):
        return self.infos_tournoi

    def __str__(self) -> str:
        return (
            f"***** Bienvenue au Tournoi *****\n"
            f"*****  {self.nom} *****\n"
            f"Lieu: {self.lieu}\n"
            f"date : {self.date}\n"
            f"Système: {self.temps}\n"
            f"Description :{self.description}\n"
        )

    def afficher_tournoi(self):
        print(
            "***** Bienvenue au Tournoi *****\n"
            f"*****  {self.nom} *****\n"
            f"Lieu: {self.lieu}\n"
            f"date : {self.date}\n"
            f"Système: {self.temps}\n"
            f"Description :{self.description}\n"
        )
        self.afficher_joueurs()
        self.afficher_tours()

    def afficher_joueurs(self):
        print("Joueurs :")

        if self.joueurs is None:
            print("Il n'y a pas encore de joueurs\n")
        elif len(self.joueurs) > 0:
            for joueur in self.joueurs:
                print(joueur)

    def afficher_tours(self):
        print("Tours :")
        if len(self.tours) > 0:
            tours_unserialized = []
            for tour in self.tours:
                tours_unserialized.append(tour)
            for tour in tours_unserialized:
                tour.afficher_tour()
        else:
            print("Il n'y a pas encore de tours\n")

    def afficher_matchs(self):
        print("Matchs :")
        if len(self.tours) > 0:
            for tour in self.tours:
                tour.afficher_matchs()
        else:
            print("Il n'y a pas encore de matchs")

    def tournoi_serialized(self):
        infos_tournoi = {}
        infos_tournoi["nom"] = self.nom
        infos_tournoi["lieu"] = self.lieu
        infos_tournoi["date"] = self.date
        infos_tournoi["temps"] = self.temps
        infos_tournoi["description"] = self.description
        infos_tournoi["tours_joues"] = self.tours_joues
        infos_tournoi["nombre_tours"] = self.nombre_tours
        infos_tournoi["tours"] = self.tours
        infos_tournoi["joueurs"] = self.joueurs
        return infos_tournoi

    def add_to_database(self, tournoi):
        tournois_database.insert(tournoi)

    def update_joueurs_tournoi_database(self, tournoi, joueurs):
        tournois_database.update({"joueurs": joueurs}, where("nom") == tournoi)

    def update_tours(self, tour):
        tournois_database.update({"tours": tour}, where("nom") == self.nom)
