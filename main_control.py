import sys

from vue import MenuJoueur, MenuPrincipal, MenuTournoi
from vue import NettoyerEcran
from application import RapportJoueurManager, RapportTournoiManager, TournoiManager, JoueurManager


class MenuPrincipalController:
    def __init__(self):
        self.vue = MenuPrincipal()
        self.nettoyer = NettoyerEcran()
        self.controller_choisi = None
    
    def __call__(self):
        self.nettoyer()
        self.vue.afficher_menuprincipal()
        choix_menu_principal = self.vue.choix_menu_principal()

        if choix_menu_principal == "1":
            self.controller_choisi = TournoiMenuController()
            self.controller_choisi()
        elif choix_menu_principal == "2":
            self.controller_choisi = JoueurMenuController()
            self.controller_choisi()
        elif choix_menu_principal == "3":
            self.controller_choisi = QuitterApplication()
            self.controller_choisi()



class JoueurMenuController(MenuPrincipalController):
    
    def __init__(self):
        super().__init__()
        self.creer_joueur = JoueurManager()
        # self.rapport_joueurs = RapportJoueur()
        self.menu_principal_controller = MenuPrincipalController()

    def __call__(self):
        choix = MenuJoueur.choix_menu_joueur(self)
        if choix == "1":
            # mettre a jour le classement
            # self.controller_choisi = self
            pass
        elif choix == "2":
            self.controller_choisi = RapportJoueurManager.lancer_rapport(self)
            
        elif choix == "3":
            self.controller_choisi = self.menu_principal_controller()



class TournoiMenuController(MenuPrincipalController):

    def __call__(self):
        choix = ""
        while choix != "7":
            choix = MenuTournoi.choix_menu_tournoi()
            if choix == "1":
                self.controller_choisi = TournoiManager.creer_tournoi(self)

            elif choix == "2":
                self.controller_choisi = TournoiManager.ajout_joueurs(self)

            elif choix == "3":
                self.controller_choisi = TournoiManager.lancer_tournoi(self)

            elif choix == "4":
                self.controller_choisi = TournoiManager.modifier_tournoi(self)

            elif choix == "5":
                self.controller_choisi = TournoiManager.reprendre_tournoi(self)

            elif choix == "6":
                self.controller_choisi = RapportTournoiManager.lancer_rapport(self)

            elif choix == "7":
                self.controller_choisi = MenuPrincipalController()
            
            else:
                print()
                print("... ERREUR ...")
                print(" Vous devez faire un choix entre 1 et 7.")


class QuitterApplication:

    def __call__(self):
        sys.exit()