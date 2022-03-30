class Joueur:
    """
    Classe modélisant un joueur du tournoi

    """
    def __init__(self, nom,
                 prenom, date_naissance, sexe, classement_mondial,
                  points_mondial, classement_tournoi, points_tournoi):
        self.nom = nom
        self.prenom = prenom
        self.date_naissance = date_naissance
        self.sexe = sexe
        self.classement_mondial = classement_mondial
        self.points_mondial = points_mondial
        self.classement_tournoi = classement_tournoi
        self.points_tournoi = points_tournoi
