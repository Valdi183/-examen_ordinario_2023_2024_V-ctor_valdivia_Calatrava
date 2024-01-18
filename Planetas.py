"""
Ejercicio 2 "Estrella de la muerte vs planetas". Este archivo contiene el código
principal del ejercicio 2, donde se define la clase Planeta, y las subclases que
heredan de Planeta con sus respectivos nombres y datos
"""

nombre = ""
volumen = int
clasificación = int

class Planeta:
    def __init__(self, nombre, volumen, clasificación):
        self.nombre = nombre
        self.volumen = volumen
        self.clasificación = clasificación
    
class Planeta_Concordia(Planeta):
    def __init__(self, nombre, volumen, clasificación):
        super().__init__(nombre, volumen, clasificación)
        self.nombre = "Concordia"
        self.volumen = 500 * "km^3"
        self.clasificación = 1
class Planeta_Ilum(Planeta):
    def __init__(self, nombre, volumen, clasificación):
        super().__init__(nombre, volumen, clasificación)
        self.nombre = "Ilum"
        self.volumen = 1200 * "km^3"
        self.clasificación = 2

class Planeta_Kamino(Planeta):
    def __init__(self, nombre, volumen, clasificación):
        super().__init__(nombre, volumen, clasificación)
        self.nombre = "Kamino"
        self.volumen = 800 * "km^3"
        self.clasificación = 3