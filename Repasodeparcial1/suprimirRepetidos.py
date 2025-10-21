class Contacto:
    __elemento: int
    __sig : None
    def __init__(self,elemento):
        self.__elemento = elemento
        self.__sig = None
        
    def getDato(self):
        return self.__elemento
    
    def setDato(self,dato):
        self.__elemento = dato
        
    def getSig(self)->object:
        return self.__sig
    
    def setSig(self,sig : object)->None:
        self.__sig = sig

class ListaEncadenada:
    __cabeza : Contacto
    __cant : int
    def __init__(self):
        self.__cabeza = None
        self.__cant = 0
    
    def insertar(self,elemen):
        nuevo = Contacto(elemen)
        nuevo.setSig(self.__cabeza)
        self.__cabeza= nuevo
        self.__cant+=1
        print(f"{nuevo.getDato()}", end=" ")
            
    def eliminarRepetidos(self):
        Lista =[] 
        Anterior = None
        Actual = self.__cabeza
        while Actual != None:
            if Actual.getDato() in Lista:
                Anterior.setSig(Actual.getSig())
            else:
                Lista.append(Actual.getDato())
                Anterior = Actual 
            Actual=Actual.getSig()
        print(Lista)
        
    def recorrer(self):
        aux = self.__cabeza
        print("Lista de numeros")
        while aux != None:
            print(aux.getDato())
            aux = aux.getSig()
            
if __name__=="__main__":
    listita = ListaEncadenada()
    
    listita.insertar(10)
    listita.insertar(5)
    listita.insertar(7)
    listita.insertar(5)
    listita.insertar(2)
    listita.insertar(10)
    print("\nEliminar repetidos")
    listita.eliminarRepetidos()
    listita.recorrer()