"""
----------------------------------------------------
MAIN.PY - Demarrer le jeu
----------
Auteur : Viviane 
Date : 23/11/2026
Commentaires :
- Ca sert pas à grand chose la j'utilise juste en test mdrr :')
----------------------------------------------------
"""

from game.menu import Menu
from game.talon import Talon

if __name__ == "__main__":
    m = Menu()

    print("TEST COLONNES")
    m.debut_jeu()
    for i, colonne in enumerate(m.colonnes(), start=1):
        print(f"Colonne {i} : {colonne}")

    print("TEST TALON")
    print(m.test_talon())