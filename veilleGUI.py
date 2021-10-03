import tkinter as tk
from tkinter import *
import tkinter.font as font
from tkinter import messagebox
import os
from os import walk
import json


def sauvegarder(nom_fichier):
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


def open_main_window():
    global counter_window
    global MAXIMUM_WINDOWS
    global bg_help
    global font_bouton

    def submit():
        entered_text = command_line.get()

        if entered_text.startswith("Sauvegarder"):
            save = entered_text.split(' ')[1]
            sauvegarder(save)
            response_label['text'] = f"Le fichier {save}.json a été sauvegardé"

        elif entered_text == "S":
            supprimer_story_dans_liste()


    window = tk.Tk()
    window.title("Trello en Python GUI")
    window.geometry("900x900")
    window.resizable(False, False)

    bg = PhotoImage(file="images/background.png")
    bg_help = PhotoImage(file="images/background_help.png")

    font_bouton = font.Font(family='Courier', size=20, weight='bold')

    background_label = Label(window, image=bg)
    background_label.place(x=0, y=0, relwidth=1, relheight=1)

    # Title Canvas ###########################
    canvas_title = Canvas(window, width=750, height=85, bg='#338BA8', highlightthickness=0)
    canvas_title.place(x=75, y=20)

    title_label = Label(canvas_title, text="Trello en Python GUI", bg='#338BA8', fg='#C0C0C0', font="none 52 bold")
    title_label.place(x=28, y=0)
    ##########################################

    # Main Canvas ############################
    main_canvas = Canvas(window, width=750, height=720, bg='#338BA8', highlightthickness=0)
    main_canvas.place(x=75, y=125)

    # ------------------------ #
    command_line_info = Label(main_canvas, text="↓ Entrez une commande ↓", bg='#338BA8', fg='#C0C0C0',
                            font="none 30 bold")
    command_line_info.place(x=132, y=0)

    # ------------------------ #
    command_line = Entry(main_canvas)
    command_line.place(x=132, y=58, width=486, height=25)

    # ------------------------ #
    submit_button = Button(main_canvas, text='Soumettre', bg='#0047AB', fg='#ffffff', borderwidth=0, command=submit)
    submit_button['font'] = font_bouton
    submit_button.place(x=150, y=100, width=448, height=30)

    # ------------------------ #
    response_label = Label(main_canvas, text="↓ Entrez une commande ↓", bg='#338BA8', fg='#C0C0C0', font="none 25 bold")
    response_label.place(x=130, y=130)

    # ------------------------ #
    exit_button = Button(window, text='Quitter', bg='#cc1400', fg='#ffffff', borderwidth=0, command=window.quit)
    exit_button['font'] = font_bouton
    exit_button.place(x=380, y=848)

    # ------------------------ #
    help_button = Button(window, text='Aide', bg='#65a765', fg='#ffffff', borderwidth=0, command=open_help_window)
    help_button['font'] = font_bouton
    help_button.place(x=741, y=848)

    ##########################################

    window.mainloop()


