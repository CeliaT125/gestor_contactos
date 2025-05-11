class Contacto:
# creamos los atributos
    def __init__(self, nombre, telefono, email):
        self.__nombre = nombre
        self.__telefono = telefono
        self.__email = email

# Añadimos los getters
    def get_nombre(self):
        return self.__nombre
    
    def get_telefono(self):
        return self.__telefono
    
    def get_email(self):
        return self.__email
    
# Mostramos los detalles de los contactos
    def __str__(self):
        return f"Nombre: {self.__nombre}, telefono: {self.__telefono}, email: {self.__email}"

    def escribir_peliculas(self):
        return f'{self.__nombre},{self.__telefono},{self.__email}'