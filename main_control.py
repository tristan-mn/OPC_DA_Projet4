import sys

from vue import MenuJoueur, MenuPrincipal, MenuTournoi
from vue import NettoyerEcran
from application import TournoiManager, JoueurManager


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
           JoueurMenuController() 
        elif choix_menu_principal == "2":
            TournoiMenuController
        elif choix_menu_principal == "3":
            QuitterApplication()

class JoueurMenuController(MenuPrincipalController):
    
    def __init__(self):
        super().__init__()
        self.creer_joueur = JoueurManager()
        # self.rapport_joueurs = RapportJoueur()
        self.menu_principal_controller = MenuPrincipalController()

    def __call__(self):
        choix = MenuJoueur.choix_menu_joueur()
        if choix == "1":
            # mettre a jour le classement
            # self.controller_choisi = self
            pass
        elif choix == "2":
            # rapport sur les joueurs
            pass
        elif choix == "3":
            self.controller_choisi = self.menu_principal_controller()



class TournoiMenuController(MenuPrincipalController):
    
    def __init__(self):
        super().__init__()
        self.creer_tournoi = TournoiManager()
        self.rapport_tournoi = TournoiManager()
        self.reprendre_tournoi = TournoiManager() 
        # il faut ajouter les méthodes après les objets

    def __call__(self):
        choix = MenuTournoi.choix_menu_tournoi()
        if choix == "1":
            self.controller_choisi = self.creer_tournoi()
        if choix == "2":
            self.controller_choisi = self.reprendre_tournoi()
        if choix == "3":
            self.controller_choisi = self.rapport_tournoi()
        if choix == "4":
            self.controller_choisi = MenuPrincipalController()


class QuitterApplication:

    def __call__(self):
        sys.exit()