def open_help_window():
    global counter_window
    global MAXIMUM_WINDOWS
    global bg_help
    global font_bouton

    def close_help_window():
        global counter_window

        counter_window -= 1
        window_help.destroy()

    def disable_event():
        pass

    if counter_window < MAXIMUM_WINDOWS:
        window_help = Toplevel()
        window_help.title("Fênetre d'aide")
        window_help.geometry("750x600")
        window_help.resizable(False, False)
        window_help.protocol("WM_DELETE_WINDOW", disable_event)

        background_help_label = Label(window_help, image=bg_help)
        background_help_label.place(x=0, y=0, relwidth=1, relheight=1)

        # Title Canvas ###########################
        canvas_title_help = Canvas(window_help, width=680, height=85, bg='#008b8b', highlightthickness=0)
        canvas_title_help.place(x=37, y=20)

        title_help = Label(canvas_title_help, text="Guide d'utilisation", bg='#008b8b', fg='white', font="none 52 bold")
        title_help.place(x=34, y=0)
        ##########################################

        # Main Canvas ############################
        canvas_main_help = Canvas(window_help, width=680, height=440, bg='#008b8b', highlightthickness=0)
        canvas_main_help.place(x=37, y=115)

        # ------------------------ #
        info_commands_help = Label(canvas_main_help, text="La syntaxe est simple et facile à comprendre:",
                                     bg='#008b8b', fg='white', font="none 22 bold")
        info_commands_help.place(x=26, y=0)

        # ------------------------ #
        commands_view_help = Label(canvas_main_help, text="Voir \"catégories\" / <nom de la catégorie> /"
                                                                " \"fichiers\">",
                                    bg='#008b8b', fg='white', font="none 16 bold")
        commands_view_help.place(x=26, y=40)

        # ------------------------ #
        command_save_help = Label(canvas_main_help, text="Sauvegarder <nom du fichier.json>",
                                   bg='#008b8b', fg='white', font="none 16 bold")
        command_save_help.place(x=26, y=70)

        # ------------------------ #
        command_load_help = Label(canvas_main_help, text="Charger <nom du fichier.json>",
                                   bg='#008b8b', fg='white', font="none 16 bold")
        command_load_help.place(x=26, y=100)

        # ------------------------ #
        commands_delete_help = Label(canvas_main_help,
                                      text="Supprimer <nom du fichier.json> / <nom de la carte> /",
                                      bg='#008b8b', fg='white', font="none 16 bold")
        commands_delete_help.place(x=26, y=130)

        commands_delete_end_help = Label(canvas_main_help, text="                  <nom de la catégorie>",
                                          bg='#008b8b', fg='white', font="none 16 bold")
        commands_delete_end_help.place(x=26, y=160)

        # ------------------------ #
        commands_add_help = Label(canvas_main_help, text="Ajouter <nom de la catégorie> / <nom de la carte>",
                                   bg='#008b8b', fg='white', font="none 16 bold")
        commands_add_help.place(x=26, y=190)

        # ------------------------ #
        commands_update_cat_help = Label(canvas_main_help, text="Modifier <vieux nom de la catégorie> par",
                                          bg='#008b8b', fg='white', font="none 16 bold")
        commands_update_cat_help.place(x=26, y=220)

        commands_update_cat_end_help = Label(canvas_main_help, text="              <nouveau nom de la catégorie>",
                                              bg='#008b8b', fg='white', font="none 16 bold")
        commands_update_cat_end_help.place(x=26, y=250)

        # ------------------------ #
        commands_update_card_help = Label(canvas_main_help,
                                           text="Modifier <vieux nom de la carte> par <nouveau nom de la carte>",
                                           bg='#008b8b', fg='white', font="none 16 bold")
        commands_update_card_help.place(x=26, y=280)

        commands_update_card_end_help = Label(canvas_main_help, text="             dans < nom de la catégorie > ",
                                           bg='#008b8b', fg='white', font="none 16 bold")
        commands_update_card_end_help.place(x=26, y=310)

        # ------------------------ #
        command_move_help = Label(canvas_main_help, text="Deplacer <nom de la carte> dans <nom de la liste>",
                                   bg='#008b8b', fg='white', font="none 16 bold")
        command_move_help.place(x=26, y=340)

        command_move_end_help = Label(canvas_main_help, text="                vers <nom de la nouvelle liste>",
                                       bg='#008b8b', fg='white', font="none 16 bold")
        command_move_end_help.place(x=26, y=370)

        # ------------------------ #
        command_reset_help = Label(canvas_main_help, text="Pour mettre tout effacer: Reinitialiser", bg='#008b8b',
                                    fg='white', font="none 16 bold")
        command_reset_help.place(x=26, y=400)

        # ------------------------ #
        exit_button_help = Button(window_help, text='Fermer', bg='#cc1400', fg='#ffffff', borderwidth=0,
                                  command=close_help_window)
        exit_button_help['font'] = font_bouton
        exit_button_help.place(x=37, y=562, width=680, height=30)
        ##########################################

        counter_window += 1

    else:
        messagebox.showinfo("Erreur", "Erreur! La fenêtre d'aide est déjà ouvert!")


# Test Variables
todo_list = ["Tache2", "Tache3", "Tache4"]
inprogress_list = ["Tache1", "Tache5"]
done_list = ["Tache0", "Tache6"]
category_dict = {"TODO": todo_list, "INPROGRESS": inprogress_list, "DONE": done_list}

# Global Variables
counter_window = 0
MAXIMUM_WINDOWS = 1
bg_help = None
font_bouton = None

# Application starts...
open_main_window()
