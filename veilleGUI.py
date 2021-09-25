import tkinter as tk
from tkinter import *


window = tk.Tk()
window.title("Trello en Python")
window.geometry("900x900")
window.resizable(False, False)

bg = PhotoImage(file="images/background.png")

background_label = Label(window, image=bg)
background_label.place(x=0, y=0, relwidth=1, relheight=1)

canvas_principal = Canvas(window, width=750, height=750, bg='#338BA8', highlightthickness=0)
canvas_principal.place(x=75, y=125)

canvas_titre = Canvas(window, width=750, height=70, bg='#338BA8')
canvas_titre.place(x=75, y=20)

titre_label = Label(canvas_titre, text=" Trello en Python GUI ", bg='#338BA8', fg="blue", font="none 54 bold")
titre_label.pack()


# Lancement de l'application
window.mainloop()