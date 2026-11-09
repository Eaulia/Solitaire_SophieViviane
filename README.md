# Solitaire

Jeu de Solitaire en Python avec interface graphique Tkinter, pour un projet d'NSI en fin d'année 2026. Le projet utilise les structures de données **Pile** et **File** : les zones de cartes face cachée (pioche, cartes cachées des colonnes) sont des piles, et les zones de cartes face visible (haut de la pioche -> "talon", les 4 piles par couleur dans l'ordre -> "fondations", cartes visibles des colonnes) sont des files.

## Installation

- Python 3
- Tkinter (fourni avec Python)

```bash
git clone https://github.com/Eaulia/Solitaire_SophieViviane.git
cd solitaire
```

## Utilisation

```bash
python main.py
```

Règles du jeu :

- Le plateau comporte 7 colonnes, une pioche, un talon et 4 fondations.
- On pioche trois cartes à la fois ; quand la pioche est vide, le talon est retourné pour la reconstituer.
- On déplace une carte ou une suite de cartes visibles sur une carte de valeur immédiatement inférieure et de couleur opposée. Seul un Roi peut être posé sur une colonne vide.
- Les fondations se construisent par couleur, de l'As au Roi.
- La partie est gagnée quand les 4 fondations contiennent 13 cartes chacune.
- Le bouton « Annuler le dernier coup » annule la dernière action.

## Structure du projet

```
solitaire/
├── main.py           # base
├── pile.py           # classe Pile
├── file.py           # classe File
├── carte.py          # classe Carte
├── exceptions.py     # PileVideError, FileVideError, MouvementInvalideError, CarteCacheeError
├── jeu.py            # logique du jeu 
└── interface.py      # affichage Tkinter
```

## Contributeurs

- Sophie
- Viviane

## Licence

[MIT](https://choosealicense.com/licenses/mit/)