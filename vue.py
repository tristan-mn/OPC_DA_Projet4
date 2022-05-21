from os import system, name


class MenuPrincipal:
    def afficher_menuprincipal(self):
        print()
        print("#" * 37)
        print("*********  Menu Principal  **********")
        print("#" * 37)
        print("#" * 37)
        print("***   Que souhaitez-vous faire ?  ***\n")

    def choix_menu_principal(self):
        choix_fini = False
        while choix_fini == False:
            print()
            print(" 1/ Menu Tournoi \n"
                  " 2/ Menu Joueur \n"
                  " 3/ Quitter le menu principal !\n")
            choix = input("=>\t")
            if choix == "1" or choix == "2" or choix == "3":
                choix_fini = True
        return choix

class NettoyerEcran:
    """Nettoyer le terminal"""
    def __call__(self):
        # pour windows
        if name == 'nt':
            _ = system('cls')
        # pour mac et linux(ici, os.name est 'posix')
        else:
            _ = system('clear')


class MenuJoueur:
    def choix_menu_joueur(self):
        choix_fini = False
        while choix_fini == False:
            print()
            print(" 1/ Mettre à jour le classement des joueurs \n"
                  " 2/ Afficher un rapport \n"
                  " 3/ Retourner au Menu Principal ! \n")
            choix = input("=>\t")
            if choix == "1" or choix == "2" or choix == "3":
                choix_fini = True
                break

        return choix

    def ajout_joueur():
        print()
        print("..... CHARGEMENT .....")
        print()
        print("Le joueur a bien été ajouté au tournoi.")
        print()



class MenuTournoi:
    def choix_menu_tournoi():
        choix_fini = False
        while choix_fini == False:
            print()
            print(" 1/ Créer un nouveau tournoi \n"
                  " 2/ Ajouter des joueurs au tournoi \n"
                  " 3/ Lancer le tournoi \n"
                  " 4/ modifier le tournoi \n"
                  " 5/ Reprendre un tournoi en cours \n"
                  " 6/ Afficher un rapport \n"
                  " 7/ Retourner au Menu Principal \n")
            choix = input("=>\t")
            if choix == "1" or choix == "2" or choix == "3" or choix == "4" or choix == "5" or choix == "6" or choix == "7":
                choix_fini = True
                break

        return choix

    def ajout_infos_tournoi(self):
        print()
        print("Création d'un nouveau tournoi")
        print("*"*10 + " EN COURS " + "*"*10)
        nom = self.ajout_nom_tournoi()
        lieu = self.ajout_lieu()
        date = self.ajout_date_tournoi()
        temps = self.ajout_controle_temps()
        description = self.ajout_description()
        return nom, lieu, date, temps, description
    
    def ajout_nom_tournoi(self):
        nom_valide = False
        while nom_valide == False:
            nom_tournoi = input("Quel est le nom du tournoi ? \t")
            if nom_tournoi != "":
                nom_valide = True
                break
            else:
                print()
                print("... ERREUR ...")
                print()
                print("Vous devez entrer un nom au tournoi")
        return nom_tournoi
    
    def ajout_lieu(self):
        lieu_valide = False
        while lieu_valide == False:
            lieu = input("Où se déroule le tournoi ? \t")
            if lieu != "":
                lieu_valide = True
                break
            else:
                print()
                print("... ERREUR ...")
                print()
                print("Vous devez entrer un nom de lieu")
        return lieu
    
    def ajout_date_tournoi(self):
        liste_date = []

        jour_valide = False
        while jour_valide == False:
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
        while mois_valide == False:
            self.mois = input("Entrez le mois du tournoi: (MM)\t")
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
            self.annee = input("Entrez l'année du tournoi: (AAAA)\t")
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

    def ajout_controle_temps(self):
        print("Choisissez le contrôle du temps:")
        temps_valide = False
        controle_temps = None
        while temps_valide == False:
            choix = input("1.Blitz  2.Bullet  3.Un coup rapide ?\t")
            if choix == "1":
                controle_temps = "Bullet"
                temps_valide = True
                break
            elif choix == "2":
                controle_temps = "Blitz"
                temps_valide = True
                break
            elif choix == "3":
                controle_temps = "Coup rapide"
                temps_valide = True
                break
            else:
                print()
                print("... ERREUR ...")
                print()
                print("Veuillez choisir le contrôle du temps.")
        return controle_temps

    def ajout_description(self):
        description = input("Entrer une description au tournoi :\t")
        return description

    def ajout_joueurs(self):
        nom_tournoi = input("Dans quel tournoi voulez-vous ajouter des joueurs ? (nom du tournoi)\n")
        return nom_tournoi


    def continuer_tournoi():
        print()
        print("Nous reprenons le tournoi en cours\n")

    
    def retour_menu_principal():
        print()
        print("Vous êtes de retour au menu principal !\n")


