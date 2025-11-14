from anytree import Node, RenderTree
import numpy as np
import networkx as nx
import matplotlib.pyplot as plt

"""
Ejercicio 1:  
a) Considere trabajar con el TAD árbol binario de búsqueda. 
b) Especifique e implemente la operación  que cuente la cantidad de nodos que tienen un 
solo descendiente directo.
"""

# a) Defina el objeto de datos. 
class Nodo:
    __der:object
    __izq:object
    __elem: str
    
    def __init__(self,elemento):
        self.__der = None
        self.__izq = None
        self.__elem = elemento
        
    def getDer(self): return self.__der
    def getIzq(self): return self.__izq
    def setDer(self,x): self.__der = x
    def setIzq(self,y): self.__izq = y
    def getDato(self): return self.__elem
    
    def grado(self):
        g = 0
        if self.__izq is not None:
            g += 1
        if self.__der is not None:
            g += 1
        return g
    
class Arbol1:
    __raiz:Nodo
    
    def __init__(self):
        self.__raiz = None
        
    def getRaiz(self): 
        return self.__raiz
    
    def vacio(self): 
        return self.__raiz == None
    
    def insertar(self,valor,nodo):
        if self.vacio():
            self.__raiz = Nodo(valor)
        elif valor < nodo.getDato():
            if nodo.getIzq() == None:
                nodo.setIzq(Nodo(valor))
            else:
                self.insertar(valor,nodo.getIzq())
        elif valor > nodo.getDato():
            if nodo.getDer() == None:
                nodo.setDer(Nodo(valor))
            else:
                self.insertar(valor,nodo.getDer())
        return valor
    
    def convertir_a_anytree(self,nodo):
        """Convierte un Nodo propio en un nodo de anytree.Node recursivamente."""
        if nodo is None:
            return None
        # Crear nodo raíz con el mismo dato
        nodo_any = Node(nodo.getDato())
        # Agregar hijos si existen
        if nodo.getIzq():
            nodo_any.children += (self.convertir_a_anytree(nodo.getIzq()),)
        if nodo.getDer():
            nodo_any.children += (self.convertir_a_anytree(nodo.getDer()),)
        return nodo_any
            
        
    # b) Especifique e implemente la operación  que cuente la cantidad de nodos que tienen 
    # un solo descendiente directo.        

    """--- Especificación ---"""
    
    # Nombre: PreOrden
    # Funcion: Procesa A en Preorden
    # Salida: Sujeta al proceso que se realice sobre los elementos de A

    """--- Implementación ---"""

    def preorden(self,nodo):
        c = 0
        
        if nodo != None:
            if nodo.grado() == 1:
                c += 1
                print(f"Nodo con un solo hijo: {nodo.getDato()}")
            c += self.preorden(nodo.getIzq())
            c += self.preorden(nodo.getDer())
        print("\nTotal de nodos con un solo descendiente directo:",c)
        return c

    """--- Fin de Ejercicio 1 ---"""
    
    
"""
Ejercicio 3: : Considere el TAD digrafo, formado por N vértices. 
a) Defina  el objeto de datos. 
b) Especifique e implemente la operación que muestre todos los nodos sumidero, para ello 
implemente las operaciones grado de entrada  y grado de salida 
"""

# a) Defina el objeto de datos.
class Digrafo:
    __vertices: int
    __matriz: np.ndarray
    
    def __init__(self,N):
        self.__matriz = np.zeros((N,N),dtype=int)
        self.__vertices = N   
    
    def agregarAristas(self,u,v):
        if self.__matriz[u][v] == 0:
            self.__matriz[u][v] = 1
    
    def matrizAdyacencia(self):
        print(self.__matriz)
    
    def adyacentes(self,u:int):
        lista = []
        
        for v in range(self.__vertices):
            if self.__matriz[u][v] == 1:
                lista.append(v)
                
        return lista
    
    """--- Especificación ---"""
    
    # Nombre: Grado de Entrada
    # Funcion: Determina cantidad de aristas que le llegan a u
    # Salida: Reporta el grado de entrada de u.
    
    # Nombre: Grado de Salida
    # Funcion: Determina cantidad de aristas que salen de u
    # Salida: Reporta el grado de entrada de u.
    
    # Nombre: Nodo Sumidero
    # Funcion: Evalúa si u es nodo sumidero de G
    # Salida: V si u es nodo sumidero de G
    
    """--- Implementación ---"""
    
    def grado_entrada(self, u:int):
        cont = 0
        
        for i in range(self.__vertices):
            if self.__matriz[i][u] == 1:
                cont += 1
                
        return cont

    def grado_salida(self, u:int):
        return len(self.adyacentes(u))
    
    def nodoSumideros(self):
        band = False
        
        for u in range(self.__vertices):
            if self.grado_salida(u) == 0 and self.grado_entrada(u) > 0:
                print(u)
                band= True
                
        if not band:
            print(f"No existen nodos sumideros")
            
    """--- Fin de Ejercicio 3 ---"""