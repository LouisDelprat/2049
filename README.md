#2048 - Jeu en Python
##À propos du projet
Ce projet est une implémentation en Python du célèbre jeu 2048. Il a été réalisé par moi dans le cadre d'un projet universitaire en L1 à l'Université Catholique de Lille.


Le jeu permet de déplacer les tuiles dans quatre directions (haut, bas, gauche, droite), de fusionner les tuiles identiques et de tenter d'atteindre une tuile d'une valeur de 2048 ou plus.

##Fonctionnalités
Grille personnalisable : L'utilisateur peut choisir la taille de la grille au démarrage.
Déplacements dynamiques : Les tuiles peuvent être déplacées dans quatre directions avec gestion des fusions.
Gestion de la fin du jeu : Le jeu détecte si aucun mouvement n'est plus possible.
Ajout de nombres aléatoires : Des tuiles avec des valeurs 2 ou 4 sont ajoutées à chaque tour.

##Règles du jeu
But du jeu : Fusionnez les tuiles en glissant dans les directions disponibles (gauche, droite, haut, bas) pour obtenir une tuile d'une valeur de 2048 ou plus.

##Fonctionnement :
Lorsqu'une direction est choisie, toutes les tuiles glissent dans cette direction.
Les tuiles avec des valeurs identiques fusionnent en une seule tuile avec leur somme.
Une tuile fusionnée ne peut plus fusionner à nouveau dans le même tour.
Fin de partie : Le jeu se termine lorsque plus aucun mouvement n'est possible.
