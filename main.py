from gestion_contactos import GestionContactos
from gestion_archivo import ArchivoContactos

#Creamos el menu de la aplicacion
def menu():
    #Indicamos el nombre del archivo donde se guardaran los contactos
    nombre_archivo = "ListaContactos.txt"
    #Creamos la instancia con el nombre del archivo
    archivo_contactos = ArchivoContactos(nombre_archivo)
    #Creamos la instancia de la clase GestionContactos
    gestioncontactos = GestionContactos()

    #Cargamos los contactos desde el archivo, si existe
    contactos_cargados = archivo_contactos.cargar() 
    for c in contactos_cargados:
        gestioncontactos.agregar_contacto(c)

    while True:
        print(""" 
              ---MENU GESTION DE CONTACTOS---
              
              1. Agregar un contacto
              2. Mostrar lista de contactos
              3. Buscar un contacto
              4. Eliminar un contacto
              5. Eliminar la lista de contactos
              6. Salir""")

        opcion = input("""
              Elija una opción (del 1 al 5): """)
        
        if opcion == "1":
            nuevo_contacto = gestioncontactos.pedir_datos()
            gestioncontactos.agregar_contacto(nuevo_contacto)
            archivo_contactos.guardar(gestioncontactos.get_contactos())

        elif opcion == "2":
            gestioncontactos.mostrar_contactos()

        elif opcion =="3":
            nombre = input("Escribe el nombre del contacto que quieres buscar: ").lower().strip()
            gestioncontactos.mostrar_contacto(nombre)

        elif opcion == "4":
            nombre = input("Escribe el nombre del contacto que quieres eliminar: ").lower().strip()
            gestioncontactos.eliminar_contacto(nombre)
            archivo_contactos.guardar(gestioncontactos.get_contactos())

        elif opcion == "5":
            while True:
                #Comprobamos si el usuario esta seguro de eliminar la lista
                confirmacion = input(f'Va a eliminar la lista de contactos, ¿Esta seguro? Selecione si o no (S/N):').strip().upper()
                
                if confirmacion == "S":
                    archivo_contactos.eliminar_archivo()
                    gestioncontactos.vaciar_lista()
                    print("La lista ha sido eliminada. ")
                    break

                elif confirmacion == "N":
                    print('No se ha eliminado la lista de contactos. ')
                    break
            
                else:
                    print("Escriba S para eliminar contacto / Escriba N para no eliminarlo. ")
             
        elif opcion == "6":
            print("Salimos del programa")
            break

        else:
            print("Introduce una opción válida.")

if __name__ == "__main__":
    menu()