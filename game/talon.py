"""
----------------------------------------------------
TALON.PY - Wui le talon
----------------------------------------------------
"""

from fonctions.file import File
from fonctions.pile import Pile
from exceptions import FileVideError

class Talon:
    def __init__(self) -> None:
        self.talon = File()

    def est_vide(self):
        self.talon.est_vide()

    def ajouter(self, carte):
        self.talon.enfiler(carte)

    def derniere(self):
        derniere = None
        for _ in range(self.talon.taille()):
            derniere = self.talon.defiler()
            self.talon.enfiler(derniere)
        return derniere

    def retirer_derniere(self):
        """
        retirer dernier carte du talon
        """
        if self.est_vide():
            raise FileVideError("Le Talon est vide")
        for _ in range(self.talon.taille()-1):
            self.talon.enfiler(self.talon.defiler())
        return self.talon.defiler()
    