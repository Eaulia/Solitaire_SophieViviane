"""
Carte (version 0)
Auteur : Sophie
Date : 21/11/2026
Le fichier Carte permet de créer et
de manipuler les cartes du Solitaire.
Entrée : une valeur et une couleur
Résultat : un objet Carte possédant une valeur,
une couleur et un état (visible ou cachée).
"""

from exceptions import BooleenError     # exception pour le type booléen

class Carte:
    def __init__(self, valeur, couleur, etat = False):
        self.valeur = valeur
        self.couleur = couleur
        self.set_etat(etat)

    def get_etat(self):
        return self.__etat

    def set_etat(self, val):
        if type(val) != bool:
            raise BooleenError
        self.__etat = val

    def get_valeur(self):
        """
        Valeur de la carte
        """
        return self.valeur

    def get_couleur(self):
        """
        Connaitre la couleur de la carte
        """
        return self.couleur

    def est_rouge(self):
        return self.get_couleur() == ("Coeur" or "Carreau")

    def get_nom_img(self):
        return f"cartes/{self.get_couleur}/{self.valeur}_{self.get_couleur}.gif"

    def est_visible(self):
        """
        Savoir si la carte est visible
        """
        return self.get_etat()

    def retourner(self):
        """
        Retourner une carte
        """
        self.set_etat(not self.get_etat())

    def __repr__(self) -> str:
        symboles = {"Coeur": "♥", "Carreau": "♦", "Trefle": "♣", "Pique": "♠"}
        return f"{self.valeur}{symboles[self.couleur]}"