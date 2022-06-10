from tkinter import E, Menu
from types import NoneType
from typing import Type
from tinydb import where
from vues.vue import MenuRapportJoueur, MenuRapportTournoi, MenuTournoi, MenuJoueur , MenuTour
from models.model_tournoi import Tournoi , tournois_database
from models.model_joueur import Joueur, joueurs_database
from models.model_match import Match
from models.model_tour import Tour
from models.model_joueur import Joueur
import time



class TournoiManager():
    """
    Cette classe permet de gérer toutes les méthodes en rapport avec un tournoi
    """
    def __init__(self):
        """
        le constructeur du tournoi
        """
        self.tournoi = None
        self.data = None
    
        
    def creer_tournoi(self):
        """
        méthode pour créer un tournoi
        """
        self.vue_tournoi = MenuTournoi()
        self.tournoi = Tournoi(*self.vue_tournoi.ajout_infos_tournoi())
        self.tournoi.add_to_database(self.tournoi.tournoi_serialized())


    def ajout_joueurs(self):
        """
        Cette méthode permet de demander les informations de chaque joueur participant au tournoi

        on demande d'abord de quel tournoi il s'agit
        on créé une instance de joueur pour chaque joueur avec ses informations
        on ajoute les joueurs au tournoi dans la base de données

        
        Returns:
            liste:  
            une liste des joueurs avec pour chacun une liste de leurs informations

        """
        NB_JOUEURS = 8
        liste_joueurs = []
        dict_joueurs = []
        joueur_manager = JoueurManager()
        menu_joueur = MenuJoueur()
        menu_tournoi =MenuTournoi()

        tournoi_choisi = menu_tournoi.ajout_joueurs()
        try:
            self.tournoi = Tournoi(**tournois_database.get(where("nom") == tournoi_choisi))
        except TypeError:
            print()
            print("Le tournoi ne se trouve pas dans la base de données.")
            print("Veuillez rééssayer")
        else:    
            for i in range(NB_JOUEURS):
                infos_joueur = joueur_manager.ajout_infos_joueur()
                joueur = Joueur(*infos_joueur)
                liste_joueurs.append(joueur())
                dict_joueurs.append(joueur.serialized())
                joueur.ajout_joueur_database(joueur.serialized())
                menu_joueur.ajout_joueur()
        
            self.tournoi.update_joueurs_tournoi_database(tournoi=tournoi_choisi, joueurs=dict_joueurs)


        
        return liste_joueurs


    def tri_joueurs_classement_mondial(self):
        """ Cette méthode trie les joueurs en fonction de leur rang
            au classement mondial

        Returns:
            tableau: les joueurs sont triés du rang le plus bas au plus élevé
        """
        def joueurs_unserialized():
            liste_joueurs = []
            
            for joueur in self.tournoi.joueurs:
                joueur_unserialized = Joueur(**joueur)
                liste_joueurs.append(joueur_unserialized())
            return liste_joueurs
     
        joueurs_triés = sorted(joueurs_unserialized(), reverse=True, key=lambda joueur: joueur[4])
        return joueurs_triés
    

    def tri_joueurs_points_tournoi(self):
        """
        Cette méthode trie les joueurs en fonctions des points qu'ils ont gagnés durant le tournoi

        Returns:
            tableau: les joueurs sont triés du nombre de points le plus faible au plus élevé
        """
        self.tournoi.joueurs = tournois_database.get(where("nom") == self.tournoi.nom)["joueurs"]


        def joueurs_unserialized():
            liste_joueurs = []
            for joueur in self.tournoi.joueurs:
                joueur_unserialized = Joueur(**joueur)
                liste_joueurs.append(joueur_unserialized())
            return liste_joueurs
        
        joueurs_triés = sorted(joueurs_unserialized(), key=lambda joueur: joueur[5])
        return joueurs_triés
        

    def commencer_premier_tour(self):
        """
        Cette méthode lance le premier tour d'un tournoi

        on tri les joueurs selon leurs classement mondial
        on créée les premiers matchs
        on enregistre le temps et la date du début et de la fin du tour
        on demande les résultats des matchs

        Returns:
            dict: on retourne un dictionnaire avec toutes les informations du tour
        """
        gestion_match = MatchManager()
        menu = MenuTour()
        debut = menu.commencer_tour()
        debut_temps = time.strftime(format("%d/%m/%Y - %Hh%Mm%Ss"))
        premier_tri = self.tri_joueurs_classement_mondial()
        matchs = gestion_match.creer_premiers_matchs(premier_tri)
        fin = menu.finir_tour()
        fin_temps = time.strftime(format("%d/%m/%Y - %Hh%Mm%Ss"))
        resultat_premiers_matchs = gestion_match.resultat_match(matchs)
        premier_tour = Tour(date_heure_debut=debut_temps, date_heure_fin=fin_temps, liste_matchs=resultat_premiers_matchs, numero_round=1)

        return premier_tour.serialized()


    def commencer_tour_suivant(self, nb_round):
        """
        Cette méthode lance un tour survenant systématiquement pares le premier tour d'un tournoi

        on tri les joueurs selon leurs points acquis durant le tournoi
        on créée les premiers matchs
        on enregistre le temps et la date du début et de la fin du tour
        on demande les résultats des matchs

        Returns:
            dict: on retourne un dictionnaire avec toutes les informations du tour
        """
        gestion_match = MatchManager()
        menu = MenuTour()
        debut = menu.commencer_tour()
        debut_temps = time.strftime(format("%d/%m/%Y - %Hh%Mm%Ss"))
        tri_suivant = self.tri_joueurs_points_tournoi()
        matchs = gestion_match.creer_matchs_suivants(self, tri_suivant)
        fin = menu.finir_tour()
        fin_temps = time.strftime(format("%d/%m/%Y - %Hh%Mm%Ss"))
        resultat_tour_suivant = gestion_match.resultat_match(self, matchs)
        tour_suivant = Tour(date_heure_debut=debut_temps, date_heure_fin=fin_temps, liste_matchs=resultat_tour_suivant, numero_round=nb_round)
        return tour_suivant.serialized()

        
    def lancer_tournoi(self):
        """

        c'est méthode lance le tournoi

        """

        # choix du tournoi 
        menu_tournoi = MenuTournoi()
        choix_tournoi = menu_tournoi.choix_tournoi()
        # on va chercher le tournoi dans la base de données
        try:
            self.tournoi = Tournoi(**tournois_database.get(where("nom") == choix_tournoi))

        except TypeError:
            print()
            print("Le tournoi ne se trouve pas dans la base de données.")
            print("Veuillez rééssayer")

        else:
            nb_tours_suivants = self.tournoi.nombre_tours

            # on lance le premier tour du tournoi
            try:
                premier_tour = self.commencer_premier_tour()
                self.tournoi.tours.append(premier_tour)
            except TypeError:
                return print("\n Le tournoi ne possède pas de joueurs")
                
            # on met à jour les tours du tournoi dans la base données
            self.tournoi.update_tours(self.tournoi.tours)
            self.tournoi.nombre_tours-=1
            
            
            # 3 derniers tours du tournoi
            numero = 2
            for i in range(self.tournoi.nombre_tours):
                tour_suivant = self.commencer_tour_suivant(nb_round=numero)
                self.tournoi.tours.append(tour_suivant)
                self.tournoi.update_tours(self.tournoi.tours)
                self.tournoi.nombre_tours-=1
                numero+=1
        
    

    def modifier_tournoi(self):
        """
        cette méthode permet de modifier un tournoi séléctionné dans la base données 
        """
        menu_tournoi = MenuTournoi()
        choix_valide = False
        nom_tournoi = input("Quel tournoi voulez-vous modifier ?\t")
        try:
            tournoi = Tournoi(**tournois_database.get(where("nom") == nom_tournoi))
        except TypeError:
            print()
            print("Le tournoi ne se trouve pas dans la base de données.")
            print("Veuillez rééssayer")
        else:    
            print()
            print("Voici vôtre tournoi ")
            print()
            print(tournoi)
            print("1/ nom \n"
                "2/ lieu \n"
                "3/ date \n"
                "4/ temps \n"
                "5/ description \n"
                )
            while choix_valide == False:
                print()
                choix_modification = input("Que voulez-vous modifier ?\t")

                # modification du nom
                if choix_modification == "1":
                    nom = menu_tournoi.ajout_nom_tournoi()
                    tournois_database.update({"nom": nom}, where("nom") == nom_tournoi)
                    print()
                    print("**** modification réussie ****")
                    choix_valide = True

                # modification du lieu
                elif choix_modification == "2":
                    lieu = menu_tournoi.ajout_lieu()
                    tournois_database.update({"lieu": lieu}, where("nom") == nom_tournoi)
                    print() 
                    print("**** modification réussie ****")
                    choix_valide = True

                # modification de la date
                elif choix_modification == "3":
                    date_tournoi = menu_tournoi.ajout_date_tournoi()
                    tournois_database.update({"date": date_tournoi}, where("nom") == nom_tournoi)
                    print()
                    print("**** modification réussie ****")
                    choix_valide = True
                
                # modification du temps de jeu
                elif choix_modification == "4":
                    temps = menu_tournoi.ajout_controle_temps()
                    tournois_database.update({"temps": temps}, where("nom") == nom_tournoi)
                    print()
                    print("**** modification réussie ****")
                    choix_valide = True

                # modification de la description
                elif choix_modification == "5":
                    description = menu_tournoi.ajout_description()
                    tournois_database.update({"description": description}, where("nom") == nom_tournoi)
                    print()
                    print("**** modification réussie ****")
                    choix_valide = True

                else:
                    print("ERREUR ! vous devez rentrer un nombre entre 1 et 5.")


    def reprendre_tournoi(self):
        """
        cette méthode permet de reprendre un tournoi enregistré dans la base de données
        """
        nom_tournoi = input("Quel tournoi voulez-vous reprendre ?\t")
        try:
            self.tournoi = Tournoi(**tournois_database.get(where("nom") == nom_tournoi))
            
        except TypeError:
            return print("\nLe tournoi ne se trouve pas dans la base de données.\n")
            

        nb_tours_suivants = self.tournoi.nombre_tours
        if self.tournoi.nombre_tours == 4:
            print()
            print("Nous vous informons que ce tournoi n'a pas encore commencé")
            print()
            print("Veuillez confirmer le nom du tournoi s'il vous plaît")
            print()
            self.lancer_tournoi()

        else:
            for i in range(nb_tours_suivants):
                tour_suivant = self.commencer_tour_suivant()
                self.tournoi.tours.append(tour_suivant)
                self.tournoi.update_tours(self.tournoi.tours)
                self.tournoi.nombre_tours=-1
            

