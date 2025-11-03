"""@author: Antonio Ortiz"""
import numpy as np
from grafo_sec import Grafo
from COLA_ENC import Cola
from Pila_Enc import Pila
import networkx as nx
import matplotlib.pyplot as plt

if __name__ == "__main__":
    grafo = Grafo(4)
    # Nodos: 0 1 2 3
    
    # lista de arcos de grafo conexo
    # lista = [(0,2) , (0,3) , (1,2) , (1,3) , (2,3)]
    
    # lista de arcos de grafo Simple conexo
    # lista = [(1,2) , (1,3) , (2,3)]
    
    # lista de arcos de grafo Aciclico
    lista = [(0, 1), (0, 2), (2, 3)]
    
    """----- Grafo en representacion Secuencial -----"""
    
    # Agregar aristas a Grafo
    for origen,destino in lista:
        grafo.agregarAristasGrafo(origen,destino)

    
    # Mostrar Matriz de Adyacencia de Grafo
    grafo.mostrarMatriz()
    print()
    
    
    """----- Operaciones Abstractas -----"""
    
    """ ADYACENTES """
    print("los nodos adyacentes de 0 son:",grafo.adyacentes(0))
    print("los nodos adyacentes de 1 son:",grafo.adyacentes(1))
    print("los nodos adyacentes de 2 son:",grafo.adyacentes(2))
    print("los nodos adyacentes de 3 son:",grafo.adyacentes(3))
    print()
    
    """ BFS ITERATIVO """
    print("Busqueda BFS desde el nodo 0:",grafo.bfs_Iterativo(0))
    print()  

    """ DFS ITERATIVO - Utiliza reversed """
    print("Recorrido DFS desde el nodo 0:",grafo.dfs_Iterativo(0))  
    print()

    """ CAMINO """
    print("Caminos de u a v en el Grafo Dirigido")
    u = int(input("Ingrese origen del camino (0 - 1 - 2 - 3):"))
    v = int(input("Ingrese destino del camino (0 - 1 - 2 - 3):"))
    grafo.camino(u,v)
    print()
    
    """ CONEXO """
    if grafo.es_conexo():
        print("Grafo conexo\n")
    else:
        print("No es conexo\n")
    print()
    
    """ ACICLICO """

    if grafo.aciclico():
        print("El grafo es aciclico\n")
    else:
        print("El grafo no es aciclico\n")

    
    """----- Graficar el Grafo Conexo ------"""
    # Crear un grafo dirigido
    G = nx.Graph()
    # Añadir las conexiones
    G.add_edges_from(lista)
    # Dibujar el grafo
    nx.draw(G, with_labels=True, node_color='lightgreen', font_weight='bold', node_size=1500)
    # Mostrar el grafo
    plt.show()