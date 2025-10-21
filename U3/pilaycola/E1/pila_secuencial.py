"""Ejercicio 1 con pila secuencial - Mejor salida en consola"""
import numpy as np

class PilaSec:
    # Crear Pila
    def __init__(self, cantidad):
        self.cant = cantidad
        self.tope = -1
        self.items = np.zeros(cantidad, dtype=int)
        
    # Vaciar Pila
    def vacia(self):
        return self.tope == -1
    
    # Pila_llena()
    def llena(self,x):
        if self.cant <= len(self.items):
            print(f"No se pudo insertar {x} la pila esta llena")
    
    # Insertar
    def insertar(self, x):
        if self.tope < self.cant-1:
            self.tope += 1
            self.items[self.tope] = x
            print(f"✔ Se apiló el elemento: {x}")
        else:
            self.llena(x)
        
    # Recorrer
    def recorrer(self):
        print("\nEstado actual de la pila:")
        if self.vacia():
            print("Pila vacia imposible de recorrer.")
        else:
            for i in range(self.tope,-1,-1):
                print(self.items[i], end= " ")

    
    # Suprimir
    def suprimir(self):
        if self.vacia():
            print("No se puede desapilar, la pila ya está vacia.")
        else:
            ultimo = self.items[self.tope]  # me posiciono en el último elemento
            self.tope -= 1  # y después bajo el tope
            print(f"Se desapilo el elemento(por ser pila el ultimo): {ultimo}")
        
    #Retorna la cantidad de elementos que hay apilados
    def __len__(self):
        return self.tope + 1
        

if __name__ == '__main__':

    pila = PilaSec(cantidad=3)

    # Insertar y mostrar elementos
    print("\n=== APILANDO ELEMENTOS ===")
    pila.insertar(10)  
    pila.insertar(20)
    pila.insertar(30)   
    pila.insertar(60)  # cuarto elemento -> pila llena
    pila.recorrer()    
    print(f"La pila tiene {len(pila)} elemento/s.\n")        

    # Suprimir elementos y verificar si la pila aún sigue con elementos
    print("\n=== DESAPILANDO ===")
    pila.suprimir()       
    pila.recorrer() 
    print(f"La pila tiene {len(pila)} elemento/s.\n")

    pila.suprimir()       
    pila.recorrer() 
    print(f"La pila tiene {len(pila)} elemento/s.\n")
    
    pila.suprimir()       
    pila.recorrer()
    pila.suprimir()   # intentar desapilar vacía