class MatchManager(TournoiManager):
    """
    cette classe s'occupe de la création des matchs
    elle s'occupe aussi de la gestion des résultats de ces mêmes matchs

    Args:
        TournoiManager (class): classe héritée qui s'occupe de la gestion du tournoi
    """
    def __init__(self):
        pass


    def creer_premiers_matchs(self, joueurs_triés):
        """
        cette méthode créée les matchs du premier tour

        Args:
            joueurs_tri (tableau): un tableau avec les joueurs triés selon leurs classements mondial

        Returns:
            tableau: retourne un tableau des instances de tous les matchs
        """
        indice_premier_joueur = 7
        indice_joueur_milieu = 3
        nb_matchs = 4
        match_numero = 1
        matchs = []
        
        for un_match in range(nb_matchs):
            un_match = Match(joueur1=joueurs_triés[indice_premier_joueur],joueur2=joueurs_triés[indice_joueur_milieu], numero=match_numero)
            match_numero+=1
            indice_premier_joueur-=1
            indice_joueur_milieu-=1
            matchs.append(un_match)
        return matchs
    

    def creer_matchs_suivants(self, joueurs_triés):
        """
        cette méthode créée les matchs du deuxieme au quatrieme tour

        Args:
            joueurs_tri (tableau): un tableau avec les joueurs triés selon leurs points pendant le tournoi

        Returns:
            tableau: retourne un tableau des instances de tous les matchs
        """
        indice_premier_joueur = 7
        indice_deuxieme_joueur = 6
        nb_matchs = 4
        match_numero = 1
        matchs = []

        for un_match in range(nb_matchs):
            un_match = Match(joueur1=joueurs_triés[indice_premier_joueur],joueur2=joueurs_triés[indice_deuxieme_joueur], numero=match_numero)
            match_numero+=1
            indice_premier_joueur-=2
            indice_deuxieme_joueur-=2
            matchs.append(un_match)
        return matchs


    def resultat_match(self, matchs):
        """
        Cette méthode permet de demander au responsable du tournoi le resultat de chaque match

        Args:
            matchs (list): liste de tous les matchs pour chaque tour

        Returns:
            list: liste des matchs avec les scores mis à jour
        """
        matchs_serialized = []
        for match in matchs:
            print("Victoire > 1 point")
            print("Match nul > 0.5 point")
            print("Défaite > 0 point")
            print()
            print(match)
            print

            match_serialized = match.match_serialized()
            
            joueur1 = match_serialized["prenom_joueur1"] + " " + match_serialized["nom_joueur1"]
            joueur2 = match_serialized["prenom_joueur2"] + " " + match_serialized["nom_joueur2"]

            print(f"quel est le score du joueur {joueur1}\t")
            score_joueur1 = input("=>\t")
            # ajout des points dans les infos du match
            match_serialized["score_joueur1"] += float(score_joueur1)



            print(f"quel est le score du joueur {joueur2}\t")
            score_joueur2 = input("=>\t")
            # ajout des points dans les infos du match
            match_serialized["score_joueur2"] += float(score_joueur2)
            
            # ajout des points dans la liste des infos du joueur
            #match_serialized["joueur2"][5] += float(score_joueur2)

            if score_joueur1 == score_joueur2:
                vainqueur = "C'est un match nul"
                match_serialized["vainqueur"] = vainqueur

            elif score_joueur1 > score_joueur2:
                vainqueur = f"Le vainqueur est {joueur1} !"
                match_serialized["vainqueur"] = joueur1

            elif score_joueur1 < score_joueur2:
                vainqueur = f"Le vainqueur est {joueur2} !"
                match_serialized["vainqueur"] = joueur2
            
            
            matchs_serialized.append(match_serialized)

            joueurs = tournois_database.get(where("nom") == self.tournoi.nom)["joueurs"]
            joueurs_modifies = []
            for joueur in joueurs:
                if joueur["prenom"] == match_serialized["prenom_joueur1"] and joueur["nom"] == match_serialized["nom_joueur1"]:
                    joueur["score"] += match_serialized["score_joueur1"]
                    joueurs_modifies.append(joueur)
                elif joueur["prenom"] == match_serialized["prenom_joueur2"] and joueur["nom"] == match_serialized["nom_joueur2"]:
                    joueur["score"] += match_serialized["score_joueur2"]
                    joueurs_modifies.append(joueur)
                else:
                    joueurs_modifies.append(joueur)

            tournois_database.update({"joueurs": joueurs_modifies}, where("nom") == self.tournoi.nom)

            print()
            print(vainqueur)
            print()
        
            
        return matchs_serialized    



