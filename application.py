from re import A
from turtle import update
from tinydb import where
from vue import MenuRapportJoueur, MenuTournoi, MenuJoueur , MenuTour
from model_tournoi import Tournoi , tournois_database
from model_joueur import Joueur, joueurs_database
from model_match import Match
from model_tour import Tour
from model_joueur import Joueur
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
        #self.tournoi = Tournoi(*infos_tournoi, joueurs=self.ajout_joueurs())
    
    def __call__(self):
        pass
        # self.infos_tournoi = self.vue_tournoi.ajout_infos_tournoi()
        # self.tournoi = Tournoi(*self.infos_tournoi)
        # self.debut_tournoi = self.lancer_tournoi()
        
    def creer_tournoi(self):
        """
        création du tournoi 
        """
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
        recupere le 'heure de début et de fin du tour
        tri les joueurs en fonction de leurs classement mondial avant de créer les matchs

        Returns:
            liste: retourne une liste avec les informations du premier tour
        """

        debut = MenuTour.commencer_tour()
        debut_temps = time.strftime(format("%d/%m/%Y - %Hh%Mm%Ss"))
        premier_tri = self.tri_joueurs_classement_mondial()
        matchs = MatchManager.creer_premiers_matchs(self, premier_tri)
        fin = MenuTour.finir_tour()
        fin_temps = time.strftime(format("%d/%m/%Y - %Hh%Mm%Ss"))
        resultat_premiers_matchs = MatchManager.resultat_match(self, matchs)
        premier_tour = Tour(date_heure_debut=debut_temps, date_heure_fin=fin_temps, liste_matchs=resultat_premiers_matchs, numero_round=1)

        return premier_tour()


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
        resultat_tour_suivant = MatchManager.resultat_match(self, matchs)
        
        round_numero = 2
        tour_suivant = Tour(date_heure_debut=debut_temps, date_heure_fin=fin_temps, liste_matchs=resultat_tour_suivant, numero_round=round_numero)
        round_numero+=1
        return tour_suivant()

        
    def lancer_tournoi(self):
        """
        Cette méthode permet de lancer le tournoi Suisse

        """

        # choix du tournoi 
        gestion_tournoi = TournoiManager()
        choix_tournoi = MenuTournoi.choix_tournoi()
        tournoi = Tournoi(**tournois_database.get(where("nom") == choix_tournoi))
        gestion_tournoi.tournoi = tournoi
        
        nb_tours_suivants = 3
        # modifier le nombre de tour à jouer en soustrayant le nombre de tours joués qui est en paramètre

        #premier tour du tournoi
        premier_tour = gestion_tournoi.commencer_premier_tour()
        gestion_tournoi.tournoi.tours.append(premier_tour)
        gestion_tournoi.tournoi.update_tours(gestion_tournoi.tournoi.tours)
        
        
        # 3 derniers tours du tournoi
        for i in range(nb_tours_suivants):
            tour_suivant = gestion_tournoi.commencer_tour_suivant()
            gestion_tournoi.tournoi.tours.append(tour_suivant)
            gestion_tournoi.tournoi.update_tours(gestion_tournoi.tournoi.tours)



class MatchManager(TournoiManager):
    def __init__(self):
        pass

    def creer_premiers_matchs(self, joueurs_triés):
        """_summary_

        Args:
            joueurs_tri (_type_): _description_

        Returns:
            _type_: _description_
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
        Cette méthode permet de créer les 4 matchs pour les 3 derniers tours du tournoi suisse

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
            list: liste des matchs avec les score mis à jour
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
            
            joueur1 = match_serialized["joueur1"][0] + " " + match_serialized["joueur1"][1]
            joueur2 = match_serialized["joueur2"][0] +  " " + match_serialized["joueur2"][1]

            print(f"quel est le score du joueur {joueur1}\t")
            score_joueur1 = input("=>\t")
            # ajout des points dans les infos du match
            match_serialized["score_joueur1"] += float(score_joueur1)
            # ajout des points dans la liste des infos du joueur
            match_serialized["joueur1"][5] += float(score_joueur1)

                


            print(f"quel est le score du joueur {joueur2}\t")
            score_joueur2 = input("=>\t")
            # ajout des points dans les infos du match
            match_serialized["score_joueur2"] += float(score_joueur2)
            # ajout des points dans la liste des infos du joueur
            match_serialized["joueur2"][5] += float(score_joueur2)

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
            
            for joueur in joueurs:
                if joueur.get("prenom") == match_serialized["joueur1"][0] and joueur.get("nom") == match_serialized["joueur1"][1]:
                    joueur.update({"score": match_serialized["joueur1"][5]})
                elif joueur.get("prenom") == match_serialized["joueur2"][0] and joueur.get("nom") == match_serialized["joueur2"][1]:
                    joueur.update({"score": match_serialized["joueur2"][5]})
                else:
                    pass

            tournois_database.update({"joueurs": joueurs}, where("nom") == self.tournoi.nom)

            print()
            print(vainqueur)
            print()
        
            
        return matchs_serialized    



class JoueurManager:
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
    def lancer_rapport(self):
        """
        lance rapport demandé en invite de commande

        si le nombre 1 est choisi > on affiche tous les joueurs dans l'ordre alphabétique
        si le nombre 2 est choisi > on affiche tous les joueurs dans l'ordre du classement mondial
        si le nombre 3 est choisi > on affiche le joueur demandé

        """
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


class RapportTournoiManager:
    def lancer_rapport(self):
        pass
