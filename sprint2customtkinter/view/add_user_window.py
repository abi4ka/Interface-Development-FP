import tkinter as tk
import customtkinter as ctk

import os
from PIL import Image

class AddUserWindow(ctk.CTkToplevel):
    def __init__(self, parent, controller):
        super().__init__(parent)
        self.controller = controller
        self.title("Añadir Usuario")
        self.geometry("400x500")
        self.resizable(False, False)
        self.grab_set()

        ctk.CTkLabel(self, text="Nombre:").pack(pady=(20, 5))
        self.entry_name = ctk.CTkEntry(self, width=250)
        self.entry_name.pack()

        ctk.CTkLabel(self, text="Edad:").pack(pady=(15, 5))
        self.scale_age = ctk.CTkSlider(self, from_=0, to=100, number_of_steps=100)
        self.scale_age.set(25)
        self.scale_age.pack(pady=5)
        self.age_label = ctk.CTkLabel(self, text="25 años")
        self.age_label.pack()
        self.scale_age.configure(command=lambda v: self.age_label.configure(text=f"{int(float(v))} años"))

        ctk.CTkLabel(self, text="Género:").pack(pady=(15, 5))
        self.gender_var = tk.StringVar(value="Masculino")
        gender_frame = ctk.CTkFrame(self)
        gender_frame.pack(pady=5)
        ctk.CTkRadioButton(gender_frame, text="Masculino", variable=self.gender_var, value="Masculino").pack(side="left", padx=5)
        ctk.CTkRadioButton(gender_frame, text="Femenino", variable=self.gender_var, value="Femenino").pack(side="left", padx=5)
        ctk.CTkRadioButton(gender_frame, text="Otro", variable=self.gender_var, value="Otro").pack(side="left", padx=5)

        ctk.CTkLabel(self, text="Avatar:").pack(pady=(15, 5))
        self.avatar_frame = ctk.CTkFrame(self)
        self.avatar_frame.pack(pady=5)

        res_path = os.path.join(os.path.dirname(os.path.dirname(__file__)), "assets")

        self.avatars = [
            ctk.CTkImage(Image.open(os.path.join(res_path, "avatar1.png")), size=(60, 60)),
            ctk.CTkImage(Image.open(os.path.join(res_path, "avatar2.png")), size=(60, 60)),
            ctk.CTkImage(Image.open(os.path.join(res_path, "avatar3.png")), size=(60, 60))
        ]

        self.selected_avatar_index = 0
        self.avatar_buttons = []
        for a, img in enumerate(self.avatars):
            btn = ctk.CTkButton(
                self.avatar_frame,
                image=img,
                text="",
                width=70,
                height=70,
                fg_color=("gray75", "gray25") if a != self.selected_avatar_index else ("blue", "blue"),
                command=lambda i=a: self.select_avatar(i)
            )
            btn.grid(row=0, column=a, padx=5)
            self.avatar_buttons.append(btn)

        self.selected_avatar = self.avatars[self.selected_avatar_index]

        ctk.CTkButton(self, text="Confirmar", command=self.confirm).pack(pady=20)

    def select_avatar(self, index):
        self.selected_avatar_index = index
        self.selected_avatar = self.avatars[index]
        for i, btn in enumerate(self.avatar_buttons):
            btn.configure(fg_color=("blue", "blue") if i == index else ("gray75", "gray25"))

    def confirm(self):
        name = self.entry_name.get().strip()
        if not name:
            return

        age = int(float(self.scale_age.get()))
        gender = self.gender_var.get()

        avatar_img = self.selected_avatar
        avatar_name = f"avatar{self.selected_avatar_index + 1}.png"

        self.controller.add_user(name, age, gender, avatar_img, avatar_name)
        self.destroy()