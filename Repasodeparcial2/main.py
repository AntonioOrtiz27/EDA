from modeloParcial2 import *
from modeloParcial1 import *


def modeloParcial():
    opcion = int(input("""
                   [0] Para salir
                   [1] Modelo de parcial 1
                   [2] Modelo de parcial 2
                   [3] Modelo de parcial 3
                   --->"""))
    return opcion

def menu1():
    op = int(input("""
                   [0] Para salir
                   
                   [1] Mostrar [ABB] en terminal
                   [2] Inciso 1-b) Nodos con un solo Descendiente Directo
                   
                   [3] Mostrar [DIGRAFO] y Matriz de Adyacencia
                   [4] Inciso 3-b) Nodos Sumideros
                   
                   --->"""))
    return op

def menu2():
    op = int(input("""
                   [0] Para salir
                   
                   [1] Mostrar [ABB] en terminal
                   [2] Inciso 1-b) Mostrar nodos de un nivel
                   
                   [3] Mostrar [TABLA HASH] en terminal
                   [4] Inciso 2-c) Buscar_clave
                   
                   [5] Mostrar [DIGRAFO]
                   [6] Inciso 1-b) Matriz de Adyacencia
                   
                   --->"""))
    return op

if __name__ == "__main__":
    
    """--- Modelo de parcial 1 ---"""
    
    arbol1 = Arbol1()
    noditos = ['D','C','E','F','B','A','G']
    for nodo in noditos:
        arbol1.insertar(nodo,arbol1.getRaiz())
    
    n = 5
    digrafo = Digrafo(n)
    aristas = [(0,1),(0,2),(0,4),(1,2),(1,4),(3,4)]
    for u,v in aristas:
        digrafo.agregarAristas(u,v)
    
    """--- Modelo de parcial 2 ---"""
    
    arbol2 = Arbol2()
    noditos = ['D','C','E','F','B','A','G']
    for nodo in noditos:
        arbol2.insertar(nodo,arbol2.getRaiz())
        
    tabla = Hash(5)
    valores = [0,1,2,3,4,5,6,7,8,9,10,11,12]
    for valor in valores:
        tabla.insertar(valor)
    
    n = 5
    digrafo2 = Digrafo2(n)
    aristas2 = [(1,0),  (1,2) , (2,0) , (4,0) , (4,1) , (4,3)]
    for u,v in aristas2:
        digrafo2.agregarAristas2(u,v)
    
    
    opcion = modeloParcial()
    while opcion != 0:
        
        if opcion == 1:
            print("""
            --- Modelo de Parcial 1 ---
                
            Ejercicio 1: Considere trabajar con el TAD árbol binario de búsqueda. 
            a) Defina el objeto de datos. 
            b) Especifique e implemente la operación  que cuente 
            la cantidad de nodos que tienen un solo descendiente directo. 
            
            Ejercicio 3: : Considere el TAD digrafo, formado por N vértices. 
            a) Defina  el objeto de datos. 
            b) Especifique e implemente la operación que muestre todos los 
            nodos sumidero, para ello implemente las operaciones 
            grado de entrada  y grado de salida.
            """)
            
            opmenu1 = menu1()
            while opmenu1 != 0:
                
                if opmenu1 == 1:
                    raiz_anytree = arbol1.convertir_a_anytree(arbol1.getRaiz())
                    for pre, fill, node in RenderTree(raiz_anytree):
                        print(f"{pre}{node.name}")
                        
                elif opmenu1 == 2:
                    print("\nCantidad total de nodos con un solo descendiente directo:", arbol1.preorden(arbol1.getRaiz()))
                
                elif opmenu1 == 3:
                    digrafo.matrizAdyacencia()  
                    D = nx.DiGraph()
                    D.add_edges_from(aristas)
                    nx.draw(D, with_labels=True, node_color='lightgreen', font_weight='bold', node_size=1500, arrows=True)
                    plt.show()
                    
                elif opmenu1 == 4:
                    print("Mostrar todos los nodos sumidero")
                    digrafo.nodoSumideros()
                    
                opmenu1 = menu1()
                
        elif opcion == 2:
            print("""
                --- Modelo de Parcial 2 ---
                
                Ejercicio 1:  Considere trabajar con el TAD árbol binario de búsqueda. 
                a) Defina el objeto de datos. 
                b) Especifique e implemente la operación  que que imprima 
                todos los nodos se  encuentran en un nivel n ingresado por teclado. 
                (Considere el Nivel de la raiz 1) 
                
                Ejercicio 2: Considere trabajar con el TAD hashing, 
                con la política de manejo de colisiones: Encadenamiento. 
                a. Defina el objeto de datos, considerando aproximadamente 1000 claves. 
                b. Implemente la función hash a usar. 
                c. Especifique e implemente la operación Buscar_clave y 
                muestre la cantidad de intentos en que la encontró. 
                
                Ejercicio 3: : Considere el TAD digrafo, formado por N vértices. 
                a) Defina  el objeto de datos. 
                b) Iimplemente la operación que genere la Matriz de Adyacencia.
                """)
            
            opmenu2 = menu2()
            while opmenu2 !=0:
                
                if opmenu2 == 1:
                    raiz_anytree = arbol2.convertir_a_anytree(arbol2.getRaiz())
                    for pre, fill, node in RenderTree(raiz_anytree):
                        print(f"{pre}{node.name}")
                        
                elif opmenu2 == 2:
                    n = int(input("Ingrese un nivel:"))
                    print(f"Nodos en el nivel {n}: ", end="")
                    arbol2.nivel(arbol2.getRaiz(),n)
                    
                elif opmenu2 == 3:
                    tabla.mostrarEncadenamiento()

                elif opmenu2 == 4:
                    clave = int(input("Ingrese la clave a buscar: "))
                    tabla.buscar(clave)
                    
                elif opmenu2 == 5:
                    D = nx.DiGraph()
                    D.add_edges_from(aristas2)
                    nx.draw(D, with_labels=True, node_color='lightgreen', font_weight='bold', node_size=1500, arrows=True)
                    plt.show()
                    
                elif opmenu2 == 6:
                    digrafo.matrizAdyacencia()  
                
                opmenu2 = menu2()