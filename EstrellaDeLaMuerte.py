from Planetas import Planeta

nombre = ""
volumen = int
clasificación = int
objeto = Planeta(nombre, volumen, clasificación) 
puntos_de_vida = 1000

class Estrella_de_la_muerte(Planeta):
    def __init__(self, puntos_de_vida):
        super().__init__(nombre, volumen, clasificación)
        self.puntos_de_vida = puntos_de_vida
    
    def destruir_planeta(self, objeto.volumen):
        if self.volumen <= self.puntos_de_vida:
            print("La estrella de la muerte ha destruido el planeta")
        if self.volumen > puntos_de_vida:
            print("La estrella de la muerte no puede destruir el planeta")
        

        