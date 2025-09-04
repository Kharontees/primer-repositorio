#agenda
contactos = []
def agregar_contactos(nombre, fono):
    contactos.append({"nombre":nombre, "telefono":fono})

def listar_contactos():
    print("\nLista de contactos")
    for c in contactos:
        print(f"Nombre: {c['nombre']}, Teléfono: {c['telefono']}")


#Ingreso de datos
nombre = input("Ingresa nombre: ")
telefono = input("Ingresa num de telefono: ")

#Agrega a la lista y despuesa gregar
agregar_contactos(nombre,telefono)
print("Contacto agregado")

#Lista los contactos
listar_contactos()

