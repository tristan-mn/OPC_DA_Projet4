# Application gérant un tournoi d'échecs

### Openclassroom projet 04

Durant ce projet, j'ai créé une application gérant le déroulement d'un tournoi d'échecs selon les règles suisses du début à la fin de celui-ci.

l'algorithme génère automatiquement les matchs avec une paire de joueurs séléctionnée toujours selon les règles du tournoi suisse.

Le programme utilise le design pattern MVC (Modèles - Vues - Controlleurs), et utilise la librairie TinyDB pour sauvegarder les joueurs et les tournois dans une base de données.

Il permet de :

- Créer et sauvegarder des joueurs.
- Mettre à jour le classement d'un joueur.
- Créer et sauvegarder des tournois.
- Lancer des tournois.
- Arrêter un tournoi en cours et le reprendre plus tard.



------------------  

## Installation

* ### 1 - installer Python 3  

  sudo apt-get install python3 python3-venv python3-pip

* ### 2 - mise ne place de l'environnement virtuel  

Accéder au répertoire du projet puis taper cette commande pour créer l'environnement    

    python3 -m venv env

* ### 3 - Ouverture de l'environnement virtuel et ajout des modules 

  source env/bin/activate  

  pip install -r requirements.txt

-----------------  


## Autheur  
    Montemitro Tristan

------------------  

## Utilisation du programme :  

* ### 1 - Lancement

       python3 main.py


## Rapport flake8

* ### 1 - Lancement

flake8 --htmldir=flake8_rapport --format=html --max-line-length 119  main.py controllers vues models 

Le rapport se trouve dans le repertoire ```flake8_rapport```