
from vues.vue import MenuJoueur, MenuPrincipal, MenuTournoi, Quitter, NettoyerEcran
from controllers.application import ModifierJoueur, RapportJoueurManager, RapportTournoiManager, TournoiManager


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

    def __call__(self):
        choix = ""
        menu = MenuJoueur()
        rapport_joueur = RapportJoueurManager()
        modification_joueur = ModifierJoueur()
        while choix != "3":
            choix = menu.choix_menu_joueur()
            if choix == "1":
                self.controller_choisi = modification_joueur()

            elif choix == "2":
                self.controller_choisi = rapport_joueur.lancer_rapport()
                
            elif choix == "3":
                self.controller_choisi = MenuPrincipalController()
                self.controller_choisi()
            else:
                print()
                print("... ERREUR ...")
                print(" Vous devez faire un choix entre 1 et 3.")



class TournoiMenuController(MenuPrincipalController):

    def __call__(self):
        choix = ""

        menu_tournoi = MenuTournoi()
        tournoi_manager = TournoiManager()
        rapport_tournoi_manager = RapportTournoiManager()

        while choix != "7":
            choix = menu_tournoi.choix_menu_tournoi()
            if choix == "1":
                self.controller_choisi = tournoi_manager.creer_tournoi()

            elif choix == "2":
                self.controller_choisi = tournoi_manager.ajout_joueurs()

            elif choix == "3":
                self.controller_choisi = tournoi_manager.lancer_tournoi()

            elif choix == "4":
                self.controller_choisi = tournoi_manager.modifier_tournoi()

            elif choix == "5":
                self.controller_choisi = tournoi_manager.reprendre_tournoi()

            elif choix == "6":
                self.controller_choisi = rapport_tournoi_manager.lancer_rapport()

            elif choix == "7":
                self.controller_choisi = MenuPrincipalController()
                self.controller_choisi()
            
            else:
                print()
                print("... ERREUR ...")
                print(" Vous devez faire un choix entre 1 et 7.")


class QuitterApplication:

    def __call__(self):
        Quitter.quitter()