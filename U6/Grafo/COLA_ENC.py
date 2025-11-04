class Celda:
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
        
class Cola:
    __primero : Celda
    __ultimo : Celda
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
        nuevo = Celda(elem)
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