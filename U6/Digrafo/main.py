"""@author: Antonio Ortiz"""
import numpy as np
from digrafo_secuencial import *
import networkx as nx
import matplotlib.pyplot as plt

def menu():
    op = int(input("""
                   [0] Para salir
                   [1] Grado de Entrada 
                   [2] Grado de Salida 
                   [3] Nodo Fuente 
                   [4] Nodo Sumidero 
                   --->"""))
    return op

if __name__ == "__main__":
    digrafo = Digrafo(4)
    # Nodos: 0 1 2 3
    
    lista = [(0,2) , (0,3) , (1,2) , (1,3) , (2,3)]
    
    """----- Digrafo en representacion Secuencial -----"""
    
    # Agregar aristas a Grafo
    for origen,destino in lista:
        digrafo.agregarAristasGrafo(origen,destino)

    
    # Mostrar Matriz de Adyacencia de Grafo
    print("Matriz de adyacencia\n")
    digrafo.mostrarMatriz()
    print()
    
    
    """----- Operaciones Abstractas -----"""
    
    op = menu()
    while op != 0:
        
        if op == 1:
            nodo = int(input("\nIngrese nodo U (0 - 1 - 2 - 3): "))
            print(f"\nGrado de Entrada de {nodo}")
            print(f"Cantidad de aristas que llegan a {nodo}: ",digrafo.grado_entrada(nodo))
            print()
        elif op == 2:
            nodo = int(input("\nIngrese nodo U (0 - 1 - 2 - 3): "))
            print(f"\nGrado de Salida de {nodo}")
            print(f"Cantidad de aristas que salen de {nodo}: ",digrafo.grado_salida(nodo))
            print()

        elif op == 3:
            print("Nodo Fuente")
            nodo = int(input("\nIngrese nodo U (0 - 1 - 2 - 3): "))
            digrafo.nodoFuente(nodo)
            print()

        elif op == 4:
            print("Nodo Sumidero")
            nodo = int(input("\nIngrese nodo U (0 - 1 - 2 - 3): "))
            digrafo.nodoSumidero(nodo)
            
        op = menu()
    
    """----- Graficar el Grafo Conexo ------"""
    # Crear un grafo dirigido
    D = nx.DiGraph()

    # Añadir las conexiones
    D.add_edges_from(lista)

    # Dibujar el digrafo
    nx.draw(D, with_labels=True, node_color='lightgreen', font_weight='bold', node_size=1500, arrows=True)
    plt.show()