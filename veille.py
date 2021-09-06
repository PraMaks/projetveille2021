def afficher_menu():
    print("A: Ajouter une nouvelle carte")
    print("S: Supprimer une carte")
    print("L: Lire une carte / afficher les informations")
    print("N: Ajouter une nouvelle catégorie de cartes")
    print("M: Modifier le contenu d'une carte")
    print("Q: Quitter l'application")


def afficher_listes():
    print("Voici la liste des categories de cartes disponibles: ")
    for key in category_dict:
        print("     - {}".format(key))
    print("----------")


def afficher_listes_dictionnaire():
    afficher_listes()

    input_menu_read = input("Quel liste voulez vous afficher? ")
    afficher_contenu_liste(input_menu_read)


def afficher_contenu_liste(input_menu_read):
    try:
        counter = 0
        for story in category_dict[input_menu_read]:
            print("     - {} ({})".format(story, counter))
            counter += 1
    except KeyError:
        print("Clé invalide! Retour au menu")


def ajouter_story_dans_liste():
    afficher_listes()

    input_story = input("Entrez votre story à ajouter: ")

    input_menu_read = input("Dans quelle liste voulez vous ajouter la story? ")
    try:
        category_dict[input_menu_read].append(input_story)
    except KeyError:
        print("Clé invalide! Retour au menu....")


def supprimer_story_dans_liste():
    afficher_listes()

    input_menu_delete = input("Dans quelle liste voulez vous supprimer la story: ")
    afficher_contenu_liste(input_menu_delete)

    while True:
        input_story_delete = input("Entrez le numéro de la carte que vous voulez supprimer: ")

        try:
            input_int = int(input_story_delete)
            try:
                category_dict[input_menu_delete].pop(input_int)
                print("Carte supprimée!")
                break

            except IndexError:
                print("Erreur! Retour au menu...")
                break

        except ValueError:
            print("Cela n'est pas un nombre")


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
        ajouter_story_dans_liste()

    elif input_menu[0] == "S":
        supprimer_story_dans_liste()

    elif input_menu[0] == "L":
        afficher_listes_dictionnaire()

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
