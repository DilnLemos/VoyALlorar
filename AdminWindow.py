import tkinter as tk
from tkinter import Image
from tkinter import messagebox
from AfiliadosWindow import AfiliadosWindow
from ConexionBaseDatos import ConexionBaseDatos

class AdminWindow:
    def __init__(self):
        self.ventana_Admin = tk.Tk()
        self.ventana_Admin.title("Panel de Administrador - EPS")
        self.ventana_Admin.geometry("800x600")

        # Header con información del administrador
        self.create_header()

        # Frame principal para los botones
        self.create_main_buttons()

        # Conexión a la base de datos
        self.db = ConexionBaseDatos()

    def create_header(self):
        header_frame = tk.Frame(self.ventana_Admin)
        header_frame.pack()

        # Título y descripción
        self.title_frame = tk.Frame(header_frame)
        self.title_frame.pack(fill=tk.X)

        self.titulo_admin = tk.PhotoImage(file="titulo_admin.2.png")
        self.label_titulo = tk.Label(self.ventana_Admin, image=self.titulo_admin, bd=0)
        self.label_titulo.pack(padx=180, pady=50)

    def create_main_buttons(self):
        frame_botones = tk.Frame(self.ventana_Admin)
        frame_botones.pack()

        # Primera fila de botones
        self.afiliados_imagen = tk.PhotoImage(file='AFILIADOS.png')
        self.afiliado_Label = tk.Button(self.ventana_Admin, image=self.afiliados_imagen, bd=0, command=self.show_afiliados)
        self.afiliado_Label.place(x=140, y=180)

        self.afiliados_imagen2 = tk.PhotoImage(file='EMPRESAS.png')
        self.afiliado_Label2 = tk.Button(self.ventana_Admin, image=self.afiliados_imagen2, bd=0, command=self.show_empresas)
        self.afiliado_Label2.place(x=460, y=180)

        self.afiliados_imagen3 = tk.PhotoImage(file='ORDENES.png')
        self.afiliado_Label3 = tk.Button(self.ventana_Admin, image=self.afiliados_imagen3, bd=0, command=self.show_ips_ordenes)
        self.afiliado_Label3.place(x=140, y=280)

        self.afiliados_imagen4 = tk.PhotoImage(file='CONTRATOS.png')
        self.afiliado_Label4 = tk.Button(self.ventana_Admin, image=self.afiliados_imagen4, bd=0, command=self.show_contratos)
        self.afiliado_Label4.place(x=460, y=280)

        self.afiliados_imagen5 = tk.PhotoImage(file='REPORTES.png')
        self.afiliado_Label5 = tk.Button(self.ventana_Admin, image=self.afiliados_imagen5, bd=0, command=self.show_reportes)
        self.afiliado_Label5.place(x=300, y=400)

    def show_afiliados(self):
        messagebox.showinfo("Afiliados", "Abriendo gestión de afiliados...")
        afiliados_window = AfiliadosWindow()
        afiliados_window.run()

    def show_empresas(self):
        if not self.db.connect():
            messagebox.showerror("Error", "No se pudo conectar a la base de datos")
            return

        empresas = self.db.execute_query("SELECT * FROM empresa")
        self.db.disconnect()

        if not empresas:
            messagebox.showinfo("Empresas", "No hay empresas registradas.")
            return

        empresas_window = tk.Toplevel(self.ventana_Admin)
        empresas_window.title("Empresas Registradas")
        empresas_window.geometry("600x400")

        # Crear scrollbar
        scrollbar = tk.Scrollbar(empresas_window)
        scrollbar.pack(side=tk.RIGHT, fill=tk.Y)

        # Crear lista
        listbox = tk.Listbox(empresas_window, yscrollcommand=scrollbar.set, width=80, height=20)
        for empresa in empresas:
            listbox.insert(tk.END, f"ID: {empresa[0]}, Nombre: {empresa[1]}, Dirección: {empresa[2]}")
        listbox.pack(side=tk.LEFT, fill=tk.BOTH, expand=True)

        scrollbar.config(command=listbox.yview)

    def show_ips_ordenes(self):
        if not self.db.connect():
            messagebox.showerror("Error", "No se pudo conectar a la base de datos")
            return

        ordenes = self.db.execute_query("SELECT * FROM ips")
        self.db.disconnect()

        if not ordenes:
            messagebox.showinfo("IPS y Órdenes", "No hay órdenes registradas.")
            return

        ips_window = tk.Toplevel(self.ventana_Admin)
        ips_window.title("Órdenes Registradas")
        ips_window.geometry("600x400")

        # Crear scrollbar
        scrollbar = tk.Scrollbar(ips_window)
        scrollbar.pack(side=tk.RIGHT, fill=tk.Y)

        # Crear lista
        listbox = tk.Listbox(ips_window, yscrollcommand=scrollbar.set, width=80, height=20)
        for orden in ordenes:
            listbox.insert(tk.END, f"ID: {orden[0]}, Detalle: {orden[1]}, Fecha: {orden[2]}")
        listbox.pack(side=tk.LEFT, fill=tk.BOTH, expand=True)

        scrollbar.config(command=listbox.yview)

    def show_contratos(self):
        if not self.db.connect():
            messagebox.showerror("Error", "No se pudo conectar a la base de datos")
            return

        contratos = self.db.execute_query("SELECT * FROM contrato")
        self.db.disconnect()

        if not contratos:
            messagebox.showinfo("Contratos", "No hay contratos registrados.")
            return

        contratos_window = tk.Toplevel(self.ventana_Admin)
        contratos_window.title("Contratos Registrados")
        contratos_window.geometry("600x400")

        # Crear scrollbar
        scrollbar = tk.Scrollbar(contratos_window)
        scrollbar.pack(side=tk.RIGHT, fill=tk.Y)

        # Crear lista
        listbox = tk.Listbox(contratos_window, yscrollcommand=scrollbar.set, width=80, height=20)
        for contrato in contratos:
            listbox.insert(tk.END, f"ID: {contrato[0]}, Detalle: {contrato[1]}, Fecha: {contrato[2]}")
        listbox.pack(side=tk.LEFT, fill=tk.BOTH, expand=True)

        scrollbar.config(command=listbox.yview)

    def show_reportes(self):
        if not self.db.connect():
            messagebox.showerror("Error", "No se pudo conectar a la base de datos")
            return

        reportes = self.db.execute_query("SELECT * FROM pago_aporte")
        self.db.disconnect()

        if not reportes:
            messagebox.showinfo("Reportes", "No hay reportes registrados.")
            return

        reportes_window = tk.Toplevel(self.ventana_Admin)
        reportes_window.title("Reportes Registrados")
        reportes_window.geometry("600x400")

        # Crear scrollbar
        scrollbar = tk.Scrollbar(reportes_window)
        scrollbar.pack(side=tk.RIGHT, fill=tk.Y)

        # Crear lista
        listbox = tk.Listbox(reportes_window, yscrollcommand=scrollbar.set, width=80, height=20)
        for reporte in reportes:
            listbox.insert(tk.END, f"ID: {reporte[0]}, Detalle: {reporte[1]}, Fecha: {reporte[2]}")
        listbox.pack(side=tk.LEFT, fill=tk.BOTH, expand=True)

        scrollbar.config(command=listbox.yview)

    def run(self):
        self.ventana_Admin.mainloop()


if __name__ == "__main__":
    app = AdminWindow()
    app.run()
