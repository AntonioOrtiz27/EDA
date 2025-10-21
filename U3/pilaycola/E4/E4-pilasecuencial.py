import numpy as np
class Pila:
    def __init__(self,cantidad):
        self.cant = cantidad
        self.tope = -1
        self.elementos = np.zeros(cantidad,dtype=int)
        
    def vacia(self):
        return self.tope == -1

    def insertar(self, ultimo):
        if self.tope < self.cant-1:
            self.tope+=1
            self.elementos[self.tope] = ultimo
            print(f"Se apilo el elemento {ultimo}")
        
    def suprimir(self):
        if self.vacia():
            print("La pila esta vacia.")
            return None
        else:
            x = self.elementos[self.tope]
            self.tope -= 1
            return x
        
def mostrar_estado(p1,p2,p3):
    print("Estado de las pilas")
    print("Pila 1: ")
    p1.recorrer()
    print("Pila 2: ")
    p2.recorrer()
    print("Pila 3: ")
    p3.recorrer()
        
if __name__=="__main__":
    n=int(input("Ingresa la cantidad de discos: "))
    num_discos=n
    pila1=Pila(n)
    pila2=Pila(n)
    pila3=Pila(n)
    
    while n>0:
        pila1.insertar(n)
        n-=1
    mostrar_estado(pila1,pila2,pila3)
    