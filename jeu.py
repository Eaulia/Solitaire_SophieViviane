"""
Jeu (version 0)
Auteur : Sophie
Date : 23/11/2026
Le fichier Jeu permet de créer et
de gérer le jeu Solitaire
Entrée : 52 cartes avec leurs valeurs et leurs couleurs/fondations
Résultat : paquet de 52 cartes mélangées et à être distribué
"""

from carte import Carte     # importation de la classe Carte
from pile import Pile       # importation de la classe Pile
import random               # module le mélange de carte

class Jeu:
    def __init__(self):
        self.valeurs = ["As", "2", "3", "4", "5", "6", "7", "8", "9", "10" "Valet", "Dame", "Roi"]
        self.fondations = ["Coeur", "Carreau", "Trèfle", "Pique"]
        self.cartes = []
        self.pioche = Pile()

    def creer_paquet(self):
        """
        Creer les 52 cartes du jeu
        """
        for valeur in self.valeur:      # choisi une valeur
            for fondations in self.fondations:      # parcourt les 4 fondations
                # crée un nouvel objet carte et l'ajoute à self.carte
                self.cartes.append(Carte(valeur, couleur))

    def melanger(self):
        """
        Melange le paquet
        """
        random.shuffle(self.cartes)     # mélange les 52 cartes directement dans la liste
        for elem in self.cartes:    # parcourt les cartes mélangées
            self.pioche.empiler(elem)   # ajoute chaque carte dans la pile self.pioche

    def distribuer(self):
        """
        Distribu les cartes dans differents colonnes
        """
        pass