"""
Este código contiene el programa que genera una pirámide de asteriscos, según el número
que pida el usuario
"""
numero_usuario = 0
asteriscos = ["*"]

def preguntar_usuario(numero_usuario):
    while True:
        try:
            numero_usuario = int(input("Introduzca un número entero positivo menor que 8: "))
            if numero_usuario > 8 or numero_usuario < 1:
                print("Introduzca un numero válido")
        except:
            ValueError
        return numero_usuario

def generar_pirámide(numero_usuario,asteriscos):
    while True:
        if len(asteriscos) == numero_usuario:
            print(asteriscos)

preguntar_usuario(numero_usuario)
generar_pirámide(numero_usuario,asteriscos)