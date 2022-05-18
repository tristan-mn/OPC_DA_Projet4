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
            # rapport sur les joueurs
            pass
        elif choix == "3":
            self.controller_choisi = self.menu_principal_controller()



class TournoiMenuController(MenuPrincipalController):
    
    # def __init__(self):
    #     super().__init__()
    #     self.creer_tournoi = TournoiManager.creer_tournoi()
    #     self.ajout_joueurs = TournoiManager.ajout_joueurs(self)
    #     self.commencer_tournoi = TournoiManager()
    #     self.modifier_tournoi = TournoiManager()
    #     self.reprendre_tournoi = TournoiManager() 
    #     self.rapport_tournoi = TournoiManager()
        # il faut ajouter les méthodes après les objets

    def __call__(self):
        choix = ""
        while choix != "7":
            choix = MenuTournoi.choix_menu_tournoi()
            if choix == "1":
                self.controller_choisi = TournoiManager.creer_tournoi(self)
            if choix == "2":
                self.controller_choisi = TournoiManager.ajout_joueurs(self)
            if choix == "3":
                pass
                self.controller_choisi = TournoiManager.lancer_tournoi(self)
            if choix == "4":
                pass
                # self.controller_choisi = modifier_tournoi
            if choix == "5":
                pass
                # self.controller_choisi = reprendre_tournoi
            if choix == "6":
                pass
                # self.controller_choisi = afficher_rapport
            if choix == "7":
                self.controller_choisi = MenuPrincipalController()


class QuitterApplication:

    def __call__(self):
        sys.exit()