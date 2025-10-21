import numpy as np

class ListaSecuencial:
    __ultimo: 0
    __dimension: int
    __elementos:np.ndarray

    def __init__(self,dimension):
        self.__elementos = np.empty(dimension,dtype=int)
        self.__dimension = dimension
        self.__ultimo= 0

    def getElementos(self):
        return self.__elementos
    
    def vacia(self):
        return self.__ultimo == 0
    
    def llena(self):
        return self.__ultimo >= len(self.__elementos)
    
    def insertar(self, valor, pos):
        if self.llena():
            print(f"Lista llena, no se pudo insertar el elemento {valor}\n")
        else:
            if 1 <= pos <= self.__ultimo + 1:
                for i in range(self.__ultimo, pos - 1, -1):  
                    self.__elementos[i] = self.__elementos[i-1]
                self.__elementos[pos - 1] = valor
                self.__ultimo += 1
            else:
                print("Posicion incorrecta\n")

    def suprimir(self, p):
        if 1 <= p <= self.__ultimo:
            elemento = self.__elementos[p - 1]
            for i in range(p - 1, self.__ultimo-1):
                self.__elementos[i] = self.__elementos[i + 1]
            self.__ultimo -= 1
        else:
            print("Posicion incorrecta\n")
            return None
        
        return elemento
    
    def recorrer(self):
        if not self.vacia():
            for i in range(self.__ultimo):
                print(self.__elementos[i],end=" ")
        else:
            print("Lista vacia\n")
           
    def buscar(self, x):
        band = False
        i = 0
        while i < self.__ultimo and not band:
            if self.__elementos[i] == x:
                band = True 
            else:
                i += 1
    
        if band:
            print(f"Se encontro el elemento {x} en la posición {i+1}\n")
            return i+1
        else:
            print(f"No se encontró el elemento {x}\n")
            return None
        
    def anterior(self,pos):
        if 1 < pos <= self.__ultimo:
            print(f"anterior posicion a la que ingreso: {pos-1}\n")
        else:
            print("No existe la posicion anterior, a la que ingreso\n")
            
    def siguiente(self,pos):
        if 1 <= pos < self.__ultimo:
            print(f"Siguiente posicion a la que ingreso: {pos+1}\n")
        else:
            print("No existe la posicion anterior, a la que ingreso\n")
            
    def elementoPosterior(self,pos):
        if 1 <= pos < self.__ultimo:
            print(f"el elemento que se encuentra posterior a la posicion {pos} es el elemento: {self.__elementos[pos]}") 
        else:
            print(f"No existe un elemento luego de la posicion {pos}.\n")
            
    def elementoAnterior(self,pos):
        if 1 < pos <= self.__ultimo:
            print(f"el elemento que se encuentra anterior a la posicion {pos} es el elemento: {self.__elementos[pos-2]}") 
        else:
            print(f"No existe un elemento antes de la posicion {pos}.\n")
            
    def primerElemento(self):
        return self.__elementos[0]

    def ultimoElemento(self):
        return self.__elementos[self.__ultimo-1]

if __name__=="__main__":
    listita = ListaSecuencial(4)
    #insertar
    listita.insertar(10,1)
    listita.insertar(40,2)
    listita.insertar(20,3)
    listita.insertar(70,4)
    print("Mi lista de elementos inicial:")
    #recorrer
    listita.recorrer()
    #mostrar primer elemento
    print(f"\nel primer elemento de la lista es: {listita.primerElemento()}")
    #mostrar ulitmo elemento
    print(f"\nel ultimo elemento de la lista es: {listita.ultimoElemento()}")
    #suprimir
    print("\nSuprimiendo elemento ")
    listita.suprimir(1)
    #recorrer luego de suprimir
    listita.recorrer()
    #buscar
    elemento = int(input("\ningrese el elemento a buscar:"))
    listita.buscar(elemento)
    #metodo que devuelve el anterior
    pos = int(input("ingrese una pos para ver cual es la anterior:"))
    listita.anterior(pos)
    #metodo que devuelve el siguiente
    pos2 = int(input("ingrese una pos para ver cual es la pos siguiente:"))
    listita.siguiente(pos2)
    print("Estado actual de la lista:\n")
    listita.recorrer()
    #metodo que nos va devolver el elemento que se encuentra en la posicion siguiente a la ingresada
    pos3 = int(input("\ningrese una pos para ver cual es el elemento de la posicion siguiente:"))
    listita.elementoPosterior(pos3)
    #metodo que nos va devolver el elemento que se encuentra en la posicion anterior a la ingresada
    pos4 = int(input("ingrese una pos para ver cual es el elemento de la posicion anterior:"))
    listita.elementoAnterior(pos4)
    
"""
Este código esta compuesto por las operaciones básicas de un TAD Lista Secuencial:
insertar - eliminar - recorrer - buscar - anterior - siguiente 
"""



    
