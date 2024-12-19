import tkinter as tk
from tkinter import ttk, PhotoImage
from tkinter import messagebox
from ConexionBaseDatos import ConexionBaseDatos, UsuariosAutentificados
from AdminWindow import AdminWindow

class ventana:
    def __init__(self):
        self.ventana = tk.Tk()
        self.ventana.title("EPS - Esperar Para Salvarse")
        self.ventana.geometry("450x450")

        # Centrar la ventana
        ancho_ventana = self.ventana.winfo_screenwidth()
        alto_ventana = self.ventana.winfo_screenheight()
        x = (ancho_ventana - 450) // 2
        y = (alto_ventana - 350) // 2
        self.ventana.geometry(f"450x450+{x}+{y}")

        # Crear y configurar el frame principal
        self.frame_principal = tk.Frame(self.ventana)
        self.frame_principal.pack()

        #imagen
        self.titulo_eps = tk.PhotoImage(file="TITULO.png")
        self.label_titulo = tk.Label(self.frame_principal, image = self.titulo_eps, bd = 0)
        self.label_titulo.pack(padx = 10, pady=10)

        # Crear un frame para el login
        self.frame_de_login = tk.Frame(self.ventana, relief="ridge", borderwidth=2)
        self.frame_de_login.pack(pady=30)
        # Etiqueta y entrada para el usuario
        tk.Label(self.frame_de_login, text="Usuario:").grid(row=0, column=0, padx=10, pady=10)
        self.entrada_usuario = tk.Entry(self.frame_de_login)
        self.entrada_usuario.grid(row=0, column=1, padx=10, pady=10)

        # Etiqueta y entrada para la contraseña
        tk.Label(self.frame_de_login, text="Contraseña:").grid(row=1, column=0, padx=10, pady=10)
        self.entrada_contraseña = tk.Entry(self.frame_de_login, show="*")
        self.entrada_contraseña.grid(row=1, column=1, padx=10, pady=10)

        # Botón de inicio de sesión
        self.boton_login = tk.Button(self.frame_de_login, text="Iniciar Sesión", command=self.login)
        self.boton_login.grid(row=2, column=0, columnspan=2, pady=10)

        # Inicializar conexión a base de datos
        self.db = ConexionBaseDatos()
        self.user_auth = UsuariosAutentificados(self.db)

    def login(self):
        self.Usuario = self.entrada_usuario.get()
        self.contraseña = self.entrada_contraseña.get()

        if not self.Usuario or not self.contraseña:
            messagebox.showerror("Error", "Por favor complete todos los campos")
            return

        if not self.db.connect():
            messagebox.showerror("Error", "No se pudo conectar a la base de datos")
            return

        if self.user_auth.verify_credentials(self.Usuario, self.contraseña):
            self.ventana.destroy()  # Cerrar ventana de login
            admin_window = AdminWindow()
            admin_window.run()
        else:
            messagebox.showerror("Error", "Credenciales inválidas")

        self.db.disconnect()

    def run(self):
        self.ventana.mainloop()


if __name__ == "__main__":
    login_window = ventana()
    login_window.run()