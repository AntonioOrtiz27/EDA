import numpy as np
class Pila:
    def __init__(self,tamaño):
        self.cant = 0
        self.tope = -1
        self.tamaño= tamaño
        self.elementos = np.zeros(tamaño,dtype=int)
        
    def vacia(self):
        return self.tope == -1

    def insertar(self, ultimo):
        if self.tope < self.tamaño-1:
            self.tope+=1
            self.elementos[self.tope] = ultimo
            print(f"Se apilo el elemento {ultimo}")
        
    def suprimir(self,x):
        if self.vacia():
            print("La pila esta vacia.")
            return None
        else:
            x = self.elementos[self.tope]
            self.tope =- 1
            return x

if __name__=="__main__":
    pila = Pila()
    