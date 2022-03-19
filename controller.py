from models_tournoi import Tournoi

mon_tournoi = Tournoi()

class MenuManager:
    pass

class TournoiManager:
    pass


class UtilisateurManager:
    def demander_infos_joueur(self):
        """ Cette fonction recupère les informations sur chaque joueur avec des inputs

        Returns:
            tableau : la fonction retourne un tableau avec les informations sur chaque joueur
                    qui ont été entrées par les organisateurs du tournoi
        """
        prenom_joueur = input("Quel est le prénom du joueur ?  ")
        nom_joueur = input("Quel est le nom du joueur ?  ")
        date_naissance_joueur = input("Qelle sa date de naissance ? (JJ/MM/AAAA)  ")
        sexe_joueur = input("Quel est son sexe ? (M/F) ")
        points_mondial_joueur = input("Quel est le total de son nombre de points mondialement ?  ")
        infos_joueur = [prenom_joueur, nom_joueur, date_naissance_joueur, sexe_joueur, points_mondial_joueur]
        return infos_joueur


    def ajout_joueurs(self):
        """  Cette fonction demande à l'organisateur du tournoi
            s'il souhaite ajouter un nouveau joueur au tournoi

        Returns:
            tableau: cette fonction renvoie un tableau de plusieurs tableaux 
                    chaque tableau correspond aux informations de chaque nouveau joueur
        """
        quest = False
        joueurs = []
        while quest == False:
            quest_ajout = input("Voulez-vous ajouter un nouveau joueur au tournoi ?  ")
            if quest_ajout == "oui":
                new_joueur = self.demander_infos_joueur()
                joueurs.append(new_joueur)
                quest = False
            elif quest_ajout == "non":
                print()
                print("l'ajout des joueurs est terminé !")
                print()
                quest = True
            else:
                print()
                print("Erreur ! veuillez répondre par oui ou non.")
                print()
        return joueurs