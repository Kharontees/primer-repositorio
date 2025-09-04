
#Aquí las funciones
contactos = []

def agregar_contacto(nombre):
    for c in contactos:
        if c['nombre'].lower() == nombre.lower():
            print(f"Error: El contacto '\033[31m{nombre}\033[0m' ya existe.")
            return False
    
    contactos.append({"nombre": nombre})
    return True

def listar_contactos():
    print("\nLista de contacto")
    if contactos:
        for i,c in enumerate(contactos):
            print(f"{i+1}. Nombre: {c['nombre']}")
    else:
        print("No hay contactos")

def buscar_contacto(nombre):
    for c in contactos:
        if c['nombre'].lower() == nombre.lower():
            print(f"Contacto encontrado: '\033[32m{c['nombre']}\033[0m'")
            return True
    print("Contacto no encontrado")
    return False

def menu():
    while True:
        print("\n---Menú---")
        print("1.Agregar Contacto")
        print("2.Listar Contacto")
        print("3.Buscar Contacto")
        print("4.SALIR")

        opcion = input("Selecciona una opción (1-4): ")
        

        if opcion == '1':
            print("\nAgregar Contacto")
            nombre = input("Ingresa el nombre del contacto: ").lower()
            if agregar_contacto(nombre):
                print(f"Contacto '\033[32m{nombre.capitalize()}\033[0m' agregado")
        elif opcion == '2':
            print("\nLista de Contactos")
            listar_contactos()
        elif opcion == '3':
            print("\nBuscar Contacto")
            nombre_buscar = input("Ingresa el nombre del contacto a buscar: ")
            buscar_contacto(nombre_buscar)
        elif opcion == '4':
            print("Saliendo...")
            break
        else:
            print("Opción no válida")