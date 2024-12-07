import random

def creer_grille():
    """
    Demande à l'utilisateur la taille de la grille et crée une grille vide.

    La taille doit être un entier supérieur ou égal à 2. Chaque case de la grille
    est initialisée avec le caractère "#".

    Retourne :
        list : Une grille vide représentée comme une liste de listes.
    """
    taille = 0
    while taille < 2:
        taille_texte = input("Entrez la taille de la grille (minimum 2) : ")
        if taille_texte.isnumeric():
            taille = int(taille_texte)
            if taille < 2:
                print("La taille doit être au moins 2.")
        else:
            print("Veuillez entrer un nombre valide.")
            taille = 0
    grille = []
    for _ in range(taille):
        grille.append(["#" for _ in range(taille)])
    return grille

def ajouter_nombre(grille):
    """
    Ajoute un nombre (2 ou 4) dans une case vide aléatoire de la grille.

    Paramètre :
        grille (list) : La grille dans laquelle le nombre sera ajouté.

    Retourne :
        bool : True si un nombre a été ajouté, False si la grille est pleine.
    """
    taille = len(grille)
    cases_vides = []
    for i in range(taille):
        for j in range(taille):
            if grille[i][j] == "#":
                cases_vides.append((i, j))
    if not cases_vides:
        return False
    i, j = random.choice(cases_vides)
    grille[i][j] = random.choice([2, 4])
    return True

def afficher_grille(grille):
    """
    Affiche la grille dans un format lisible.

    Chaque case est séparée par des lignes et colonnes. Les cases vides
    sont représentées par des espaces.

    Paramètre :
        grille (list) : La grille à afficher.
    """
    taille = len(grille)
    ligne_sep = "-" * (5 * taille + 1)
    print(ligne_sep)
    for ligne in grille:
        ligne_affichee = "|"
        for case in ligne:
            if case == "#":
                ligne_affichee += "    |"
            else:
                ligne_affichee += f" {case:3}|"
        print(ligne_affichee)
        print(ligne_sep)

def deplacer_ligne_gauche(ligne):
    """
    Déplace et fusionne les éléments d'une ligne vers la gauche.

    Paramètre :
        ligne (list) : Une liste représentant une ligne de la grille.

    Retourne :
        list : La ligne après déplacement et fusion.
    """
    nouvelle_ligne = []
    for case in ligne:
        if case != "#":
            nouvelle_ligne.append(case)
    while len(nouvelle_ligne) < len(ligne):
        nouvelle_ligne.append("#")
    for i in range(len(nouvelle_ligne) - 1):
        if nouvelle_ligne[i] != "#" and nouvelle_ligne[i] == nouvelle_ligne[i + 1]:
            nouvelle_ligne[i] *= 2
            nouvelle_ligne[i + 1] = "#"
    ligne_finale = []
    for case in nouvelle_ligne:
        if case != "#":
            ligne_finale.append(case)
    while len(ligne_finale) < len(ligne):
        ligne_finale.append("#")
    return ligne_finale

def deplacer_grille(grille, direction):
    """
    Déplace toutes les cases de la grille dans une direction donnée.

    Paramètres :
        grille (list) : La grille à déplacer.
        direction (str) : La direction du déplacement ('g', 'd', 'h', 'b').

    Retourne :
        None : La grille est modifiée directement.
    """
    taille = len(grille)
    if direction == "g":
        for i in range(taille):
            grille[i] = deplacer_ligne_gauche(grille[i])
    elif direction == "d":
        for i in range(taille):
            grille[i] = list(reversed(deplacer_ligne_gauche(list(reversed(grille[i])))))
    elif direction == "h":
        for j in range(taille):
            colonne = [grille[i][j] for i in range(taille)]
            nouvelle_colonne = deplacer_ligne_gauche(colonne)
            for i in range(taille):
                grille[i][j] = nouvelle_colonne[i]
    elif direction == "b":
        for j in range(taille):
            colonne = [grille[i][j] for i in range(taille)]
            nouvelle_colonne = list(reversed(deplacer_ligne_gauche(list(reversed(colonne)))))
            for i in range(taille):
                grille[i][j] = nouvelle_colonne[i]

def mouvement_possible(grille):
    """
    Vérifie si des mouvements sont encore possibles dans la grille.

    Paramètre :
        grille (list) : La grille à vérifier.

    Retourne :
        bool : True si au moins un mouvement est possible, False sinon.
    """
    taille = len(grille)
    for i in range(taille):
        for j in range(taille):
            if grille[i][j] == "#":
                return True
            if i < taille - 1 and grille[i][j] == grille[i + 1][j]:
                return True
            if j < taille - 1 and grille[i][j] == grille[i][j + 1]:
                return True
    return False

def jeu():
    """
    Lancement du jeu 2048.

    Le joueur choisit les directions ('g', 'd', 'h', 'b') pour déplacer
    les cases de la grille. Le jeu se termine si aucun mouvement n'est
    possible.
    """
    grille = creer_grille()
    ajouter_nombre(grille)
    ajouter_nombre(grille)
    while True:
        afficher_grille(grille)
        if not mouvement_possible(grille):
            print("Game Over !")
            break
        direction = input("Entrez une direction (g = gauche, d = droite, h = haut, b = bas) : ").lower()
        if direction not in ("g", "d", "h", "b"):
            print("Direction invalide. Réessayez.")
            continue
        ancienne_grille = [ligne[:] for ligne in grille]  # Copie de la grille
        deplacer_grille(grille, direction)
        if grille != ancienne_grille:  # Si la grille a changé
            if not ajouter_nombre(grille):
                print("Game Over !")
                break

# Lancer le jeu
jeu()
