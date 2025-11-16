
import tkinter as tk
from doctest import master

import customtkinter as ctk


from view.add_user_window import AddUserWindow


class MainView(ctk.CTkFrame):
    def __init__(self, master, controller):
        super().__init__(master)
        self.controller = controller

        self.pack(fill="both", expand=True)

        self.grid_rowconfigure(2, weight=1)
        self.grid_columnconfigure(1, weight=1)

        menubar = tk.Menu(master)
        menu_archivo = tk.Menu(menubar, tearoff=0)
        menu_archivo.add_command(label="Guardar", command=self.controller.guardar_lista)
        menu_archivo.add_command(label="Cargar", command=self.controller.cargar_lista)
        menu_archivo.add_command(label="Salir", command=self.controller_exit)
        menubar.add_cascade(label="Archivo", menu=menu_archivo)

        menu_ayuda = tk.Menu(menubar, tearoff=0)
        menu_ayuda.add_command(label="Acerca de", command=lambda: None)
        menubar.add_cascade(label="Ayuda", menu=menu_ayuda)

        master.configure(menu=menubar)

        self.filter_frame = ctk.CTkFrame(self)
        self.filter_frame.grid(row=1, column=0, columnspan=2, sticky="ew", padx=10, pady=5)
        self.filter_frame.grid_columnconfigure(5, weight=1)

        self.label_buscar = ctk.CTkLabel(self.filter_frame, text="Buscar:")
        self.label_buscar.grid(row=0, column=0, padx=(10, 5), pady=5)
        self.entry_buscar = ctk.CTkEntry(self.filter_frame, width=150)
        self.entry_buscar.grid(row=0, column=1, padx=5, pady=5)
        self.entry_buscar.bind("<KeyRelease>", lambda e: self.controller.filtrar_usuarios())

        self.label_genero = ctk.CTkLabel(self.filter_frame, text="Género:")
        self.label_genero.grid(row=0, column=2, padx=(20, 5), pady=5)

        self.option_genero = ctk.CTkOptionMenu(
            self.filter_frame,
            values=["Todos", "Masculino", "Femenino", "Otro"],
            command=lambda _: self.controller.filtrar_usuarios()
        )
        self.option_genero.grid(row=0, column=3, padx=5, pady=5)

        self.filter_frame.grid_columnconfigure(4, weight=1)
        buttons_frame = ctk.CTkFrame(self.filter_frame, fg_color="transparent")
        buttons_frame.grid(row=0, column=5, padx=(5, 10), pady=5, sticky="e")

        self.btn_eliminar = ctk.CTkButton(buttons_frame, text="Eliminar", width=90, command=self.controller.delete_user)
        self.btn_eliminar.pack(side="left", padx=5)
        self.set_delete_enabled(False)

        self.btn_anadir = ctk.CTkButton(buttons_frame, text="Añadir", width=90, command=self.open_add_window)
        self.btn_anadir.pack(side="left", padx=5)

        self.frame_list = ctk.CTkScrollableFrame(self, label_text="Lista de Usuarios (0)", width=250)
        self.frame_list.grid(row=2, column=0, padx=10, pady=10, sticky="ns")

        self.frame_preview = ctk.CTkFrame(self)
        self.frame_preview.grid(row=2, column=1, padx=10, pady=10, sticky="nsew")
        self.label_preview = ctk.CTkLabel(self.frame_preview, text="Previsualización", font=ctk.CTkFont(size=16, weight="bold"))
        self.label_preview.pack(pady=10)
        self.label_avatar = ctk.CTkLabel(self.frame_preview, text="")
        self.label_avatar.pack(pady=10)

        self.bottom_panel = ctk.CTkFrame(self, height=40)
        self.bottom_panel.grid(row=3, column=0, columnspan=2, sticky="ew")
        self.grid_rowconfigure(3, weight=0)

        self.autosave_button = ctk.CTkButton(
            self.bottom_panel,
            text="Auto-guardar: OFF",
            width=140,
            command=self.controller.toggle_autosave
        )
        self.autosave_button.pack(side="left", padx=10, pady=5)

    def open_add_window(self):
        AddUserWindow(self, self.controller)

    def controller_exit(self):
        self.controller.stop_autosave()
        self.destroy()

    def update_user_list(self, users):
        self.frame_list.configure(label_text=f"Lista de Usuarios ({len(users)})")

        for widget in self.frame_list.winfo_children():
            widget.destroy()

        for user in users:
            btn = ctk.CTkButton(self.frame_list, text=user["text"],
                                command=lambda u=user: self.controller.select_user(u))
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

    def set_autosave_status(self, enabled):
        if enabled:
            self.autosave_button.configure(text="Auto-guardar: ON", fg_color="green")
        else:
            self.autosave_button.configure(text="Auto-guardar: OFF", fg_color="red")

    def show_message(self, text):
        print(text)

    def set_delete_enabled(self, enabled: bool):
        if enabled:
            self.btn_eliminar.configure(state="normal")
        else:
            self.btn_eliminar.configure(state="disabled")

    def clear_preview(self):
        for widget in self.frame_preview.winfo_children():
            widget.destroy()
        self.label_preview = ctk.CTkLabel(self.frame_preview, text="Previsualización",
                                          font=ctk.CTkFont(size=16, weight="bold"))
        self.label_preview.pack(pady=10)
        self.label_avatar = ctk.CTkLabel(self.frame_preview, text="")
        self.label_avatar.pack(pady=10)