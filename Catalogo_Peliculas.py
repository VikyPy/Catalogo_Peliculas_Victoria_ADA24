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
        if os.path.isfile(self.ruta_archivo):
             cat_existe = input("El Catálogo " + self.ruta_archivo + " ya existe. ¿Desea sobrescribirlo? (S/N): ")
             if cat_existe.lower() != 's':
                return "No se creó el Catálogo."

        with open(self.ruta_archivo, "w") as f:
            pass  
        return "Catálogo creado!"

    def agregar_pelicula(self, movie):
        f = open(self.ruta_archivo, "a")
        f.write(movie.titulo + "\n" + movie.director + "\n" + movie.anio + "\n" + movie.genero + "\n" + movie._valoracion + "\n")
        f.close()
        return ("Película agregada!")

    def listar_pelicula(self):
        try:
            f = open(self.ruta_archivo, "r")
        except FileNotFoundError:
            return ("El Catálogo no existe!")
        else:
            print(f.read())
            f.close()

    def eliminar_catalogo(self):
        os.remove(self.ruta_archivo)
        return ("Catálogo eliminado!")

def menu():
    print("╔═══════════════════════╗")
    print("║    Menú de Opciones   ║")
    print("╚═══════════════════════╝")
    print("1. Agregar Película")
    print("2. Listar Películas")
    print("3. Eliminar Catálogo de Películas")
    print("4. Salir")
    print("≡ ≡ ≡ ≡ ≡ ≡ ")

def directorio():
         nombre = input("► Ingrese el nombre del Catálogo: ")
         ruta_archivo = nombre + ".txt"
         ruta = CatalogoPeli(nombre, ruta_archivo)
         print(ruta.crear_catalogo())

         while True:
            menu()
            seleccion = int(input("► Ingrese la opción: "))

            if seleccion == 1:
                print("► Ingrese los siguientes datos de la Peícula: ")
                titulo = input("► Título: ")
                director = input("► Director: ")
                anio = input("► Año: ")
                genero = input("► Género: ")
                valoracion = input("► Valoración: ")
                pelicula1 = Pelicula(titulo,director,anio,genero,valoracion)
                print(ruta.agregar_pelicula(pelicula1))
            elif seleccion == 2:
                print(ruta.listar_pelicula())
            elif seleccion == 3:
                ruta.eliminar_catalogo()
            elif seleccion == 4:
                print("► Seguro? S/N")
                rta = input()
                if rta == "s": 
                    print("Saliendo del Catálogo ➜")
                    break
                else:
                    print("Volviendo al menú ↻")
            else:
                print("Opción no válida ✖")

directorio()