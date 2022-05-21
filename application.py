from multiprocessing.sharedctypes import Value
from tkinter import Menu
from unittest import result

from tinydb import where
from vue import MenuPrincipal, MenuRapportJoueur, MenuRapportTournoi, MenuTournoi, MenuJoueur , MenuTour
from model_tournoi import Tournoi
from model_joueur import Joueur, joueurs_database
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
        joueur_manager = JoueurManager()

        tournoi_choisi = MenuTournoi.ajout_joueurs(self)

        for i in range(NB_JOUEURS):
            infos_joueur = joueur_manager.ajout_infos_joueur()
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

        
    def lancer_tournoi(self, tour):
        """
        Cette méthode permet de lancer le tournoi Suisse

        """
        nb_tours_suivants = 3
        # modifier le nombre de tour à jouer en soustrayant le nombre de tours joués qui est en paramètre
        premiers_matchs = self.commencer_premier_tour()
        resultat_premiers_matchs = MatchManager.resultat_match(self,premiers_matchs)
        self.tournoi.liste_tours.append(resultat_premiers_matchs)
        print(resultat_premiers_matchs)
        for tour in range(nb_tours_suivants):
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
    def ajout_infos_joueur(self):
        prenom = self.ajout_prenom_joueur()
        nom = self.ajout_nom_joueur()
        date_naissance = self.ajout_date_naissance_joueur()
        sexe = self.ajout_sexe_joueur()
        classement = self.ajout_classement_joueur()
        return [prenom, nom, date_naissance, sexe, classement]
    

    def ajout_prenom_joueur(self):
        prenom_valide = False
        while prenom_valide == False:
            prenom_joueur = input("Quel est le prénom du joueur ?\t")
            if prenom_joueur != "":
                prenom_valide = True
                break
            else:
                print()
                print("... ERREUR ...")
                print()
                print("Vous devez entrer un prenom.")
        return prenom_joueur
                
                
    def ajout_nom_joueur(self):
        nom_valide = False
        while nom_valide == False:
            nom_joueur = input("Quel est le nom du joueur ?\t")
            if nom_joueur != "":
                nom_valide = True
                break
            else:
                print()
                print("... ERREUR ...")
                print()
                print("Vous devez entrer un nom.")
        return nom_joueur
                
                
    def ajout_date_naissance_joueur(self):
        liste_date = []
        jour_valide = False
        
        while jour_valide == False:
            self.jour = input("Entrez le jour de naissance: (JJ)\t")
            if self.jour.isdigit() and len(self.jour) == 2 and int(self.jour) < 32:
                jour_valide = True
                liste_date.append(self.jour)
                break
            else:
                print()
                print("... ERREUR ...")
                print()
                print("Vous devez entrer un nombre à 2 chiffres <= 31")
                
        mois_valide = False
        while mois_valide == False:
            self.mois = input("Entrez le mois de naissance: (MM)\t")
            if self.mois.isdigit() and len(self.mois) == 2 and int(self.mois) < 13:
                mois_valide = True
                liste_date.append(self.mois)
                break
            else:
                print()
                print("... ERREUR ...")
                print()
                print("Vous devez entrer un nombre à 2 chiffres <= 12")
        
        annee_valid = False
        while annee_valid == False:
            self.annee = input("Entrez l'année de naissance: (AAAA)\t")
            if self.annee.isdigit() and len(self.annee) == 4:
                annee_valid = True
                liste_date.append(self.annee)
                break
            else:
                print()
                print("... ERREUR ...")
                print()
                print("Veuillez entrer une année à 4 chiffres")

        return f"{liste_date[0]}/{liste_date[1]}/{liste_date[2]}"
        
        
    def ajout_sexe_joueur(self):
        sexe_valide = False
        while sexe_valide == False:
            sexe_joueur = input("Quel est son sexe ? (M/F)\t")
            if sexe_joueur == "M" or sexe_joueur == "F":
                sexe_valide = True
                break
            else:
                print()
                print("... ERREUR ...")
                print()
                print("Vous devez entrer M pour masculin ou F pour Féminin.")
        return sexe_joueur
    
    
    def ajout_classement_joueur(self):
        classement_valide = False
        while classement_valide == False:
            classement_joueur = int(input("Quel est le classement mondial du joueur ? (1 --> 100)\t"))
            if classement_joueur >= 1 and classement_joueur <= 100:
                classement_valide = True
                break
            else:
                print()
                print("... ERREUR ...")
                print()
                print("Vous devez entrer un nombre entre 1 et 100.")
        return classement_joueur
        


class RapportJoueurManager:
    def lancer_rapport(self):
        menu_rapport_joueur = MenuRapportJoueur()
        choix = menu_rapport_joueur.afficher_menu_rapport_joueur()
        if choix == "1":
            # alphabetique
            menu_rapport_joueur.afficher_joueurs_orde_alphabetique()
            joueurs = joueurs_database.all()
            joueurs_tri_alphabetique = sorted(joueurs, key=lambda joueur:joueur['nom'])
            print()

            for joueur in joueurs_tri_alphabetique:
                rapport_joueur = Joueur(**joueur)
                print(rapport_joueur)

            
        elif choix == "2":
            # classement
            menu_rapport_joueur.afficher_joueurs_ordre_classement()

            joueurs = joueurs_database.all()
            joueurs_tri_score = sorted(joueurs, key=lambda joueur: joueur['classement'])
            print()

            for joueur in joueurs_tri_score:
                rapport_joueur = Joueur(**joueur)
                print(rapport_joueur)

        elif choix == "3":
            # recherche par nom et prenom
            print()
            prenom = input("Quel est le prenom du joueur ?\t")
            nom = input("Quel est le nom du joueur ?\t")
            joueur = Joueur(**joueurs_database.get(where("nom") == nom and where("prenom") == prenom))
            print()
            menu_rapport_joueur.afficher_un_joueur()
            print()
            print(joueur)

    def rapport_joueurs(self):
        pass

class RapportTournoiManager:
    def lancer_rapport(self):
        pass
