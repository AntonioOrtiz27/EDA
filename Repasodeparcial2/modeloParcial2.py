from anytree import Node, RenderTree
import numpy as np
import networkx as nx
import matplotlib.pyplot as plt


"""
Ejercicio 1:  Considere trabajar con el TAD árbol binario de búsqueda. 
a) Defina el objeto de datos. 
b) Especifique e implemente la operación  que que imprima todos los nodos se  encuentran 
en un nivel n ingresado por teclado. (Considere el Nivel de la raiz 1)
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
    
class Arbol2:
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
    
    
    
    # b) Especifique e implemente la operación que imprima todos los nodos que se encuentran 
    # en un nivel n ingresado por teclado. (Considere el Nivel de la raiz 1)
    
    # Nombre: Nivel
    # Funcion: Calcula el nivel del nodo con clave X
    # Salida: Reporta el nivel del nodo con clave X si X pertenece A; Error en caso contrario
    
    def nivel(self, nodo, n):
        if nodo is not None:
            if n == 1:
                print(nodo.getDato(), end=" ")
            elif n > 1:
                self.nivel(nodo.getIzq(), n - 1)
                self.nivel(nodo.getDer(), n - 1)
                
    """--- Fin de Ejercicio 1 ---"""

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
    
    """
    Ejercicio 2: 
    Considere trabajar con el TAD hashing, con la política de manejo de colisiones: Encadenamiento. 
    a. Defina el objeto de datos, considerando aproximadamente 1000 claves. 
    b. Implemente la función hash a usar. 
    c. Especifique e implemente la operación Buscar_clave y muestre la cantidad de intentos en 
    que la encontró.
    """
    
class Nodito:
    __elem : int
    __sig : None

    def __init__(self,elem:int):
        self.__elem = elem
        self.__sig = None
        
    def getElem(self): return self.__elem
    
    def setElem(self,elem): self.__elem = elem
        
    def getSig(self): return self.__sig
    
    def setSig(self,sig):self.__sig = sig
        
class ListaEnlazada:
    __cabeza : Nodito
    
    def __init__(self):
        self.__cabeza = None
        
    def getCab(self): return self.__cabeza
        
    def __str__(self):
        actual = self.__cabeza
        elementos = []
        while actual:
            elementos.append(str(actual.getElem()))  # convertimos a string ya que join funciona solo para
            actual = actual.getSig()
        return " -> ".join(elementos)

    def insertar(self, valor:int):
        nuevo = Nodito(valor)
        actual = self.__cabeza
        repetido = False

        if not actual:
            self.__cabeza = nuevo
        else:
            while actual.getSig() != None:
                if actual.getElem() == valor:
                    repetido = True
                actual = actual.getSig()
            if actual.getElem() == valor:
                repetido = True
                print(f"el elemento {valor} no se inserto ya esta en la tabla")
            if not repetido:
                actual.setSig(nuevo)
                
# a) Defina el objeto de datos. Considerando 1000 claves                
class Hash:
    __tabla:np.ndarray
    __tamaño:int
    
    def __init__(self, tamaño):
        self.__tamaño = int(np.ceil(self.getPrimo(tamaño/0.7)))
        self.__tabla = np.empty(self.__tamaño, dtype=object)
        for i in range(self.__tamaño):
            self.__tabla[i] = ListaEnlazada()

    def getPrimo(self,n):
        n += 1
        while not self.es_primo(n):
            n += 1
        return n
    
    def es_primo(self,n):
        if n <= 1:
            return False
        for i in range(2, int(n**0.5) + 1):
            if n % i == 0:
                return False
        return True
    
    def mostrarEncadenamiento(self):
        for i, lista in enumerate(self.__tabla):
            print(f"[{i}] {lista}")
    
    def insertar(self,valor:int):
        indice = self.hash(valor)
        self.__tabla[indice].insertar(valor)
        
    """Implementación"""
    
    # b. Implemente la función hash a usar.
    def hash(self,valor):
        return valor % self.__tamaño
    
    
    # c. Operación Buscar_clave y mostrar la cantidad de intentos en que encontró la clave.
    def buscar(self, valor:int):
        i = self.hash(valor)
        aux = self.__tabla[i].getCab() 
        intentos = 1
        encontrado = False
        
        while aux != None and aux.getElem() != valor:
            aux = aux.getSig()
            intentos += 1
            
        if aux != None:
            encontrado = True 
            print(f"el valor {valor} está en el índice {i}")
            print(f"Se encontró en {intentos} intento(s)")
        else:
            print(f"el valor {valor} no se encontró después de {intentos} intento(s)")

        return encontrado
    

"""
Ejercicio 3: : Considere el TAD digrafo, formado por N vértices. 
a) Defina  el objeto de datos. 
b) Implemente la operación que genere la Matriz de Adyacencia. 
"""    

    
# a) Defina el objeto de datos.
class Digrafo2:
    __vertices: int
    __matriz: np.ndarray
    
    def __init__(self,N):
        self.__matriz = np.zeros((N,N),dtype=int)
        self.__vertices = N   
        
    # b) Matriz de Adyacencia
    def agregarAristas2(self,u,v):
        if self.__matriz[u][v] == 0:
            self.__matriz[u][v] = 1
    
    def matrizAdyacencia(self):
        print(self.__matriz)