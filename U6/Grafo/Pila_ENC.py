class Celda:
    __elem:int
    __sig:None
    
    def __init__(self,elem:int):
        self.__elem = elem
        self.__sig = None
    
    def getSig(self):
        return self.__sig
    
    def setSig(self,sig):
        self.__sig = sig
    
    def getElem(self):
        return self.__elem
    
class Pila:
    __tope : Celda
    __cant : int
    
    def __init__(self):
        self.__tope = None
        self.__cant = 0
        
    def vacia(self):
        return self.__cant == 0
    
    def insertar(self,elem:int):
        nuevo  = Celda(elem) 
        nuevo.setSig(self.__tope) 
        self.__tope = nuevo 
        self.__cant += 1 
        
    def suprimir(self):
        if self.vacia():
            return 0 
        else:
            self.__cant-=1 
            borrado = self.__tope.getElem() 
            self.__tope = self.__tope.getSig() 
            return borrado 