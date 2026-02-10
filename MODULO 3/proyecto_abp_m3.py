# CLASE CONTACTO
class Contacto:
    def __init__(self, nombre, telefono, correo, direccion):
        self.nombre = nombre
        self.telefono = telefono
        self.correo = correo
        self.direccion = direccion


# CLASE AGENDA
class Agenda:
    def __init__(self):
        self.contactos = []

    def agregar_contacto(self, contacto):
        self.contactos.append(contacto)

    def mostrar_contactos(self):
        if not self.contactos:
            print("No hay contactos registrados.")
        else:
            for contacto in self.contactos:
                print("Nombre:", contacto.nombre)
                print("Teléfono:", contacto.telefono)
                print("Correo:", contacto.correo)
                print("Dirección:", contacto.direccion)
                print("-" * 30)


# PROGRAMA PRINCIPAL
agenda = Agenda()

while True:
    print("\n--- MENÚ AGENDA ---")
    print("1. Agregar contacto")
    print("2. Mostrar contactos")
    print("3. Salir")

    opcion = input("Seleccione una opción: ")

    if opcion == "1":
        nombre = input("Nombre: ")
        telefono = input("Teléfono: ")
        correo = input("Correo: ")
        direccion = input("Dirección: ")

        contacto = Contacto(nombre, telefono, correo, direccion)
        agenda.agregar_contacto(contacto)

        print("Contacto agregado correctamente.")

    elif opcion == "2":
        agenda.mostrar_contactos()

    elif opcion == "3":
        print("Saliendo del programa...")
        break

    else:
        print("Opción no válida. Intente nuevamente.")
