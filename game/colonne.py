"""
----------------------------------------------------
COLONNE.PY - Les 7 colonnes du jeu
----------------------------------------------------
"""

from fonctions.pile import Pile
from fonctions.file import File
from exceptions import MouvementInvalideError

class Colonne:
    def __init__(self):
        self.cachees = Pile()
        self.visibles = File()

    def ajouter_cachee(self, carte):
        """
        Ajoute une carte face cachée
        """
        self.cachees.empiler(carte)

    def ajouter_visible(self, carte):
        """
        Ajoute une carte face visible
        """
        self.visibles.enfiler(carte)

    def derniere_visible(self):
        """
        Obtenir derniere carte visible dans une colonne. Exemple
        [??]
        [8♠] 
        [7♦]
        [6♠] <- avoir cette carte
        """
        derniere = None
        for _ in range(self.visibles.taille()):
            derniere = self.visibles.defiler()
            self.visibles.enfiler(derniere)
        return derniere

    def retirer_suite(self, carte):
        """
        Retirer suite de cartes dans une colonne. Exemple
        [??]
        [8♠] <- avoir cette carte
        [7♦] <- avoir cette carte
        [6♠] <- avoir cette carte
        """
        reste = File()
        suite = File()
        trouvee = False
        
        for _ in range(self.visibles.taille()):
            c = self.visibles.defiler()
            if c is carte:
                trouvee = True
            if trouvee:
                suite.enfiler(c)
            else:
                reste.enfiler(c)

        self.visibles = reste #remet le reste

        if not trouvee:
            raise MouvementInvalideError("Mouvement impossible")
        
        return suite

    def retourner_si_besoin(self):
        """
        Retourne la carte si toutes les cartes visibles ont ete deplacees
        """
        if self.visibles.est_vide() and not self.cachees.est_vide():
            carte = self.cachees.depiler()
            carte.set_etat(True)
            self.visibles.enfiler(carte)

    def __repr__(self) -> str:
        texte = "[??]" * self.cachees.taille()
        for _ in range(self.visibles.taille()):
            carte = self.visibles.defiler()
            texte += f"[{carte}] "
            self.visibles.enfiler(carte)    # on la remet : la file ne change pas
        return texte
