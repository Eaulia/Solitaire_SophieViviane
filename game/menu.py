from game.jeu import Jeu
from game.talon import Talon

class Menu:
    def __init__(self) -> None:
        self.jeu = Jeu()

    def debut_jeu(self):
        self.jeu.creer_paquet()
        self.jeu.distribuer()

    def colonnes(self):
        return self.jeu.colonnes

    def test_talon(self):
        t = Talon()
        t.talon.enfiler("A")
        t.talon.enfiler("B")
        t.talon.enfiler("C")
        print(t.retirer_derniere())
        print(t.retirer_derniere())
        print(t.talon.defiler())  