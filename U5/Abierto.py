import numpy as np
from sympy import nextprime


class TablaHashA:
    __tamaño : int
    __tabla : np.ndarray

    def __init__(self,tamaño : int,FCarga= 0.7):
        #El tamaño del arreglo debe ser la cantidad de valor necesario a guardar (m) dividido en 0.7 y dicho numero debe ser primo
        #aqui lo que hago es obtener el entero del tamaño dividido en 0.7 luego redondearlo ya que necesito un numero entero y finalmente
        #envio el valor resultante a la funcion obtener primo que devuelve el valor que envie si es primo o el primo siguiente
        #asi finalmente el tamaño de la tabla es un primo que cumple con las condiciones necesarias
        self.__tamaño = int(np.ceil(self.getPrimo(tamaño/FCarga)))
        self.__tabla = np.full(self.__tamaño,None,dtype = object)
        
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
    
    def getPrimoIlegal(self, n): 
        return nextprime(n)
        
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
    
    def insertar(self, valor:int):
        indice = self.metodo_division(valor)
        repetido = False #En tablas hash no se insertan valores repetidos

        if self.__tabla[indice] == None: #Si en la posicion del valor hasheado esta libre se inserta
            self.__tabla[indice] = valor
        elif self.__tabla[indice] == valor: #si en la posicion del valor hasheado esta otro valor igual  no se inserta
            repetido = True
        else: #Hubo una colisicion guardamos en una variable final el indice en el que estabamos esto nos servira para saber que reccorimos toda la tabla
            final = indice
            indice = (indice + 1) % self.__tamaño # aqui nos movemos a la siguiente posicion, el % self.__tamaño hara que el recorrido sea circular es decir posamos recorrer toda la tabla, si! como en cola circular XD
            while self.__tabla[indice] != None and indice != final:
                if self.__tabla[indice] == valor:
                    repetido = True
                indice = (indice + 1) % self.__tamaño
            if repetido is False: #si el valor se repite no se inserta nada
                if indice != final:# si el indice es igual al final quiere decir que se recorrio todo el arreglo y no se encontro posicion valida, osea que si son distintos se encontro lugar disponible
                    self.__tabla[indice] = valor
        if repetido is True:
            print(f"Valor {valor} no insertado por que ya esta en la lista")
            
            
    def insertarClubes(self, valor:str):
        indice = self.metodo_alfanumerico(valor)
        repetido = False 

        if self.__tabla[indice] == None: 
            self.__tabla[indice] = valor
        elif self.__tabla[indice] == valor: 
            repetido = True
        else: 
            final = indice
            indice = (indice + 1) % self.__tamaño 
            while self.__tabla[indice] != None and indice != final:
                if self.__tabla[indice] == valor:
                    repetido = True
                indice = (indice + 1) % self.__tamaño
            if repetido is False: 
                if indice != final:
                    self.__tabla[indice] = valor
        if repetido is True:
            print(f"El equipo {valor} no se agrego a la tabla anual por que ya esta en la liga(LPF)")

    def buscar(self, valor):
        indice = self.metodo_division(valor)
        encontrado = False
        intentos = 1
        
        if self.__tabla[indice] == valor: # si el valor de la posicion encontrada con hash es igual al valor se encontro el valor, no hubo colisiones
            print(f"el valor {valor} se encontro en el indice {indice} en {intentos} intentos")
            encontrado = True
        else: #sino es que hubo colisiones 
            fin = indice
            indice = (indice + 1) % self.__tamaño  #nos permite hacer la busqueda circular
            while self.__tabla[indice] != valor and indice != fin:
                intentos += 1
                indice = (indice + 1) % self.__tamaño

            if indice != fin:
                print(f"El valor {valor} se encontró en el índice {indice} en {intentos} intento(s).")
                encontrado = True
        if encontrado == False:
            print(f"El valor {valor} no se encontró en la tabla después de {intentos} intento(s).")
        
        return encontrado
    
    def buscarClubes(self, valor):
        indice = self.metodo_alfanumerico(valor)
        encontrado = False
        if self.__tabla[indice] == valor: # si el valor de la posicion encontrada con hash es igual al valor se encontro el valor, no hubo colisiones
            encontrado = True
            print(f"el equipo {valor} se encontro en la posicion {indice}")
        else: #sino es que hubo colisiones :c
            fin = indice
            indice = (indice + 1) % self.__tamaño  #nos permite hacer la busqueda circular
            while self.__tabla[indice] != valor and indice != fin:
                indice = (indice + 1) % self.__tamaño
            if indice != fin:
                encontrado = True
        return encontrado
    
    def mostrarDireccionamiento(self): #no es un metodo de la funcion misma pero ta buena pal debug
        for i in range(self.__tamaño):
            print(f"[{i}] {self.__tabla[i]}")
    

 
        
