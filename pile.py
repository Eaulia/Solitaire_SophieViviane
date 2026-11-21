"""
Pile (version 0)
Auteur : Le cours pptx/Mr.Rossier
Date : 21/11/2026
Le fichier Pile du cours
Entrée : élément à empiler avec empiler()
Résultat : pile avec les éléments ajoutés, consultés ou retirés
"""

from exceptions import PileVideError    # exception pour dépiler une pile vide

class Pile:
    def __init__(self):
        self.p = self.creer_pile_vide()

    def creer_pile_vide(self):
        return []

    def est_vide(self):
        return len(self.p) == 0

    def taille(self):
        return len(self.p)
    
    def sommet(self):
        if self.est_vide():
            raise PileVideError
        return self.p[-1]
        
    def empiler(self, val):
        self.p.append(val)

    def depiler(self):
        if self.est_vide():
            raise PileVideError
        return self.p.pop()