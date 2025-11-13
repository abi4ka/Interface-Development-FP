import os
import tkinter as tk
import customtkinter as ctk
from PIL import Image


class MainView(ctk.CTk):
    def __init__(self, controller):
        super().__init__()
        ctk.set_appearance_mode("Light")
        ctk.set_default_color_theme("blue")
        self.controller = controller
        self.title("Ejercicio 14 - Registro de Usuarios (MVC)")
        self.geometry("800x500")
        self.minsize(700, 400)
        self.grid_rowconfigure(2, weight=1)
        self.grid_columnconfigure(1, weight=1)

        menubar = tk.Menu(self)
        menu_archivo = tk.Menu(menubar, tearoff=0)
        menu_archivo.add_command(label="Guardar Lista", command=lambda: None)
        menu_archivo.add_command(label="Cargar Lista", command=lambda: None)
        menubar.add_cascade(label="Archivo", menu=menu_archivo)
        menu_ayuda = tk.Menu(menubar, tearoff=0)
        menu_ayuda.add_command(label="Acerca de", command=lambda: None)
        menubar.add_cascade(label="Ayuda", menu=menu_ayuda)
        self.config(menu=menubar)

        self.filter_frame = ctk.CTkFrame(self)
        self.filter_frame.grid(row=1, column=0, columnspan=2, sticky="ew", padx=10, pady=5)
        self.filter_frame.grid_columnconfigure(5, weight=1)

        self.label_buscar = ctk.CTkLabel(self.filter_frame, text="Buscar:")
        self.label_buscar.grid(row=0, column=0, padx=(10, 5), pady=5)
        self.entry_buscar = ctk.CTkEntry(self.filter_frame, width=150)
        self.entry_buscar.grid(row=0, column=1, padx=5, pady=5)

        self.label_genero = ctk.CTkLabel(self.filter_frame, text="Género:")
        self.label_genero.grid(row=0, column=2, padx=(20, 5), pady=5)
        self.option_genero = ctk.CTkOptionMenu(self.filter_frame, values=["Todos", "Masculino", "Femenino"])
        self.option_genero.grid(row=0, column=3, padx=5, pady=5)

        self.btn_eliminar = ctk.CTkButton(self.filter_frame, text="Eliminar", width=90)
        self.btn_eliminar.grid(row=0, column=4, padx=(20, 5), pady=5)
        self.btn_anadir = ctk.CTkButton(self.filter_frame, text="Añadir", width=90, command=self.open_add_window)
        self.btn_anadir.grid(row=0, column=5, padx=(5, 10), pady=5, sticky="e")

        self.frame_list = ctk.CTkScrollableFrame(self, label_text="Lista de Usuarios", width=250)
        self.frame_list.grid(row=2, column=0, padx=10, pady=10, sticky="ns")

        self.frame_preview = ctk.CTkFrame(self)
        self.frame_preview.grid(row=2, column=1, padx=10, pady=10, sticky="nsew")
        self.label_preview = ctk.CTkLabel(self.frame_preview, text="Previsualización", font=ctk.CTkFont(size=16, weight="bold"))
        self.label_preview.pack(pady=10)
        self.label_avatar = ctk.CTkLabel(self.frame_preview, text="")
        self.label_avatar.pack(pady=10)

    def open_add_window(self):
        AddUserWindow(self, self.controller)

    def update_user_list(self, users):
        for widget in self.frame_list.winfo_children():
            widget.destroy()
        for user in users:
            btn = ctk.CTkButton(self.frame_list, text=user["text"], command=lambda u=user: self.controller.select_user(u))
            btn.pack(fill="x", pady=2, padx=5)

    def show_preview(self, user):
        for widget in self.frame_preview.winfo_children():
            widget.destroy()

        if user.get("avatar_img"):
            self.label_avatar = ctk.CTkLabel(self.frame_preview, image=user["avatar_img"], text="")
        else:
            self.label_avatar = ctk.CTkLabel(self.frame_preview, text="Sin avatar")
        self.label_avatar.pack(pady=10)

        self.label_nombre = ctk.CTkLabel(self.frame_preview, text=f"Nombre: {user['name']}", font=ctk.CTkFont(size=14),
                                         anchor="w", justify="left")
        self.label_nombre.pack(pady=5, fill="x", padx=10)

        self.label_edad = ctk.CTkLabel(self.frame_preview, text=f"Edad: {user['age']} años", font=ctk.CTkFont(size=14),
                                       anchor="w", justify="left")
        self.label_edad.pack(pady=5, fill="x", padx=10)

        self.label_genero = ctk.CTkLabel(self.frame_preview, text=f"Género: {user['gender']}",
                                         font=ctk.CTkFont(size=14), anchor="w", justify="left")
        self.label_genero.pack(pady=5, fill="x", padx=10)


