from dataclasses import dataclass

@dataclass
class Joueur:
    nom : str
    prenom : str
    date_naissance : str
    sexe : str
    classement_mondial : int
    points_mondial : int
    classement_championnat : int = 0
    point_championnat : int = 0
