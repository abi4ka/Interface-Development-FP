import tkinter as tk
from tkinter import messagebox

def open_file():
    messagebox.showinfo("Abrir", "Un mensaje (Abrir)")

def about():
    messagebox.showinfo("Acerca de", "Un mensaje (Acerca de)")

def exit_app():
    window.destroy()

window = tk.Tk()
window.title("Ejercicio 9 - Menu")
window.geometry("300x200")

menubar = tk.Menu(window)

# Archivo menu
file_menu = tk.Menu(menubar, tearoff=0)
file_menu.add_command(label="Abrir", command=open_file)
file_menu.add_separator()
file_menu.add_command(label="Salir", command=exit_app)
menubar.add_cascade(label="Archivo", menu=file_menu)

# Ayuda menu
help_menu = tk.Menu(menubar, tearoff=0)
help_menu.add_command(label="Acerca de", command=about)
menubar.add_cascade(label="Ayuda", menu=help_menu)

window.config(menu=menubar)

window.mainloop()
