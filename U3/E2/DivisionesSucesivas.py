import numpy as np
class PilaSecuencial:
    def __init__(self,cantidad):
        self.cant= cantidad
        self.tope = -1
        self.elementos = np.zeros(cantidad,dtype=int)
        
    def vacia(self):
        return self.tope == -1
    
    def insertar(self,elemento):
        if self.tope < self.cant-1:
            self.tope += 1
            self.elementos[self.tope] = elemento
        else:
            print(f"No se pudo apilar el elemento {elemento}, la pila está llena.")
    
    def suprimir(self):
        if self.vacia():
            print("La pila esta vacia.")
            return None
        else:
            ultimo = self.elementos[self.tope]
            self.tope -= 1
            return ultimo
        
if __name__=="__main__":
    print("Numero decimal a convertir: 450")
    decimalRandom = 450
    binario = ""
    pilasecuencial= PilaSecuencial(decimalRandom) 
    
    while decimalRandom > 0:
        resto = decimalRandom%2
        pilasecuencial.insertar(resto)
        decimalRandom = decimalRandom // 2
        
    print("-"*30)   
    
    while not pilasecuencial.vacia():
        binario += str(pilasecuencial.suprimir())
    print(f"Número 450 en binario:{binario}")