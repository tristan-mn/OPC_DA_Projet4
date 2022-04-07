class Joueur:
    """
    Classe modélisant un joueur du tournoi

    """
    def __init__(self, nom=None, prenom=None, date_naissance=None, sexe=None, points_mondial=0, points_tournoi=0):
                  
        self.nom = nom
        self.prenom = prenom
        self.date_naissance = date_naissance
        self.sexe = sexe
        self.points_mondial = points_mondial
        self.points_tournoi = points_tournoi
        self.infos_joueur = [self.prenom, self.nom, self.date_naissance, self.sexe, self.points_mondial, self.points_tournoi]
    
    def __call__(self):
        return self.infos_joueur