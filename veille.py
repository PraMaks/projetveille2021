def afficher_menu():
    print("A: Ajouter une nouvelle carte")
    print("S: Supprimer une carte")
    print("L: Lire une carte / afficher les informations")
    print("N: Ajouter une nouvelle catégorie de cartes")
    print("M: Modifier le contenu d'une carte")
    print("Q: Quitter l'application")


def afficher_listes_dictionnaire():
    afficher_listes()

    input_menu_read = input("Quel liste voulez vous afficher? ")
    try:
        for story in category_dict[input_menu_read]:
            print("     - {}".format(story))
    except KeyError:
        print("Clé invalide! Retour au menu")


def afficher_listes():
    print("Voici la liste des categories de cartes disponibles: ")
    for key in category_dict:
        print("     - {}".format(key))
    print("----------")


def ajouter_carte_dans_liste():
    afficher_listes()

    input_menu_read = input("Quel liste voulez vous afficher? ")
    try:
        for story in category_dict[input_menu_read]:
            print("     - {}".format(story))
    except KeyError:
        print("Clé invalide! Retour au menu")

todo_list = ["Tache2", "Tache3", "Tache4"]
inprogress_list = ["Tache1", "Tache5"]
done_list = ["Tache0", "Tache6"]
category_dict = {"TODO": todo_list, "INPROGRESS": inprogress_list, "DONE": done_list}

print("Lancement de l'application...")
while True:
    afficher_menu()

    input_menu = input("Entrez une lettre: ")
    input_menu = input_menu.upper()

    if input_menu[0] == "A":
        print("Ajout")

    elif input_menu[0] == "S":
        print("Supprimer")

    elif input_menu[0] == "L":
        afficher_listes_dictionnaires()

    elif input_menu[0] == "N":
        print("Nouveau")

    elif input_menu[0] == "M":
        print("Modification")

    elif input_menu[0] == "Q":
        break

    else:
        print("Choix invalide! Réesayez")
    print()

# for i in category_dict["TODO"]:
    # print(i)

print("Fermeture de l'application...")