class AddUserWindow(ctk.CTkToplevel):
    def __init__(self, parent, controller):
        super().__init__(parent)
        self.controller = controller
        self.title("Añadir Usuario")
        self.geometry("400x500")
        self.resizable(False, False)
        self.grab_set()

        ctk.CTkLabel(self, text="Nombre:").pack(pady=(20, 5))
        self.entry_name = ctk.CTkEntry(self, width=250)
        self.entry_name.pack()

        ctk.CTkLabel(self, text="Edad:").pack(pady=(15, 5))
        self.scale_age = ctk.CTkSlider(self, from_=0, to=100, number_of_steps=100)
        self.scale_age.set(25)
        self.scale_age.pack(pady=5)
        self.age_label = ctk.CTkLabel(self, text="25 años")
        self.age_label.pack()
        self.scale_age.configure(command=lambda v: self.age_label.configure(text=f"{int(float(v))} años"))

        ctk.CTkLabel(self, text="Género:").pack(pady=(15, 5))
        self.gender_var = tk.StringVar(value="Masculino")
        gender_frame = ctk.CTkFrame(self)
        gender_frame.pack(pady=5)
        ctk.CTkRadioButton(gender_frame, text="Masculino", variable=self.gender_var, value="Masculino").pack(side="left", padx=5)
        ctk.CTkRadioButton(gender_frame, text="Femenino", variable=self.gender_var, value="Femenino").pack(side="left", padx=5)
        ctk.CTkRadioButton(gender_frame, text="Otro", variable=self.gender_var, value="Otro").pack(side="left", padx=5)

        ctk.CTkLabel(self, text="Avatar:").pack(pady=(15, 5))
        self.avatar_frame = ctk.CTkFrame(self)
        self.avatar_frame.pack(pady=5)

        res_path = os.path.join(os.path.dirname(os.path.dirname(__file__)), "res")

        self.avatars = [
            ctk.CTkImage(Image.open(os.path.join(res_path, "avatar1.png")), size=(60, 60)),
            ctk.CTkImage(Image.open(os.path.join(res_path, "avatar2.png")), size=(60, 60)),
            ctk.CTkImage(Image.open(os.path.join(res_path, "avatar3.png")), size=(60, 60))
        ]

        self.selected_avatar_index = 0
        self.avatar_buttons = []
        for a, img in enumerate(self.avatars):
            btn = ctk.CTkButton(
                self.avatar_frame,
                image=img,
                text="",
                width=70,
                height=70,
                fg_color=("gray75", "gray25") if a != self.selected_avatar_index else ("blue", "blue"),
                command=lambda i=a: self.select_avatar(i)
            )
            btn.grid(row=0, column=a, padx=5)
            self.avatar_buttons.append(btn)

        self.selected_avatar = self.avatars[self.selected_avatar_index]

        ctk.CTkButton(self, text="Confirmar", command=self.confirm).pack(pady=20)

    def select_avatar(self, index):
        self.selected_avatar_index = index
        self.selected_avatar = self.avatars[index]
        for i, btn in enumerate(self.avatar_buttons):
            btn.configure(fg_color=("blue", "blue") if i == index else ("gray75", "gray25"))

    def confirm(self):
        name = self.entry_name.get().strip()
        if not name:
            return
        age = int(float(self.scale_age.get()))
        gender = self.gender_var.get()
        avatar = self.selected_avatar
        self.controller.add_user(name, age, gender, avatar)
        self.destroy()