def afficher_menu():
    print("A: Ajouter une nouvelle carte")
    print("S: Supprimer une carte")
    print("L: Lire une carte / afficher les informations")
    print("N: Ajouter une nouvelle catégorie de cartes")
    print("M: Modifier le contenu d'une carte")
    print("C: Modifier le nom d'une catégorie de cartes")
    print("D: Supprimer une catégorie de cartes")
    print("Q: Quitter l'application")


def afficher_listes():
    print("Voici la liste des categories de cartes disponibles: ")
    for key in category_dict:
        print("     - {}".format(key))
    print("----------")


def afficher_listes_dictionnaire():
    if category_dict:
        afficher_listes()
        input_menu_read = input("Quel liste voulez vous afficher? ")
        afficher_contenu_liste(input_menu_read)
    else:
        print("Il n'y a pas de listes")


def afficher_contenu_liste(input_menu_read):
    try:
        if category_dict[input_menu_read]:
            counter = 0
            for story in category_dict[input_menu_read]:
                print("     - {} ({})".format(story, counter))
                counter += 1
        else:
            print("La liste est vide!")
    except KeyError:
        print("Clé invalide! Retour au menu")


def ajouter_story_dans_liste():
    if category_dict:
        afficher_listes()

        input_story = input("Entrez votre story à ajouter: ")

        input_menu_read = input("Dans quelle liste voulez vous ajouter la story? ")
        try:
            category_dict[input_menu_read].append(input_story)
            print("Story ajoutée!!!")
        except KeyError:
            print("Clé invalide! Retour au menu....")
    else:
        print("Il n'y a pas de listes")


def supprimer_story_dans_liste():
    if category_dict:
        afficher_listes()

        input_menu_delete = input("Dans quelle liste voulez vous supprimer la story: ")
        afficher_contenu_liste(input_menu_delete)

        while True:
            input_story_delete = input("Entrez le numéro de la story que vous voulez supprimer: ")

            try:
                input_int = int(input_story_delete)
                try:
                    category_dict[input_menu_delete].pop(input_int)
                    print("Story supprimée!!!")
                    break

                except IndexError:
                    print("Erreur! Retour au menu...")
                    break

            except ValueError:
                print("Cela n'est pas un nombre")
    else:
        print("Il n'y a pas de listes")


def modifier_story_dans_liste():
    if category_dict:
        afficher_listes()

        input_menu_modif = input("Dans quelle liste se trouve la story à modifier: ")
        afficher_contenu_liste(input_menu_modif)

        while True:
            input_story_modif = input("Entrez le numéro de la story que vous voulez modifier: ")
            input_story_content = input("Entrez le nouveau texte à mettre dans la story: ")

            try:
                input_int = int(input_story_modif)
                try:
                    category_dict[input_menu_modif][input_int] = input_story_content
                    print("Story modifiée!!!")
                    break

                except IndexError:
                    print("Erreur! Retour au menu...")
                    break

            except ValueError:
                print("Cela n'est pas un nombre")
    else:
        print("Il n'y a pas de listes")


def ajouter_nouvelle_liste():
    nouvelle_liste_nom = input("Entrez le nom de la nouvelle liste: ")
    category_dict[nouvelle_liste_nom] = []
    print("Nouvelle catégorie ajoutée!")


def supprimer_liste():
    if category_dict:
        afficher_listes()
        liste_a_supprimer = input("Entrez le nom de la liste de cartes à supprimer: ")
        try:
            category_dict.pop(liste_a_supprimer)
            print("Liste supprimée!!!")
        except KeyError:
            print("Le nom de la liste entré n'existe pas!!!")
    else:
        print("Il n'y a pas de listes")


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
        ajouter_nouvelle_liste()

    elif input_menu[0] == "M":
        modifier_story_dans_liste()

    elif input_menu[0] == "C":
        print("Categorie")

    elif input_menu[0] == "D":
        supprimer_liste()

    elif input_menu[0] == "Q":
        break

    else:
        print("Choix invalide! Réesayez")
    print()

# for i in category_dict["TODO"]:
    # print(i)

print("Fermeture de l'application...")
