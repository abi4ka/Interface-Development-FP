from model.user_model import UserModel
from view.main_view import MainView
import threading
import time
from view.add_user_window import AddUserWindow


class AppController:
    def __init__(self, root):
        self.root = root
        self.model = UserModel()
        self.selected_user = None
        self.selected_index = None
        self.autosave_running = False
        self.autosave_thread = None

        self.view = MainView(root, self)
        self.view.btn_anadir.configure(command=self.open_add_modal)
        self.view.btn_eliminar.configure(command=self.delete_selected)
        self.view.autosave_button.configure(command=self.toggle_autosave)

        # Загрузка списка
        self.refresh_user_list()

    # Вспомогательные методы
    def refresh_user_list(self):
        users = self.model.get_users()
        self.view.update_user_list(users, self.select_user)
        self.view.clear_preview()
        self.view.set_delete_enabled(False)
        self.selected_user = None
        self.selected_index = None

    def select_user(self, user):
        try:
            self.selected_index = self.model.get_users().index(user)
        except ValueError:
            self.selected_index = None
        self.selected_user = user
        self.view.show_preview(user)
        self.view.set_delete_enabled(self.selected_index is not None)

    def open_add_modal(self):
        AddUserWindow(self.root, self)

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
        self.refresh_user_list()

    def delete_selected(self):
        if self.selected_index is not None:
            self.model.delete_user_by_index(self.selected_index)
            self.refresh_user_list()

    def filtrar(self):
        text = self.view.entry_buscar.get().strip()
        gender = self.view.option_genero.get()
        filtered = self.model.filter_users(text, gender)
        self.view.update_user_list(filtered, self.select_user)
        self.view.clear_preview()
        self.view.set_delete_enabled(False)
        self.selected_user = None
        self.selected_index = None

    # Меню
    def menu_guardar(self):
        self.model.save_users()
        self.view.show_message("Lista guardada correctamente.")

    def menu_cargar(self):
        self.model.load_users()
        self.refresh_user_list()
        self.view.show_message("Lista cargada correctamente.")

    def menu_salir(self):
        self.stop_autosave()
        self.root.destroy()

    def menu_acerca_de(self):
        self.view.show_message("Registro de Usuarios v1.0")

    # Авто-сохранение
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
            self.root.after(0, lambda: self.view.show_message("Auto-guardado"))

    def stop_autosave(self):
        self.autosave_running = False
