"""@author: Antonio Ortiz"""
import numpy as np
from COLA_ENC import Cola
from Pila_Enc import Pila

# Tad de Grafo Secuencial
class Grafo:
    __numVertices: int
    __matriz: np.ndarray
    
    def __init__(self, N):
        self.__numVertices = N
        self.__matriz = np.zeros((N, N),dtype=int)
        
    # Agregar aristas entre nodos 
    def agregarAristasGrafo(self, origen, destino):
        if self.__matriz[origen][destino] == 0:
            self.__matriz[origen][destino] = 1
            self.__matriz[destino][origen] = 1
        else:
            print(f"La arista ({origen},{destino}) ya existe")
            
    def mostrarMatriz(self):
        print(self.__matriz)
        
    # Operación: Nodos Adyacentes 
    # Funcion: Determina los nodos adyacentes de u
    # Salida: Reporta los nodos adyacentes de u    
        
    def adyacentes(self,origen):
        adyacentes = []
        for i in range(self.__numVertices):
            if self.__matriz[origen][i] == 1:
                adyacentes.append(i)
        return adyacentes
    
    def adyacente(self,xnodo,xady):
        return self.__matriz[xnodo-1][xady-1] == 1

    # Operación: BFS(Busqueda en Amplitud)
    # Funcion: Procesa todos los elementos de G en Amplitud
    # Salida: Está sujeta al proceso que se realice sobre los elementos de G

    def bfs_Iterativo(self, u):
        visitado = [False] * self.__numVertices
        recorrido = []
        cola = Cola()
        
        visitado[u] = True
        cola.insertar(u)
        
        while not cola.vacia():
            v = cola.suprimir()
            recorrido.append(v)
            
            for w in self.adyacentes(v):
                if not visitado[w]:
                    visitado[w] = True
                    cola.insertar(w)
        
        return recorrido

    # Operación: DFS (Busqueda en Profundidad)
    # Funcion: Procesa todos los elementos de G en profundidad
    # Salida: Está sujeta al proceso que se realice sobre los elementos de G
       
    def dfs_Iterativo(self, u):
        visitado = [False] * self.__numVertices
        recorrido = []
        pila = Pila()

        pila.insertar(u)

        while not pila.vacia():
            v = pila.suprimir()
            if not visitado[v]:
                visitado[v] = True
                recorrido.append(v)
                for w in reversed(self.adyacentes(v)):
                    if not visitado[w]:
                        pila.insertar(w)
        return recorrido
    
    # Operación: Camino
    # Funcion: Determina el camino de u a v
    # Salida: Reporta el camino de u a v, si v es alcanzable desde u; Error en caso contrario
    
    def camino(self,u,v):
        visitados = []
        camino = []
        band = True
        if self.busqueda_en_amplitud(u,v,camino,visitados):
            print(f"Camino de {u} a {v}:", end=" ")
            camino.append(v)
            for i in camino:
                print(f"[{i}]",end=" ")
                band=True
        else:
            print(f"No existe camino de {u} a {v}")
            band = False
            
        return band
        
    def busqueda_en_amplitud(self,u,v,visitados,camino):
        cola = Cola()
        cola.insertar(u)
        
        while not cola.vacia():
            u = cola.suprimir()
            camino.append(u)
            visitados.append(u)
            adyacentes_u = self.adyacentes(u)
            for adyacente in adyacentes_u:
                    if adyacente == v:
                        return True
                    elif adyacente not in visitados:        
                        cola.insertar(adyacente)
        return False
    
    # Operación: Conexo
    # Funcion: Evalúa si G es conexo (Simple o  Fuerte)
    # Salida: d

    def es_conexo(self):
        i= 1
        visitados = np.full(self.__numVertices, False, dtype=bool)
        cola = Cola()
        visitados[i-1] = True
        cola.insertar(i)

        while cola.vacia() is False:
            v = cola.suprimir()
            for u in range(self.__numVertices):
                if self.adyacente(v, u+1) and visitados[u]==False:
                    visitados[u] = True
                    cola.insertar(u+1)
        return all(visitados) #El all evalua si todos los elementos del arreglo son True. En caso de serlo devuelve un True, sino False.     
    
    # Operación: aciclico
    # Funcion: Evalúa si G es acíclico
    # Salida: V si G es acíclico, F en caso contrario
    def aciclico(self):
        aciclico = True
        i = 0
        while i < self.__numVertices and aciclico:
            if self.camino(i,i):
                aciclico = False
            else:
                i+=1
        return aciclico
