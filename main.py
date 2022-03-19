from vue import Print_menu
from controller import UtilisateurManager
from models_tournoi import Tournoi

def main():
    class Menu():
        def commencer_tournoi(self):
            print_menu = Print_menu()
            user_manager = UtilisateurManager()
            commencer = ""
            while commencer != "oui" and commencer != "non":
                commencer = input("Voulez-vous démarrer un tournoi ? (oui/non)  ")
                if commencer == "oui":
                    print_menu.commencer()
                    mon_tournoi = Tournoi()
                    joueurs = user_manager.ajout_joueurs()
                elif commencer == "non":
                    print_menu.aurevoir()
                else:
                    print_menu.erreur_oui_non()


    begin = Menu()
    begin.commencer_tournoi()

if __name__ == "__main__":
    main()