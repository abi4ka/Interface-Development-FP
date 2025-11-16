import tkinter as tk
import customtkinter as ctk


class MainView(ctk.CTkFrame):
    def __init__(self, master, controller):
        super().__init__(master)
        self.controller = controller
        self.pack(fill="both", expand=True)

        self.grid_rowconfigure(2, weight=1)
        self.grid_columnconfigure(1, weight=1)

        menubar = tk.Menu(master)
        menu_archivo = tk.Menu(menubar, tearoff=0)
        menu_archivo.add_command(label="Guardar", command=lambda: self.controller.menu_guardar())
        menu_archivo.add_command(label="Cargar", command=lambda: self.controller.menu_cargar())
        menu_archivo.add_command(label="Salir", command=lambda: self.controller.menu_salir())
        menubar.add_cascade(label="Archivo", menu=menu_archivo)

        menu_ayuda = tk.Menu(menubar, tearoff=0)
        menu_ayuda.add_command(label="Acerca de", command=lambda: self.controller.menu_acerca_de())
        menubar.add_cascade(label="Ayuda", menu=menu_ayuda)
        master.configure(menu=menubar)

        self.filter_frame = ctk.CTkFrame(self)
        self.filter_frame.grid(row=1, column=0, columnspan=2, sticky="ew", padx=10, pady=5)
        self.filter_frame.grid_columnconfigure(5, weight=1)

        self.label_buscar = ctk.CTkLabel(self.filter_frame, text="Buscar:")
        self.label_buscar.grid(row=0, column=0, padx=(10, 5), pady=5)
        self.entry_buscar = ctk.CTkEntry(self.filter_frame, width=150)
        self.entry_buscar.grid(row=0, column=1, padx=5, pady=5)
        self.entry_buscar.bind("<KeyRelease>", lambda e: self.controller.filtrar())

        self.label_genero = ctk.CTkLabel(self.filter_frame, text="Género:")
        self.label_genero.grid(row=0, column=2, padx=(20, 5), pady=5)
        self.option_genero = ctk.CTkOptionMenu(self.filter_frame, values=["Todos", "Masculino", "Femenino", "Otro"], command=lambda _: self.controller.filtrar())
        self.option_genero.grid(row=0, column=3, padx=5, pady=5)

        buttons_frame = ctk.CTkFrame(self.filter_frame, fg_color="transparent")
        buttons_frame.grid(row=0, column=5, padx=(5, 10), pady=5, sticky="e")

        self.btn_eliminar = ctk.CTkButton(buttons_frame, text="Eliminar", width=90)
        self.btn_eliminar.pack(side="left", padx=5)
        self.set_delete_enabled(False)

        self.btn_anadir = ctk.CTkButton(buttons_frame, text="Añadir", width=90)
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

        self.autosave_button = ctk.CTkButton(self.bottom_panel, text="Auto-guardar: OFF", width=140)
        self.autosave_button.pack(side="left", padx=10, pady=5)

    def set_delete_enabled(self, enabled: bool):
        self.btn_eliminar.configure(state="normal" if enabled else "disabled")

    def set_autosave_status(self, enabled: bool):
        self.autosave_button.configure(text="Auto-guardar: ON" if enabled else "Auto-guardar: OFF",
                                       fg_color="green" if enabled else "red")

    def update_user_list(self, users, on_select_callback):
        self.frame_list.configure(label_text=f"Lista de Usuarios ({len(users)})")
        for w in self.frame_list.winfo_children():
            w.destroy()
        for user in users:
            btn = ctk.CTkButton(self.frame_list, text=user["text"], command=lambda u=user: on_select_callback(u))
            btn.pack(fill="x", pady=2, padx=5)

    def show_preview(self, usuario):
        for w in self.frame_preview.winfo_children():
            w.destroy()

        self.label_preview = ctk.CTkLabel(
            self.frame_preview, text="Previsualización",
            font=ctk.CTkFont(size=16, weight="bold")
        )
        self.label_preview.pack(pady=10)

        if usuario.avatar_img:
            label_avatar = ctk.CTkLabel(self.frame_preview, image=usuario.avatar_img, text="")
        else:
            label_avatar = ctk.CTkLabel(self.frame_preview, text="Sin avatar")
        label_avatar.pack(pady=10)

        ctk.CTkLabel(
            self.frame_preview, text=f"Nombre: {usuario.nombre}",
            font=ctk.CTkFont(size=14), anchor="w", justify="left"
        ).pack(pady=5, fill="x", padx=10)

        ctk.CTkLabel(
            self.frame_preview, text=f"Edad: {usuario.edad} años",
            font=ctk.CTkFont(size=14), anchor="w", justify="left"
        ).pack(pady=5, fill="x", padx=10)

        ctk.CTkLabel(
            self.frame_preview, text=f"Género: {usuario.genero}",
            font=ctk.CTkFont(size=14), anchor="w", justify="left"
        ).pack(pady=5, fill="x", padx=10)

    def clear_preview(self):
        for w in self.frame_preview.winfo_children():
            w.destroy()
        self.label_preview = ctk.CTkLabel(self.frame_preview, text="Previsualización", font=ctk.CTkFont(size=16, weight="bold"))
        self.label_preview.pack(pady=10)

    def show_message(self, param):
        print(param)

    def update_user_list(self, usuarios, on_select_callback, on_edit_callback):
        self.frame_list.configure(label_text=f"Lista de Usuarios ({len(usuarios)})")
        for w in self.frame_list.winfo_children():
            w.destroy()

        for u in usuarios:
            text = f"{u.nombre} ({u.genero}, {u.edad} años)"
            btn = ctk.CTkButton(
                self.frame_list,
                text=text,
                command=lambda u=u: on_select_callback(u)
            )
            btn.pack(fill="x", pady=2, padx=5)

            btn.bind("<Double-1>", lambda e, u=u: on_edit_callback(u))
