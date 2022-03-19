from dataclasses import dataclass, field
from datetime import date


@dataclass
class Tournoi:
    nom : str = input("Quel est le nom du tournoi ? ")
    lieu : str = input("Où se déroule le tournoi ? ")
    description : str = input(" description du tournoi : ")
    date : str = str(date.today())
    nombre_tours : int = 4
   # tournees : list = []
   # joueurs : list[str]
   # controle_temps : float
   # blitz = 10 min ou moins pour jouer l'ensemble des coups
   # bullet = 3 min ou moins pour jouer l'ensemble des coups
   # jeu rapide = au moins 15 min et moins de 60 min pour jouer l'ensemble des coups

