from model.user_model import UserModel
from view.main_view import MainView

class AppController:
    def __init__(self):
        self.model = UserModel()
        self.view = MainView(self)
        self.view.update_user_list(self.model.get_users())

    def select_user(self, user):
        self.view.show_preview(user)

    def exit_app(self):
        self.view.destroy()

    def run(self):
        self.view.mainloop()
