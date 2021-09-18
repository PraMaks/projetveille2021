import json
import os
from os import walk

def afficher_menu():
    print("A: Ajouter une nouvelle carte")
    print("N: Ajouter une nouvelle catégorie de cartes")
    print("L: Lire une carte / afficher les informations")
    print("M: Modifier le contenu d'une carte")
    print("C: Modifier le nom d'une catégorie de cartes")
    print("D: Supprimer une catégorie de cartes")
    print("S: Supprimer une carte")
    print("F: Déplacer une carte dans une autre liste")
    print("X: Supprimer toutes les listes et cartes")
    print("I: Sauvegarder les cartes")
    print("O: Cherger un fichier de sauvegarde")
    print("Q: Quitter l'application")


def afficher_listes():
    print("Voici la liste des categories de cartes disponibles: ")
    for key in category_dict:
        print("     - {}".format(key))
    print("----------")


def afficher_listes_dictionnaire():
    if category_dict:
        afficher_listes()
        input_menu_read = input("Entrez le nom de la liste à afficher:  ")
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
        print("Clé invalide!")


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


def modifier_nom_categorie_liste():
    if category_dict:
        afficher_listes()
        liste_nom_vieux = input("Entrez le nom de catégorie à changer: ")
        liste_nom_nouveau = input("Entrez le nouveau nom de catégorie: ")
        try:
            # En Python on n'a pas besoin de garder la donnée effacée en mémoire contrairement à Java
            category_dict[liste_nom_nouveau] = category_dict.pop(liste_nom_vieux)
            print("Nom modifiée!")
        except KeyError:
            print("Le nom de la liste entré n'existe pas!!!")
    else:
        print("Il n'y a pas de listes!")


def deplacer_carte_dans_autre_liste():
    if category_dict:
        afficher_listes()
        input_liste_de = input("Dans quelle liste se trouve la carte à déplacer?: ")
        input_liste_a = input("Dans quelle liste faut déplacer la carte?: ")
        try:
            afficher_contenu_liste(input_liste_de)
            input_index_carte = int(input("Quel est le nombre de la carte à deplacer?: "))
            category_dict[input_liste_a].append(category_dict[input_liste_de].pop(input_index_carte))
            print("Carte deplacée!!!")
        except KeyError:
            print("Le nom de la liste entré n'existe pas!!!")
    else:
        print("Il n'y a pas de listes")


def effacer_tout():
    choix = input("Êtes-vous certain de tout effacer(O/N): ")
    choix = choix.upper()
    if choix == "O":
        category_dict.clear()
        print("Tout est effacé...")
    else:
        print("Annulation d'effacement du dictionnaire des données. Retour au menu...")


def sauvegarder():
    nom_fichier = input("Entrez le nom de fichier de sauvegarde : ")
    dossier_sauvegarde = "saves"
    rep_parent = "./"
    path = os.path.join(rep_parent, dossier_sauvegarde)

    try:
        os.mkdir(path)

    except FileExistsError:
        pass

    finally:
        json_data = json.dumps(category_dict)
        parsed = json.loads(json_data)
        fichier = open(f"./{dossier_sauvegarde}/{nom_fichier}.json", "w")
        fichier.write(json.dumps(parsed, indent=4, sort_keys=True))
        fichier.close()
        print(f"Le fichier est sauvegardé dans le dossier ./{dossier_sauvegarde}/{nom_fichier}.json")


def charger_json():
    dossier_sauvegarde = "saves"
    json_extension = ".json"
    # Source de la ligne du bas: https://stackoverflow.com/questions/3207219/how-do-i-list-all-files-of-a-directory
    fichiers_initiales = next(walk(f"./{dossier_sauvegarde}/"), (None, None, []))[2]
    fichiers_json = []


    for fichier in fichiers_initiales:
        if fichier.endswith(json_extension):
            fichiers_json.append(fichier)

    print("Voici la liste des fichiers de sauvegarde: ")
    for fichier in fichiers_json:
        print(f"    - {fichier}")

    fichier_a_charger = input("Entrez le nom du fichier de sauvegarde que vous voulez charger (avec .json): ")

    if not fichier_a_charger.endswith(json_extension):
        print("Ceci n'est pas un fichier de sauvegarde. Retour au menu...")

    else:
        try:
            with open(f"./{dossier_sauvegarde}/{fichier_a_charger}") as json_file:
                data_chargee = json.load(json_file)
                print("Le fichier a été chargé!")
                return data_chargee

        except FileNotFoundError:
            print("Le fichier n'a pas été trouvé!")


# Variables de tests
todo_list = ["Tache2", "Tache3", "Tache4"]
inprogress_list = ["Tache1", "Tache5"]
done_list = ["Tache0", "Tache6"]
category_dict = {"TODO": todo_list, "INPROGRESS": inprogress_list, "DONE": done_list}

# Lancement de l'application
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
        modifier_nom_categorie_liste()

    elif input_menu[0] == "D":
        supprimer_liste()

    elif input_menu[0] == "F":
        deplacer_carte_dans_autre_liste()

    elif input_menu[0] == "X":
        effacer_tout()

    elif input_menu[0] == "I":
        sauvegarder()

    elif input_menu[0] == "O":
        category_dict = charger_json()

    elif input_menu[0] == "Q":
        break

    else:
        print("Choix invalide! Réessayez!")
    print()

print("Fermeture de l'application...")
