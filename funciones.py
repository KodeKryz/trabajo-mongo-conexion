#3.1.1.I.2.---Implementa el Requerimiento 1: Lista todos los eventos mostrando código, nombre, fecha, lugar y categoría.-
def primero(coleccion_eventos):
    try:
                proyeccion = {
                "codigo": 1, 
                "nombre": 1, 
                "fecha": 1, 
                "lugar": 1, 
                "categoria": 1, 
                "_id": 0  
            }
                eventos = coleccion_eventos.find({}, proyeccion)
                print("Código                 Nombre              Fecha                   Lugar          Categoría")
                for i in eventos:
                    print(i["codigo"], "\t", i["nombre"], "\t", i["fecha"], "\t", i["lugar"], "\t", i["categoria"])
    except Exception as e:
        print("Error al listar eventos:", e)


def segundo(campo: str, valor: str, coleccion_eventos) -> None:
    try:
        resultados = list(coleccion_eventos.find({campo: valor}))
        
        if not resultados: raise IndexError
        
        for e in resultados:
            print("EVENTO:", e["nombre"], "|", campo.upper(), ":", e[campo])
            
    except (IndexError, KeyError):
        print("No se encontraron eventos para ese criterio.")


def tercero(texto_buscado: str, coleccion_invitados) -> None:
    try:
        regex = list(coleccion_invitados.find({
            "nombre": {"$regex": texto_buscado, "$options": "i"}
        }))
        for i in regex:
            print(i)
    except Exception as e:
        print("error:", e)


def cuarto(coleccion_invitados):
    inacapmail = coleccion_invitados.find({
        "correo": {
            "$regex": r"@inacap.cl$",
            "$options": "i"}
    })
    for i in inacapmail:
        print(i)


def quinto(rut, coleccion_eventos):
    ver_evento = coleccion_eventos.find({
        "invitados": {
            "$elemMatch": {
                "rut": rut,
                "estado": "confirmado"
            }
        }
    })
    print("EVENTOS CONFIRMADOS PARA EL RUT:", rut)
    print("--------------------------------------------------")
    for i in ver_evento:
        print("EVENTO:", i["nombre"], "| Código:", i["codigo"], "| Lugar:", i["lugar"])


def sexto(coleccion_eventos):
    cantidad_confirmados = coleccion_eventos.aggregate([
    # 1. Desarmar el array de invitados
    {
        "$unwind": "$invitados"
    },
        {
        "$match": {
            "invitados.estado": "confirmado"
            }
    },
        {
        "$group": {
            "_id": {
                "codigo": "$codigo",
                "nombre": "$nombre"
            },
            "totalconfirmados": {"$sum": 1}
            }
        },
        {
            "$sort": {
                "totalconfirmados": -1
            }
        },
        {
            "$limit": 3
        }
    ])
    for i in cantidad_confirmados:
        print(i)

def setimo(codigo_evento: str, rut_invitado: str, coleccion_eventos) -> None:
    res = list(coleccion_eventos.aggregate([
        {"$match": {"codigo": codigo_evento}},
        {"$unwind": "$invitados"},
        {"$match": {"invitados.rut": rut_invitado}},
        {"$lookup": {"from": "invitados", "localField": "invitados.rut", "foreignField": "rut", "as": "p"}}
    ]))
    
    if not res or not res[0]["p"]:
        print("No registrado.")
        return
        
    inv, perf = res[0]["invitados"], res[0]["p"][0]
    
    if perf["estado"] == "bloqueado":
        print("DENEGADO:", perf["nombre"], "está bloqueado.")
    elif inv["estado"] != "confirmado":
        print("DENEGADO: Estado", inv["estado"].upper())
    else:
        print("PERMITIDO:", perf["nombre"], "entra.")


def menu(coleccion_eventos, coleccion_invitados):
    while True:
        print("\n--- MENÚ DE OPCIONES ---")
        print("1. Listar todos los eventos")
        print("2. Consultar eventos por criterio")
        print("3. Buscar invitados por nombre")
        print("4. Mostrar correos de INACAP")
        print("5. Ver eventos confirmados de un RUT")
        print("6. Ver Top 3 eventos con más confirmados")
        print("7. Validar acceso de invitado")
        print("8. Salir")
        
        opcion = input("Selecciona una opción (1-8): ")
        
        if opcion == "1":
            primero(coleccion_eventos)
        elif opcion == "2":
            campo = input("Ingresa el campo (ej: categoria, lugar): ")
            valor = input("Ingresa el valor a buscar: ")
            segundo(campo, valor, coleccion_eventos)
        elif opcion == "3":
            nombre = input("Ingresa el nombre a buscar: ")
            tercero(nombre, coleccion_invitados)
        elif opcion == "4":
            cuarto(coleccion_invitados)
        elif opcion == "5":
            rut = input("Ingresa el RUT del invitado: ")
            quinto(rut, coleccion_eventos)
        elif opcion == "6":
            sexto(coleccion_eventos)
        elif opcion == "7":
            evt = input("Ingresa el código del evento: ")
            rut = input("Ingresa el RUT del invitado: ")
            setimo(evt, rut, coleccion_eventos)
        elif opcion == "8":
            print("Saliendo del programa...")
            break
        else:
            print("Opción no válida, intenta otra vez.")