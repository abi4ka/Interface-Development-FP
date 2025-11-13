import tkinter as tk
import customtkinter as ctk


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

        # tool bar
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

        self.btn_anadir = ctk.CTkButton(self.filter_frame, text="Añadir", width=90)
        self.btn_anadir.grid(row=0, column=5, padx=(5, 10), pady=5, sticky="e")



        self.frame_list = ctk.CTkScrollableFrame(self, label_text="Lista de Usuarios", width=250)
        self.frame_list.grid(row=2, column=0, padx=10, pady=10, sticky="ns")

        self.frame_preview = ctk.CTkFrame(self)
        self.frame_preview.grid(row=2, column=1, padx=10, pady=10, sticky="nsew")

        self.label_preview = ctk.CTkLabel(self.frame_preview, text="Previsualización", font=ctk.CTkFont(size=16, weight="bold"))
        self.label_preview.pack(pady=10)

    def update_user_list(self, users):
        for widget in self.frame_list.winfo_children():
            widget.destroy()
        for user in users:
            btn = ctk.CTkButton(self.frame_list, text=user, command=lambda u=user: self.controller.select_user(u))
            btn.pack(fill="x", pady=2, padx=5)

    def show_preview(self, user):
        self.label_preview.configure(text=f"Previsualizando: {user}")
