from dataclasses import dataclass
from datetime import date
from models_match import Match
import time

un_match = Match()

@dataclass
class Tour:
    date_debut : str = str(date.today())
    heure_debut : str = time.strftime('%Hh : %Mmin : %Ssec')
    date_fin : str = time.strftime('%Hh : %Mmin : %Ssec')
    tour = [un_match.match]
    nom : str = "Round" + str(1)