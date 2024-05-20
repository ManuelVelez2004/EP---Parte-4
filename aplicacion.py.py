# -*- coding: utf-8 -*-

import gestion_productos

def verificar_credenciales(login, clave):
    with open("usuarios.txt", "r") as file_login:
        login_correcto = file_login.read().strip()

    with open("claves.txt", "r") as file_clave:
        clave_correcta = file_clave.read().strip()

    if login == login_correcto and clave == clave_correcta:
        return True
    else:
        return False

def mostrar_menu():
    print("Menú de opciones:")
    print("1. Listar")
    print("2. Agregar")
    print("3. Salir")
    
def agregar():
    print("-- Agregar Datos a un Archivo --")
    archivo = input("Archivo: ")
    contenido = input("Contenido: ")
    gestion_productos.agregar_prod(archivo, contenido)
    
def listar():
    print("-- Mostrar contenido de un archivo -- \n")

    # Obtener datos de los archivos
    producto_nombre = gestion_productos.listar_nombre().splitlines()
    producto_codigo = gestion_productos.listar_codigo().splitlines()
    producto_precio = gestion_productos.listar_precio().splitlines()

    # Imprimir encabezados
    print("{:<20}\t{:<10}\t{:<10}".format("Nombre", "Código", "Precio"))

    # Iterar sobre los datos y mostrarlos con el formato adecuado
    for nombre, codigo, precio in zip(producto_nombre, producto_codigo, producto_precio):
        print("{:<20}\t{:<10}\t{:<10}".format(nombre, codigo, precio))


def salir():
    print("Gracias por su visita....")

def error():
    print("Opción incorrecta")

def main():
    intentos = 0
    while intentos < 3:
        login = input("Ingrese su login: ")
        clave = input("Ingrese su clave: ")

        if verificar_credenciales(login, clave):
            print("Bienvenido al sistema.")
            opcion = 1
            while opcion != 3:
                mostrar_menu()
                opcion = int(input("Opción: "))
                if opcion == 1:
                    listar()
                elif opcion == 2:
                    agregar()
                elif opcion == 3:
                    salir()
                else:
                    error()
            break 
        else:
            intentos += 1
            print("Credenciales incorrectas. Por favor, inténtelo de nuevo.")

    if intentos == 3:
        print("Demasiados intentos fallidos. El programa terminará.")


main()