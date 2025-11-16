from model.user_model import UserModel
from view.main_view import MainView
import threading
import time

class AppController:
    def __init__(self):
        self.model = UserModel()
        self.view = MainView(self)
        self.view.update_user_list(self.model.get_users())
        self.autosave_running = False
        self.autosave_thread = None

    def add_user(self, name, age, gender, avatar):
        new_user = {
            "name": name,
            "age": age,
            "gender": gender,
            "avatar_img": avatar,
            "text": f"{name} ({gender}, {age} años)"
        }
        self.model.add_user(new_user)
        self.view.update_user_list(self.model.get_users())

    def select_user(self, user):
        self.view.show_preview(user)

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