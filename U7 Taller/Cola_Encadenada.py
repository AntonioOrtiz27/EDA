class Celda:
    __elem : object
    __sig : None
    
    def __init__(self, elem: object):
        self.__elem = elem
        self.__sig = None
        
    def getElem(self): return self.__elem
    def setElem(self,elem): self.__elem = elem
    def getSig(self): return self.__sig
    def setSig(self,sig): self.__sig = sig
        
""" 
La cola permite una exploración por niveles (búsqueda en amplitud) 
si se insertan siempre en ese orden; combinada con la poda por cota, 
controla qué ramas seguir explorando.       
"""

class ColaEncadenada:
    __primero : Celda
    __ultimo : Celda
    __cant : int
    
    def __init__(self):
        self.__primero = None
        self.__ultimo = None
        self.__cant = 0
        
    def vacia(self): return self.__cant == 0

    def insertar(self,elem : int):
        nuevo = Celda(elem)
        if self.vacia():
            self.__primero = nuevo
        else:
            self.__ultimo.setSig(nuevo)
        self.__ultimo = nuevo
        self.__cant += 1

    def suprimir(self):
        if self.vacia():
            return None
        else:
            suprimido = self.__primero.getElem()
            self.__cant -= 1
            self.__primero = self.__primero.getSig()
            return suprimido
        
    def recuperar(self)->Celda: return self.__primero
    
    def recorrer(self):
        aux = self.__primero
        while aux != None:
            print(aux.getElem())
            aux = aux.getSig()