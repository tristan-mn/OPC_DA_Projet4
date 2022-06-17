from os import system, name
import sys
import time


class MenuPrincipal:
    """
    toutes les methodes d'affichage en lien avec menu principal
    """

    def afficher_menuprincipal(self):
        """
        affiche le menu principal
        """
        print()
        print()
        print("#" * 37)
        print("*********  Menu Principal  **********")
        print("#" * 37)
        print("#" * 37)
        print("***   Que souhaitez-vous faire ?  ***\n")

    def choix_menu_principal(self):
        """
        affiche les choix disponibles pour le menu principal
        Returns:
            str: recupere le choix
        """
        choix_fini = False
        while choix_fini is False:
            print()
            print(
                " 1/ Menu Tournoi \n"
                " 2/ Menu Joueur \n"
                " 3/ Quitter le menu principal !\n"
            )
            choix = input("=>\t")
            if choix == "1" or choix == "2" or choix == "3":
                choix_fini = True
        return choix


class NettoyerEcran:
    """Nettoyer le terminal"""

    def __call__(self):
        # pour windows
        if name == "nt":
            _ = system("cls")
        # pour mac et linux(ici, os.name est 'posix')
        else:
            _ = system("clear")


class Quitter:
    def quitter():
        """
        methode pour quitter l'application
        """
        print()
        print()
        print(37 * "*")
        print(37 * "*")
        time.sleep(2)
        print(14 * "*" + "  MERCI  " + 14 * "*")
        time.sleep(2)
        print(12 * "*" + "  AU REVOIR  " + 12 * "*")
        time.sleep(2)
        print(37 * "*")
        print(37 * "*")

        sys.exit()


class MenuJoueur:
    """
    toutes les methodes d'affichage en lien avec le menu des joueurs
    """

    def choix_menu_joueur(self):
        """
        affiche les choix disponibles pour le menu joueur

        Returns:
            str: recupere le choix
        """
        choix_fini = False
        while choix_fini is False:
            print()
            print(
                " 1/ Modifier des informations concernant un joueur \n"
                " 2/ Afficher un rapport \n"
                " 3/ Retourner au Menu Principal ! \n"
            )
            choix = input("=>\t")
            if choix == "1" or choix == "2" or choix == "3":
                choix_fini = True

        return choix

    def ajout_joueur(self):
        """
        affiche la confirmation que le joueur a bien été ajouté
        """
        print()
        print("..... CHARGEMENT .....")
        print()
        time.sleep(1)
        print("Le joueur a bien été ajouté au tournoi.")
        print()


