from contacto import Contacto
import re

class GestionContactos:
# Creamos una lista vacia donde se añadirán los contactos
    def __init__(self):
        self.__contactos = []

    def get_contactos(self):
        return self.__contactos
        

#Creamos el metodo para añadir contactos a la lista 
    def agregar_contacto(self, contacto):
        self.__contactos.append(contacto)
        print("El contacto se ha añadido a la lista de contactos.")

#Pedimos al usuario que introduzca los datos del nuevo contacto
    def pedir_datos(self):

        while True:
            nombre = input("Escribe el nombre: ").lower().strip()
            #Comprobamos que no lo deje vacio
            if not nombre:
                print("Debe escribir un nombre para el contacto.")
                continue 
            #Aseguramos que no haya un contacto con el mismo nombre
            if any(contacto.get_nombre() == nombre for contacto in self.__contactos):
                print("Nombre de contacto ya registrado, escriba uno diferente a los contactos existentes.")
                continue
            break
        
        while True:
            try:
                telefono = int(input("Escribe el numero de telefono: "))    
                #Comprobamos que tenga 9 digitos           
                if len(str(telefono)) != 9:
                    print("El telefono debe tener 9 digitos.")
                    continue
                if any(contacto.get_telefono() == telefono for contacto in self.__contactos):
                    print("Telefono ya registrado, escriba uno diferente a los contactos existentes.")
                    continue
                break
                    
            except ValueError:
                print("El telefono solo debe contener digitos numericos, prueba de nuevo.")
            except Exception as e:
                print(f"Error al guardar teléfono: {e}")


        while True:
            email = input("Escribe el email: ").lower().strip()
            #Escribimos el formato que debe tener el email
            patron = r"^[\w\.-]+@[\w\.-]+\.\w+$"

            if not email:
                print("Debe escribir un email para el contacto.")
                continue

            #Comprobamos que tenga el formato correcto
            if not re.match(patron, email):
                print("El email debe tener un formato correcto. ")
                continue            
            
            if any(contacto.get_email() == email for contacto in self.__contactos):
                print("Email ya registrado, escriba uno diferente a los contactos existentes.")
                continue          
            break

        #Creamos contacto con los datos introducidos
        return Contacto(nombre, telefono, email)
    
#Creamos metodo para ver la lista de contactos    
    def mostrar_contactos(self):
        if not self.__contactos:
            print("No hay contactos guardados.")
        else:
            for contacto in self.__contactos:
                print(contacto)

#Creamos metodo para buscar contacto por nombre
    def buscar_contacto(self, nombre):           
        for contacto in self.__contactos:
            if contacto.get_nombre() == nombre:
                return contacto                
        return None

#Creamos metodo para mostrar el contacto buscado
    def mostrar_contacto(self, nombre):
        contacto = self.buscar_contacto(nombre)
        if contacto:
            print(contacto)
        else:
            print("Contacto no encontrado. ")

#Creamos metodo para vaciar la lista de contactos
    def vaciar_lista(self):
        self.__contactos.clear()

#Creamos metodo para eliminar un contacto
    def eliminar_contacto(self, nombre):
        contacto = self.buscar_contacto(nombre)
        if contacto:
            

            while True:
                #Comprobamos si el usuario esta seguro de eliminarlo
                confirmacion = input(f'Va a eliminar el contacto {nombre}, ¿Esta seguro? Selecione si o no (S/N):').strip().upper()
                
                if confirmacion == "S":
                    self.__contactos.remove(contacto)
                    print(f'El contacto {nombre} ha sido eliminado. ')
                    break

                elif confirmacion == "N":
                    print(f'No se ha eliminado el contacto {nombre}.')
                    break
            
                else:
                    print("Escriba S para eliminar contacto / Escriba N para no eliminarlo. ")
                    
            
            
        else:
            print("Contacto no encontrado. ")
