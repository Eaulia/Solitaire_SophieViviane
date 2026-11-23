"""
File (version 0)
Auteur : Le cours pptx/M.Rossier
Date : 21/11/2026
Le fichier File du cours
Entrée : élément à enfiler avec la fonction enfiler()
Résultat : file contenant les éléments ajoutés, consultés ou retirés
"""

from exceptions import FileVideError    # exception pour défiler une pile vide

class File:
    def __init__(self):
        self.f = self.creer_file_vide()

    def creer_file_vide(self):
        return []

    def est_vide(self):
        return len(self.f) == 0

    def tete(self):
        if self.est_vide():
            raise FileVideError
        return self.f[0]

    def taille(self):
        return len(self.f)

    def enfiler(self, elem):
        self.f.append(elem)

    def defiler(self):
        if self.est_vide():
            raise FileVideError
        return self.f.pop(0)