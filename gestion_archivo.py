import os
from contacto import Contacto 
from gestion_contactos import GestionContactos

#Creamos clase para gestionar el archivo con la lista de contactos
class ArchivoContactos:
    def __init__(self, nombre_archivo):
        self.nombre_archivo = nombre_archivo   

    #Creamos metodo para guardar los contactos en un archivo
    #Sera de tipo w porque el archivo se sobreescribe cada vez que 
    # actualizamos la lista
    def guardar(self, lista_contactos):
        try:
            with open(self.nombre_archivo, "w", encoding='utf-8' ) as archivo:
                for contacto in lista_contactos:
                    archivo.write(f'{contacto.get_nombre()},{contacto.get_telefono()},{contacto.get_email()}\n')

        except Exception as e:
            print(f"Error al guardar los contactos: {e}")

    #Creamos metodo que se utilizara para cargar, lee el archivo y convierte cada
    # linea en un objeto de la clase contacto
    def cargar(self):
        contactos = []
        try: 
            with open(self.nombre_archivo, "r", encoding='utf-8') as archivo:
                #Cada linea del archivo es "nombre, telefono, email" de cada contacto 

                for linea in archivo:
                    #Quitamos los espacios de cada linea y la separamos en distintas partes separadas por ,
                    #Por ejemplo: "ana,654321987,ana@gmail.com" --> ['ana', '654321987', 'ana@gmail.com']
                    partes = linea.strip().split(",")
                    
                    if len(partes) == 3:
                        #Asignamos cada parte (nombre, telefono o email) a su variable correspondiente
                        nombre, telefono, email = partes
                        #Creamos un objeto de tipo Contacto con esos valores y los añadimos a la lista de 
                        # contactos llamada "contactos" creada al ppio de este metodo, luego se devolverá 
                        # en el return
                        contactos.append(Contacto(nombre, int(telefono), email))

        #Si no hay archivo creado devolvemos la lista vacia
        except FileNotFoundError:
            pass
        
        except Exception as e:
            print(f"Error al cargar los contactos: {e}")

        return contactos
    
    #Creamos metodo para eliminar el archivo creado
    def eliminar_archivo(self):
        os.remove(self.nombre_archivo)
 
    