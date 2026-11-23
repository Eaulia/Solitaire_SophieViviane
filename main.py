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

from menu import Menu

if __name__ == "__main__":
    m = Menu()
    m.debut_jeu()
    print(m.colonnes())