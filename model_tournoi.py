from textwrap import indent
from tinydb import TinyDB, where

tournois_database = TinyDB('tournois.json', indent=4)


class Tournoi:
    """
    classe modelisant un tournoi

    """
    def __init__(self,nom ,lieu ,date ,temps , description, nombre_tours=4, joueurs=None, tours=[], tournoi_id=None):
        self.nom = nom
        self.lieu = lieu
        self.date = date
        self.temps = temps
        self.description = description
        self.nombre_tours = nombre_tours
        self.tours = tours
        self.joueurs = joueurs
        self.tournoi_id = tournoi_id
        self.infos_tournoi = [self.nom, self.lieu, self.date, self.temps, self.description, self.nombre_tours, self.joueurs, self.tours]

    def __call__(self):
        return self.infos_tournoi

    def __str__(self):
        return f"### Bienvenue au Tournoi ###\n" \
               f"#####  {self.nom} #####\n" \
               f"Lieu: {self.lieu} \n" \
               f"date : {self.date} \n" \
               f"Système: {self.temps}\n" \
               f"Description :{self.description}\n" \
               f" {self.tours}"
               #f"Joueurs : {'---'.join([str(j) for j in self.joueurs])}" \


    def tournoi_serialized(self):
        infos_tournoi = {}
        infos_tournoi['nom'] = self.nom
        infos_tournoi['lieu'] = self.lieu
        infos_tournoi['date'] = self.date
        infos_tournoi['temps'] = self.temps
        infos_tournoi['description'] = self.description
        infos_tournoi['nombre_tours'] = self.nombre_tours
        infos_tournoi["joueurs"] = self.joueurs
        infos_tournoi["tours"] = self.tours
        return infos_tournoi

    def add_to_database(self, tournoi):
        tournoi_id = tournois_database.insert(tournoi)
        tournois_database.update({"tournoi_id": tournoi_id}, doc_ids=[tournoi_id])
    
    def update_tours(self, tour):
        tournois_database.update({"tours": tour}, where("nom") == self.nom)


   # blitz = 10 min ou moins pour jouer l'ensemble des coups
   # bullet = 3 min ou moins pour jouer l'ensemble des coups
   # jeu rapide = au moins 15 min et moins de 60 min pour jouer l'ensemble des coups

