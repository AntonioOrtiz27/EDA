class Nodo:
    __elem : str
    __sig : None
    
    def __init__(self,elem : str)->None:
        self.__elem = elem
        self.__sig = None
        
    def getElem(self)->str:
        return self.__elem
    
    def setElem(self,elem)->None:
        self.__elem = elem
        
    def getSig(self)->object:
        return self.__sig
    
    def setSig(self,sig : object)->None:
        self.__sig = sig