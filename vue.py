
class MenuPrincipal:
    def afficher_menuprincipal(self):
        print()
        print("#" * 37)
        print("*********  Menu Principal  **********")
        print("#" * 37)
        print("#" * 37)
        print("***   Que souhaitez-vous faire ?  ***\n")

    def choix_menu_principal(self):
        print()
        print(" 1/ Menu Tournoi \n"
              " 2/ Menu Joueur \n"
              " 3/ Quitter le menu principal !\n")
        choix = input("=>\t")
        return choix


class MenuJoueur:
    def menu_joueur(self):
        print()
        print(" 1/ Ajouter un joueur \n"
              " 2/ Mettre à joueur le classement du joueur \n"
              " 3/ Afficher informations joueurs \n"
              " 4/ Retourner au Menu Principal ! \n")
        choix = input("=>\t")
        return choix

    def ajout_joueur(self):
        print()
        print("Le joueur a bien été ajouté au tournoi.")

    def menu_informations_joueur(self):
        print()
        print(" 1/ Afficher les joueurs par ordre alphabétique \n"
              " 2/ Afficher classement mondial des joueurs par points \n"
              " 3/ Retourner au Menu Principal \n")
        choix = input("=>\t")
        return choix
    
    def menu_classement_alphabetique_joueur(self):
        print()
        print("Voici le classement des joueurs par ordre alphabétique.\n")

    def menu_classement_points_joueur(self):
        print()
        print("Voici le classement des joueurs par ordre de points.\n")


class MenuTournoi:
    def menu_tournoi(self):
        print()
        print(" 1/ Créer un nouveau tournoi \n"
              " 2/ Reprendre un tournoi en cours \n"
              " 3/  Afficher informations tournoi \n"
              " 4/ Retourner au Menu Principal \n")
        choix = input("=>\t")
        return choix

    def creer_tournoi(self):
        print()
        print("Création d'un nouveau tournoi")
        print("*"*10 + " EN COURS " + "*"*10)

    def continuer_tournoi(self):
        print()
        print("Nous reprenons le tournoi en cours\n")

    def afficher_informations_tournoi(self):
        print()
        print("Voici tous les tournois enregistrés : \n")

    def menu_informations_tous_tournois(self):
        print()
        print("1/ Afficher tous les tournois \n"
              "2/ Choisir un tournoi \n"
              "3/ Retourner au Menu Principal \n")
        choix = input("=>\t")
        return choix

    def menu_informations_un_tournoi(self):
        print()
        print(" 1/ Afficher les joueurs \n"
              " 2/ Afficher les tours \n"
              " 3/ Afficher les matchs \n"
              " 4/ Retour au Menu Principal \n")
        choix = input("=>\t")
        return choix
    
    def retour_menu_principal(self):
        print()
        print("Vous êtes de retour au menu principal !\n")


class MenuTempsPartie:
    def menu_temps_partie(self):
        print()
        print(" 1/ Bullet \n"
              " 2/ Blitz \n"
              " 3/ Coup rapide \n")
        choix = input("=>\t")
        return choix

    def afficher_bullet(self):
        pass
    def afficher_blitz(self):
        pass
    def afficher_coup_rapide(self):
        pass


    


