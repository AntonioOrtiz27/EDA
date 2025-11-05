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

    # grado de entrada = 0 y grado de salida > 0
    def nodoFuente(self, u):
        if self.grado_entrada(u) == 0 and self.grado_salida(u) > 0:
            print(f"El nodo {u} es fuente")
        else:
            print(f"El nodo {u} no es fuente")
    
    # Operación: Nodo Sumidero
    # Funcion: Evalúa si u es nodo sumidero de G
    # Salida: V si u es nodo sumidero de G
    
    # grado de salida = 0 y grado de entrada > 0
    def nodoSumidero(self, u):
        if self.grado_salida(u) == 0 and self.grado_entrada(u) > 0:
            print(f"El nodo {u} es sumidero")
        else:
            print(f"El nodo {u} no es sumidero")
        
    """
    Preguntas Posibles de digrafo secuencial
    - Implemente la operación que muestre todos los nodos sumideros, 
    para ello implemente las operaciones grado de entrada y grado de salida(la que sea necesaria) 
    
    - Implemente la operación que muestre todos los nodos fuente,
    para ello implemente las operaciones grado de entrada y grado de salida (la que sea necesaria)
    
    - Implemente la operación que genere la Matriz de Adyacencia.(Inicializar la matriz en 0 en el constructor)
    
    - Mostrar los adyacentes de un Nodo.
    
    - Agregar Aristas (No lo evaluaron pero podria ir tranquilamente)
    """
        
        