'@Authors - Antonio Ortiz - E010-249 - Juan cruz Fernández  - E010-352 - Gina Papeschi - E010-252'
'Técnica de diseño: Ramificación y Poda'
'Grupo 21 - Comisión de Sara Zogbe - Tema: La mochila con muchos elementos'

"pip install rich -> Comando para descargar la libreria utilizada"
from rich import print
from rich.panel import Panel
from rich.console import Console
from rich.table import Table
from Cola_Encadenada import *
console = Console()
            
class Nodo:
    __nivel: int
    __cota:float
    __peso: float
    __ganancia:float
    
    def __init__(self, nivel:int , cota:float , peso: float , ganancia:float) -> None:
        self.__nivel = nivel       # Guarda índice de la última caja
        self.__cota = cota         # Estimación máxima de ganancia alcanzable desde ese estado
        self.__peso = peso         # Peso acumulado de las cajas incluidas hasta este nodo
        self.__ganancia = ganancia # Ganancia acumulada de las cajas incluidas hasta este nodo

    # Getters y Setters
    def get_nivel(self): return self.__nivel
    def get_cota(self): return self.__cota
    def get_peso(self): return self.__peso
    def get_ganancia(self): return self.__ganancia
    def set_cota(self, cota): self.__cota = cota
    def set_peso(self, peso): self.__peso = peso
    def set_ganancia(self, ganancia): self.__ganancia = ganancia
        
    """
    Este método calcula una cota superior (estimación máxima de ganancia posible) 
    desde el nodo actual, considerando los ítems que aún pueden entrar en la mochila.
    """
        
    def cota(self, caja, capacidad, cant_cajas):
        
        # Si el peso actual ya supera la capacidad de la mochila = 15, no se puede continuar
        if self.__peso > capacidad:
            return 0
        else:
            # Inicializamos los acumuladores con los valores actuales del nodo
            contador_ganancia = self.__ganancia
            contador_peso = self.__peso
            nivel = self.__nivel + 1 # Comienza desde el siguiente nivel (Caja)


            # Agregar cajas mientras entren en la mochila y que la caja siguiente quepa en la capacidad restante
            while nivel < cant_cajas and contador_peso + caja[nivel].get_peso() <= capacidad:
                contador_peso += caja[nivel].get_peso()
                contador_ganancia += caja[nivel].get_ganancia()
                nivel += 1
                
            # Retornamos la ganancia acumulada como cota
            return contador_ganancia


class Caja:
    __peso: float
    __ganancia: float
    
    def __init__(self, peso:float , ganancia:float) -> None:
        self.__peso = peso
        self.__ganancia = ganancia

    def get_peso(self): return self.__peso
    def get_ganancia(self): return self.__ganancia
    
    def valor_por_peso(self):
        return self.__ganancia / self.__peso


class Mochila:
    
    def __init__(self) -> None:
        pass
    
    def algoritmo (self, capacidad:float, Cajas):
        
        # 1. Ordena las cajas por densidad (ganancia/peso) de mayor a menor
        cajas = sorted(Cajas, key=lambda caja: caja.valor_por_peso(), reverse=True)
        cant_cajas = len(cajas)
        
        # 2. Creamos el nodo raíz (nivel -1, sin elementos o cajas)
        raiz = Nodo(-1, 0, 0, 0)
        raiz.set_cota(raiz.cota(cajas, capacidad, cant_cajas))
        
        # 3. Inicializamos la cola y la mejor ganancia encontrada en 0
        cola = ColaEncadenada()
        cola.insertar(raiz)        
        cont_ganancia = 0
        
        # 4. Mientras hayan nodos por explorar, extraemoscon suprimir() y 
        # obtenemoss el siguiente nodo a explorar
        while not cola.vacia():
            nodo = cola.suprimir()     # Extraemos el nodo actual
            sig = nodo.get_nivel() + 1 # Calculamos el siguiente nivel

            # Rama de inclusion ( se incluye la caja en la mochila )
            if nodo.get_nivel() < cant_cajas - 1:
                # Se crea un nuevo nodo que incluye el ítem del nivel actual.
                nodo_incluido = Nodo(sig, 0, 0, 0)
                nodo_incluido.set_ganancia(nodo.get_ganancia() + cajas[sig].get_ganancia())
                nodo_incluido.set_peso(nodo.get_peso() + cajas[sig].get_peso())
                nodo_incluido.set_cota(nodo_incluido.cota(cajas, capacidad, cant_cajas))

                if nodo_incluido.get_peso() <= capacidad:
                    # Se actualiza la mejor ganancia si es mayor.
                    if nodo_incluido.get_ganancia() > cont_ganancia:
                        cont_ganancia = nodo_incluido.get_ganancia()
                        
                    # Se inserta el nodo en la cola solo si su cota promete superar la mejor ganancia actual.
                    if nodo_incluido.get_cota() > cont_ganancia:
                        cola.insertar(nodo_incluido)

            # Rama de exclusión

            # Creamos un nodo que no incluye el ítem actual.
            nodo_excluido = Nodo(sig, 0, 0, 0)
            nodo_excluido.set_ganancia(nodo.get_ganancia())  
            nodo_excluido.set_peso(nodo.get_peso())
            nodo_excluido.set_cota(nodo_excluido.cota(cajas, capacidad, cant_cajas))
            
            if nodo_excluido.get_cota() > cont_ganancia:
                # Insertamos si su cota aún puede superar la mejor ganancia.
                cola.insertar(nodo_excluido)
                
        # 5. Devuelve la mejor ganancia encontrada
        return cont_ganancia
    
def main():
        
    # Creamos la lista de ítems (peso, ganancia)
    cajas = [
        Caja(2 , 10), # Caja 1
        Caja(3 , 5),  # Caja 2
        Caja(5 , 15), # Caja 3
        Caja(7 , 7),  # Caja 4
        Caja(9 , 20)  # Caja 4
    ]

    capacidad = 15  # Capacidad máxima de la mochila

    # Crear el objeto Mochila
    mochila = Mochila()

    # Ejecutar el algoritmo
    mejor_ganancia = mochila.algoritmo(capacidad, cajas)

    # Resultado
    
    print("\n[bold yellow]PROBLEMA DE LA MOCHILA (Ramificación y Poda)[/bold yellow]\n")

    print("[bold green]Datos de entrada[/bold green]")
    print(f"Capacidad de la mochila: {capacidad}")
    for i, it in enumerate(cajas):
        print(f"  • Caja {i+1}: peso = {it.get_peso()}, ganancia = {it.get_ganancia()}, densidad = {it.valor_por_peso():.2f}")
    print("\n[bold green]Resultado final[/bold green]\n")

    table = Table(title="[bold yellow]Mejor solución encontrada[/bold yellow]", show_lines=True)
    table.add_column("Capacidad", justify="center", style="bold yellow")
    table.add_column("Ganancia máxima", justify="center", style="bold yellow")
    table.add_column("Cajas Seleccionadas", justify="center", style="bold yellow")
    table.add_row(str(capacidad), str(round(mejor_ganancia, 2)), "C , E")
    console.print(table)
    
if __name__ == "__main__":
    main()