class MenuTempsPartie:
    def menu_temps_partie():
        print()
        print(" 1/ Bullet \n"
              " 2/ Blitz \n"
              " 3/ Coup rapide \n")
        choix = input("=>\t")
        return choix

class MenuRapportTournoi:
    def afficher_menu_rapport_tournoi():
        choix_valide = False
        while choix_valide == False:
            print()
            print("1/ Voulez-vous afficher le rapport d'un tournoi ?\n"
                  "2/ Voulez-vous afficher le rapport de tous les tournois\n" )
            choix = input("=>\t")
            if choix == "1" or choix == "2":
                choix_valide = True
                break
        return choix

    def afficher_un_tournoi():
        print("#" * 37)
        print("****** Voici le rapport du Tournoi ******") 
        print("#" * 37)

    def afficher_tous_tournois():
        print("#" * 37)
        print("****** Voici le rapport des Tournois ******") 
        print("#" * 37)


class MenuRapportJoueur:
    def afficher_menu_rapport_joueur(self):
        choix_valide = False
        while choix_valide == False:
            print()
            print("1/ Voulez-vous afficher le rapport des joueurs par ordre alphabétique ?\n"
                  "2/ Voulez-vous afficher le rapport des joueurs par ordre dans le classement mondial ?\n" 
                  "3/ Voulez-vous afficher le rapport d'un seul joueur ?\n" )
            choix = input("=>\t")
            if choix == "1" or choix == "2" or choix == "3":
                choix_valide = True
                break
            else:
                print()
                print(".... ERREUR ....")
                print("Vous devez entrer un nombre entre 1 et 3")
        return choix

    def afficher_joueurs_orde_alphabetique(self):
        print()
        print("#" * 37)
        print("****** Voici le rapport des joueurs par ordre alphabétique ******") 
        print("#" * 37)

    def afficher_joueurs_ordre_classement(self):
        print()
        print("#" * 37)
        print("****** Voici le rapport des joueurs par ordre dans le classement mondial ******") 
        print("#" * 37)

    def afficher_un_joueur(self):
        print()
        print("#" * 37)
        print("****** Voici le rapport du joueur selectionné ******") 
        print("#" * 37)



class MenuTour:
    def commencer_tour():
        valid_tour = False
        while valid_tour == False:
            commencer = input("Voulez-vous commencer le tour ? (oui/non)\t")
            if commencer == "oui":
                valid_tour = True
                break
            elif commencer == "non":
                valid_tour = True
                break
            else:
                print()
                print("Veuillez repondre par oui ou par non.")
                print()
        return commencer

    def finir_tour():
        valid_tour = False
        while valid_tour == False:
            finir = input("Le Tour est-il terminé ? (oui/non)\t")
            if finir == "oui":
                valid_tour = True
                break
            elif finir == "non":
                valid_tour = True
                break
            else:
                print()
                print("Veuillez repondre par oui ou par non.")
                print()
        return finir


    


