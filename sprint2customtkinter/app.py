from controller.app_controller import AppController
import customtkinter as ctk

if __name__ == "__main__":
    ctk.set_appearance_mode("Light")
    ctk.set_default_color_theme("blue")

    root = ctk.CTk()
    root.title("Ejercicio 14 - Registro de Usuarios (MVC)")
    root.geometry("800x500")
    root.minsize(700, 400)

    controller = AppController(root)
    root.mainloop()
