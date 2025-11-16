import os

AVATAR_PATH = os.path.join(os.path.dirname(os.path.dirname(__file__)), "assets")

class UserModel:
    def __init__(self):
        self.users = []

    def add_user(self, user):
        self.users.append(user)

    def get_users(self):
        return self.users

    def save_users(self):
        with open("users.csv", "w", encoding="utf-8") as f:
            for u in self.users:
                name = u["name"]
                age = u["age"]
                gender = u["gender"]
                avatar = u.get("avatar_name", "avatar1.png")
                f.write(f"{name},{age},{gender},{avatar}\n")

    def load_users(self):
        from PIL import Image
        import customtkinter as ctk

        self.users.clear()

        try:
            with open("users.csv", "r", encoding="utf-8") as f:
                for line in f:
                    name, age, gender, avatar_name = line.strip().split(",")

                    avatar_path = os.path.join(AVATAR_PATH, avatar_name)

                    avatar_img = None
                    if os.path.exists(avatar_path):
                        avatar_img = ctk.CTkImage(Image.open(avatar_path), size=(60, 60))

                    self.users.append({
                        "name": name,
                        "age": int(age),
                        "gender": gender,
                        "avatar_img": avatar_img,
                        "avatar_name": avatar_name,
                        "text": f"{name} ({gender}, {age} años)"
                    })
        except FileNotFoundError:
            pass

    def delete_user_by_index(self, index):
        try:
            del self.users[index]
        except IndexError:
            pass

    def delete_user_by_name(self, name):
        self.users = [u for u in self.users if u.get("name") != name]

    def filter_users(self, text_search, gender):
        text_search = text_search.lower()

        result = []
        for u in self.users:
            if text_search not in u["name"].lower():
                continue

            if gender != "Todos" and u["gender"] != gender:
                continue

            result.append(u)

        return result