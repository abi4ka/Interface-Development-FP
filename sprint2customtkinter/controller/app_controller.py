from model.user_model import UserModel
from view.main_view import MainView
import threading
import time

class AppController:
    def __init__(self, root):
        self.root = root
        self.model = UserModel()
        self.view = MainView(root, self)
        self.view.update_user_list(self.model.get_users())
        self.autosave_running = False
        self.autosave_thread = None

    def add_user(self, name, age, gender, avatar_img, avatar_name):
        new_user = {
            "name": name,
            "age": age,
            "gender": gender,
            "avatar_img": avatar_img,
            "avatar_name": avatar_name,
            "text": f"{name} ({gender}, {age} años)"
        }
        self.model.add_user(new_user)
        self.view.update_user_list(self.model.get_users())

    def select_user(self, user):
        try:
            self.selected_index = self.model.get_users().index(user)
        except ValueError:
            self.selected_index = None
        self.selected_user = user
        self.view.show_preview(user)
        self.view.set_delete_enabled(self.selected_index is not None)

    def guardar_lista(self):
        self.model.save_users()
        print("Lista guardada correctamente.")

    def cargar_lista(self):
        self.model.load_users()
        self.view.update_user_list(self.model.get_users())
        print("Lista cargada correctamente.")

    def run(self):
        self.view.mainloop()

    def toggle_autosave(self):
        if not self.autosave_running:
            self.autosave_running = True
            self.autosave_thread = threading.Thread(target=self.autosave_loop, daemon=True)
            self.autosave_thread.start()
            self.view.set_autosave_status(True)
        else:
            self.autosave_running = False
            self.view.set_autosave_status(False)

    def autosave_loop(self):
        while self.autosave_running:
            time.sleep(10)
            self.model.save_users()
            self.view.after(0, lambda: self.view.show_message("Auto-guardado"))

    def stop_autosave(self):
        self.autosave_running = False

    def delete_user(self):
        if self.selected_index is None:
            return
        self.model.delete_user_by_index(self.selected_index)
        self.selected_index = None
        self.selected_user = None
        self.view.update_user_list(self.model.get_users())
        self.view.clear_preview()
        self.view.set_delete_enabled(False)

    def filtrar_usuarios(self):
        text = self.view.entry_buscar.get().strip()
        gender = self.view.option_genero.get()

        filtrados = self.model.filter_users(text, gender)
        self.view.update_user_list(filtrados)

        self.view.clear_preview()
        self.view.set_delete_enabled(False)

        self.selected_user = None
