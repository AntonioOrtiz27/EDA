"""@author: Antonio Ortiz"""
import numpy as np

# TAD de Digrafo Secuencial
class Digrafo:
    __numVertices: int
    __matriz: np.ndarray
    
    def __init__(self, N):
        self.__numVertices = N
        self.__matriz = np.zeros((N, N),dtype=int)
        
    # Agregar aristas entre nodos de ida unicamente
    def agregarAristasGrafo(self, origen, destino):
        if self.__matriz[origen][destino] == 0:
            self.__matriz[origen][destino] = 1
        else:
            print(f"La arista ({origen},{destino}) ya existe")
    # Mostrar matriz de adyacencia 
    def mostrarMatriz(self):
        print(self.__matriz)
    
    # Operación: Nodos Adyacentes 
    # Funcion: Determina los nodos adyacentes de u
    # Salida: Reporta los nodos adyacentes de u   
    
    def adyacentes(self,origen):
        lista = []
        for v in range(self.__numVertices):
            if self.__matriz[origen][v] == 1:
                lista.append(v)
        return lista

    # Operación: Grado de Entrada 
    # Funcion: Determina cantidad de aristas que llegan a u
    # Salida: Reporta el grado de salida de u  

    def grado_entrada(self,u):
        cont = 0
        for i in range(self.__numVertices):
            if self.__matriz[i][u] == 1:
                cont+=1
        return cont
    
    # Operación: Grado de Salida 
    # Funcion: Determina cantidad de aristas que salen a u
    # Salida: Reporta el grado de salida de u
    
    def grado_salida(self,u):
        return len(self.adyacentes(u))
    
    # Operación: Nodo Fuente
    # Funcion: Evalúa si u es nodo fuente de G 
    # Salida: V si u es nodo fuente de G    

    def nodoFuente(self, u):
        i = 0
        while i < self.__numVertices:
            if self.__matriz[i, u] == 1:
                print(f"El nodo {u} no es fuente")
                return
            i += 1
        print(f"El nodo {u} es fuente")
    
    # Operación: Nodo Sumidero
    # Funcion: Evalúa si u es nodo sumidero de G
    # Salida: V si u es nodo sumidero de G
    
    def nodoSumidero(self, u):
        i = 0
        while i < self.__numVertices:
            if self.__matriz[u, i] == 1:
                print(f"El nodo {u} no es sumidero")
                return
            i += 1
        print(f"El nodo {u} es sumidero")
        
        