class MenuTournoi:
    """
    toutes les methodes d'affichage en lien avec le menu du tournoi
    """

    def choix_menu_tournoi(self):
        """affiche les choix disponibles pour le menu tournoi

        Returns:
            str: recupere le choix
        """
        choix_fini = False
        while choix_fini is False:
            print()
            print(
                " 1/ Créer un nouveau tournoi \n"
                " 2/ Ajouter des joueurs à un tournoi \n"
                " 3/ Lancer un tournoi \n"
                " 4/ modifier un tournoi \n"
                " 5/ Reprendre un tournoi en cours \n"
                " 6/ Afficher un rapport \n"
                " 7/ Retourner au Menu Principal \n"
            )
            choix = input("=>\t")
            if (
                choix == "1"
                or choix == "2"
                or choix == "3"
                or choix == "4"
                or choix == "5"
                or choix == "6"
                or choix == "7"
            ):
                choix_fini = True

        return choix

    def ajout_infos_tournoi(self):
        """
        demande les informations a lors de la création d'un tournoi

        Returns:
            tableau: retourne un tableau avec
            toutes les informations demandées sur le tournoi
        """
        print()
        print("Création d'un nouveau tournoi")
        print("*" * 10 + " EN COURS " + "*" * 10)
        time.sleep(1)
        nom = self.ajout_nom_tournoi()
        lieu = self.ajout_lieu()
        date = self.ajout_date_tournoi()
        temps = self.ajout_controle_temps()
        description = self.ajout_description()
        return [nom, lieu, date, temps, description]

    def ajout_nom_tournoi(self):
        """
        demande un nom valide pour le tournoi

        Returns:
            str: nom du tournoi
        """
        nom_valide = False
        while nom_valide is False:
            nom_tournoi = input("Quel est le nom du tournoi ? \t")
            if nom_tournoi != "":
                nom_valide = True
            else:
                print()
                print("... ERREUR ...")
                print()
                print("Vous devez entrer un nom au tournoi")
        return nom_tournoi

    def ajout_lieu(self):
        """
        demande un lieu valide pour le tournoi

        Returns:
            str: lieu du tournoi
        """
        lieu_valide = False
        while lieu_valide is False:
            lieu = input("Où se déroule le tournoi ? \t")
            if lieu != "":
                lieu_valide = True
            else:
                print()
                print("... ERREUR ...")
                print()
                print("Vous devez entrer un nom de lieu")
        return lieu

    def ajout_date_tournoi(self):
        """
        demande la date du tournoi au format DD/MM/YYYY

        Returns:
            str: recupere la date du tournoi
        """
        liste_date = []

        jour_valide = False
        while jour_valide is False:
            self.jour = input("Entrez le jour du tournoi: (JJ)\t")
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
        while mois_valide is False:
            self.mois = input("Entrez le mois du tournoi: (MM)\t")
            if self.mois.isdigit() and len(self.mois) == 2 and int(self.mois) < 13:
                mois_valide = True
                liste_date.append(self.mois)
            else:
                print()
                print("... ERREUR ...")
                print()
                print("Vous devez entrer un nombre à 2 chiffres <= 12")

        annee_valid = False
        while annee_valid is False:
            self.annee = input("Entrez l'année du tournoi: (AAAA)\t")
            if self.annee.isdigit() and len(self.annee) == 4:
                annee_valid = True
                liste_date.append(self.annee)
            else:
                print()
                print("... ERREUR ...")
                print()
                print("Veuillez entrer une année à 4 chiffres")

        return f"{liste_date[0]}/{liste_date[1]}/{liste_date[2]}"

    def ajout_controle_temps(self):
        """
        demande quel type de partie va être joué
        pour connaitre le temps défini pour la partie

        Returns:
            str: retourne le nom du type de partie
        """
        print("Choisissez le contrôle du temps:")
        temps_valide = False
        controle_temps = None
        while temps_valide is False:
            choix = input("1.Blitz  2.Bullet  3.Un coup rapide ?\t")
            if choix == "1":
                controle_temps = "Bullet"
                temps_valide = True
            elif choix == "2":
                controle_temps = "Blitz"
                temps_valide = True
            elif choix == "3":
                controle_temps = "Coup rapide"
                temps_valide = True
            else:
                print()
                print("... ERREUR ...")
                print()
                print("Veuillez choisir le contrôle du temps.")
        return controle_temps

    def ajout_description(self):
        """
        demande la description du tournoi

        Returns:
            str: retourne la description du tournoi
        """
        description = input("Entrer une description au tournoi :\t")
        return description

    def ajout_joueurs(self):
        """demande le nom du tournoi dans lequel les joueurs vont être ajoutés

        Returns:
            str: nom du tournoi
        """
        print()
        nom_tournoi = input(
            "Dans quel tournoi voulez-vous ajouter des joueurs ? (nom)\n"
        )
        return nom_tournoi

    def choix_tournoi(self):
        choix_valide = False
        while choix_valide is False:
            choix = input("Quel est le nom du tournoi à lancer ?\t")
            if choix != "":
                choix_valide = True
                break
        return choix


