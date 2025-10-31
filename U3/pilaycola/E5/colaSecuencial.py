import numpy as np
class ColaSecuencial:
    __Pr : int
    __Ul: int
    __max: int
    __cant:int 
    
    #Crear
    def __init__(self,maximo : int):
        self.__lista = np.empty(maximo,dtype=int)
        self.__Pr = 0
        self.__Ul = 0
        self.__max = maximo
        self.__cant = 0
        
    def GetPrimero(self):
        return self.__Pr
    
    def GetCantidad(self):
        return self.__cant
    
    def llena(self):
        return self.__cant == self.__max
    #vacia
    def vacia(self):
        return self.__cant == 0
    #Insercion
    def insertar(self,elem:int):
        if self.__cant < self.__max:
            self.__lista[self.__Ul] = elem
            self.__Ul = (self.__Ul+1) % self.__max
            self.__cant += 1
            print(f"se agrego: {elem}")
        else:
            print(f"No se pudo insertar el elemento {elem} ya que la cola esta llena de elementos.")
    #eliminar
    def suprimir(self):
        if self.vacia():
            return 0
        else:
            x = self.__lista[self.__Pr]
            self.__Pr = (self.__Pr + 1) % self.__max
            self.__cant -= 1
            print(f"Se elimino el elemento {x}")
            
    #recorrer
    def recorrer(self):
        print("Elementos de la Cola")
        if not self.vacia():
            i = self.__Pr
            j = 0
            while j < self.__cant:
                print(self.__lista[i])
                i = (i + 1) % self.__max
                j += 1
    
if __name__ == '__main__':
    print("Cola Secuencial de 5 elementos")
    ColaS = ColaSecuencial(5)
    ColaS.insertar(1)
    ColaS.insertar(2)
    ColaS.insertar(3)
    ColaS.insertar(4)
    ColaS.insertar(5)
    ColaS.insertar(6)
    ColaS.recorrer()
    ColaS.suprimir()
    ColaS.recorrer()
