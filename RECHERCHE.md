explication de la logique pour la partie 5 (castle):

But et pricipe générale:

le but de caste est de pouvoir bouger le KING et le ROOK de deux pas vers des direction opposés(changement de place) quand il n'y a aucune piece entre les deux et que ni KING ni le ROOK a fait de mouvement encore. Pour faire la geste, il faut séléctionner le KING et si le mouvement est possible, il parait sur l'écran que le KING peut faire 2 pas vers la direction du ROOK.

Implémentation et logique:

Afin d'implémenter le castle dans le code,j'ai divisé le processus en deux étapes principales : d'abord, dans la méthode get_moves() de la classe King fichier(pieces.py), je dois vérifie si les conditions de base sont remplies pour autoriser le roque: le KING et la ROOK concernée ne doivent pas avoir bougé  (vérifié avec move_count == 0), les cases entre eux doivent être vides (NONE) et la ROOK doit être présente à sa position initiale. Si ces conditions sont satisfaites, le mouvement du KING (de deux cases vers la ROOK) est ajouté aux déplacements possibles. Ensuite, dans move_piece() de la classe Board, lorsqu'un déplacement du KING de deux cases est détecté (ce qui ne peut arriver que losque je fais un castle), le code exécute automatiquement le mouvement coordonné : il déplace le KING à sa nouvelle position et positionne la ROOK de l'autre côté du KING, en trouvant la ROOK correspondante (soit en h1 pour le petit roque, soit en a1 pour le grand roque) et en la déplaçant à sa nouvelle position (f1 pour le petit roque, ou d1 pour le grand roque). Cette implémentation couvre les mécanismes essentiels du roque en gérant correctement le déplacement efficace des pièces et les deux variantes (petit et grand roque).
