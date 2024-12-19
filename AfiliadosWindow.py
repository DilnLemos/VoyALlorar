import tkinter as tk
from tkinter import ttk, messagebox
from ConexionBaseDatos import ConexionBaseDatos
from datetime import datetime


class AfiliadosWindow:
    def __init__(self):
        self.ventana_afiliados = tk.Tk()
        self.ventana_afiliados.title("ADMINISTRADOR -> PESTAÑA AFILIADOS")
        self.ventana_afiliados.geometry("1200x700")
        self.db = ConexionBaseDatos()

        # Frame izquierdo para botones
        self.create_left_panel()

        # Frame derecho para el formulario
        self.create_right_panel()

    def create_left_panel(self):
        left_frame = ttk.Frame(self.ventana_afiliados, padding="20")
        left_frame.grid(row=0, column=0, sticky="nsew")

        # Header
        header_label = ttk.Label(
            left_frame,
            text="Administrador: Puede gestionar afiliados, empresas, IPS, contratos, \nÓrdenes de servicio y generar reporte de afiliados por estado,\nórdenes por paciente y afiliados por empresa.",
            wraplength=400,
            justify=tk.LEFT
        )
        header_label.pack(pady=(0, 30))

        # Botón de Registro
        registro_frame = ttk.Frame(left_frame)
        registro_frame.pack(fill=tk.X, pady=10)
        ttk.Button(
            registro_frame,
            text="REGISTRO 👤",
            command=self.show_registro_window
        ).pack(fill=tk.X)

        # Botón de Consulta
        consulta_frame = ttk.Frame(left_frame)
        consulta_frame.pack(fill=tk.X, pady=10)
        ttk.Label(
            consulta_frame,
            text="BUSCAR AFILIADOS EN SISTEMA\nPARA VERIFICAR DATOS",
            justify=tk.CENTER
        ).pack()
        ttk.Button(
            consulta_frame,
            text="CONSULTA 🔍",
            command=self.show_consulta_window
        ).pack(fill=tk.X)

        # Botón de Modificar
        ttk.Button(
            left_frame,
            text="MODIFICAR DATOS 💬",
            command=self.show_modificar_form
        ).pack(fill=tk.X, pady=10)

    def create_right_panel(self):
        global right_frame
        right_frame = ttk.Frame(self.ventana_afiliados, padding="20")

        right_frame.grid(row=0, column=1, sticky="nsew")

        # Título del formulario
        title_label = ttk.Label(
            right_frame,
            text="FORMULARIO MODIFICACION DATOS\nCOTIZANTE/AFILIADO",
            justify=tk.CENTER,
            font=('Helvetica', 12, 'bold')
        )
        title_label.pack(pady=10)

        # Crear formulario
        form_frame = ttk.Frame(right_frame)
        form_frame.pack(fill=tk.BOTH, expand=True)

        # Campos generales
        self.create_form_field(form_frame, "Tipo y número de documento de identidad")
        self.create_form_field(form_frame, "Apellidos")
        self.create_form_field(form_frame, "Nombres")
        self.create_form_field(form_frame, "Fecha de nacimiento")
        self.create_form_field(form_frame, "Género")
        self.create_form_field(form_frame, "Dirección")
        self.create_form_field(form_frame, "Ciudad de residencia")
        self.create_form_field(form_frame, "Teléfono")
        self.create_form_field(form_frame, "Estado civil")
        self.create_form_field(form_frame, "Correo electrónico")

        # Sección Cotizante
        ttk.Label(
            form_frame,
            text="SOLO COTIZANTE",
            font=('Helvetica', 10, 'bold'),
            foreground='red'
        ).pack(pady=(10, 5))

        self.create_form_field(form_frame, "Fecha de la primera afiliación")
        self.create_form_field(form_frame, "Estado actual")
        self.create_form_field(form_frame, "Salario")
        self.create_form_field(form_frame, "Rango salarial")

        # Sección Afiliado
        ttk.Label(
            form_frame,
            text="SOLO AFILIADO",
            font=('Helvetica', 10, 'bold'),
            foreground='red'
        ).pack(pady=(10, 5))

        self.create_form_field(form_frame, "Parentesco con el cotizante")
        self.create_form_field(form_frame, "Estado actual (debe ser igual al del cotizante afiliado)")

        # Botones de acción
        buttons_frame = ttk.Frame(form_frame)
        buttons_frame.pack(pady=20)
        ttk.Button(buttons_frame, text="Guardar Cambios", command=self.guardar_cambios).place(x = 100, y=100)
        ttk.Button(buttons_frame,text="Cancelar",command=self.limpiar_formulario).pack(side=tk.LEFT, padx=5)

    def create_form_field(self, parent, label_text):
        field_frame = ttk.Frame(parent)
        field_frame.pack(fill=tk.X, pady=2)

        ttk.Label(field_frame, text=label_text).pack(anchor=tk.W)
        entry = ttk.Entry(field_frame)
        entry.pack(fill=tk.X)
        return entry

    def show_registro_window(self):
        # Implementar ventana de registro
        messagebox.showinfo("Registro", "Abriendo ventana de registro...")

    def show_consulta_window(self):
        # Implementar ventana de consulta
        messagebox.showinfo("Consulta", "Abriendo ventana de consulta...")

    def show_modificar_form(self):
        # Ya está implementado en el panel derecho
        messagebox.showinfo("Modificar", "El formulario de modificación está a la derecha")

    def guardar_cambios(self):
        # Implementar guardado en base de datos
        messagebox.showinfo("Guardar", "Guardando cambios...")

    def limpiar_formulario(self):
        # Implementar limpieza de formulario
        messagebox.showinfo("Limpiar", "Limpiando formulario...")

    def run(self):
        self.ventana_afiliados.mainloop()


if __name__ == "__main__":
    app = AfiliadosWindow()
    app.run()