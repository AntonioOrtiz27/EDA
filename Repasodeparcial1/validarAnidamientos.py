class Celda:
    def __init__(self,elemento, sig):
        self.__elemento = elemento
        self.__sig = sig
        
    def obtener_elemento(self):
        return self.__elemento
    
    def cargar_elemento(self,elemento):
        self.__elemento = elemento
        
    def cargar_siguiente(self,tope):
        self.__sig = tope
        
    def obtener_siguiente(self):
        return self.__sig
    
class Pila_enc:
    __cant: int
    __tope: None
    
    def __init__(self,tope=None,cant=0):
        self.__cant = cant
        self.__tope = tope
        
    def vacia(self):
        return self.__cant == 0
    
    def insertar(self,x):
        nueva_celda = Celda(x,self.obtener_tope())
        self.__tope = nueva_celda
        self.__cant+=1
        
    def obtener_tope(self):
        return self.__tope
        
    def mostrar(self, aux=None):
        print("Estado actual de la pila:")
        if self.vacia():
            print("La pila está vacía")
        else:
            actual = self.__tope
            while actual is not None:
                if actual == self.__tope:
                    print(actual.obtener_elemento(),end=" ")
                else:
                    print(actual.obtener_elemento(),end=" ")
                actual = actual.obtener_siguiente()

    def suprimir(self):
        if self.vacia():
            return None
        else:
            elem = self.obtener_tope().obtener_elemento()
            self.__tope = self.obtener_tope().obtener_siguiente()
            self.__cant-=1
            return elem
        
    def validarAnidamiento(self,expresion:str) -> bool:
        pares = {')': '(', ']': '[', '}': '{'}   
        for char in expresion:
            if char in "([{":
                self.insertar(char)
            elif char in ")]}":
                if self.vacia():
                    return False
                tope = self.suprimir()
                if tope != pares[char]:
                    return False
        return self.vacia()  
            
        
if __name__=="__main__":
    pila_enc = Pila_enc()
    expresion1 = "{[()]}"  
    expresion2 = "{[(])}"   
    expresion3 = "([{}])()" 
    
    print(expresion1,pila_enc.validarAnidamiento(expresion1))
    pila_enc = Pila_enc() 
    print(expresion2,pila_enc.validarAnidamiento(expresion2))
    pila_enc = Pila_enc() 
    print(expresion3,pila_enc.validarAnidamiento(expresion3))
