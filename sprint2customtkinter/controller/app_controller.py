from model.user_model import GestorUsuarios, Usuario
from view.edit_user_window import EditUserWindow
from view.main_view import MainView
from view.add_user_window import AddUserWindow
import threading
import time


class AppController:
    def __init__(self, root):
        self.root = root
        self.model = GestorUsuarios()
        self.selected_user = None
        self.selected_index = None
        self.autosave_running = False
        self.autosave_thread = None

        # Инициализация view
        self.view = MainView(root, self)
        self.view.btn_anadir.configure(command=self.open_add_modal)
        self.view.btn_eliminar.configure(command=self.delete_selected)
        self.view.autosave_button.configure(command=self.toggle_autosave)

        # Загрузка списка пользователей
        self.model.cargar_csv()
        self.refresh_user_list()

    # -----------------------
    # Методы для работы с пользователями
    # -----------------------
    def refresh_user_list(self):
        usuarios = self.model.listar()
        self.view.update_user_list(usuarios, self.select_user, self.open_edit_modal)
        self.view.clear_preview()
        self.view.set_delete_enabled(False)
        self.selected_user = None
        self.selected_index = None

    def select_user(self, usuario: Usuario):
        try:
            self.selected_index = self.model.listar().index(usuario)
            self.selected_user = usuario
        except ValueError:
            self.selected_index = None
            self.selected_user = None

        self.view.show_preview(usuario)
        self.view.set_delete_enabled(self.selected_index is not None)

    def update_user(self, usuario: Usuario, nombre, edad, genero, avatar_img, avatar_name):
        if self.selected_index is not None:
            # Обновляем объект пользователя
            usuario.nombre = nombre
            usuario.edad = edad
            usuario.genero = genero
            usuario.avatar = avatar_name
            usuario.avatar_img = avatar_img
            self.refresh_user_list()

    def open_add_modal(self):
        AddUserWindow(self.root, self)

    def add_user(self, nombre, edad, genero, avatar_img, avatar_name):
        try:
            usuario = Usuario(nombre=nombre, edad=edad, genero=genero, avatar=avatar_name)
            usuario.avatar_img = avatar_img
            self.model.añadir(usuario)
            self.refresh_user_list()
        except ValueError as e:
            self.view.show_message(str(e))

    def delete_selected(self):
        if self.selected_index is not None:
            try:
                self.model.eliminar(self.selected_index)
                self.refresh_user_list()
            except IndexError:
                self.view.show_message("Error al eliminar usuario")

    def filtrar(self):
        texto = self.view.entry_buscar.get().strip()
        genero = self.view.option_genero.get()
        usuarios_filtrados = self.model.filtrar(texto, genero)

        # Передаем объекты Usuario напрямую
        self.view.update_user_list(usuarios_filtrados, self.select_user, self.open_edit_modal)
        self.view.clear_preview()
        self.view.set_delete_enabled(False)
        self.selected_user = None
        self.selected_index = None

    # -----------------------
    # Меню
    # -----------------------
    def menu_guardar(self):
        self.model.guardar_csv()
        self.view.show_message("Lista guardada correctamente.")

    def menu_cargar(self):
        self.model.cargar_csv()
        self.refresh_user_list()
        self.view.show_message("Lista cargada correctamente.")

    def menu_salir(self):
        self.stop_autosave()
        self.root.destroy()

    def menu_acerca_de(self):
        self.view.show_message("Registro de Usuarios v1.0")

    # -----------------------
    # Авто-сохранение
    # -----------------------
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
            self.model.guardar_csv()
            self.root.after(0, lambda: self.view.show_message("Auto-guardado"))

    def stop_autosave(self):
        self.autosave_running = False

    def open_edit_modal(self, user):
        EditUserWindow(self.root, self, user)