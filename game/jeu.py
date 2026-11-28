"""
----------------------------------------------------
JEU.PY - Mise en place + pioche
----------------------------------------------------

Jeu (version 0)
Auteur : Sophie
Date : 23/11/2026
Le fichier Jeu permet de créer et
de gérer le jeu Solitaire
Entrée : 52 cartes avec leurs valeurs et leurs couleurs/fondations
Résultat : paquet de 52 cartes mélangées et à être distribué

----------
Auteur : Viviane 
Date : 23/11/2026
Commentaires :
- J'ai fusionné creer paquet et melanger 
"""

from game.carte import Carte     # importation de la classe Carte
from fonctions.pile import Pile       # importation de la classe Pile
from game.colonne import Colonne # importation de la classe Colonne
import random               # module le mélange de carte
from game.talon import Talon         # importation de la classe Talon

class Jeu:
    def __init__(self):
        self.valeurs = ["As", "2", "3", "4", "5", "6", "7", "8", "9", "10", "Valet", "Dame", "Roi"]
        self.couleurs = ["Coeur", "Carreau", "Trefle", "Pique"]
        self.pioche = Pile()
        self.colonnes = [Colonne() for _ in range(7)]

    def creer_paquet(self):
        """
        Creer les 52 cartes du jeu et melange le jeu
        """
        paquet = []
        for valeur in self.valeurs:      # choisi une valeur
            for couleur in self.couleurs:      # parcourt les 4 couleurs
                # crée un nouvel objet carte et l'ajoute à paquet
                paquet.append(Carte(str(valeur), str(couleur)))

        random.shuffle(paquet)
        for carte in paquet:
            # crée un nouvel objet carte et l'ajoute à pioche
            self.pioche.empiler(carte)

    def distribuer(self):
        """
        Distribue les cartes dans differents colonnes
        """
        for i in range(7):
            col = self.colonnes[i]
            for _ in range(i): #i : nb de cartes cachees
                col.ajouter_cachee(self.pioche.depiler())
            carte = self.pioche.depiler()
            carte.set_etat(True)
            col.ajouter_visible(carte) #derniere carte visible

    def retourner_talon(self):
        p = Pile()
        while not Talon().talon.est_vide():
            p.empiler(Talon().talon.defiler())
        while not p.est_vide():
            carte = p.depiler()
            carte.set_etat(False)
            return self.pioche.empiler(carte)
        
    def piocher(self):
        """
        Piocher des cartes
        """
        if self.pioche.est_vide():
            self.retourner_talon()
        else:
            carte = self.pioche.depiler()
            carte.set_etat(True)
            Talon().talon.enfiler(carte)