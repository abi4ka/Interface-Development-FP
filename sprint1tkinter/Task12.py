import tkinter as tk
from tkinter import messagebox

# List of users
users = []

# --- Functions ---
def add_user():
    name = entry_name.get()
    age = scale_age.get()
    gender = gender_var.get()

    user = f"{name} - {age} años - {gender}"
    users.append(user)
    listbox_users.insert(tk.END, user)
    entry_name.delete(0, tk.END)
    scale_age.set(0)
    gender_var.set("Otro")

def delete_user():
    selection = listbox_users.curselection()
    if selection:
        index = selection[0]
        listbox_users.delete(index)
        users.pop(index)
    else:
        messagebox.showinfo("Information", "Select a user to delete.")

def save_list():
    messagebox.showinfo("Save List", "Save function")

def load_list():
    messagebox.showinfo("Load List", "Load function")

def exit_app():
    window.destroy()

# --- Main window ---
window = tk.Tk()
window.title("Ejercicio 12 - Registro de Usuarios")
window.geometry("450x400")

# --- Top section ---
frame_top = tk.Frame(window)
frame_top.pack(pady=10)

# Name
label_name = tk.Label(frame_top, text="Nombre:")
label_name.grid(row=0, column=0, padx=5)
entry_name = tk.Entry(frame_top, width=25)
entry_name.grid(row=0, column=1, padx=5)

# Age
label_age = tk.Label(frame_top, text="Edad:")
label_age.grid(row=1, column=0, padx=5)
scale_age = tk.Scale(frame_top, from_=0, to=100, orient="horizontal")
scale_age.grid(row=1, column=1, padx=5)

# Gender
label_gender = tk.Label(frame_top, text="Género:")
label_gender.grid(row=2, column=0, padx=5)

gender_var = tk.StringVar(value="Masculino")

# Radiobuttons
frame_gender = tk.Frame(frame_top)
frame_gender.grid(row=2, column=1, columnspan=2, sticky="w")

radio_m = tk.Radiobutton(frame_gender, text="Masculino", variable=gender_var, value="Masculino")
radio_f = tk.Radiobutton(frame_gender, text="Femenino", variable=gender_var, value="Femenino")
radio_o = tk.Radiobutton(frame_gender, text="Otro", variable=gender_var, value="Otro")

radio_m.pack(side="left")
radio_f.pack(side="left", padx=5)
radio_o.pack(side="left")

# --- Buttons section ---
frame_buttons = tk.Frame(window)
frame_buttons.pack(pady=5)

button_add = tk.Button(frame_buttons, text="Añadir", command=add_user)
button_add.grid(row=0, column=0, padx=5)

button_delete = tk.Button(frame_buttons, text="Eliminar", command=delete_user)
button_delete.grid(row=0, column=1, padx=5)

button_exit = tk.Button(frame_buttons, text="Salir", command=exit_app)
button_exit.grid(row=0, column=2, padx=5)

# --- Listbox with scrollbar ---
frame_list = tk.Frame(window)
frame_list.pack(fill="both", expand=True, padx=10, pady=10)

scroll = tk.Scrollbar(frame_list)
scroll.pack(side="right", fill="y")

listbox_users = tk.Listbox(frame_list, yscrollcommand=scroll.set, width=50, height=10)
listbox_users.pack(side="left", fill="both", expand=True)

scroll.config(command=listbox_users.yview)

# --- Menu bar ---
menubar = tk.Menu(window)
menu_file = tk.Menu(menubar, tearoff=0)
menu_file.add_command(label="Guardar Lista", command=save_list)
menu_file.add_command(label="Cargar Lista", command=load_list)
menubar.add_cascade(label="Archivo", menu=menu_file)
window.config(menu=menubar)

# --- Run the application ---
window.mainloop()
