"""Ejercicio 3 - Las escaleras"""
import numpy as np
from random import randint
class Pila:
    def __init__(self,cantidad):
        self.cant=cantidad
        self.tope = -1
        self.elementos = np.zeros(cantidad,dtype=int)
        print(f"Cantidad de peldaños de la escalera: {self.cant}")
        
    def vacia(self):
        return self.tope == -1
    
    def insertar(self, ultimo):
        if self.tope < self.cant-1:
            self.tope += 1
            self.elementos[self.tope] = ultimo
            print(f"Se apilo el elemento {ultimo}")
        else:
            print(f"No se puede apilar {ultimo} ya que la pila esta llena.")
            return 0

    def mostrar(self):
        print("\nEstado actual de la pila:")
        if not self.vacia():
            actual = self.tope
            while actual >= 0:
                if actual == self.tope:
                    print(f"[ {self.elementos[actual]} ]  <-- tope")
                else:
                    print(f"[ {self.elementos[actual]} ]")
                actual -= 1
        else:
            print("⚠ La pila está vacia")
        print("-" * 30)    
        
    def suprimir(self):
        if self.vacia():
            print("No se puede desapilar, la pila ya está vacia.")
        else:
            ultimo = self.elementos[self.tope]  
            self.tope -= 1  
            print(f"Se desapilo el elemento: {ultimo}")
        
def subirescaleras(n,pilita:Pila):
    while n>0:
        caso =randint(1,2)
        if caso == 1:
            pilita.insertar(1)
            n-=1
        else:
            pilita.insertar(2)
            n -= 1
    print("-"*30)
    while not pilita.vacia():
        pilita.suprimir()
        
                          
        
if __name__=="__main__":
    cantidad = int(input("Ingrese el tamaño (N) de la escalera(en peldaños):"))
    pila = Pila(cantidad)
    print("-"*50)
    
    subirescaleras(cantidad,pila)
    pila.mostrar()


        
        
