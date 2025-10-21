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
        self.__tamaño = int(np.ceil(self.getPrimo(tamaño/0.7)))
        #en este ejercicio decidi que era bastante comodo hacer un arreglo numpy de listas enlazadas 
        self.__tabla = np.array([ListaEnlazada() for _ in range(self.__tamaño)], dtype=ListaEnlazada)
    

    def getPrimo(self,n):
        n += 1
        while not self.es_primo(n):
            n += 1
        return n
    
    def es_primo(self,n):
        if n <= 1:
            return False
        for i in range(2, int(n**0.5) + 1):
            if n % i == 0:
                return False
        return True

    def metodo_division(self, valor:int):
        #Metodo de transformacion hay varios, este especificamente solo funciona para enteros
        return valor % self.__tamaño
    
    def metodo_extraccion(self,clave):
        return int(clave[-3:])
    def metodo_plegado(self,clave):
        clave_str = str(clave)
        suma = 0
        # Vamos sumando los dígitos en bloques de 2
        for i in range(0, len(clave_str), 2):
            suma += int(clave_str[i:i+2])
        # Retornamos la suma módulo del tamaño de la tabla
        return suma % self.__M
    def metodo_cuadrado_medio(self,clave):
        cuadrado = str(int(clave )** 2)
        # Extraemos los dígitos centrales
        mid_index = len(cuadrado) // 2
        if len(cuadrado) > 2:
            resultado = int(cuadrado[mid_index - 1: mid_index + 1])
        else:
            resultado = int(cuadrado)
        return resultado % self.__M
    def metodo_alfanumerico(self,clave):
        suma = 0
        for char in str(clave):
            suma += ord(char)  # ord() devuelve el valor ASCII de un carácter
        return suma % self.__tamaño
    
    def insertar(self, valor : int):
        #directamente insertamos valor en el indice las colisiones el manejo de colisiones es automatico practicamente jaja
        indice = self.metodo_division(valor)
        self.__tabla[indice].insertarEnteros(valor) #los repetidos directamente los maneja el insertar de lista enlazada

    def insertarEquipos(self, valor : str):
        #directamente insertamos valor en el indice las colisiones el manejo de colisiones es automatico practicamente jaja
        indice = self.metodo_alfanumerico(valor)
        self.__tabla[indice].insertarCadenas(valor) #los repetidos directamente los maneja el insertar de lista enlazada

    def buscar(self,valor : str):
        indice = self.metodo_division(valor)
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
    
    def buscarEquipos(self,valor : str):
        indice = self.metodo_alfanumerico(valor)
        aux = self.__tabla[indice].getCabeza() 
        encontrado = False
        while aux != None and aux.getElem() != valor: #buscamos entre el valor y las colisiones si es que hubo
            aux = aux.getSig()
        if aux != None:
            encontrado = True 
            print(f"el equipo {valor} esta en la posicion {indice}")
        else:
            print(f"el equipo {valor} pincho. No está en la tabla.")

        return encontrado
    
    def mostrarEncadenamiento(self):
        for i, lista in enumerate(self.__tabla):
            print(f"[{i}] {lista}")

