#agenda
contactos = []
def agregar_contactos(nombre, fono):
    contactos.append({"nombre":nombre, "fono":fono})

def listar_contactos():
    print("\nLista de contactos")
    for c in contactos:
        print(f"Nombre: {c['nombre']}, Teléfono: {c['fono']}")

def buscar_contacto(nombre):
    for c in contactos:
        if c['nombre'].lower() == nombre.lower():
            print("\n")
            print(f"Contacto encontrado: {c['nombre']} - {c['fono']}")
            return True
    print("Contacto no encontrado")

#Ingreso de datos
while True:
    nombre = input("Ingresa nombre: ")
    fono = input("Ingresa num de telefono: ")

    #Agrega a la lista y despuesa gregar
    agregar_contactos(nombre,fono)
    print("Contacto agregado")
    
    #Lista los contactos
    listar_contactos()

    nombre_buscar = input("Nombre a buscar: ")

    if buscar_contacto(nombre_buscar) == True:
        break

