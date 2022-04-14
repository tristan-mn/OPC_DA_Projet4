from vue import MenuPrincipal, MenuTournoi
from model_tournoi import Tournoi
from model_joueur import Joueur
from model_match import Match
from model_tour import Tour
from datetime import datetime


class TournoiManager:
    def __call__(self):
        self.tours_joués = []
        self.tournoi = Tournoi(*self.demander_infos_tournoi(), joueurs=self.ajout_joueurs(), liste_tours=self.tours_joués)
    


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


    def modifier(self):
        pass

    def sauvegarder(self):
        pass

    def afficher(self):
        print(self.tournoi)

    def ajout_joueurs(self):
        """
        Cette méthode permet de demander les informations sur chaque joueur participant au tournoi
        
        Returns:
            liste:  les informations de chaque joueur sont enregistrées sous forme de liste
                    les joueurs sont ensuite ajoutés au tournoi

        """
        NB_JOUEURS = 2
        liste_joueurs = []

        for i in range(NB_JOUEURS):
           infos_joueur = JoueurManager.demander_infos_joueur(self)
           joueur = Joueur(*infos_joueur)
           liste_joueurs.append(joueur())
        return liste_joueurs


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
        """
        Cette méthode trie les joueurs en fonctions des points qu'ils ont gagnés durant le tournoi

        Returns:
            tableau: les joueurs sont triés du nombre de points le plus faible au plus élevé
        """
        for joueur in self.tournoi.joueurs:
            joueurs_triés = sorted(self.tournoi.joueurs, key=lambda joueur: joueur[5])
        return joueurs_triés
        
    def commencer_premier_tour(self):
        premier_tri = self.tri_joueurs_classement_mondial()
        matchs = MatchManager.creer_premiers_matchs(self, premier_tri)
        self.tours_joués.append()
        return matchs

    def commencer_tour_suivant(self):
        tri_suivant = self.tri_joueurs_points_tournoi(self, tri_suivant)
        matchs = MatchManager.creer_matchs_suivants()
        self.tours_joués.append(matchs)
        return matchs

        
            

    def demander_fin_tour(self):
        fin = input("Le tour est-il terminé ?(oui/non)\t")
        return fin






class MatchManager:
    def __init__(self):
        pass

    def creer_premiers_matchs(self, joueurs_triés):
        """
            Cette méthode permet de créer les 4 matchs pour le premier tour du tournoi

        """
        indice_premier_joueur = 7
        indice_joueur_milieu = 3
        nb_matchs = 4
        matchs = []
        
        for match in range(nb_matchs):
            un_match = Match(joueur1=joueurs_triés[indice_premier_joueur],joueur2=joueurs_triés[indice_joueur_milieu])
            indice_premier_joueur-=1
            indice_joueur_milieu-=1
            matchs.append(un_match)
        return matchs
    
    def creer_matchs_suivants(self, joueurs_triés):
        """
        Cette méthode permet de créer les 4 matchs pour les 3 derniers tours du tournoi

        """
        indice_premier_joueur = 7
        indice_deuxieme_joueur = 6
        nb_matchs = 4
        matchs = []

        for match in range(nb_matchs):
            un_match = Match(joueur1=joueurs_triés[indice_premier_joueur],joueur2=joueurs_triés[indice_deuxieme_joueur])
            indice_premier_joueur-=2
            indice_joueur_milieu-=2
            matchs.append(match)
        return matchs


    def resultat_match(self, joueur1, joueur2):
        """
        Cette méthode permet de demander au responsable du tournoi le resultat de chaque match

        Args:
            joueur1 (str): nom et prenom du premier joueur
            joueur2 (str): nom et prenom du deuxieme joueur
        """
        score_joueur1 = input(f"quel est le score du joueur {joueur1}\t")
        score_joueur2 = input(f"quel est le score du joueur {joueur2}\t")








class JoueurManager:
    def demander_infos_joueur(self):
        """ Cette méthode recupère les informations sur chaque joueur avec des inputs

        Returns:
            tableau : la méthode retourne un tableau avec les informations sur chaque joueur
                    qui ont été entrées par les organisateurs du tournoi
        """
        print()
        print("Veuillez ajouter un joueur au tournoi ...")
        print()
        prenom_joueur = input("Quel est le prénom du joueur ?\t")
        nom_joueur = input("Quel est le nom du joueur ?\t")
        date_naissance_joueur = input("Qelle sa date de naissance ? (JJ/MM/AAAA)\t")
        sexe_joueur = input("Quel est son sexe ? (M/F)\t")
        points_mondial_joueur = input("Quel est le total de son nombre de points mondialement ?\t")
        joueur = [prenom_joueur, nom_joueur, date_naissance_joueur, sexe_joueur, int(points_mondial_joueur)]
        return joueur
        







class RapportManager:
    def rapport_joueurs(self):
        pass

    def rapport_tournois(self):
        pass

tournoi = TournoiManager()
tournoi()
tournoi.commencer_premier_tour()
print(tournoi.tours_joués)