class JoueurManager:
    """
    cette classe s'occupe de la gestion des joueurs pendant le tournoi
    """
    def ajout_infos_joueur(self):
        """cette fonction demande dans l'invite de commande les infos d'un joueur

        Returns:
            tableau: un tableau qui rassemble toutes les informations demandées dans les inputs
        """
        prenom = self.ajout_prenom_joueur()
        nom = self.ajout_nom_joueur()
        date_naissance = self.ajout_date_naissance_joueur()
        sexe = self.ajout_sexe_joueur()
        classement = self.ajout_classement_joueur()
        return [prenom, nom, date_naissance, sexe, classement]
    

    def ajout_prenom_joueur(self):
        """demande le prenom du joueur

        Returns:
            str: prenom du joueur
        """
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
        """ demande le nom du joueur

        Returns:
            str: nom du joueur
        """
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
        """demande la date de naissance du joueur

        Returns:
            str: date de naissance au format DD/MM/YYYY
        """
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
        """ demande le sexe du joueur

        Returns:
            str: sexe du joueur au format M ou F
        """
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
        """ demande le classement mondial du joueur

        Returns:
            int: retourne un nombre entre 1 et 100
        """
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
    """
    cette classe s'occupe de la gestion des rapports sur les joueurs d'un tournoi
    """
    def lancer_rapport(self):
        """
        lance le rapport demandé en invite de commande

        si le nombre 1 est choisi > on affiche tous les joueurs dans l'ordre alphabétique
        si le nombre 2 est choisi > on affiche tous les joueurs dans l'ordre du classement mondial
        si le nombre 3 est choisi > on affiche le joueur demandé

        """
        menu_rapport_joueur = MenuRapportJoueur()
        choix = menu_rapport_joueur.afficher_menu_rapport_joueur()
        if choix == "1":

            
            joueurs = joueurs_database.all()
            if joueurs == []:
                return print("\nil n'y a pas de joueurs dans la base de données\n")

            joueurs_tri_alphabetique = sorted(joueurs, key=lambda joueur:joueur['nom'])
            

            menu_rapport_joueur.afficher_joueurs_orde_alphabetique()
            for joueur in joueurs_tri_alphabetique:
                rapport_joueur = Joueur(**joueur)
                print(rapport_joueur)

            
        elif choix == "2":

            joueurs = joueurs_database.all()
            if joueurs == []:
                return print("\nil n'y a pas de joueurs dans la base de données\n")

            joueurs_tri_score = sorted(joueurs, key=lambda joueur: joueur['classement'])

            menu_rapport_joueur.afficher_joueurs_ordre_classement()
            for joueur in joueurs_tri_score:
                rapport_joueur = Joueur(**joueur)
                print(rapport_joueur)

        elif choix == "3":
            # recherche par nom et prenom
            print()
            prenom = input("Quel est le prenom du joueur ?\t")
            nom = input("Quel est le nom du joueur ?\t")

            # on vérifie que le joueur se trouve bien dans la base de données
            try:
                joueur = Joueur(**joueurs_database.get(where("nom") == nom and where("prenom") == prenom))
            except TypeError:
                return print("\nLe joueur ne se trouve pas dans la base de données.\n")

            
            print()
            menu_rapport_joueur.afficher_un_joueur()
            print()
            print(joueur)


