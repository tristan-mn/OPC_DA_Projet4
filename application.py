from vue import MenuPrincipal
from model_tournoi import Tournoi

#test


class MenuManager:
    def __init__(self):
        self.menu_principal = MenuPrincipal()

class TournoiManager:
    def __init__(self):
        self.tournoi = None
        self.data = None

    def demander_infos_tournoi(self):
        nom = input("Quel est le nom du tournoi ?\t")
        lieu = input("Où se déroule le tournoi ?\t")
        date = input("Quand se déroule le tournoi (JJ/MM/AAAA) ?\t")
        temps = int(input("1.Blitz  2.Bullet  3.Un coup rapide ?\t"))
        description = input("Entrez une desciption du tournoi ?\t")
        return nom, lieu, date, temps, description

    def creer_tournoi(self):
        self.tournoi = Tournoi(*self.demander_infos_tournoi())
        return self.tournoi

    def modifier(self):
        pass

    def sauvegarder(self):
        pass

    def afficher(self):
        print(self.tournoi)

    def ajout_joueurs(self):
        NB_JOUEURS = 8
        for i in range(NB_JOUEURS):
           joueur = UtilisateurManager.demander_infos_joueur(self)
           self.tournoi.joueurs.append(joueur)

    def commencer(self):
        pass
    

class UtilisateurManager:
    def demander_infos_joueur(self):
        """ Cette fonction recupère les informations sur chaque joueur avec des inputs

        Returns:
            tableau : la fonction retourne un tableau avec les informations sur chaque joueur
                    qui ont été entrées par les organisateurs du tournoi
        """
        prenom_joueur = input("Quel est le prénom du joueur ?\t")
        nom_joueur = input("Quel est le nom du joueur ?\t")
        date_naissance_joueur = input("Qelle sa date de naissance ? (JJ/MM/AAAA)\t")
        sexe_joueur = input("Quel est son sexe ? (M/F)\t")
        points_mondial_joueur = input("Quel est le total de son nombre de points mondialement ?\t")
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
            quest_ajout = input("Voulez-vous ajouter un nouveau joueur au tournoi ? \t")
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

new = TournoiManager()
tournoi = new.creer_tournoi()
new.ajout_joueurs()
print(tournoi)
