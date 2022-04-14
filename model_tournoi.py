class Tournoi:
    """
    classe modelisant un tournoi

    """
    def __init__(self,nom ,lieu ,date ,temps , description, nombre_tours=4, joueurs=None, liste_tours=None):
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

   # controle_temps : float
   # blitz = 10 min ou moins pour jouer l'ensemble des coups
   # bullet = 3 min ou moins pour jouer l'ensemble des coups
   # jeu rapide = au moins 15 min et moins de 60 min pour jouer l'ensemble des coups

