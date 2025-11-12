import tkinter as tk
from tkinter import messagebox


class RegistroApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Ejercicio 14 - Registro de Usuarios")
        self.root.geometry("450x400")

        self.users = []

        frame_top = tk.Frame(self.root)
        frame_top.pack(pady=10)

        tk.Label(frame_top, text="Nombre:").grid(row=0, column=0, padx=5)
        self.entry_name = tk.Entry(frame_top, width=25)
        self.entry_name.grid(row=0, column=1, padx=5)

        tk.Label(frame_top, text="Edad:").grid(row=1, column=0, padx=5)
        self.scale_age = tk.Scale(frame_top, from_=0, to=100, orient="horizontal")
        self.scale_age.grid(row=1, column=1, padx=5)

        tk.Label(frame_top, text="Género:").grid(row=2, column=0, padx=5)
        self.gender_var = tk.StringVar(value="Masculino")

        frame_gender = tk.Frame(frame_top)
        frame_gender.grid(row=2, column=1, columnspan=2, sticky="w")

        tk.Radiobutton(frame_gender, text="Masculino", variable=self.gender_var, value="Masculino").pack(side="left")
        tk.Radiobutton(frame_gender, text="Femenino", variable=self.gender_var, value="Femenino").pack(side="left", padx=5)
        tk.Radiobutton(frame_gender, text="Otro", variable=self.gender_var, value="Otro").pack(side="left")

        frame_buttons = tk.Frame(self.root)
        frame_buttons.pack(pady=5)

        tk.Button(frame_buttons, text="Añadir", command=self.añadir_usuario).grid(row=0, column=0, padx=5)
        tk.Button(frame_buttons, text="Eliminar", command=self.eliminar_usuario).grid(row=0, column=1, padx=5)
        tk.Button(frame_buttons, text="Salir", command=self.salir).grid(row=0, column=2, padx=5)

        frame_list = tk.Frame(self.root)
        frame_list.pack(fill="both", expand=True, padx=10, pady=10)

        scroll = tk.Scrollbar(frame_list)
        scroll.pack(side="right", fill="y")

        self.listbox_users = tk.Listbox(frame_list, yscrollcommand=scroll.set, width=50, height=10)
        self.listbox_users.pack(side="left", fill="both", expand=True)

        scroll.config(command=self.listbox_users.yview)

        menubar = tk.Menu(self.root)
        menu_file = tk.Menu(menubar, tearoff=0)
        menu_file.add_command(label="Guardar Lista", command=self.guardar_lista)
        menu_file.add_command(label="Cargar Lista", command=self.cargar_lista)
        menubar.add_cascade(label="Archivo", menu=menu_file)
        self.root.config(menu=menubar)


    def añadir_usuario(self):
        name = self.entry_name.get()
        age = self.scale_age.get()
        gender = self.gender_var.get()

        user = f"{name} - {age} años - {gender}"
        self.users.append(user)
        self.listbox_users.insert(tk.END, user)

        self.entry_name.delete(0, tk.END)

    def eliminar_usuario(self):
        selection = self.listbox_users.curselection()
        if selection:
            index = selection[0]
            self.listbox_users.delete(index)
            self.users.pop(index)
        else:
            messagebox.showinfo("Información", "Selecciona un usuario para eliminar.")

    def guardar_lista(self):
        messagebox.showinfo("Guardar Lista", "Guardar Lista")

    def cargar_lista(self):
        messagebox.showinfo("Cargar Lista", "Cargar Lista")

    def salir(self):
        self.root.destroy()


if __name__ == "__main__":
    root = tk.Tk()
    app = RegistroApp(root)
    root.mainloop()
