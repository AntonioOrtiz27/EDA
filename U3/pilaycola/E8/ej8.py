import random
class Nodo:
    def __init__(self, tiempo, sig=None):
        self.tiempo = tiempo  # Almacena el valor del nodo
        self.sig = sig  # Almacena la referencia al siguiente nodo (inicialmente None)

    def obtener_tiempo(self):
        return self.tiempo  # Devuelve el valor almacenado en el nodo

    def cargar_tiempo(self, xtiempo):
        self.tiempo = xtiempo  # Asigna un valor al nodo

    def cargar_sig(self, xtope):
        self.sig = xtope  # Asigna el siguiente nodo en la lista enlazada

    def obtener_sig(self):
        return self.sig  # Devuelve el siguiente nodo en la lista enlazada

class Cola:
    def __init__(self, pr=None, ul=None, cant=0):
        self.pr = pr  # Puntero al primer nodo de la cola
        self.ul = ul  # Puntero al último nodo de la cola
        self.cant = cant  # Número de elementos en la cola

    def vacia(self):
        return self.cant == 0  # Devuelve True si la cola está vacía

    def insertar(self, x):
        ps1 = Nodo(x)  # Crea un nuevo nodo
        ps1.cargar_tiempo(x)  # Asigna el valor al nuevo nodo
        ps1.cargar_sig(None)  # El nuevo nodo será el último, así que su siguiente es None
        
        if self.ul is None:
            self.pr = ps1  # Si la cola estaba vacía, el nuevo nodo es también el primero
        else:
            self.ul.cargar_sig(ps1)  # Conecta el último nodo actual con el nuevo nodo
        
        self.ul = ps1  # Actualiza el puntero al último nodo
        self.cant += 1  # Incrementa la cantidad de elementos en la cola
        return self.ul.obtener_tiempo()  # Devuelve el valor del nodo insertado

    def suprimir(self):
        if self.vacia():
            return 0
        else:
            aux = self.pr  # Almacena el nodo que va a ser eliminado
            x = self.pr.obtener_tiempo()  # Obtiene el valor del primer nodo
            self.pr = self.pr.obtener_sig()  # Actualiza el puntero al primer nodo
            self.cant -= 1  # Decrementa la cantidad de elementos en la cola
            
            if self.cant == 0:
                self.ul = None  # Si la cola queda vacía, ul debe ser None también
            
            return x  # Devuelve el valor eliminado
    
    def obtener_pr(self):
        return self.pr
    
    def obtener_cant(self):
        return self.cant

    def recorrer(self,aux):
        if aux is not None:
            print(aux.obtener_tiempo())  # Imprime el valor del nodo actual
            self.recorrer(aux.obtener_sig())  # Llama recursivamente a la función para el siguiente nodo


def simulartiempo(tiempoSimulacion,tiempodellegada,cola):
    tiempoactual=0
    clientesAtendidos= 0
    tiempoTotal = 0
    cajero = 0
    acum = 0
    
    while tiempoactual <= tiempoSimulacion:
        if random.random() <= tiempodellegada:
            cola.insertar(tiempoactual)
        if cajero == 0:
            cola.suprimir()
            atendido = cola.suprimir()
            cajero = 5
        elif cajero > 0:
            cajero -= 1
            if cajero == 1:
                clientesAtendidos += 1
                tiempoEspera = tiempoactual - atendido
                tiempoTotal += tiempoEspera
        tiempoactual+=1
    long= cola.obtener_cant()
    while not cola.vacia():
        acum += cola.suprimir()

    print(f"Cantidad de Clientes atendidos: {clientesAtendidos}")
    print(f"Tiempo promedio de espera de los clientes atendidos {tiempoTotal/clientesAtendidos}")
    print(f"Clientes no Atendidos: {long}")
    print(f"Tiempo promedio de espera de los clientes no atendidos es: {acum/long:.2f}")
    

if __name__=="__main__":
    cola = Cola()
    simulartiempo(60, 0.5,cola)
