from anytree import Node, RenderTree
import numpy as np
import networkx as nx
import matplotlib.pyplot as plt

"""
Ejercicio 1: Considere el TAD árbol. 
a) Defina  el objeto de datos. 
b) Especifique e implemente la operación que imprima los descendientes 
terminales de un nodo ingresado previamente por teclado. 
"""

# a) Defina el objeto de datos. 
class Nodo: 
    __izq:object
    __der: object
    __elem: str
    
    def __init__(self,x):
        self.__izq = None
        self.__der = None
        self.__elem = x

    def getDer(self): return self.__der
    def getIzq(self): return self.__izq
    def setDer(self,x): self.__der = x
    def setIzq(self,y): self.__izq = y
    def getDato(self): return self.__elem
    
    def grado(self):
        g = 0
        if self.__izq is not None:
            g+=1
        if self.__der is not None:
            g+=1
        return g        
                                                                                                                                                                               
class Arbol3:
    __raiz:Nodo
    
    def __init__(self):
        self.__raiz = None
        
    def getRaiz(self): return self.__raiz    
        
    def vacia(self): return self.__raiz == None
        
    def insertar(self,nodo:Nodo,valor:str):
        
        if self.vacia():
            self.__raiz = Nodo(valor)
        else:
            if valor < nodo.getDato():
                if nodo.getIzq() == None:
                    nodo.setIzq(Nodo(valor))
                else:
                    self.insertar(nodo.getIzq(),valor)
            elif valor > nodo.getDato():
                if nodo.getDer() == None:
                    nodo.setDer(Nodo(valor))
                else:
                    self.insertar(nodo.getDer(),valor)
                
    def convertir_a_anytree(self, nodo):
        if nodo is None:
            return None
        nodo_any = Node(str(nodo.getDato()))
        if nodo.getIzq() is not None:
            hijo_izq = self.convertir_a_anytree(nodo.getIzq())
            hijo_izq.parent = nodo_any
        if nodo.getDer() is not None:
            hijo_der = self.convertir_a_anytree(nodo.getDer())
            hijo_der.parent = nodo_any
        return nodo_any


    def buscar(self,nodo:Nodo,valor:int):
        if nodo is None:
            encontrado = None      
        else:
            if nodo.getDato() == valor:
                encontrado = nodo
            elif valor < nodo.getDato():
                encontrado = self.buscar(nodo.getIzq(),valor)
            else:
                encontrado = self.buscar(nodo.getDer(),valor)
    
        return encontrado
    
    # b) Especifique e implemente la operación que imprima los descendientes 
    # terminales de un nodo ingresado previamente por teclado. 

    def hojas(self, nodo):
        if nodo is not None:
            if nodo.getIzq() is None and nodo.getDer() is None:
                print(nodo.getDato(), end=" ")
            self.hojas(nodo.getIzq())
            self.hojas(nodo.getDer())
            
    def descendientesTerminales(self,raiz, valor):
        nodo = self.buscar(raiz, valor)
        if nodo is None:
            print("El nodo no existe en el árbol.")
        else:
            print(f"Descendientes terminales de {valor}: ", end="")
            self.hojas(nodo)
            print()

    
                
