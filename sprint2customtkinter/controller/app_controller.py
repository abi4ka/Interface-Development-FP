from model.user_model import UserModel
from view.main_view import MainView


class AppController:
    def __init__(self):
        self.model = UserModel()
        self.view = MainView(self)
        self.view.update_user_list(self.model.get_users())

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
