def afficher_menu():
    print("A: Ajouter une nouvelle carte")
    print("S: Supprimer une carte")
    print("L: Lire une carte / afficher les informations")
    print("N: Ajouter une nouvelle catégorie de cartes")
    print("M: Modifier le contenu d'une carte")
    print("Q: Quitter l'application")


todo_list = ["Tache2", "Tache3", "Tache4"]
inprogress_list = ["Tache1", "Tache5"]
done_list = ["Tache0", "Tache6"]
category_dict = {"TODO": todo_list, "INPROGRESS": inprogress_list, "DONE": done_list}

print("Lancement de l'application...")
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
    elif inputMenu[0] == "Q":
        break
    else:
        print("Choix invalide! Réesayez")
    print("\n")

for i in category_dict["TODO"]:
    print(i)
print("Fermeture")
