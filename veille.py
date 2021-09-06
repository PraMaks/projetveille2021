def afficher_menu():
    print("A: Ajouter une nouvelle carte")
    print("S: Supprimer une carte")
    print("L: Lire une carte / afficher les informations")
    print("N: Ajouter une nouvelle catégorie de cartes")
    print("M: Modifier le contenu d'une carte")
    print("Q: Quitter l'application")

print("Lancement de l'application")
while True:
    afficher_menu()
    inputMenu = input("Entrez une lettre: ")
    inputMenu = inputMenu.upper()

    if inputMenu[0] == "A":
        print("Ajout")
    elif inputMenu[0] == "S":
        print("Supprimer")
    elif inputMenu[0] == "L":
        print("Lire")
    elif inputMenu[0] == "N":
        print("Nouveau")
    elif inputMenu[0] == "M":
        print("Modification")

    print(inputMenu)

    break
