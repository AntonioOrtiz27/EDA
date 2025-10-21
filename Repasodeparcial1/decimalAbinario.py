import numpy as np
class Celda:
    __elem:int
    __sig:None
    def __init__(self,elem:int):
        self.__elem = elem
        self.__sig = None
    def getSig(self):
        return self.__sig
    def setSig(self,sig):
        self.__sig = sig
    def getElem(self):
        return self.__elem
    
class PilaEncadenada:
    __tope : Celda
    __cant : int
    def __init__(self):
        self.__tope = None
        self.__cant = 0
        
    def vacia(self):
        return self.__cant == 0
    
    def insertar(self,elem:int):
        nuevo  = Celda(elem) 
        nuevo.setSig(self.__tope) 
        self.__tope = nuevo 
        self.__cant += 1 
   
    def suprimir(self):
        self.__cant-=1 
        borrado = self.__tope.getElem() 
        self.__tope = self.__tope.getSig() 
        return borrado 
    
    def recorrer(self):
        aux = self.__tope 
        while aux != None: 
            print(aux.getElem())
            aux = aux.getSig()

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
    
    def suprimir(self):
        if self.vacia():
            return None
        else:
            ultimo = self.items[self.tope]
            self.tope -= 1
            return ultimo

pilaEnc = PilaEncadenada()
pilaSecuencial = PilaSec(30)

def DivisionesSucesivas(n,pilaEnc:PilaEncadenada):
    while n > 2:
        pilaEnc.insertar(n % 2)
        n = n // 2
    pilaEnc.insertar(n % 2)
    while not pilaEnc.vacia():
        print(pilaEnc.suprimir())
        
def DivisionesSucesivas2(n, pilaSecuencial:PilaSec):
    while n > 2:
        pilaSecuencial.insertar(n % 2)
        n = n // 2
    pilaSecuencial.insertar(n % 2)
    while not pilaSecuencial.vacia():
        print(pilaSecuencial.suprimir())

print("Pila Secuencial - Numero 30 a binario")
DivisionesSucesivas2(30, pilaSecuencial)
print("Pila Encadenada - Numero 25 a binario")
DivisionesSucesivas(25, pilaEnc)
