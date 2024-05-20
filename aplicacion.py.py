# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""

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
    print("1. Listar personas")
    print("2. Agregar personas")
    print("3. Salir")

def main():
    intentos = 0
    while intentos < 2:
        login = input("Ingrese su login: ")
        clave = input("Ingrese su clave: ")

        if verificar_credenciales(login, clave):
            print("Bienvenido al sistema.")
            mostrar_menu()
            break
        else:
            intentos += 1
            print("Credenciales incorrectas. Por favor, inténtelo de nuevo.")

    if intentos == 2:
        print("Demasiados intentos fallidos. El programa terminará.")

main()
