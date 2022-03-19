from dataclasses import dataclass

@dataclass
class Match:
    """joueur_1 : list = [nom_joueur_1, score_joueur1]
    joueur_2 : list = [nom_joueur2, score_joueur2]"""
    match : tuple = ("joueur_1", "joueur_2")