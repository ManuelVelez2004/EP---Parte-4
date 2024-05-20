

def agregar_prod(nombre, contenido):
    archivo = open(nombre,"at")
    archivo.write("\n" + contenido)
    archivo.close()

def listar_nombre():
    nombre = "nombre.txt"
    archivo = open(nombre,"rt")
    contenido = archivo.read()
    return contenido
def listar_codigo():
    nombre = "codigo.txt"
    archivo = open(nombre,"rt")
    contenido = archivo.read()
    return contenido
def listar_precio():
    nombre = "precio.txt"
    archivo = open(nombre,"rt")
    contenido = archivo.read()
    return contenido