
#Aquí las funciones
contactos = []

def agregar_contacto(nombre):
    contactos.append({"nombre": nombre})

def listar_contactos():
    print("\nLista de contacto")
    if contactos:
        for c in contactos:
            print(f"Nombre: {c['nombre']}")
    else:
        print("No hay contactos")

def buscar_contacto(nombre):
    for c in contactos:
        if c['nombre'].lower() == nombre.lower():
            print(f"Contacto encontrado: {c['nombre']}")
            return
    print("Contacto no encontrado")
    
def menu():
    while True:
        print("\n---Menú---")
        print("1.Agregar Contacto")
        print("2.Listar Contacto")
        print("3.Bucar Contacto")
        print("4.SALIR")
        
        opcion = input("Selecciona una opción (1-5): ")

        if opcion == '1':
            nombre = input("Ingresa el nombre del contacto: ")
            agregar_contacto(nombre)
            print(f"Contacto '\033[32m{nombre}\033[0m' agregado.")
        elif opcion == '2':
            listar_contactos()
        elif opcion == '3':
            nombre_buscar = input("Ingresa el nombre del contacto a buscar: ")
            buscar_contacto(nombre_buscar)
        elif opcion == '4':
            print("Saliendo...")
            break
        else:
            print("Opción no válida")