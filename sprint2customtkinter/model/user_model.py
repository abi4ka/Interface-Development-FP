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
                f.write(f"{name},{age},{gender}\n")

    def load_users(self):
        self.users.clear()
        try:
            with open("users.csv", "r", encoding="utf-8") as f:
                for line in f:
                    name, age, gender = line.strip().split(",")
                    self.users.append({
                        "name": name,
                        "age": int(age),
                        "gender": gender,
                        "avatar_img": None,
                        "text": f"{name} ({gender}, {age} años)"
                    })
        except FileNotFoundError:
            pass