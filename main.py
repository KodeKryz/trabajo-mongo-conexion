import os
from dotenv import load_dotenv
from pymongo import MongoClient
import funciones
# Cargar las variables de entorno desde el archivo .env
load_dotenv()

# encuentra la variable 'MONGO_URI' desde el dotenv
MONGO_URI = os.getenv("MONGO_URI")

try:
    #conectamos el mongo client con la variable mongo uri
    cliente=MongoClient(MONGO_URI)
    cliente.admin.command("ping")
    print("¡Conexión exitosa a MongoDB!")

except  Exception as e:
    print(f" error en la conexion de la bd {e}")

# Elegir la base de datos
db_ecommerce_marketing = cliente["ecommerce_marketing"]

# Coleccion Clientes
coleccion_invitados = db_ecommerce_marketing["invitados"]

# Coleccion Pedidos
coleccion_eventos = db_ecommerce_marketing["eventos"]


def insercion_inicial_coleccion_eventos() -> None:
    try:
        respuesta = coleccion_eventos.insert_many([
            {
                "codigo": "EVT-2025-001",
                "nombre": "Evento 1 - Datos",
                "fecha": "2025-12-25T20:00:00Z",
                "lugar": "Auditorio B",
                "categoria": "charla",
                "invitados": [
                    {"rut": "11.118.512-6", "estado": "confirmado", "checkin": False},
                    {"rut": "11.098.760-0", "estado": "confirmado", "checkin": False},
                    {"rut": "11.079.008-4", "estado": "confirmado", "checkin": False},
                    {"rut": "11.009.876-3", "estado": "confirmado", "checkin": False},
                    {"rut": "11.059.256-8", "estado": "confirmado", "checkin": False},
                    {"rut": "11.029.628-9", "estado": "pendiente", "checkin": False},
                    {"rut": "11.138.264-2", "estado": "confirmado", "checkin": False},
                    {"rut": "11.148.140-5", "estado": "confirmado", "checkin": False},
                    {"rut": "11.197.520-0", "estado": "confirmado", "checkin": False},
                    {"rut": "11.187.644-7", "estado": "confirmado", "checkin": False},
                    {"rut": "11.019.752-6", "estado": "confirmado", "checkin": False},
                    {"rut": "11.246.900-5", "estado": "confirmado", "checkin": False},
                    {"rut": "11.177.768-4", "estado": "pendiente", "checkin": False},
                    {"rut": "11.207.396-3", "estado": "pendiente", "checkin": False},
                    {"rut": "11.237.024-2", "estado": "rechazado", "checkin": False},
                    {"rut": "11.217.272-6", "estado": "pendiente", "checkin": False},
                    {"rut": "11.227.148-9", "estado": "pendiente", "checkin": False},
                    {"rut": "11.128.388-9", "estado": "pendiente", "checkin": False}
                ]
            },
            {
                "codigo": "EVT-2025-002",
                "nombre": "Evento 2 - Seguridad",
                "fecha": "2025-12-27T20:00:00Z",
                "lugar": "Auditorio A",
                "categoria": "charla",
                "invitados": [
                    {"rut": "11.158.016-8", "estado": "pendiente", "checkin": False},
                    {"rut": "11.187.644-7", "estado": "pendiente", "checkin": False},
                    {"rut": "11.059.256-8", "estado": "confirmado", "checkin": False},
                    {"rut": "11.088.884-7", "estado": "rechazado", "checkin": False},
                    {"rut": "11.098.760-0", "estado": "rechazado", "checkin": False},
                    {"rut": "11.009.876-3", "estado": "pendiente", "checkin": False},
                    {"rut": "11.049.380-5", "estado": "pendiente", "checkin": False},
                    {"rut": "11.138.264-2", "estado": "confirmado", "checkin": False},
                    {"rut": "11.118.512-6", "estado": "confirmado", "checkin": False},
                    {"rut": "11.108.636-3", "estado": "confirmado", "checkin": False},
                    {"rut": "11.029.628-9", "estado": "confirmado", "checkin": False},
                    {"rut": "11.167.892-1", "estado": "confirmado", "checkin": False},
                    {"rut": "11.217.272-6", "estado": "rechazado", "checkin": False},
                    {"rut": "11.207.396-3", "estado": "confirmado", "checkin": False}
                ]
            },
            {
                "codigo": "EVT-2025-003",
                "nombre": "Evento 3 - MongoDB",
                "fecha": "2025-12-27T20:00:00Z",
                "lugar": "Auditorio B",
                "categoria": "workshop",
                "invitados": [
                    {"rut": "11.039.504-2", "estado": "confirmado", "checkin": False},
                    {"rut": "11.049.380-5", "estado": "confirmado", "checkin": False},
                    {"rut": "11.237.024-2", "estado": "confirmado", "checkin": False},
                    {"rut": "11.197.520-0", "estado": "confirmado", "checkin": False},
                    {"rut": "11.128.388-9", "estado": "confirmado", "checkin": False},
                    {"rut": "11.069.132-1", "estado": "confirmado", "checkin": False},
                    {"rut": "11.177.768-4", "estado": "confirmado", "checkin": False},
                    {"rut": "11.029.628-9", "estado": "confirmado", "checkin": False},
                    {"rut": "11.019.752-6", "estado": "confirmado", "checkin": False},
                    {"rut": "11.009.876-3", "estado": "confirmado", "checkin": False},
                    {"rut": "11.207.396-3", "estado": "confirmado", "checkin": False},
                    {"rut": "11.108.636-3", "estado": "confirmado", "checkin": False},
                    {"rut": "11.187.644-7", "estado": "confirmado", "checkin": False},
                    {"rut": "11.098.760-0", "estado": "confirmado", "checkin": False},
                    {"rut": "11.158.016-8", "estado": "confirmado", "checkin": False},
                    {"rut": "11.246.900-5", "estado": "confirmado", "checkin": False},
                    {"rut": "11.138.264-2", "estado": "confirmado", "checkin": False},
                    {"rut": "11.217.272-6", "estado": "pendiente", "checkin": False},
                    {"rut": "11.227.148-9", "estado": "pendiente", "checkin": False},
                    {"rut": "11.079.008-4", "estado": "pendiente", "checkin": False},
                    {"rut": "11.059.256-8", "estado": "pendiente", "checkin": False},
                    {"rut": "11.118.512-6", "estado": "pendiente", "checkin": False}
                ]
            },
            {
                "codigo": "EVT-2025-004",
                "nombre": "Evento 4 - DevOps",
                "fecha": "2025-12-25T19:00:00Z",
                "lugar": "Auditorio B",
                "categoria": "meetup",
                "invitados": [
                    {"rut": "11.079.008-4", "estado": "confirmado", "checkin": False},
                    {"rut": "11.128.388-9", "estado": "confirmado", "checkin": False},
                    {"rut": "11.246.900-5", "estado": "pendiente", "checkin": False},
                    {"rut": "11.069.132-1", "estado": "confirmado", "checkin": False},
                    {"rut": "11.167.892-1", "estado": "pendiente", "checkin": False},
                    {"rut": "11.158.016-8", "estado": "pendiente", "checkin": False},
                    {"rut": "11.118.512-6", "estado": "confirmado", "checkin": False},
                    {"rut": "11.009.876-3", "estado": "rechazado", "checkin": False},
                    {"rut": "11.177.768-4", "estado": "confirmado", "checkin": False},
                    {"rut": "11.088.884-7", "estado": "confirmado", "checkin": False}
                ]
            },
            {
                "codigo": "EVT-2025-005",
                "nombre": "Evento 5 - MongoDB",
                "fecha": "2025-12-30T18:00:00Z",
                "lugar": "Auditorio A",
                "categoria": "charla",
                "invitados": [
                    {"rut": "11.197.520-0", "estado": "pendiente", "checkin": False},
                    {"rut": "11.246.900-5", "estado": "rechazado", "checkin": False},
                    {"rut": "11.009.876-3", "estado": "confirmado", "checkin": False},
                    {"rut": "11.158.016-8", "estado": "confirmado", "checkin": False},
                    {"rut": "11.207.396-3", "estado": "rechazado", "checkin": False},
                    {"rut": "11.118.512-6", "estado": "pendiente", "checkin": False},
                    {"rut": "11.029.628-9", "estado": "confirmado", "checkin": False},
                    {"rut": "11.039.504-2", "estado": "confirmado", "checkin": False},
                    {"rut": "11.128.388-9", "estado": "confirmado", "checkin": False},
                    {"rut": "11.069.132-1", "estado": "rechazado", "checkin": False},
                    {"rut": "11.079.008-4", "estado": "pendiente", "checkin": False},
                    {"rut": "11.187.644-7", "estado": "confirmado", "checkin": False},
                    {"rut": "11.217.272-6", "estado": "pendiente", "checkin": False},
                    {"rut": "11.108.636-3", "estado": "rechazado", "checkin": False},
                    {"rut": "11.059.256-8", "estado": "pendiente", "checkin": False},
                    {"rut": "11.019.752-6", "estado": "confirmado", "checkin": False}
                ]
            },
            {
                "codigo": "EVT-2025-006",
                "nombre": "Evento 6 - MongoDB",
                "fecha": "2025-12-24T20:00:00Z",
                "lugar": "Auditorio B",
                "categoria": "charla",
                "invitados": [
                    {"rut": "11.237.024-2", "estado": "confirmado", "checkin": False},
                    {"rut": "11.207.396-3", "estado": "pendiente", "checkin": False},
                    {"rut": "11.039.504-2", "estado": "confirmado", "checkin": False},
                    {"rut": "11.167.892-1", "estado": "confirmado", "checkin": False},
                    {"rut": "11.049.380-5", "estado": "pendiente", "checkin": False},
                    {"rut": "11.138.264-2", "estado": "confirmado", "checkin": False},
                    {"rut": "11.069.132-1", "estado": "pendiente", "checkin": False},
                    {"rut": "11.187.644-7", "estado": "rechazado", "checkin": False},
                    {"rut": "11.009.876-3", "estado": "pendiente", "checkin": False},
                    {"rut": "11.088.884-7", "estado": "pendiente", "checkin": False},
                    {"rut": "11.227.148-9", "estado": "confirmado", "checkin": False},
                    {"rut": "11.246.900-5", "estado": "pendiente", "checkin": False}
                ]
            },
            {
                "codigo": "EVT-2025-007",
                "nombre": "Evento 7 - Datos",
                "fecha": "2025-12-29T18:00:00Z",
                "lugar": "Sala 204",
                "categoria": "charla",
                "invitados": [
                    {"rut": "11.217.272-6", "estado": "confirmado", "checkin": False},
                    {"rut": "11.009.876-3", "estado": "confirmado", "checkin": False},
                    {"rut": "11.108.636-3", "estado": "confirmado", "checkin": False},
                    {"rut": "11.019.752-6", "estado": "confirmado", "checkin": False},
                    {"rut": "11.148.140-5", "estado": "confirmado", "checkin": False},
                    {"rut": "11.079.008-4", "estado": "confirmado", "checkin": False},
                    {"rut": "11.177.768-4", "estado": "confirmado", "checkin": False},
                    {"rut": "11.158.016-8", "estado": "confirmado", "checkin": False},
                    {"rut": "11.128.388-9", "estado": "confirmado", "checkin": False},
                    {"rut": "11.118.512-6", "estado": "confirmado", "checkin": False},
                    {"rut": "11.049.380-5", "estado": "confirmado", "checkin": False},
                    {"rut": "11.227.148-9", "estado": "confirmado", "checkin": False},
                    {"rut": "11.207.396-3", "estado": "confirmado", "checkin": False},
                    {"rut": "11.197.520-0", "estado": "confirmado", "checkin": False},
                    {"rut": "11.088.884-7", "estado": "confirmado", "checkin": False},
                    {"rut": "11.138.264-2", "estado": "rechazado", "checkin": False},
                    {"rut": "11.237.024-2", "estado": "pendiente", "checkin": False},
                    {"rut": "11.059.256-8", "estado": "rechazado", "checkin": False},
                    {"rut": "11.069.132-1", "estado": "pendiente", "checkin": False},
                    {"rut": "11.039.504-2", "estado": "pendiente", "checkin": False}
                ]
            },
            {
                "codigo": "EVT-2025-008",
                "nombre": "Evento 8 - Seguridad",
                "fecha": "2025-12-28T19:00:00Z",
                "lugar": "Auditorio B",
                "categoria": "workshop",
                "invitados": [
                    {"rut": "11.128.388-9", "estado": "pendiente", "checkin": False},
                    {"rut": "11.148.140-5", "estado": "rechazado", "checkin": False},
                    {"rut": "11.108.636-3", "estado": "confirmado", "checkin": False},
                    {"rut": "11.029.628-9", "estado": "pendiente", "checkin": False},
                    {"rut": "11.079.008-4", "estado": "pendiente", "checkin": False},
                    {"rut": "11.138.264-2", "estado": "confirmado", "checkin": False},
                    {"rut": "11.217.272-6", "estado": "rechazado", "checkin": False},
                    {"rut": "11.069.132-1", "estado": "rechazado", "checkin": False},
                    {"rut": "11.098.760-0", "estado": "confirmado", "checkin": False}
                ]
            }
        ])
        print("Se han insertado {} eventos correctamente.".format(len(respuesta.inserted_ids)))
    except Exception as e:
        print("Error al realizar la inserción masiva: {}".format(e))

