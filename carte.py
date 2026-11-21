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

class Carte:
    def __init__(self, valeur, couleur, etat):
        self.valeur = valeur
        self.couleur = couleur
        self._etat(etat)