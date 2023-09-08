import libro as l

# Crear una lista vacía para almacenar los libros
libros = []

# Añadir los diccionarios a la lista
libros.append(l.libro1)
libros.append(l.libro2)
libros.append(l.libro3)


def registrar_nuevo_libro():
    nuevo_libro = l.nuevo_libro()
    #completar
    libros.append(nuevo_libro) 
    print("Se ha registrado un nuevo libro satisfactoriamente. Sus datos son:\n")
    print(f"Codigo: {nuevo_libro['cod']} --- Titulo: {nuevo_libro['titulo']} --- Autor: {nuevo_libro['autor']} --- Ejemplares adquiridos: {nuevo_libro['cant_ej_ad']}" )
    return None

def eliminar_ejemplar_libro(libro):
    cantidad_eliminar = int(input("Ingrese la cantidad de ejemplares a eliminar: "))
    if cantidad_eliminar <= libro['cant_ej_ad']:
        libro['cant_ej_ad'] -= cantidad_eliminar
        print("Ejemplar(es) eliminado(s) con éxito.")
    else:
        print("Error: La cantidad a eliminar es mayor que la cantidad adquirida.")

def prestar_ejemplar_libro(indice):
    libro = libros[indice]
    print(f"Autor: {libro['autor']}. Titulo: {libro['titulo']}. Ejemplares disponibles: {libro['cant_ej_ad']}")
    if libro["cant_ej_ad"] > 0:
        libros[indice]["cant_ej_ad"] -= 1
        libros[indice]["cant_ej_pr"] += 1
        print("El prestamo ha sido gestionado satisfactoriamente. \n")
    else:
        print("No quedan ejemplares para prestar.\n")
    return None

def devolver_ejemplar_libro(indice):
    libro = libros[indice]
    if libro["cant_ej_pr"] > 0:
        libros[indice]["cant_ej_ad"] += 1
        libros[indice]["cant_ej_pr"] -= 1
        print("La devolucion ha sido gestionado satisfactoriamente. \n")
    else:
        print("No hay ejemplares prestados de ese libro.\n")
    return None

def ejemplares_prestados(libros):
    for libro in libros:
        if libro['cant_ej_pr'] > 0:
            print(f"Título: {libro['titulo']}")
            print(f"Cantidad de ejemplares prestados: {libro['cant_ej_pr']}")
    else:
        print("No hay ejemplares prestados en este momento.")
