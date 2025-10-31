"""@author: Antonio Ortiz"""
import numpy as np
from COLA_ENC import Cola
from Pila_Enc import Pila
import networkx as nx
import matplotlib.pyplot as plt

# Tad de Grafo Secuencial
class Grafo:
    __tamaño: int
    __matriz: np.ndarray
    
    def __init__(self, N):
        self.__tamaño = N
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
        
    def adyacentes(self,origen):
        adyacentes = []
        for i in range(self.__tamaño):
            if self.__matriz[origen][i] == 1:
                adyacentes.append(i)
        return adyacentes
    
    def adyacente(self,xnodo,xady):
        return self.__matriz[xnodo][xady] == 1

    """
    --- 
    -Busqueda en Amplitud (BFS) Iterativa y Recursiva.
    -REA Recorrido en Amplitud (BFS) - Este recorrido permite 
    calcular la distancia mínima en cantidad de aristas o niveles 
    desde el vértice de ingresado hacia todos los demás vértices del grafo.
    ---
    """


    def bfs_Iterativo(self, u):
        visitado = [False] * self.__tamaño
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
    
    def bfs_Recursivo(self, u):
        visitado = [False] * self.__tamaño
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
    
    def REA(self, origen):
        distancia = [float('inf')] * self.__tamaño
        cola = Cola()

        # Inicializamos el nodo origen
        distancia[origen] = 0
        cola.insertar(origen)


        # Mientras haya nodos por visitar
        while not cola.vacia():
            v = cola.suprimir()

            # Recorremos SOLO los adyacentes del nodo v
            for u in self.adyacentes(v):
                if distancia[u] == float('inf'):
                    distancia[u] = distancia[v] + 1
                    cola.insertar(u)

        # Mostrar las distancias finales desde nodo ingresado
        print(f"\nDistancias finales desde {origen}:")
        for i in range(self.__tamaño):
            print(f"Vértice {i}: {distancia[i]}")

       
    """
    --- 
    Busqueda en profundidad (DFS) Iterativa y Recursiva y
    REP Recorrido en Profundidad (DFS) con tiempos de descubrimiento (d) y finalización(f) 
    ---
    """
       
    def dfs_Iterativo(self, u):
        visitado = [False] * self.__tamaño
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
    
    def dfs_Recursivo(self, u):
        visitado = [False] * self.__tamaño
        recorrido = []
        pila = Pila()  
        
        def recorrer(v):
            visitado[v] = True
            recorrido.append(v)
            pila.insertar(v)   
            for w in self.adyacentes(v):
                if not visitado[w]:
                    recorrer(w)
            x = pila.suprimir() 

        recorrer(u)
        return recorrido

    # Recorrido en profundidad con tiempos de la teoria
    def REP(self): 
        d = [0] * self.__tamaño
        f = [0] * self.__tamaño
        tiempo = [0]  # Tiempo lo guardamos en una lista para que sea mutable en la recursión
        for s in range(self.__tamaño):
            # Si el vértice no ha sido descubierto aún
            if d[s] == 0:
                # Llamamos a REP-Visita para explorar el vértice y sus adyacentes
                self.REP_Visita( s, d, f, tiempo)
        print(f"Tiempos de descubrimiento:{d}")
        print(f"Tiempos de finalización:{f}")

    # Función recursiva para visitar los nodos en profundidad
    def REP_Visita(self, s, d, f, tiempo):
        tiempo[0] += 1
        d[s] = tiempo[0]  # Asignamos el tiempo de descubrimiento
        # Para cada vértice adyacente a s
        adyacentes_s = self.adyacentes(s)
        for u in adyacentes_s:
            if d[u] == 0:  # Si u no ha sido visitado aún
                self.REP_Visita(u, d, f, tiempo)
        tiempo[0] += 1
        f[s] = tiempo[0]  # Asignamos el tiempo de finalización
    
    """
    --- 
    Camino de un nodo u a un nodo v en un Grafo Dirigido con BFS (REA)
    ---
    """
    
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
    

if __name__ == "__main__":
    grafo = Grafo(4)
    # Nodos: 0 1 2 3
    
    # lista de arcos
    lista = [(0,2) , (0,3) , (1,2) , (1,3) , (2,3) , (0,2)]
    
    """----- Grafo en representacion Secuencial -----"""
    
    # Agregar aristas a Grafo
    for origen,destino in lista:
        grafo.agregarAristasGrafo(origen,destino)
    
    
    # Mostrar Matriz de Adyacencia de Grafo
    grafo.mostrarMatriz()
    print()
    
    
    """----- Operaciones Abstractas -----"""
    
    # Operación: Nodos Adyacentes 
    # Funcion: Determina los nodos adyacentes de u
    # Salida: Reporta los nodos adyacentes de u
    
    print("los nodos adyacentes de 0 son:",grafo.adyacentes(0))
    print("los nodos adyacentes de 1 son:",grafo.adyacentes(1))
    print("los nodos adyacentes de 2 son:",grafo.adyacentes(2))
    print("los nodos adyacentes de 3 son:",grafo.adyacentes(3))
    print()
    
    
    # Operación: BFS(Busqueda en Amplitud)
    # Funcion: Procesa todos los elementos de G en Amplitud
    # Salida: Está sujeta al proceso que se realice sobre los elementos de G
    
    """ BFS ITERATIVA """
    print("Busqueda BFS desde el nodo 0:",grafo.bfs_Iterativo(0))
    print()  
    
    """ BFS Recursivo """
    print("Recorrido BFS desde el nodo 0:",grafo.bfs_Recursivo(0))
    print()  
    
    """
    REA
    El método REA busca hacer un BFS desde el origen
    dónde se manejan distancias minimas desde un nodo 
    origen hacia otros nodos.
    """
    u = int(input("Ingrese el nodo origen para calcular la distancia mínima hacia los demás nodos (0 - 1 - 2 - 3): "))
    grafo.REA(u)
    print()

    
    # Operación: DFS (Busqueda en Profundidad)
    # Funcion: Procesa todos los elementos de G en profundidad
    # Salida: Está sujeta al proceso que se realice sobre los elementos de G
    
    """ DFS ITERATIVO - Utiliza reversed """
    print("Recorrido DFS desde el nodo 0:",grafo.dfs_Iterativo(0))  
    print()
    
    """ DFS- Recursivo - No utiliza reversed """
    print("Recorrido DFS desde el nodo 0:",grafo.dfs_Recursivo(0))  
    print()
    
    """
    REP
    El método REP busca hacer un DFS con registro de tiempos de 
    descubrimiento (d) y finalización (f), lo que le corresponde
    al algoritmo clásico de “Recorrido en Profundidad (DFS) con tiempos”.
    """
    grafo.REP()
    print()
    
    # Operación: Camino
    # Funcion: Determina el camino de u a v
    # Salida: Reporta el camino de u a v, si v es alcanzable desde u; Error en caso contrario
    
    print("Caminos de u a v en el Grafo Dirigido")
    u = int(input("Ingrese origen del camino (0 - 1 - 2 - 3):"))
    v = int(input("Ingrese destino del camino (0 - 1 - 2 - 3):"))
    grafo.camino(u,v)
    print()
    



    
    """----- Graficar el Grafo Dirigido ------"""
    # Crear un grafo dirigido
    G = nx.Graph()
    # Añadir las conexiones
    G.add_edges_from(lista)
    # Dibujar el grafo
    nx.draw(G, with_labels=True, node_color='lightgreen', font_weight='bold', node_size=1500)
    # Mostrar el grafo
    plt.show()
