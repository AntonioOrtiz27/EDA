class Nodo:
    __elem:int                                 
    __izquierda: object                         #Referencia al arbol izquierdo
    __derecha: object                         #Referencia al arbol derecho
    
    def __init__(self, elem:int):
        self.__elem = elem
        self.__izquierda = None                 #Deben apuntar a None xq todavia la parte izq del arbol esta vacio
        self.__derecha = None                   #Deben apuntar a None xq todavia la parte der del arbol esta vacio

    #agregar el GRADO en el nodo
    
    def grado(self):
        grado = 0
        if self.__elem.getIzquierda():
            grado+=1
        if self.__elem.getDerecha():
            grado+=1
        return grado
        
    def getDato(self):
        return self.__elem                      #Retorna el elemento del dato guardado
        
    def setDato(self,elemento):
        self.__elem = elemento                  #Setea el elemento del dato guardado        

    def getIzquierda(self):
        return self.__izquierda                 #Retorna la referencia al arbol izquierdo
    
    def getDerecha(self):
        return self.__derecha                   #Retorna la referencia al arbol derecho
        
    def setIzquierda(self, nodo):
        self.__izquierda = nodo                 #Setea la referencia del arbol izquierdo
        
    def setDerecha(self, nodo):
        self.__derecha = nodo                   #Setea la referencia del arbol derecho
