import os

class Pelicula:
    def __init__(self, titulo, director, anio, genero, valoracion):
        self.titulo = titulo
        self.director = director
        self.anio = anio
        self.genero = genero
        self._valoracion = valoracion 

class CatalogoPeli:
    def __init__(self, nombre, ruta_archivo):
        self.nombre = nombre 
        self.ruta_archivo = ruta_archivo

    def crear_catalogo(self):
        f = open(self.ruta_archivo, "w")
        f.close()
        return ("Catalogo creado")

    def agregar_pelicula(self, movie):
        f = open(self.ruta_archivo, "a")
        f.write(movie.titulo + "\n" + movie.director + "\n" + movie.anio + "\n" + movie.genero + "\n" + movie._valoracion + "\n")
        f.close()
        return ("Pelicula agregada!")

    def listar_pelicula(self):
        f = open(self.ruta_archivo, "r")
        print(f.read())
        f.close()

    def eliminar_catalogo(self):
        os.remove(self.ruta_archivo)
        return ("Catalogo eliminado")
    
def menu():
    print("|| Menu de opciones ||")
    print("====================")
    print("1. Crear Catalogo")
    print("2. Agregar Pelicula")
    print("3. Listar Peliculas")
    print("4. Eliminar catalogo de peliculas")
    print("5. Salir")
     
def directorio():
        ruta = CatalogoPeli("Test1", "Catalogo1.txt")
        while True:
            menu()
            seleccion = int(input("Ingrese la opcion: ")) 

                       
            if seleccion == 1:
                print(ruta.crear_catalogo()) 
            elif seleccion == 2:
                print("Ingrese los siguientes datos: ")
                print("Titulo: ")
                titulo = input("")
                print("Director: ")
                director = input("")
                print("Año: ")
                anio = input("")
                print("Genero: ")
                genero = input("")
                print("Valoracion: ")
                valoracion = input("")
                pelicula1 = Pelicula(titulo,director,anio,genero,valoracion)
                print(ruta.agregar_pelicula(pelicula1)) 
            elif seleccion == 3:
                print(ruta.listar_pelicula()) 
            elif seleccion == 4:
                ruta.eliminar_catalogo() 
            elif seleccion == 5:
                print("Seguro? S/N")
                rta = input()
                if rta == "S":
                    print("Saliendo del catalogo")
                    break
                else:
                    print("volver")
            else:
                print("Opcion no valida.")

directorio()