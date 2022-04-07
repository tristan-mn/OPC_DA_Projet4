from vue import MenuPrincipal
from model_tournoi import Tournoi
from model_joueur import Joueur

class MenuManager:
    def __init__(self):
        self.menu_principal = MenuPrincipal()

class TournoiManager:
    def __init__(self):
        self.tournoi = None
        self.data = None

    def demander_infos_tournoi(self):
        """ Cette methode recupère les informations pour créer un tournoi

        Returns:
            tableau: la methode retourne un tableau avec les informations du tournoi
        """
        nom = input("Quel est le nom du tournoi ?\t")
        lieu = input("Où se déroule le tournoi ?\t")
        date = input("Quand se déroule le tournoi (JJ/MM/AAAA) ?\t")
        temps = int(input("1.Blitz  2.Bullet  3.Un coup rapide ?\t"))
        description = input("Entrez une desciption du tournoi ?\t")
        return nom, lieu, date, temps, description

    def creer_tournoi(self):
        """ cette methode recupère les informations du tournoi de la methode demander_infos_tournoi
            pour créer un instance de tournoi à partir du model Tournoi

        Returns:
            str : la méthode retourne la représentation str de l'instance du tournoi
        """
        self.tournoi = Tournoi(*self.demander_infos_tournoi())
        return self.tournoi

    def modifier(self):
        pass

    def sauvegarder(self):
        pass

    def afficher(self):
        print(self.tournoi)

    def ajout_joueurs(self):
        NB_JOUEURS = 3
        for i in range(NB_JOUEURS):
           infos_joueur = UtilisateurManager.demander_infos_joueur(self)
           joueur = Joueur(*infos_joueur)
           self.tournoi.joueurs.append(joueur())

    def tri_joueurs_classement_mondial(self):
        """ Cette méthode trie les joueurs en fonction de leur rang
            au classement mondial

        Returns:
            tableau: les joueurs sont triés du rang le plus bas au plus élevé
        """
        for joueur in self.tournoi.joueurs:
            joueurs_triés = sorted(self.tournoi.joueurs, key=lambda joueur: joueur[4])
        return joueurs_triés
    
    def tri_joueurs_points_tournoi(self):
        pass

class UtilisateurManager:
    def demander_infos_joueur(self):
        """ Cette méthode recupère les informations sur chaque joueur avec des inputs

        Returns:
            tableau : la méthode retourne un tableau avec les informations sur chaque joueur
                    qui ont été entrées par les organisateurs du tournoi
        """
        prenom_joueur = input("Quel est le prénom du joueur ?\t")
        nom_joueur = input("Quel est le nom du joueur ?\t")
        date_naissance_joueur = input("Qelle sa date de naissance ? (JJ/MM/AAAA)\t")
        sexe_joueur = input("Quel est son sexe ? (M/F)\t")
        points_mondial_joueur = input("Quel est le total de son nombre de points mondialement ?\t")
        joueur = [prenom_joueur, nom_joueur, date_naissance_joueur, sexe_joueur, int(points_mondial_joueur)]
        return joueur
        


    def ajout_joueurs(self):
        """  Cette méthode demande à l'organisateur du tournoi
            s'il souhaite ajouter un nouveau joueur au tournoi

        Returns:
            tableau: cette méthode renvoie un tableau de plusieurs tableaux 
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
new.creer_tournoi()
ajout = new.ajout_joueurs()
tri = new.tri_joueurs_classement_mondial()
print(tri)
