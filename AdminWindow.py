import tkinter as tk
from tkinter import ttk
from tkinter import messagebox
from AfiliadosWindow import AfiliadosWindow

class AdminWindow:
    def __init__(self):
        self.ventana_Admin = tk.Tk()
        self.ventana_Admin.title("Panel de Administrador - EPS")
        self.ventana_Admin.geometry("800x600")


        # Header con información del administrador
        self.create_header()

        # Frame principal para los botones
        self.create_main_buttons()

    def create_header(self):
        header_frame = tk.Frame(self.ventana_Admin)
        header_frame.pack()

        # Título y descripción
        self.title_frame = tk.Frame(header_frame)
        self.title_frame.pack(fill=tk.X)

        self.titulo_admin = tk.PhotoImage(file="titulo_admin.2.png")
        self.label_titulo = tk.Label(self.ventana_Admin, image = self.titulo_admin, bd=0)
        self.label_titulo.pack(padx=180, pady=10)


    def create_main_buttons(self):
        frame_botones = tk.Frame(self.ventana_Admin)
        frame_botones.pack()


        # Primera fila de botones
        self.create_menu_button(frame_botones, "AFILIADOS", "👤", 0, 0,
            self.show_afiliados, "#90EE90"  # Verde claro
        )

        self.create_menu_button(
            frame_botones, "EMPRESAS", "⬠", 0, 1,
            self.show_empresas, "#FFE4B5"  # Beige
        )

        # Segunda fila de botones
        self.create_menu_button(
            frame_botones, "IPS - ORDENES", "✚", 1, 0,
            self.show_ips_ordenes, "#FFB6C1"  # Rosa claro
        )

        self.create_menu_button(
            frame_botones, "CONTRATOS", "□", 1, 1,
            self.show_contratos, "#87CEEB"  # Azul claro
        )

        # Botón de reportes (centrado en la última fila)
        self.create_menu_button(
            frame_botones, "GENERAR REPORTES", "★", 2, 0,
            self.show_reportes, "#DDA0DD",  # Violeta claro
            columnspan=2
        )

    def create_menu_button(self, parent, text, icon, row, column, command, color, columnspan=1):
        # Frame para el botón con padding
        button_frame = ttk.Frame(parent)
        button_frame.grid(row=row, column=column, columnspan=columnspan,
                          padx=10, pady=10, sticky="nsew")

        # Crear un frame personalizado para el botón
        custom_button = tk.Frame(
            button_frame,
            background=color,
            relief="raised",
            borderwidth=1
        )
        custom_button.pack(fill=tk.X, pady=5, padx=5)

        # Hacer que todo el frame sea clickeable
        custom_button.bind("<Button-1>", lambda e: command())

        # Contenido del botón
        button_content = tk.Frame(custom_button, background=color)
        button_content.pack(padx=20, pady=10)

        # Texto del botón
        label = tk.Label(
            button_content,
            text=f"{text}  {icon}",
            font=('Helvetica', 12),
            background=color
        )
        label.pack()

    def show_afiliados(self):

        messagebox.showinfo("Afiliados", "Abriendo gestión de afiliados...")
        afiliados_window = AfiliadosWindow()
        afiliados_window.run()
        # Aquí implementaremos la ventana de gestión de afiliados

    def show_empresas(self):
        messagebox.showinfo("Empresas", "Abriendo gestión de empresas...")
        # Aquí implementaremos la ventana de gestión de empresas

    def show_ips_ordenes(self):
        messagebox.showinfo("IPS y Órdenes", "Abriendo gestión de IPS y órdenes...")
        # Aquí implementaremos la ventana de gestión de IPS y órdenes

    def show_contratos(self):
        messagebox.showinfo("Contratos", "Abriendo gestión de contratos...")
        # Aquí implementaremos la ventana de gestión de contratos

    def show_reportes(self):
        messagebox.showinfo("Reportes", "Abriendo generación de reportes...")
        # Aquí implementaremos la ventana de generación de reportes

    def run(self):
        self.ventana_Admin.mainloop()


if __name__ == "__main__":
    app = AdminWindow()
    app.run()