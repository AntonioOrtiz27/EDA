from grafo_sec import Grafo

def tipodeGrafo():
    op = int(input("""
    --- Seleccione que tipo de Grafo  quiere diseñar ---
    [0] SALIR
    [1] Grafo
    [2] Digrafo
    ---- >"""))
    return op

def menu(nodos):
    op = int(input(f"""
    --- Operaciones Abstractas disponibles del Grafo/Digrafo de {nodos} nodos que acaba de crear  ---
    [0] SALIR
    [1] Agregar aristas entre nodos desde 0 hasta {nodos-1}
    [2] Mostrar matriz de adyacencia
    [3] Mostrar Nodos Adyacentes de un nodo origen
    ---- >"""))
    return op

if __name__ =="__main__":

    grafo = tipodeGrafo()
    while grafo != 0:
        if grafo == 1:
            nodos = int(input("Ingrese la cantidad vertices (nodos) del grafo:"))
            grafito = Grafo(nodos)
            main = menu(nodos)
            while main != 0:
                if main == 1:
                    cant = int(input("¿Cuántas aristas desea agregar?: "))
                    for _ in range(cant):
                        u = int(input(f"Ingrese el origen (0 a {nodos-1}): "))
                        v = int(input(f"Ingrese el destino (0 a {nodos-1}): "))
                        grafito.agregarAristasGrafo(u, v)
                elif main == 2:
                    grafito.mostrarMatriz()
                elif main == 3:
                    origen = int(input("ingrese el nodo para buscar sus adyacentes:"))
                    grafito.adyacentes(origen)
                else:
                    print("Saliendo...")
                main = menu(nodos)
        elif grafo == 2:
            nodos = int(input("Ingrese la cantidad vertices (nodos) del digrafo"))
        else:
            print("Saliendo...")
    grafo = tipodeGrafo()


    