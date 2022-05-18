from textwrap import indent
import time
from model_tournoi import tournois_database

from tinydb import TinyDB, where

joueurs_database = TinyDB('joueurs.json', indent=4)

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
        infos_joueur['prenom'] = self.prenom
        infos_joueur['nom'] = self.nom
        infos_joueur['date de naissance'] = self.date_naissance
        infos_joueur['sexe'] = self.sexe
        infos_joueur['classement'] = self.classement_mondial
        infos_joueur['score'] = self.points_tournoi
        #infos_joueur['Id du joueur'] = self.player_id
        return infos_joueur

    def unserialized(self, joueur_serialized):
        prenom = joueur_serialized["prenom"]
        nom = joueur_serialized["nom"]
        date_naissance = joueur_serialized["date de naissance"]
        sexe = joueur_serialized["sexe"]
        classement_mondial = joueur_serialized["classement"]
        points_tournoi = joueur_serialized["score"]
        #player_id = joueur_serialized["Id du joueur"]
        return Joueur(prenom,nom,date_naissance,sexe,classement_mondial,points_tournoi)

    
    def ajout_joueur_database(self, joueur):
        # print(joueur.serialized())
        joueur_id = joueurs_database.insert(joueur)
        joueurs_database.update({'id du joueur': joueur_id}, doc_ids=[joueur_id])

    def ajout_tournoi_database(self, tournoi, joueurs):
        tournois_database.update({"joueurs": joueurs}, where("nom") == tournoi)
        
        #time.sleep(2)