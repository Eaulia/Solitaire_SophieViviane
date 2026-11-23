from jeu import Jeu

class Menu:
    def __init__(self) -> None:
        self.jeu = Jeu()

    def debut_jeu(self):
        self.jeu.creer_paquet()
        self.jeu.distribuer()

    def colonnes(self):
        return self.jeu.colonnes