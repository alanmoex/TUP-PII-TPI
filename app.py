# Trabajo Práctico I - Programación II


import os
import bibloteca
import cod_generator
import libro


print("Bienvenido!")
respuesta = ''


def menu():
    print("1 - Gestionar Prestamo")
    print("2 - Gestionar Devolucion")
    print("3 - Registrar nuevo libro")
    print("4 - Elimiar ejemplar")
    print("5 - Mostrar ejemplares perstados")
    print("6 - Salir")

def gestionarPrestamo():
    encontrado = False
    cod = input("Ingrese el codigo del libro: \n")
    for dicc in bibloteca.libros:
        if dicc["cod"] == cod:
            encontrado = True
            indice = bibloteca.libros.index(dicc)
            print(f"Autor: {dicc['autor']}. Titulo: {dicc['titulo']}. Ejemplares disponibles: {dicc['cant_ej_ad']}")
            if dicc["cant_ej_ad"] > 0:
                bibloteca.prestar_ejemplar_libro(indice)
            else:
                print("No quedan ejemplares para prestar.\n")

    if not encontrado:
        print("Libro no encontrado")

while respuesta != "salir":
    menu()
    opt = input("\n Ingrese la opción de menú: ")
    os.system ("cls") #Limpiar pantalla
    if opt.isnumeric():
        if int(opt) == 1:
            gestionarPrestamo()
            print()
        elif int(opt) == 2:
            #completar
            print()
        elif int(opt) == 3:
            #completar
            bibloteca.registrar_nuevo_libro()
            
            print()
        elif int(opt) == 4:
            #completar
            print()
        elif int(opt) == 5:
            #completar
            print()
        elif int(opt) == 6:
            respuesta = "salir"
        else: print("Ingrese una opción válida")
    else: 
        print("Ingrese una opción numérica")
    
    input("Presione cualquier tecla para continuar....") # Pausa

print("Hasta luego!.")