from .model_tournoi import tournois_database
from tinydb import TinyDB, where


joueurs_database = TinyDB('joueurs.json', indent=4)

class Joueur:
    """
    Classe modélisant un joueur du tournoi

    """
    def __init__(self, prenom=None, nom=None, date_naissance=None, sexe=None, classement=0, score=0):
                  
        self.prenom = prenom
        self.nom = nom
        self.date_naissance = date_naissance
        self.sexe = sexe
        self.classement = classement
        self.score = score
        self.infos_joueur = [self.prenom, self.nom, self.date_naissance, self.sexe, self.classement, self.score]
    

    def __call__(self):
        return self.infos_joueur


    def __str__(self):
        return f"Nom: {self.nom}\n" \
               f"Prénom: {self.prenom}\n" \
               f"date de naissance: {self.date_naissance}\n" \
               f"Sexe: {self.sexe}\n" \
   		       f"Classement mondial: {self.classement}\n" \
               f"Score: {self.score}\n"

    
    def serialized(self):
        """
        cette fonction récupère les informations du joueur à partir de l'instance du joueur
        elle retourne ensuite  un dictionnaire avec toutes les informations du joueur

        Returns:
            dictionnaire: le dictionnaire retourné contient toutes les informations dérialisées pour un joueur
        """
        infos_joueur = {}
        infos_joueur['prenom'] = self.prenom
        infos_joueur['nom'] = self.nom
        infos_joueur['date_naissance'] = self.date_naissance
        infos_joueur['sexe'] = self.sexe
        infos_joueur['classement'] = self.classement
        infos_joueur['score'] = self.score
        return infos_joueur

    
    def ajout_joueur_database(self, joueur):
        """
        Cette fonction permet d'ajouter un joueur avec  ses informations dans la base de données

        Args:
            joueur (dictionnaire): le dictionnaire contient les informations du joueur serialisées
        """
        joueurs_database.insert(joueur)

    def ajout_tournoi_database(self, tournoi, joueurs):
        tournois_database.update({"joueurs": joueurs}, where("nom") == tournoi)