def insercion_inicial_coleccion_invitados() -> None:
    try:
        respuesta = coleccion_invitados.insert_many([          
            {
                "rut": "11.009.876-3",
                "nombre": "Camila Herrera",
                "correo": "camila.herrera@empresa.cl",
                "empresa": "EmpresaX",
                "estado": "bloqueado"
            },
            {
                "rut": "11.019.752-6",
                "nombre": "Carla Rojas",
                "correo": "carla.rojas@empresa.cl",
                "empresa": "BlueCom",
                "estado": "activo"
            },
            {
                "rut": "11.029.628-9",
                "nombre": "Luis Fernández",
                "correo": "luis.fernandez@contratista.cl",
                "empresa": "DataShield",
                "estado": "activo"
            },
            {
                "rut": "11.039.504-2",
                "nombre": "Ana Martínez",
                "correo": "ana.martinez@empresa.cl",
                "empresa": "Inacap",
                "estado": "activo"
            },
            {
                "rut": "11.049.380-5",
                "nombre": "Diego López",
                "correo": "diego.lopez@empresa.cl",
                "empresa": "EmpresaX",
                "estado": "activo"
            },
            {
                "rut": "11.059.256-8",
                "nombre": "María González",
                "correo": "maria.gonzalez@inacap.cl",
                "empresa": "DataShield",
                "estado": "bloqueado"
            },
            {
                "rut": "11.069.132-1",
                "nombre": "José Pérez",
                "correo": "jose.perez@contratista.cl",
                "empresa": "EmpresaX",
                "estado": "activo"
            },
            {
                "rut": "11.079.008-4",
                "nombre": "Felipe Castro",
                "correo": "felipe.castro@contratista.cl",
                "empresa": "DataShield",
                "estado": "activo"
            },
            {
                "rut": "11.088.884-7",
                "nombre": "Valentina Soto",
                "correo": "valentina.soto@empresa.cl",
                "empresa": "AndesLog",
                "estado": "activo"
            },
            {
                "rut": "11.098.760-0",
                "nombre": "Ricardo Núñez",
                "correo": "ricardo.nunez@empresa.cl",
                "empresa": "AndesLog",
                "estado": "activo"
            },
            {
                "rut": "11.108.636-3",
                "nombre": "Tomás Vergara",
                "correo": "tomas.vergara@contratista.cl",
                "empresa": "Inacap",
                "estado": "activo"
            },
            {
                "rut": "11.118.512-6",
                "nombre": "Daniela Salinas",
                "correo": "daniela.salinas@contratista.cl",
                "empresa": "BlueCom",
                "estado": "activo"
            },
            {
                "rut": "11.128.388-9",
                "nombre": "Andrés Muñoz",
                "correo": "andres.munoz@empresa.cl",
                "empresa": "EmpresaX",
                "estado": "activo"
            },
            {
                "rut": "11.138.264-2",
                "nombre": "Fernanda Campos",
                "correo": "fernanda.campos@contratista.cl",
                "empresa": "CyberLab",
                "estado": "activo"
            },
            {
                "rut": "11.148.140-5",
                "nombre": "Javier Ortiz",
                "correo": "javier.ortiz@contratista.cl",
                "empresa": "NorteDigital",
                "estado": "activo"
            },
            {
                "rut": "11.158.016-8",
                "nombre": "Paula Rivera",
                "correo": "paula.rivera@empresa.cl",
                "empresa": "TechNova",
                "estado": "activo"
            },
            {
                "rut": "11.167.892-1",
                "nombre": "Cristóbal Sáez",
                "correo": "cristobal.saez@contratista.cl",
                "empresa": "AndesLog",
                "estado": "activo"
            },
            {
                "rut": "11.177.768-4",
                "nombre": "Ignacia Torres",
                "correo": "ignacia.torres@empresa.cl",
                "empresa": "NorteDigital",
                "estado": "activo"
            },
            {
                "rut": "11.187.644-7",
                "nombre": "Matías Castillo",
                "correo": "matias.castillo@empresa.cl",
                "empresa": "Inacap",
                "estado": "activo"
            },
            {
                "rut": "11.197.520-0",
                "nombre": "Rocío Paredes",
                "correo": "rocio.paredes@empresa.cl",
                "empresa": "BlueCom",
                "estado": "bloqueado"
            },
            {
                "rut": "11.207.396-3",
                "nombre": "Sebastián Fuentes",
                "correo": "sebastian.fuentes@empresa.cl",
                "empresa": "EmpresaX",
                "estado": "activo"
            },
            {
                "rut": "11.217.272-6",
                "nombre": "Gabriela Vega",
                "correo": "gabriela.vega@inacap.cl",
                "empresa": "BlueCom",
                "estado": "bloqueado"
            },
            {
                "rut": "11.227.148-9",
                "nombre": "Nicolás Araya",
                "correo": "nicolas.araya@empresa.cl",
                "empresa": "NorteDigital",
                "estado": "activo"
            },
            {
                "rut": "11.237.024-2",
                "nombre": "Catalina Contreras",
                "correo": "catalina.contreras@contratista.cl",
                "empresa": "Inacap",
                "estado": "activo"
            },
            {
                "rut": "11.246.900-5",
                "nombre": "Joaquín Reyes",
                "correo": "joaquin.reyes@inacap.cl",
                "empresa": "Inacap",
                "estado": "activo"
            }
        ])
        print("Se han insertado {} invitados correctamente.".format(len(respuesta.inserted_ids)))
    except Exception as e:
        print("Error al realizar la inserción masiva de invitados: {}".format(e))

insercion_inicial_coleccion_eventos()
insercion_inicial_coleccion_invitados()

#limpiar_la_base_de_datos()
#coleccion_invitados.drop()
#coleccion_eventos.drop()

funciones.menu(coleccion_eventos, coleccion_invitados)