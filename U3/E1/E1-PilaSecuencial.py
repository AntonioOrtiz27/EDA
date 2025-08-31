"""Ejercicio 1 con pila secuencial - Mejor salida en consola"""
import numpy as np

class Pila:
    # Crear Pila
    def __init__(self, cantidad):
        self.cant = cantidad
        self.tope = -1
        self.items = np.zeros(cantidad, dtype=int)
        
    # Vaciar Pila
    def vacia(self):
        return self.tope == -1
    
    # Insertar
    def insertar(self, x):
        if self.tope < self.cant - 1:
            self.tope += 1
            self.items[self.tope] = x
            print(f"✔ Se apiló el elemento: {x}")
        else:
            print(f"✘ No se pudo apilar el elemento {x}, la pila está llena.")
            return 0
        
    # Mostrar
    def mostrar(self):
        print("\nEstado actual de la pila:")
        if not self.vacia():
            actual = self.tope
            while actual >= 0:
                if actual == self.tope:
                    print(f"[ {self.items[actual]} ]  <-- tope")
                else:
                    print(f"[ {self.items[actual]} ]")
                actual -= 1
        else:
            print("⚠ La pila está vacia")
        print("-" * 30)          
    
    # Suprimir
    def suprimir(self):
        if self.vacia():
            print("No se puede desapilar, la pila ya está vacia.")
        else:
            ultimo = self.items[self.tope]  # me posiciono en el último elemento
            self.tope -= 1  # y después bajo el tope
            print(f"Se desapilo el elemento(por ser pila el ultimo): {ultimo}")
            return ultimo
        
    #Retorna la cantidad de elementos que hay apilados
    def __len__(self):
        return self.tope + 1
        

if __name__ == '__main__':

    pila = Pila(cantidad=3)

    # Insertar y mostrar elementos
    print("\n=== APILANDO ELEMENTOS ===")
    pila.insertar(10)  
    pila.insertar(20)
    pila.insertar(30)   
    pila.insertar(60)  # cuarto elemento -> pila llena
    pila.mostrar()    
    print(f"La pila tiene {len(pila)} elemento/s.\n")        

    # Suprimir elementos y verificar si la pila aún sigue con elementos
    print("\n=== DESAPILANDO ===")
    pila.suprimir()       
    pila.mostrar() 
    print(f"La pila tiene {len(pila)} elemento/s.\n")

    pila.suprimir()       
    pila.mostrar() 
    print(f"La pila tiene {len(pila)} elemento/s.\n")
    
    pila.suprimir()       
    pila.mostrar()
    pila.suprimir()   # intentar desapilar vacía
