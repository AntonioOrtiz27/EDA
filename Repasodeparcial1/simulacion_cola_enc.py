import random
class Nodo:
    __elem : int
    __sig : None
    
    def __init__(self,elem):
        self.__elem = elem
        self.__sig = None
        
    def getElem(self):
        return self.__elem
    
    def setElem(self,elem):
        self.__elem = elem
        
    def getSig(self):
        return self.__sig

    def setSig(self,sig):
        self.__sig = sig
        
class ColaEncadenada:
    __primero : Nodo
    __ultimo : Nodo
    __cant : int
    #crear
    def __init__(self):
        self.__primero = None
        self.__ultimo = None
        self.__cant = 0
    #vacia
    def vacia(self):
        return self.__cant == 0
    #insercion
    def insertar(self,elem : int):
        nuevo = Nodo(elem)
        if self.vacia():
            self.__primero = nuevo
        else:
            self.__ultimo.setSig(nuevo)
        self.__ultimo = nuevo
        self.__cant += 1

    #eliminar
    def suprimir(self):
        if self.vacia():
            return 0
        else:
            suprimido = self.__primero.getElem()
            self.__cant -= 1
            self.__primero = self.__primero.getSig()
            return suprimido
        
if __name__=="__main__":
    cola = ColaEncadenada()
    tiempo_total = 300  # 5 horas
    t_cajero1 = 6
    t_cajero2 = 4

    libre1 = 0
    libre2 = 0
    atendidos1 = 0
    atendidos2 = 0
    
    frecuencia = 3

    for minuto in range(1, tiempo_total + 1):
        # Llega un pensionado con probabilidad 1/3
        if random.random() <= 1/frecuencia:
            cola.insertar(minuto)
        
        # Cajero 1 atiende
        if libre1 == 0 and not cola.vacia():
            cola.suprimir()
            libre1 = t_cajero1
            atendidos1 += 1
        
        # Cajero 2 atiende
        if libre2 == 0 and not cola.vacia():
            cola.suprimir()
            libre2 = t_cajero2
            atendidos2 += 1
        
        # Pasar el tiempo de atención
        if libre1 > 0:
            libre1 -= 1
        if libre2 > 0:
            libre2 -= 1
            
    print(f"la cantidad de pensionados atendidos por el cajero 1: {atendidos1}")
    print(f"la cantidad de pensionados atendidos por el cajero 2: {atendidos2}")


