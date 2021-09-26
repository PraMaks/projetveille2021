import tkinter as tk
from tkinter import *
import tkinter.font as font
from tkinter import messagebox


def ouvrir_fenetre_principale():
    global counter_fenetres
    global MAXIMUM_FENETRES
    global bg_help
    global font_bouton

    window = tk.Tk()
    window.title("Trello en Python GUI")
    window.geometry("900x900")
    window.resizable(False, False)

    bg = PhotoImage(file="images/background.png")
    bg_help = PhotoImage(file="images/background_help.png")

    font_bouton = font.Font(family='Courier', size=20, weight='bold')

    background_label = Label(window, image=bg)
    background_label.place(x=0, y=0, relwidth=1, relheight=1)

    canvas_titre = Canvas(window, width=750, height=85, bg='#338BA8', highlightthickness=0)
    canvas_titre.place(x=75, y=20)

    titre_label = Label(canvas_titre, text="Trello en Python GUI", bg='#338BA8', fg='#C0C0C0', font="none 52 bold")
    titre_label.place(x=28, y=0)

    canvas_principal = Canvas(window, width=750, height=720, bg='#338BA8', highlightthickness=0)
    canvas_principal.place(x=75, y=125)

    infos_commandes = Label(canvas_principal, text="↓ Entrez une commande ↓", bg='#338BA8', fg='#C0C0C0',
                            font="none 30 bold")
    infos_commandes.place(x=132, y=0)

    ligne_de_commande = Entry(canvas_principal)
    ligne_de_commande.place(x=132, y=58, width=486, height=25)

    submit_button = Button(canvas_principal, text='Soumettre', bg='#0047AB', fg='#ffffff', borderwidth=0,
                           command=window.quit)
    submit_button['font'] = font_bouton
    submit_button.place(x=150, y=100, width=448, height=30)

    exit_button = Button(window, text='Quitter', bg='#cc1400', fg='#ffffff', borderwidth=0, command=window.quit)
    exit_button['font'] = font_bouton
    exit_button.place(x=380, y=848)

    help_button = Button(window, text='Aide', bg='#65a765', fg='#ffffff', borderwidth=0, command=ouvrir_fenetre_aide)
    help_button['font'] = font_bouton
    help_button.place(x=741, y=848)

    window.mainloop()


def ouvrir_fenetre_aide():
    global counter_fenetres
    global MAXIMUM_FENETRES
    global bg_help
    global font_bouton

    def fermer_fenetre_help():
        global counter_fenetres

        counter_fenetres -= 1
        window_help.destroy()

    if counter_fenetres < MAXIMUM_FENETRES:
        window_help = Toplevel()
        window_help.title("Fênetre d'aide")
        window_help.geometry("750x600")
        window_help.resizable(False, False)

        background_help_label = Label(window_help, image=bg_help)
        background_help_label.place(x=0, y=0, relwidth=1, relheight=1)

        canvas_titre_help = Canvas(window_help, width=676, height=85, bg='#008b8b', highlightthickness=0)
        canvas_titre_help.place(x=37, y=20)

        titre_help = Label(canvas_titre_help, text="Guide d'utilisation", bg='#008b8b', fg='white', font="none 52 bold")
        titre_help.place(x=34, y=0)

        canvas_principal_help = Canvas(window_help, width=676, height=440, bg='#008b8b', highlightthickness=0)
        canvas_principal_help.place(x=37, y=125)

        infos_commandes_help = Label(canvas_principal_help, text="La syntaxe est simple: fonction paramètre",
                                     bg='#008b8b', fg='white', font="none 23 bold")
        infos_commandes_help.place(x=26, y=0)

        exit_button_help = Button(window_help, text='Fermer', bg='#cc1400', fg='#ffffff', borderwidth=0,
                                  command=fermer_fenetre_help)
        exit_button_help['font'] = font_bouton
        exit_button_help.place(x=37, y=568, width=676, height=30)

        counter_fenetres += 1

    else:
        messagebox.showinfo("Error", "Erreur! Arrêtez d'ouvrir trop de fenêtres!")





# Variables de tests
todo_list = ["Tache2", "Tache3", "Tache4"]
inprogress_list = ["Tache1", "Tache5"]
done_list = ["Tache0", "Tache6"]
category_dict = {"TODO": todo_list, "INPROGRESS": inprogress_list, "DONE": done_list}

counter_fenetres = 0
MAXIMUM_FENETRES = 4
bg_help = None
font_bouton = None

ouvrir_fenetre_principale()


