import tkinter as tk
from tkinter import ttk
from PIL import Image, ImageTk
from ventana import ventana
import os


class MainWindow:
    def __init__(self):
        self.root = tk.Tk()
        self.root.title("ESPERAR PARA SALVARSE - EPS")
        self.root.geometry("1024x768")

        # Configurar el grid principal
        self.root.grid_columnconfigure(1, weight=3)  # La columna del contenido principal será más ancha
        self.root.grid_rowconfigure(1, weight=1)

        # Frame Superior
        self.create_header()

        # Frame Lateral Izquierdo (Menú)
        self.create_sidebar()

        # Frame Central (Contenido Principal)
        self.create_main_content()

        # Frame Inferior (Datos de Contacto)
        self.create_footer()

    def create_header(self):
        header_frame = ttk.Frame(self.root)
        header_frame.grid(row=0, column=0, columnspan=2, sticky="ew", padx=10, pady=5)

        # Título principal
        title_label = ttk.Label(
            header_frame,
            text="ESPERAR PARA SALVARSE",
            font=('Helvetica', 24, 'bold')
        )
        title_label.pack(side=tk.LEFT, padx=10)

        # Botón de acceso
        access_button = ttk.Button(
            header_frame,
            text="Acceder",
            command=self.show_login
        )
        access_button.pack(side=tk.RIGHT, padx=10)

    def create_sidebar(self):
        sidebar_frame = ttk.Frame(self.root, relief="groove", borderwidth=1)
        sidebar_frame.grid(row=1, column=0, sticky="ns", padx=10, pady=5)

        # Botones del menú
        self.create_menu_button(sidebar_frame, "EMPRESAS", "Gestión de empresas afiliadas", self.show_empresas)
        self.create_menu_button(sidebar_frame, "COTIZANTES", "Gestión de cotizantes", self.show_cotizantes)
        self.create_menu_button(sidebar_frame, "BANCOS", "Gestión de información bancaria", self.show_bancos)

    def create_menu_button(self, parent, text, tooltip, command):
        frame = ttk.Frame(parent)
        frame.pack(fill=tk.X, pady=5)

        button = ttk.Button(frame, text=text, command=command)
        button.pack(fill=tk.X)

        info_label = ttk.Label(
            frame,
            text=tooltip,
            wraplength=200,
            justify=tk.LEFT,
            font=('Helvetica', 9)
        )
        info_label.pack(fill=tk.X, padx=5)

    def create_main_content(self):
        content_frame = ttk.Frame(self.root, relief="groove", borderwidth=1)
        content_frame.grid(row=1, column=1, sticky="nsew", padx=10, pady=5)

        # Título del contenido
        content_title = ttk.Label(
            content_frame,
            text="INFORMACIÓN O IMÁGENES/VIDEOS DE LA EMPRESA",
            font=('Helvetica', 12, 'bold')
        )
        content_title.pack(pady=20)

        # Aquí puedes agregar más contenido, imágenes o información

    def create_footer(self):
        footer_frame = ttk.Frame(self.root, relief="groove", borderwidth=1)
        footer_frame.grid(row=2, column=0, columnspan=2, sticky="ew", padx=10, pady=5)

        contact_label = ttk.Label(
            footer_frame,
            text="DATOS DE CONTACTO",
            font=('Helvetica', 11, 'bold')
        )
        contact_label.pack(pady=10)

        # Aquí puedes agregar más información de contacto

    def show_login(self):
        login_window = ventana()
        login_window.run()
        print("Mostrando ventana de login...")

    def show_empresas(self):
        # Implementar vista de empresas
        print("Mostrando sección de empresas...")

    def show_cotizantes(self):
        # Implementar vista de cotizantes
        print("Mostrando sección de cotizantes...")

    def show_bancos(self):
        # Implementar vista de bancos
        print("Mostrando sección de bancos...")

    def run(self):
        self.root.mainloop()


if __name__ == "__main__":
    app = MainWindow()
    app.run()