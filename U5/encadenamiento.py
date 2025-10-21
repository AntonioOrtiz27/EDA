import numpy as np
from lista import ListaEnlazada

class TablaHashE:
    __tamaño : int
    __tabla : np.array
    
    def __init__(self,tamaño : int):
        #El tamaño del arreglo debe ser la cantidad de valor necesario a guardar (m) dividido en 0.7 y dicho numero debe ser primo
        #aqui lo que hago es obtener el entero del tamaño dividido en 0.7 luego redondearlo ya que necesito un numero entero y finalmente
        #envio el valor resultante a la funcion obtener primo que devuelve el valor que envie si es primo o el primo siguiente
        #asi finalmente el tamaño de la tabla es un primo que cumple con las condiciones necesarias
        self.__tamaño = int(np.ceil(self.obtener_primo(tamaño/0.7)))
        #en este ejercicio decidi que era bastante comodo hacer un arreglo numpy de listas enlazadas 
        self.__tabla = np.array([ListaEnlazada() for _ in range(self.__tamaño)], dtype=ListaEnlazada)
    

    def obtener_primo(self,n):
        if not self.es_primo(n):
            siguiente = n + 1
            while not self.es_primo(siguiente):
                siguiente += 1
            n = siguiente
            
        return n
    
    def es_primo(self,n):
        band = True
        if n < 2:
            band = False
        else:
            i = 2
            while i <= int(n ** 0.5) and band:
                if n % i == 0:
                    band = False
                i += 1

        return band

    def hashing(self, valor:int):
        #Metodo de transformacion hay varios, este especificamente solo funciona para enteros
        return valor % self.__tamaño
    
    def insertar(self, valor : str):
        #directamente insertamos valor en el indice las colisiones el manejo de colisiones es automatico practicamente jaja
        indice = self.hashing(valor)
        self.__tabla[indice].insertar(valor) #los repetidos directamente los maneja el insertar de lista enlazada

    def buscar(self,valor : str):
        indice = self.hashing(valor)
        aux = self.__tabla[indice].getCabeza() #obtenemos la cabeza de la lista enlazada en dicha posicion
        encontrado = False
        while aux != None and aux.getElem() != valor: #buscamos entre el valor y las colisiones si es que hubo
            aux = aux.getSig()
        if aux != None:
            encontrado = True 
            print(f"el valor {valor} esta en el indice {indice}")
        else:
            print(f"el valor {valor} no se encontro")

        return encontrado
    
    def mostrarEncadenamiento(self):
        for i, self.__tabla in enumerate(self.__tabla):
            print(f"[{i}] {self.__tabla}")

