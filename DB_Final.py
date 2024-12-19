import tkinter as tk
from tkinter import ttk
from ConexiónBaseDatos import ConexionBaseDatos, UsuariosAutentificados

ventana = tk.Tk()
ventana.title("DB_Final")
ventana.geometry("450x450")

frame = tk.Frame(ventana)
frame.pack()


titulo_eps = tk.PhotoImage(file="TITULO.png")
label_titulo = tk.Label(frame, image=titulo_eps, bd = 0).pack(pady = 50)

# Crear un frame para el login
login_frame = tk.Frame(frame, relief="ridge", borderwidth=2)
login_frame.pack(pady=30)
# Etiqueta y entrada para el usuario
tk.Label(login_frame, text="Usuario:").grid(row=0, column=0, padx=10, pady=10)
username_entry = tk.Entry(login_frame)
username_entry.grid(row=0, column=1, padx=10, pady=10)

# Etiqueta y entrada para la contraseña
tk.Label(login_frame, text="Contraseña:").grid(row=1, column=0, padx=10, pady=10)
password_entry = tk.Entry(login_frame, show="*")
password_entry.grid(row=1, column=1, padx=10, pady=10)

# Botón de inicio de sesión
login_button = tk.Button(login_frame, text="Iniciar Sesión")
login_button.grid(row=2, column=0, columnspan=2, pady=10)

# Inicializar conexión a base de datos
db = ConexionBaseDatos()
user_auth = UsuariosAutentificados(db)

def login(self):
    username = self.username_entry.get()
    password = self.password_entry.get()

    if not username or not password:
        tk.messagebox.showerror("Error", "Por favor complete todos los campos")
        return

        if not self.db.connect():
            tk.messagebox.showerror("Error", "No se pudo conectar a la base de datos")
            return none

        if self.user_auth.verify_credentials(username, password):
            self.root.destroy()  # Cerrar ventana de login
            admin_window = VentanaAdmin()
            admin_window.run()
        else:
            messagebox.showerror("Error", "Credenciales inválidas")

        self.db.disconnect()

    def run(self):
        self.root.mainloop()

def ventanaAdmin():
    ventana2 = tk.Tk()
    ventana2.title("DB_Final")
    ventana2.geometry("450x450")
    ventana2.resizable(False, False)

    frame2 = tk.Frame(ventana2)
    frame2.pack()

    titular_admin = tk.PhotoImage(file="titulo_admin.png")
    label_admin = tk.Label(frame2, image = titular_admin, bd =0 )
    label_admin.pack(pady=50)

    ventana2.mainloop()
if __name__ == "__main__":
    ventanaAdmin()