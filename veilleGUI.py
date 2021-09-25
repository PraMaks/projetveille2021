import tkinter as tk
from tkinter import *

window = tk.Tk()
window.title("Trello en Python GUI")
window.geometry("900x900")
window.resizable(False, False)

bg = PhotoImage(file="images/background.png")

background_label = Label(window, image=bg)
background_label.place(x=0, y=0, relwidth=1, relheight=1)

canvas_titre = Canvas(window, width=750, height=85, bg='#338BA8', highlightthickness=0)
canvas_titre.place(x=75, y=20)

titre_label = Label(canvas_titre, text="Trello en Python GUI", bg='#338BA8', fg='#C0C0C0', font="none 52 bold")
titre_label.place(x=28, y=0)

canvas_principal = Canvas(window, width=750, height=750, bg='#338BA8', highlightthickness=0)
canvas_principal.place(x=75, y=125)

infos_commandes = Label(canvas_principal, text="↓ Entrez une commande ↓", bg='#338BA8', fg='#C0C0C0',
                        font="none 30 bold")
infos_commandes.place(x=132, y=0)

ligne_de_commande = Entry(canvas_principal)
ligne_de_commande.place(x=132, y=58, width=486, height=25)

# exit_button = Button(canvas_principal, text="Exit", command=window.quit)
# exit_button.place(x=150, y=500)

window.mainloop()
