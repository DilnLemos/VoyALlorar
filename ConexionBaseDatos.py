import psycopg2
from psycopg2 import Error
from typing import Optional

class ConexionBaseDatos:
    def __init__(self):
        self.conexion = None
        self.cursor = None

    def connect(self) -> bool:
        try:
            self.conexion = psycopg2.connect(
                database="postgres",  # Cambia esto por el nombre de tu base de datos
                user="DilanLemos",    # Cambia esto por tu usuario
                password="UniDilan12",        # Cambia esto por tu contraseña
                host="localhost",
                port="5432"
            )
            self.cursor = self.conexion.cursor()
            return True
        except Error as e:
            print(f"Error al conectar a PostgreSQL: {e}")
            return False

    def disconnect(self):
        if self.cursor:
            self.cursor.close()
        if self.conexion:
            self.conexion.close()

    def execute_query(self, query: str, params: tuple = None) -> Optional[list]:
        try:
            self.cursor.execute(query, params)
            if query.strip().upper().startswith(('SELECT', 'SHOW')):
                return self.cursor.fetchall()
            self.conexion.commit()
            return None
        except Error as e:
            print(f"Error ejecutando query: {e}")
            self.conexion.rollback()
            return None

class UsuariosAutentificados:
    def __init__(self, db: ConexionBaseDatos):
        self.db = db

    def verify_credentials(self, username: str, password: str) -> bool:
        # Aquí implementaremos la verificación de credenciales
        # Por ahora retorna True para testing
        return True

    def get_user_role(self, username: str) -> str:
        # Aquí implementaremos la obtención del rol del usuario
        # Por ahora retorna un rol por defecto
        return "admin"