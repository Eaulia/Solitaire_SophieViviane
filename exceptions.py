"""
---------- EXCEPTIONS.PY ----------
Gere les exceptions (PileVideError, FileVideError, MouvementInvalideError, CarteCacheeError)
-----------------------------------
"""

class PileVideError(Exception):
    """si on tente de dépiler ou de consulter le sommet d’une Pile vide"""
    pass

class FileVideError(Exception):
    """si on tente de défiler ou de consulter la tête d’une File vide"""
    pass

class MouvementInvalideError(Exception):
    """si le joueur tente un déplacement contraire aux règles du jeu 
    (mauvaise couleur, mauvaise valeur, destination interdite...)"""
    pass

class CarteCacheeError(Exception):
    """si on tente de déplacer ou de manipuler une carte face cachée"""
    pass