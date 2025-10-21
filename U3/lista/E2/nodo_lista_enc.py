class Nodo:
    __elem : int
    __sig : None
    
    def __init__(self,elem):
        self.__elem = elem
        self.__sig = None
        
    def getDato(self):
        return self.__elem
    
    def setDato(self,elem):
        self.__elem = elem
        
    def getSiguiente(self):
        return self.__sig

    def setSiguiente(self,sig):
        self.__sig = sig