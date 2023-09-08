# Trabajo Práctico I - Programación II


import os
import bibloteca


print("Bienvenido!")
respuesta = ''


def menu():
    print("1 - Gestionar Prestamo")
    print("2 - Gestionar Devolucion")
    print("3 - Registrar nuevo libro")
    print("4 - Elimiar ejemplar")
    print("5 - Mostrar ejemplares perstados")
    print("6 - Salir")


def validarCodigo():
    cod = input("Ingrese el codigo del libro: \n")
    encontrado = False
    for libro in bibloteca.libros:
        if libro["cod"] == cod:
            encontrado = True
            indice = bibloteca.libros.index(libro)
            return indice
    if not encontrado:
        print("El codigo ingresado es incorrecto")
        return -1


while respuesta != "salir":
    menu()
    opt = input("\n Ingrese la opción de menú: ")
    os.system ("cls") #Limpiar pantalla
    if opt.isnumeric():
        if int(opt) == 1:
            ind = validarCodigo()
            if ind >= 0:
                bibloteca.prestar_ejemplar_libro(ind)
        elif int(opt) == 2:
            ind = validarCodigo()
            if ind >= 0:
                bibloteca.devolver_ejemplar_libro(ind)
        elif int(opt) == 3:
            bibloteca.registrar_nuevo_libro()
        elif int(opt) == 4:
            ind = validarCodigo()
            if ind >= 0:
                bibloteca.eliminar_ejemplar_libro(ind)
        elif int(opt) == 5:
            bibloteca.ejemplares_prestados()
        elif int(opt) == 6:
            respuesta = "salir"
        else: print("Ingrese una opción válida")
    else: 
        print("Ingrese una opción numérica")
    
    input("Presione cualquier tecla para continuar....") # Pausa

print("Hasta luego!.")