"""
File (version 0)
Auteur : Le cours pptx/M.Rossier
Date : 21/11/2026
Le fichier File du cours
Entrée : élément à enfiler avec la fonction enfiler()
Résultat : file contenant les éléments ajoutés, consultés ou retirés
"""

from exceptions import FileVideError    # exception pour défiler une pile vide
from fonctions.pile import Pile

class File:
    def __init__(self) -> None:
        self.entree = Pile()
        self.sorties = Pile()
    
    def est_vide(self):
        return self.entree.est_vide() and self.sorties.est_vide()

    def enfiler(self, val):
        self.entree.empiler(val)

    def taille(self):
        return self.entree.taille() + self.sorties.taille()

    def defiler(self):
        if self.est_vide():
            raise FileVideError("La file est vide")
        if self.sorties.est_vide():
            while not self.entree.est_vide():
                self.sorties.empiler(self.entree.depiler())
        return self.sorties.depiler()

    def tete(self):
        if self.est_vide():
            raise FileVideError("La file est vide")
        if self.sorties.est_vide():
            while not self.entree.est_vide():
                self.sorties.empiler(self.entree.depiler())
        return self.sorties.sommet()
