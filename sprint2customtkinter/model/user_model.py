import os
import csv
from PIL import Image
import customtkinter as ctk

AVATAR_PATH = os.path.join(os.path.dirname(os.path.dirname(__file__)), "assets")
CSV_FILE = "usuarios.csv"  # теперь имя соответствует заданию

# -------------------------------
# Класс пользователя
# -------------------------------
class Usuario:
    def __init__(self, nombre: str, edad: int, genero: str, avatar: str):
        self.nombre = nombre.strip()
        self.edad = edad
        self.genero = genero
        self.avatar = avatar  # имя файла в assets
        self.avatar_img = None  # CTkImage, загружается отдельно

    def cargar_avatar(self, size=(60, 60)):
        path = os.path.join(AVATAR_PATH, self.avatar)
        if os.path.exists(path):
            self.avatar_img = ctk.CTkImage(Image.open(path), size=size)
        else:
            self.avatar_img = None

# -------------------------------
# Класс управления пользователями
# -------------------------------
class GestorUsuarios:
    def __init__(self):
        self._usuarios = []

    def listar(self):
        return list(self._usuarios)

    def añadir(self, usuario: Usuario):
        # минимальная валидация
        if not usuario.nombre:
            raise ValueError("El nombre no puede estar vacío")
        if not (0 <= usuario.edad <= 100):
            raise ValueError("Edad fuera de rango (0-100)")
        if usuario.genero not in ["Masculino", "Femenino", "Otro"]:
            raise ValueError("Género inválido")
        usuario.cargar_avatar()
        self._usuarios.append(usuario)

    def eliminar(self, indice: int):
        if 0 <= indice < len(self._usuarios):
            del self._usuarios[indice]
        else:
            raise IndexError("Índice fuera de rango")

    def actualizar(self, indice: int, usuario_actualizado: Usuario):
        if 0 <= indice < len(self._usuarios):
            usuario_actualizado.cargar_avatar()
            self._usuarios[indice] = usuario_actualizado
        else:
            raise IndexError("Índice fuera de rango")

    def guardar_csv(self, ruta: str = CSV_FILE):
        try:
            with open(ruta, "w", encoding="utf-8", newline="") as f:
                writer = csv.writer(f)
                writer.writerow(["nombre", "edad", "genero", "avatar"])
                for u in self._usuarios:
                    writer.writerow([u.nombre, u.edad, u.genero, u.avatar])
        except Exception as e:
            print("Error guardando CSV:", e)

    def cargar_csv(self, ruta: str = CSV_FILE):
        self._usuarios.clear()
        try:
            with open(ruta, "r", encoding="utf-8", newline="") as f:
                reader = csv.DictReader(f)
                for row in reader:
                    if not {"nombre","edad","genero","avatar"} <= row.keys():
                        continue  # fila corrupta
                    try:
                        usuario = Usuario(
                            nombre=row["nombre"],
                            edad=int(row["edad"]),
                            genero=row["genero"],
                            avatar=row["avatar"]
                        )
                        usuario.cargar_avatar()
                        self._usuarios.append(usuario)
                    except Exception:
                        continue  # fila inválida
        except FileNotFoundError:
            pass

    def filtrar(self, texto_buscar: str, genero: str):
        texto_buscar = texto_buscar.lower()
        result = []
        for u in self._usuarios:
            if texto_buscar not in u.nombre.lower():
                continue
            if genero != "Todos" and u.genero != genero:
                continue
            result.append(u)
        return result