class RapportTournoiManager:
    def lancer_rapport(self):
        menu_rapport_tournoi = MenuRapportTournoi()
        choix = menu_rapport_tournoi.afficher_menu_rapport_tournoi()
        if choix == "1":
            print()
            nom_tournoi = input("Vous voulez la liste des joueurs de quel tournoi ?\t")
            print()

            # on vérifie que le tournoi se trouve bien dans la base de données
            try:
                tournoi_unserialized = Tournoi(**tournois_database.get(where("nom") == nom_tournoi))
            except TypeError:
                return print("\nLe tournoi ne se trouve pas dans la base de données\n")
                

            joueurs = tournoi_unserialized.joueurs

            choix_valide = False
            while choix_valide == False:
                menu_tri = print("1/ trier les joueurs par ordre alphabétique\n"
                                "2/ trier les joueurs par classement mondial\n")
                print()
                choix_tri = input("=>\t")

                # on trie les joueurs par ordre alphabétique
                if choix_tri == "1":
                    choix_valide = True
                    try:
                        joueurs_tri_alphabetique = sorted(joueurs, key=lambda joueur:joueur['nom'])
                        tournoi_unserialized.joueurs = []
                        for joueur in joueurs_tri_alphabetique:
                            joueur_serialized = Joueur(**joueur)
                            tournoi_unserialized.joueurs.append(joueur_serialized)
                    except TypeError:
                        return print("\nil n'y a pas encore de joueurs dans le tournoi\n")
                        

                # on trie les joueurs selon leurs classements mondial
                elif choix_tri == "2":
                    choix_valide = True
                    try:
                        joueurs_tri_score = sorted(joueurs, key=lambda joueur: joueur['classement'])
                        tournoi_unserialized.joueurs = []
                        for joueur in joueurs_tri_score:
                            joueur_serialized = Joueur(**joueur)
                            tournoi_unserialized.joueurs.append(joueur_serialized)
                    except TypeError:
                        return print("\nil n'y a pas encore de joueurs dans le tournoi\n")


                menu_rapport_tournoi.afficher_liste_joueurs_tournoi()
                tournoi_unserialized.afficher_joueurs()

        elif choix == "2":
            # on affiche les rapports de tous les tournois de la base de données

            tournois_unserialized = []
            tournois = tournois_database.all()
            numero = 1

            for tournoi in tournois:
                # on commence par désérializer tous les tournois
                tournoi_unserialized = Tournoi(**tournoi)
                # on récupère les joueurs pour les désérializer
                joueurs = tournoi_unserialized.joueurs
                # on récupère les tours pour les désérializer
                tours = tournoi_unserialized.tours

                tournoi_unserialized.joueurs = []
                tournoi_unserialized.tours = []
                try:
                    for joueur in joueurs:
                        # on désérialize
                        joueur_serialized = Joueur(**joueur)
                        tournoi_unserialized.joueurs.append(joueur_serialized)
                except:
                    print()
                    print("Le tournoi ne possède pas encore de joueurs")
                    print()
                try:
                    for tour in tours:
                        # on désérialize
                        tour_serialized = Tour(**tour, numero_round=numero)
                        numero+=1
                        tournoi_unserialized.tours.append(tour_serialized)
                except:
                    print()
                    print("Le tournoi ne possède pas encore de tour")
                    print()
                    
                tournois_unserialized.append(tournoi_unserialized)

            menu_rapport_tournoi.afficher_tous_tournois()
            for tournoi in tournois_unserialized:
                # on affiche tous les tournois dans l'invite de commande
                tournoi.afficher_tournoi()

        elif choix == "3":
            print()
            nom_tournoi = input("Vous voulez la liste des tours de quel tournoi ?\t")
            print()
            
            # on vérifie que le tournoi se trouve bien dans la base de données
            try:
                tournoi_unserialized = Tournoi(**tournois_database.get(where("nom") == nom_tournoi))
            except TypeError:
                return print("\nLe tournoi ne se trouve pas dans la base de données\n")
            
            tours = tournoi_unserialized.tours
            tournoi_unserialized.tours = []
            
            numero = 1
            for tour in tours:
                tour_serialized = Tour(**tour, numero_round=numero)
                numero+=1
                tournoi_unserialized.tours.append(tour_serialized)
            
            menu_rapport_tournoi.afficher_liste_tours_tournoi()
            # on affiche tous les tours d'un tournoi
            tournoi_unserialized.afficher_tours()
            

        elif choix == "4":
            print()
            nom_tournoi = input("Vous voulez la liste des matchs de quel tournoi ?\t")
            print()

            # on vérifie que le tournoi se trouve bien dans la base de données
            try:
                tournoi_unserialized = Tournoi(**tournois_database.get(where("nom") == nom_tournoi))
            except TypeError:
                return print("\nLe tournoi ne se trouve pas dans la base de données\n")
        
            tours = tournoi_unserialized.tours
            tournoi_unserialized.tours = []
            
            for tour in tours:
                tour_serialized = Tour(**tour)
                tournoi_unserialized.tours.append(tour_serialized)

            menu_rapport_tournoi.afficher_liste_matchs_tournoi()
            # on affiche tous les matchs d'un tournoi
            tournoi_unserialized.afficher_matchs()
                


