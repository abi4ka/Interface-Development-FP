import customtkinter as ctk

class MainView(ctk.CTk):
    def __init__(self, controller):
        super().__init__()
        ctk.set_appearance_mode("System")
        ctk.set_default_color_theme("blue")
        self.controller = controller
        self.title("Ejercicio 14 - Registro de Usuarios (MVC)")
        self.geometry("600x400")
        self.grid_columnconfigure(1, weight=1)
        self.grid_rowconfigure(0, weight=1)

        self.frame_list = ctk.CTkScrollableFrame(self, label_text="Lista de Usuarios")
        self.frame_list.grid(row=0, column=0, padx=10, pady=10, sticky="ns")

        self.frame_preview = ctk.CTkFrame(self)
        self.frame_preview.grid(row=0, column=1, padx=10, pady=10, sticky="nsew")

        self.label_preview = ctk.CTkLabel(self.frame_preview, text="Previsualización")
        self.label_preview.pack(pady=10)

        self.btn_exit = ctk.CTkButton(self, text="Salir", command=self.controller.exit_app)
        self.btn_exit.grid(row=1, column=0, columnspan=2, pady=10)

    def update_user_list(self, users):
        for widget in self.frame_list.winfo_children():
            widget.destroy()
        for i, user in enumerate(users):
            btn = ctk.CTkButton(self.frame_list, text=user, command=lambda u=user: self.controller.select_user(u))
            btn.pack(fill="x", pady=2, padx=5)

    def show_preview(self, user):
        self.label_preview.configure(text=f"Previsualizando: {user}")
