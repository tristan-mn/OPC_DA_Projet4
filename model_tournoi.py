from tinydb import TinyDB

tournois_database = TinyDB('tournois.json')


class Tournoi:
    """
    classe modelisant un tournoi

    """
    def __init__(self,nom ,lieu ,date ,temps , description, nombre_tours=4, joueurs=None, liste_tours=[]):
        self.nom = nom
        self.lieu = lieu
        self.date = date
        temps_partie = ["blitz", "bullet", "Un coup rapide"]
        self.temps = temps_partie[temps - 1]
        self.description = description
        self.nombre_tours = nombre_tours
        self.liste_tours = liste_tours
        self.joueurs = joueurs


    def __str__(self):
        return f"### Bienvenue au Tournoi ###\n" \
               f"#####  {self.nom} #####\n" \
               f"Lieu: {self.lieu} \n" \
               f"date : {self.date} \n" \
               f"Système: {self.temps}\n" \
               f"Description :{self.description}\n" \
               f"Joueurs : {'---'.join([str(j) for j in self.joueurs])}" \
               f" {self.liste_tours}"


    def serialized(self):
        infos_tournoi = {}
        infos_tournoi['Nom du tournoi'] = self.nom
        infos_tournoi['Lieu'] = self.lieu
        infos_tournoi['Date'] = self.date
        infos_tournoi['Description'] = self.description
        infos_tournoi['Controle du temps'] = self.temps
        infos_tournoi['Nombre de tours'] = self.nombre_tours
        infos_tournoi["Joueurs_id"] = self.joueurs
        infos_tournoi["Tours"] = self.liste_tours
        infos_tournoi["Id du tournoi"] = self.tournoi_id

        return infos_tournoi

    def unserialized(self, tournoi_serialized):
        nom = tournoi_serialized['Nom du tournoi']
        lieu = tournoi_serialized['Lieu']
        date = tournoi_serialized['Date']
        description = tournoi_serialized['Description']
        temps = tournoi_serialized['Controle du temps']
        nombre_tours = tournoi_serialized['Nombre de tours']
        joueurs = tournoi_serialized["Joueurs_id"]
        liste_tours = tournoi_serialized["Tours"]
        tournoi_id = tournoi_serialized["Id du tournoi"]

        return Tournoi(nom, lieu, date, description, temps, nombre_tours, joueurs, liste_tours, tournoi_id)

    def add_to_database(self, infos_tournoi):
        tournoi = Tournoi(infos_tournoi[0],
                          infos_tournoi[1],
                          infos_tournoi[2],
                          infos_tournoi[3],
                          infos_tournoi[4],
                          infos_tournoi[5],
                          infos_tournoi[6],
                                )
        tournoi_id = tournois_database.insert(tournoi.serialized())
        tournois_database.update({"Id du tournoi": tournoi_id}, doc_ids=[tournoi_id])


   # controle_temps : float
   # blitz = 10 min ou moins pour jouer l'ensemble des coups
   # bullet = 3 min ou moins pour jouer l'ensemble des coups
   # jeu rapide = au moins 15 min et moins de 60 min pour jouer l'ensemble des coups

