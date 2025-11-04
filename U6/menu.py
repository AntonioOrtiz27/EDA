from Grafo.grafo_secuencial import *
from Digrafo.digrafo_secuencial import *

def tipodeGrafo():
    op = int(input("""
    --- Seleccione que tipo de Grafo  quiere diseñar ---
    [0] SALIR
    [1] Grafo
    [2] Digrafo
    ---- >"""))
    return op

def menuGrafo(nodos):
    op = int(input(f"""
    --- Operaciones Abstractas disponibles del Grafo/Digrafo de {nodos} nodos que acaba de crear  ---
    [0] SALIR
    [1] Agregar aristas entre nodos desde 0 hasta {nodos-1}
    [2] Mostrar matriz de adyacencia
    [3] Mostrar Nodos Adyacentes de un nodo
    [4] BFS (Desde nodo 0)
    [5] DFS (Desde nodo 0)
    [6] Camino entre dos nodos
    [7] Verificar si el Grafo es Conexo
    [8] Verificar si el Grafo Aciclico
    ---- >"""))
    return op

def menuDigrafo():
    op = int(input("""
                   [0] Para salir
                   [1] Agregar aristas entre nodos desde 0 hasta {nodos-1}
                   [2] Mostrar matriz de adyacencia
                   [3] Mostrar Nodos Adyacentes de un nodo
                   [4] Grado de Entrada 
                   [5] Grado de Salida 
                   [6] Nodo Fuente 
                   [7] Nodo Sumidero 
                   --->"""))
    return op

if __name__ =="__main__":

    grafo = tipodeGrafo()
    while grafo != 0:
        
        if grafo == 1:
            nodos = int(input("Ingrese la cantidad vertices (nodos) del grafo:"))
            grafito = Grafo(nodos)
            
            op = menuGrafo(nodos)
            while op != 0:
                
                if op == 1:
                    cant = int(input("¿Cuántas aristas desea agregar?: "))
                    for _ in range(cant):
                        u = int(input(f"Ingrese el origen (0 a {nodos-1}): "))
                        v = int(input(f"Ingrese el destino (0 a {nodos-1}): "))
                        grafito.agregarAristasGrafo(u, v)
                        
                elif op == 2:
                    grafito.mostrarMatriz()
                    
                elif op == 3:
                    u = int(input("ingrese el nodo para buscar sus adyacentes:"))
                    print(f"los nodos adyacentes de {u} son:",grafito.adyacentes(u))
                    
                elif  op == 4:
                    print("Busqueda BFS desde el nodo 0:",grafito.bfs_Iterativo(0))
                    
                elif  op == 5:
                    print("Busqueda DFS desde el nodo 0:",grafito.dfs_Iterativo(0))   
                    
                elif  op == 6:
                    u = int(input("Ingrese origen del camino (0 - 1 - 2 - 3):"))
                    v = int(input("Ingrese destino del camino (0 - 1 - 2 - 3):"))
                    grafito.camino(u,v) 
                    
                elif op == 7:
                    if grafito.es_conexo():
                        print("Grafo conexo\n")
                    else:
                        print("No es conexo\n")
                    print()
                else:
                    print("Saliendo...")
                op = menuGrafo(nodos)
                
                
        elif grafo == 2:
            nodos = int(input("Ingrese la cantidad vertices (nodos) del digrafo"))
            digrafito = Digrafo(nodos)
            
            op = menuDigrafo(nodos)
            while op != 0:
                
                if op == 1:
                    cant = int(input("¿Cuántas aristas desea agregar?: "))
                    for _ in range(cant):
                        u = int(input(f"Ingrese el origen (0 a {nodos-1}): "))
                        v = int(input(f"Ingrese el destino (0 a {nodos-1}): "))
                        digrafito.agregarAristasGrafo(u, v)
                        
                elif op == 2:
                    digrafito.mostrarMatriz()
                    
                elif op == 3:
                    u = int(input("ingrese el nodo para buscar sus adyacentes:"))
                    print(f"los nodos adyacentes de {u} son:",digrafito.adyacentes(u))
                    
                elif op == 4:
                    nodo = int(input("\nIngrese nodo U (0 - 1 - 2 - 3): "))
                    print(f"\nGrado de Entrada de {nodo}")
                    print(f"Cantidad de aristas que llegan a {nodo}: ",digrafito.grado_entrada(nodo))
                    print()
                    
                elif op == 5:
                    nodo = int(input("\nIngrese nodo U (0 - 1 - 2 - 3): "))
                    print(f"\nGrado de Salida de {nodo}")
                    print(f"Cantidad de aristas que salen de {nodo}: ",digrafito.grado_salida(nodo))
                    print()

                elif op == 6:
                    print("Nodo Fuente")
                    nodo = int(input("\nIngrese nodo U (0 - 1 - 2 - 3): "))
                    digrafito.nodoFuente(nodo)
                    print()

                elif op == 7:
                    print("Nodo Sumidero")
                    nodo = int(input("\nIngrese nodo U (0 - 1 - 2 - 3): "))
                    digrafito.nodoSumidero(nodo)
                op = menuDigrafo(nodos)
                    
        else:
            print("Saliendo...")
    grafo = tipodeGrafo()

"""
Lote de Prueba Grafo
1
4
1
5
0
2
0
3
1
2
1
3
2
3
"""
    