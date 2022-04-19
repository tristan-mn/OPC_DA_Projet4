import time

from tinydb import TinyDB

joueurs_database = TinyDB('joueurs.json')

class Joueur:
    """
    Classe modélisant un joueur du tournoi

    """
    def __init__(self, prenom=None, nom=None, date_naissance=None, sexe=None, classement_mondial=0, points_tournoi=0):
                  
        self.prenom = prenom
        self.nom = nom
        self.date_naissance = date_naissance
        self.sexe = sexe
        self.classement_mondial = classement_mondial
        self.points_tournoi = points_tournoi
        self.infos_joueur = [self.prenom, self.nom, self.date_naissance, self.sexe, self.classement_mondial, self.points_tournoi]
    
    def __call__(self):
        return self.infos_joueur


    def serialized(self):
        infos_joueur = {}
        infos_joueur['Prenom'] = self.prenom
        infos_joueur['Nom'] = self.nom
        infos_joueur['Date de naissance'] = self.date_naissance
        infos_joueur['Sexe'] = self.sexe
        infos_joueur['Classement'] = self.classement_mondial
        infos_joueur['Score'] = self.points_tournoi
        #infos_joueur['Id du joueur'] = self.player_id
        return infos_joueur

    def unserialized(self, joueur_serialized):
        prenom = joueur_serialized["Prenom"]
        nom = joueur_serialized["Nom"]
        date_naissance = joueur_serialized["Date de naissance"]
        sexe = joueur_serialized["Sexe"]
        classement_mondial = joueur_serialized["Classement"]
        points_tournoi = joueur_serialized["Score"]
        #player_id = joueur_serialized["Id du joueur"]
        return Joueur(prenom,nom,date_naissance,sexe,classement_mondial,points_tournoi)

    
    def add_to_database(self, infos_joueur):
        joueur = Joueur(infos_joueur[0],
                        infos_joueur[1],
                        infos_joueur[2],
                        infos_joueur[3],
                        infos_joueur[4]
                        )
        # print(joueur.serialized())
        joueur_id = joueurs_database.insert(joueur.serialized())
        joueurs_database.update({'Id du joueur': joueur_id}, doc_ids=[joueur_id])
        time.sleep(2)