class MenuRapportTournoi:
    """
    toutes les methodes en lien avec les rapports des tournois
    """

    def afficher_menu_rapport_tournoi(self):
        """affiche le menu pour les rapports sur les tournois
           et recupere le choix

        Returns:
            str: recupere le choix
        """
        choix_valide = False
        while choix_valide is False:
            print()
            print(
                "1/ afficher la liste de tous les joueurs d'un tournoi ?\n"
                "2/ afficher la liste de tous les tournois ?\n"
                "3/ afficher la liste de tous les tours d'un tournoi ?\n"
                "4/ afficher la liste de tous les matchs d'un tournoi ?\n"
            )
            choix = input("=>\t")
            if choix == "1" or choix == "2" or choix == "3" or choix == "4":
                choix_valide = True
            else:
                print()
                print(".... ERREUR ....")
                print("Vous devez entrer un nombre entre 1 et 4")
        return choix

    def afficher_liste_joueurs_tournoi(self):
        """
        affichage pour la liste de tous les joueurs d'un seul tournoi
        """
        print("#" * 37)
        print("****** Voici la liste de tous les joueurs du Tournoi ******")
        print("#" * 37 + "\n")

    def afficher_tous_tournois(self):
        """
        affichage pour la liste de tous les tournois
        """
        print("#" * 37)
        print("****** Voici la liste de tous les Tournois ******")
        print("#" * 37 + "\n")

    def afficher_liste_tours_tournoi(self):
        """
        affichage pour la liste de tous les tours d'un tournoi
        """
        print("#" * 37)
        print("****** Voici la liste de tous les tours du Tournoi ******")
        print("#" * 37 + "\n")

    def afficher_liste_matchs_tournoi(self):
        """
        affichage pour la liste de tous les matchs d'un tournoi
        """
        print("#" * 37)
        print("****** Voici la liste de tous les matchs du Tournoi ******")
        print("#" * 37 + "\n")


class MenuRapportJoueur:
    """
    toutes les méthodes d'affichage en lien avec les rapports des joueurs
    """

    def afficher_menu_rapport_joueur(self):
        """affiche le menu pour le menu des rapports sur les joueurs
           et recupere le choix

        Returns:
            str: recupere le choix
        """
        choix_valide = False
        while choix_valide is False:
            print()
            print(
                "1/ afficher le rapport des joueurs par ordre alphabétique ?\n"
                "2/ afficher le rapport des joueurs par ordre mondial ?\n"
                "3/ afficher le rapport d'un seul joueur ?\n"
            )
            choix = input("=>\t")
            if choix == "1" or choix == "2" or choix == "3":
                choix_valide = True
            else:
                print()
                print(".... ERREUR ....")
                print("Vous devez entrer un nombre entre 1 et 3")
        return choix

    def afficher_joueurs_orde_alphabetique(self):
        """
        affichage pour le rapport des joueurs en ordre alphabétique
        """
        print()
        print("#" * 37)
        print("**Voici le rapport des joueurs par ordre alphabétique**")
        print("#" * 37 + "\n")

    def afficher_joueurs_ordre_classement(self):
        """
        affichage pour le rapport des joueurs en ordre de classement mondial
        """
        print()
        print("#" * 37)
        print("***Voici le rapport des joueurs par ordre mondial**")
        print("#" * 37 + "\n")

    def afficher_un_joueur(self):
        """
        affichage pour le rapport d'un seul joueur séléctionné
        """
        print()
        print("#" * 37)
        print("****** Voici le rapport du joueur selectionné ******")
        print("#" * 37 + "\n")


class MenuTour:
    """
    toutes les methodes d'affichage en lien avec le menu des tours
    """

    def commencer_tour(self):
        """
        demande si l'on doit commencer le tour ou non

        Returns:
            str: recupere le choix
        """
        valid_tour = False
        while valid_tour is False:
            print()
            commencer = input("Voulez-vous commencer le tour ? (oui/non)\t")
            if commencer == "oui":
                valid_tour = True
            elif commencer == "non":
                Quitter.quitter()

            else:
                print()
                print("Veuillez repondre par oui ou par non.")
                print()
        return commencer

    def finir_tour(self):
        """
        demande si le tour est terminé

        Returns:
            str: recupere le choix
        """
        valid_tour = False
        while valid_tour is False:
            print()
            finir = input("Le Tour est-il terminé ? (oui/non)\t")
            if finir == "oui":
                valid_tour = True
            elif finir == "non":
                valid_tour = True
            else:
                print()
                print("Veuillez repondre par oui ou par non.")
                print()
        return finir