class ModifierJoueur(JoueurManager):
    """
    cette s'occupe de la gestion de la modification des informations des joueurs 

    Args:
        JoueurManager (class): class héritée qui s'occupe de la gestion des joueurs pendant le tournoi
    """
    def __init__(self):
        """
        modelisation de l'instance avec le tournoi, les joueurs du tournoi et le joueur à modifier
        """
        self.tournoi = None
        self.joueur = None
        self.joueurs_tournoi = None
        
    def __call__(self):
        choix_joueur = self.choix_joueur()
        if choix_joueur == None:
            return print()
        else:
            modification = self.choix_modification()

    def choix_joueur(self):
        """
        cette méthode demande le nom et le prenom du joueur à modifier
        elle demande le nom du tournoi où se trouve le joueur

        Returns:
            _type_: _description_
        """
        print()
        prenom_joueur = input("Quel est le prenom du joueur à modifier?\t")
        nom_joueur = input("Quel est le nom du joueur à modifier?\t")
        print()

        choix_tournoi = input("Dans quel tournoi se trouve le joueur?\t")
        self.tournoi = tournois_database.get(where("nom") == choix_tournoi)

        if self.tournoi == None:
            return print("\nle tournoi ne se trouve pas dans la base de données.\n")
        else:    
            self.joueurs_tournoi = self.tournoi["joueurs"]


        def chercher(joueurs):
            """
            cette fonction va parcourir tous les joueurs du tournoi 
            pour verifier si le joueur demandé s'y trouve

            Args:
                joueurs (liste): liste de dictionnnaires représentant les joueurs du tournoi

            Returns:
                dict: retourne le dictionnaire du joueur demandé
            """
            try:
                for joueur in joueurs:
                    if joueur["prenom"] == prenom_joueur and joueur["nom"] == nom_joueur:
                        print("\nVoici le joueur demandé:\n")
                        afficher = print(Joueur(**joueur))
                        return joueur
                print("le joueur ne fait pas partie du tournoi")
            except TypeError:
                return print("\nLe tournoi ne possède pas de joueurs\n")

        self.joueur = chercher(joueurs=self.joueurs_tournoi)


    def choix_modification(self):
        """
        demande quelle information du joueur à modifier
        """
        choix_valid = False
        while choix_valid ==False:
            print("1/ Prenom\n"
                  "2/ Nom\n"
                  "3/ date de naissance\n"
                  "4/ sexe\n"
                  "5/ classement\n")

            choix = input("Que voulez-vous modifier concernant le joueur ?\t")

            if choix == "1":
                self.modifier_prenom()
                choix_valid = True

            elif choix == "2":
                self.modifier_nom()
                choix_valid = True

            elif choix == "3":
                self.modifier_date_naissance()
                choix_valid = True

            elif choix == "4":
                self.modifier_sexe()
                choix_valid = True

            elif choix == "5":
                self.modifier_classement()
                choix_valid = True

            else:
                print("\nERREUR: vous devez rentrer un nombre entre 1 et 5.\n")


    def modifier_prenom(self):
        print("\nVoici l'ancien prenom:\n")
        print(self.joueur["prenom"])

        ancien_joueur = self.joueur
        nouveau_prenom = self.ajout_prenom_joueur()
        

        for joueur in self.joueurs_tournoi:
            if joueur == ancien_joueur:
                joueur["prenom"] = nouveau_prenom
        
        tournois_database.update({"joueurs": self.joueurs_tournoi}, where("nom") == self.tournoi["nom"])

        print("...")
        time.sleep(2)
        print("Bavo ! Le joueur à bien été modifié !")

        
    def modifier_nom(self):
        print("\nVoici l'ancien nom:\n")
        print(self.joueur["nom"])

        ancien_joueur = self.joueur
        nouveau_nom = self.ajout_nom_joueur()
        

        for joueur in self.joueurs_tournoi:
            if joueur == ancien_joueur:
                joueur["nom"] = nouveau_nom
        
        tournois_database.update({"joueurs": self.joueurs_tournoi}, where("nom") == self.tournoi["nom"])

        print("...")
        time.sleep(2)
        print("Bavo ! Le joueur à bien été modifié !")


    def modifier_date_naissance(self):
        print("\nVoici l'ancienne date de naissance:\n")
        print(self.joueur["date_naissance"])

        ancien_joueur = self.joueur
        nouvelle_date = self.ajout_date_naissance_joueur()
        

        for joueur in self.joueurs_tournoi:
            if joueur == ancien_joueur:
                joueur["date_naissance"] = nouvelle_date
        
        tournois_database.update({"joueurs": self.joueurs_tournoi}, where("nom") == self.tournoi["nom"])

        print("...")
        time.sleep(2)
        print("Bavo ! Le joueur à bien été modifié !")


    def modifier_sexe(self):
        print("\nVoici l'ancien sexe:\n")
        print(self.joueur["sexe"])

        ancien_joueur = self.joueur
        nouveau_sexe = self.ajout_sexe_joueur()
        

        for joueur in self.joueurs_tournoi:
            if joueur == ancien_joueur:
                joueur["sexe"] = nouveau_sexe
        
        tournois_database.update({"joueurs": self.joueurs_tournoi}, where("nom") == self.tournoi["nom"])

        print("...")
        time.sleep(2)
        print("Bavo ! Le joueur à bien été modifié !")
        

    def modifier_classement(self):
        print("\nVoici l'ancien classement:\n")
        print(self.joueur["classement"])

        ancien_joueur = self.joueur
        nouveau_classement = self.ajout_classement_joueur()
        

        for joueur in self.joueurs_tournoi:
            if joueur == ancien_joueur:
                joueur["classement"] = nouveau_classement
        
        tournois_database.update({"joueurs": self.joueurs_tournoi}, where("nom") == self.tournoi["nom"])

        print("...")
        time.sleep(2)
        print("Bavo ! Le joueur à bien été modifié !")