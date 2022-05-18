from tkinter import Menu
from unittest import result
from vue import MenuPrincipal, MenuTournoi, MenuJoueur , MenuTour
from model_tournoi import Tournoi
from model_joueur import Joueur
from model_match import Match
from model_tour import Tour
from datetime import datetime
from model_joueur import Joueur
import time



class TournoiManager:
    def __init__(self):
        self.tournoi = None
        self.data = None
        #self.tournoi = Tournoi(*infos_tournoi, joueurs=self.ajout_joueurs())
    
    def __call__(self):
        pass
        # self.infos_tournoi = self.vue_tournoi.ajout_infos_tournoi()
        # self.tournoi = Tournoi(*self.infos_tournoi)
        # self.debut_tournoi = self.lancer_tournoi()
        
    def creer_tournoi(self):
        self.vue_tournoi = MenuTournoi()
        self.tournoi = Tournoi(*self.vue_tournoi.ajout_infos_tournoi())
        self.tournoi.add_to_database(self.tournoi.tournoi_serialized())

    def modifier_tournoi(self):
        pass

    def afficher_tournoi(self):
        """
        Cette méthode affiche les information du tournoi en cours

        """
        print(self.tournoi)

    def ajout_joueurs(self):
        """
        Cette méthode permet de demander les informations sur chaque joueur participant au tournoi
        
        Returns:
            liste:  les informations de chaque joueur sont enregistrées sous forme de liste
                    les joueurs sont ensuite ajoutés au tournoi

        """
        NB_JOUEURS = 8
        liste_joueurs = []
        dict_joueurs = []

        tournoi_choisi = MenuTournoi.ajout_joueurs(self)

        for i in range(NB_JOUEURS):
           infos_joueur = JoueurManager.demander_infos_joueur(self)
           joueur = Joueur(*infos_joueur)
           liste_joueurs.append(joueur())
           dict_joueurs.append(joueur.serialized())
           Joueur.ajout_joueur_database(self, joueur.serialized())
           MenuJoueur.ajout_joueur()
        
        Joueur.ajout_tournoi_database(self, tournoi=tournoi_choisi, joueurs=dict_joueurs)
        
        return liste_joueurs


    def tri_joueurs_classement_mondial(self):
        """ Cette méthode trie les joueurs en fonction de leur rang
            au classement mondial

        Returns:
            tableau: les joueurs sont triés du rang le plus bas au plus élevé
        """
        for joueur in self.tournoi.joueurs:
            joueurs_triés = sorted(self.tournoi.joueurs, reverse=True, key=lambda joueur: joueur[4])
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
        """
        Cette méthode tri les joueurs en fonction de leurs classement mondial avant de créer les matchs

        Returns:
            liste: retourne une liste avec les informations du premier tour
        """

        debut = MenuTour.commencer_tour()
        debut_temps = time.strftime(format("%d/%m/%Y - %Hh%Mm%Ss"))
        premier_tri = self.tri_joueurs_classement_mondial()
        matchs = MatchManager.creer_premiers_matchs(self, premier_tri)
        fin = MenuTour.finir_tour()
        fin_temps = time.strftime(format("%d/%m/%Y - %Hh%Mm%Ss"))
        self.tournoi.liste_tours.append(Tour(date_heure_debut=debut_temps, date_heure_fin=fin_temps, liste_matchs=matchs))

        return matchs


    def commencer_tour_suivant(self):
        """ Cette méthode tri les joueurs en fonction de leurs points accumulés durant le tournoi avant de créer les matchs
        Returns:
            liste: retourne une liste de matchs
        """
        debut = MenuTour.commencer_tour()
        debut_temps = time.strftime(format("%d/%m/%Y - %Hh%Mm%Ss"))
        tri_suivant = self.tri_joueurs_points_tournoi()
        matchs = MatchManager.creer_matchs_suivants(self, tri_suivant)
        fin = MenuTour.finir_tour()
        fin_temps = time.strftime(format("%d/%m/%Y - %Hh%Mm%Ss"))
        self.tournoi.liste_tours.append(Tour(date_heure_debut=debut_temps, date_heure_fin=fin_temps, liste_matchs=matchs))
        return matchs

         
    def lancer_tournoi(self):
        """
        Cette méthode permet de lancer le tournoi Suisse

        """
        NB_TOURS_SUIVANTS = 3
        premiers_matchs = self.commencer_premier_tour()
        resultat_premiers_matchs = MatchManager.resultat_match(self,premiers_matchs)
        self.tournoi.liste_tours.append(resultat_premiers_matchs)
        print(resultat_premiers_matchs)
        for tour in range(NB_TOURS_SUIVANTS):
            matchs_suivants = self.commencer_tour_suivant()
            print(matchs_suivants)
            resultat_tour_suivant = MatchManager.resultat_match(self, matchs_suivants)
            self.tournoi.liste_tours.append(resultat_tour_suivant)



class MatchManager:
    def __init__(self):
        pass

    def creer_premiers_matchs(self, joueurs_triés):
        """
            Cette méthode permet de créer les 4 matchs pour le premier tour du tournoi suisse

        """
        indice_premier_joueur = 7
        indice_joueur_milieu = 3
        nb_matchs = 4
        matchs = []
        
        for un_match in range(nb_matchs):
            un_match = Match(joueur1=joueurs_triés[indice_premier_joueur],joueur2=joueurs_triés[indice_joueur_milieu])
            indice_premier_joueur-=1
            indice_joueur_milieu-=1
            matchs.append(un_match())
        return matchs
    
    def creer_matchs_suivants(self, joueurs_triés):
        """
        Cette méthode permet de créer les 4 matchs pour les 3 derniers tours du tournoi suisse

        """
        indice_premier_joueur = 7
        indice_deuxieme_joueur = 6
        nb_matchs = 4
        matchs = []

        for un_match in range(nb_matchs):
            un_match = Match(joueur1=joueurs_triés[indice_premier_joueur],joueur2=joueurs_triés[indice_deuxieme_joueur])
            indice_premier_joueur-=2
            indice_deuxieme_joueur-=2
            matchs.append(un_match())
        return matchs


    def resultat_match(self, matchs):
        """
        Cette méthode permet de demander au responsable du tournoi le resultat de chaque match

        Args:
            matchs (list): liste de tous les matchs pour chaque tour

        Returns:
            list: liste des matchs avec les score mis à jour
        """

        for match in matchs:
            print("Victoire > 1 point")
            print("Match nul > 0.5 point")
            print("Défaite > 0 point")
            print(match)
            print(f"quel est le score du joueur {match[0][0][0]} {match[0][0][1]}\t")
            score_joueur1 = input("=>\t")
            # ajout des points dans le tuple du match
            match[0][1] += float(score_joueur1)
            # ajout des points dans la liste des infos du joueur
            match[0][0][5] += float(score_joueur1)
            print(f"quel est le score du joueur {match[1][0][0]} {match[1][0][1]}\t")
            score_joueur2 = input("=>\t")
            # ajout des points dans le tuple du match
            match[1][1] += float(score_joueur2)
            # ajout des points dans la liste des infos du joueur
            match[1][0][5] += float(score_joueur2)
            
        return matchs    






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
        classement_mondial = input("Quel est le classement mondial du joueur ?\t")
        # classement_mondial = 5
        joueur = [prenom_joueur, nom_joueur, date_naissance_joueur, sexe_joueur, int(classement_mondial)]
        return joueur
        







class RapportManager:
    def rapport_joueurs(self):
        pass

    def rapport_tournois(self):
        pass
