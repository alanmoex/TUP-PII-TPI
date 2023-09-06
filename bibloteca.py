import libro as l

# Crear una lista vacía para almacenar los libros
libros = []

# Añadir los diccionarios a la lista
libros.append(l.libro1)
libros.append(l.libro2)
libros.append(l.libro3)

def ejemplares_prestados():
    # completar
    return None

def registrar_nuevo_libro():
    nuevo_libro = l.nuevo_libro()
    #completar
    libros.append(nuevo_libro) 
    print(libros)
    return None

def eliminar_ejemplar_libro():
    #completar
    return None

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

def devolver_ejemplar_libro():
    #completar
    return None

def nuevo_libro():
    #completar
    return None