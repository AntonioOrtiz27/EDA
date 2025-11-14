import numpy as np

""" ABB """
class Nodo:
    __izq: object
    __der:object
    __elem:int
    
    def __init__(self,valor):
        self.__izq = None
        self.__der = None
        self.__elem = valor
        
    def getDato(self): return self.__elem
        
    def grado(self):
        g+=1
        if self.__izq is not None:
            g += 1
        if self.__der is not None:
            g += 1
        return g    
        
class Arbol:
    __raiz:Nodo
    
    def __init__(self):
        self.__raiz = None
    
    def vacia(self): return self.__raiz == None
    
    def getRaiz(self): return self.__raiz
    
    def insertar(self,nodo,valor):
        
        if self.vacia():
            self.__raiz = valor
        
        elif valor < nodo.getDato():
            if nodo.getIzq() is None:
                nodo.setIzq(Nodo(valor))
            else:
                self.insertar(nodo.getIzq(),valor)
                
        elif valor > nodo.getDato():
            if nodo.getDer() is None:
                nodo.setDer(Nodo(valor))
            else:
                self.insertar(nodo.getDer(),valor)
        else:
            print("Nodo repetido")
            
    def preorder(self,nodo):
        print(nodo.getDato())
        self.preorder(nodo.getIzq())
        self.preorder(nodo.getDer())

    def inorder(self,nodo):
        self.inorder(nodo.getIzq())
        print(nodo.getDato())
        self.inorder(nodo.getDer())
    
    
    def postorder(self,nodo):
        self.postorder(nodo.getIzq())
        self.postorder(nodo.getDer())
        print(nodo.getDato())

    def buscar(self, nodo, valor):
        
        if nodo is None:
            encontrado = None
        else:
            
            if valor == nodo.getDato():
                encontrado = nodo
            elif valor < nodo.getDato():
                encotnrado = self.buscar(nodo.getIzq(),valor)
            else:
                encontrado = self.buscar(nodo.getDer(),valor)
                
        return encontrado
    
    def gradoArbol(self,raiz):
        if raiz is None:
            aux = None
        else:
            aux = raiz.grado()
            print(f"GRADO DEL ARBOL: {aux}")
    
    """---Incisos de parciales viejos---"""
    
    
    # -una función que imprima todos los nodos hojas. (preorder)
    def Hojas(self,nodo):
        if nodo != None:
            if nodo.grado() == 0:
                print(nodo.getDato())
            self.Hojas(nodo.getIzq())
            self.Hojas(nodo.getDer())

        
    # -una función recursiva que imprima el grado de un nodo ingresado por teclado.
    def gradoNodo(self,raiz,valor):
        nodo = self.buscar(raiz,valor)
        if nodo is None:
            aux = None
        else:
            aux = nodo.grado()
            print(f"GRADO DEL NODO {valor} : {aux}")
    

            
    # -una función donde se ingresan dos claves, 
    # decir si la segunda clave es descendiente directo de la primera clave.

    def padre(self,raiz,padre,hijo):
        nodo = self.buscar(raiz,padre)
        bandera=False
        
        if nodo is not None:
            izq = nodo.getIzq()
            der = nodo.getDer()
            bandera = (izq!=None and izq.getDato()==hijo) or (der!=None and der.getDato()==hijo)

        return bandera
    
    """---Incisos de modelo de parcial---"""
    
    # una funcion que imprima la cantidad de nodos que tienen un solo descendiente directo.
    def preorden(self,nodo):
        c = 0
        
        if nodo != None:
            if nodo.grado() == 1:
                c += 1
            c += self.preorden(nodo.getIzq())
            c += self.preorden(nodo.getDer())
            
        print("\nCantidad de nodos con un solo descendiente directo:",c)
        return c
    
    # -una función que imprima todos los nodos de un nivel ingresado por teclado.
    def nivel(self, nodo, n):
        if nodo is not None:
            if n == 1:
                print(nodo.getDato(), end=" ")
            elif n > 1:
                self.nivel(nodo.getIzq(), n - 1)
                self.nivel(nodo.getDer(), n - 1)
                
    # -una función que imprima todos los descendientes terminales de un nodo ingresado por teclado
            
    def descendientesTerminales(self,raiz, valor):
        nodo = self.buscar(raiz, valor)
        
        if nodo != None:
            print(f"Descendientes terminales de {valor}: ", end="")
            self.hojas(nodo)
    
    
"""Tabla HASH Direccionamiento Abierto"""
#TAD
class hashD:
    __tabla: np.ndarray
    __tamaño: int
    
    def __init__(self,tamaño:int,Fcarga=0.7):
        self.__tamaño = self.getPrimo(tamaño/Fcarga)
        self.__tabla = np.full(self.__tamaño,None,dtype=object)
        
    # Operaciones Abstractas  
    def division(self,clave):
        return clave % self.__tamaño
    
    def extraccion(self,clave):
        return int(clave[-3:])
    
    def alfanumerico(self,clave):
        sum = 0
        for char in str(clave):
            sum += ord(char)
        return sum
    
    def insertar(self, valor:int):
        i = self.hash(valor)
        repetido = False 
        
        if self.__tabla[i] == None: 
            self.__tabla[i] = valor
        elif self.__tabla[i] == valor: 
            repetido = True
        else: 
            fin = i
            i = (i + 1) % self.__tamaño  
            while self.__tabla[i] != None and i != fin:
                if self.__tabla[i] == valor:
                    repetido = True
                i = (i + 1) % self.__tamaño
            if repetido is False: 
                if i != fin: 
                    self.__tabla[i] = valor
        if repetido is True:
            print(f"Valor {valor} no insertado por que ya esta en la lista")
            
    def buscar(self, valor):
        i = self.hash(valor)
        encontrado = False
        
        if self.__tabla[i] == valor: 
            print(f"el valor {valor} se encontro en el indice {i}")
        else: 
            fin = i
            i = (i + 1) % self.__tamaño  
            while self.__tabla[i] != valor and i != fin:
                i = (i + 1) % self.__tamaño
            if i != fin:
                encontrado = True
        return encontrado
            
"""Tabla HASH ENCADENADA"""
#TAD

class ListaEnlazada():pass # para que no rompa los huevos
class hashE:
    __tamaño: int
    __tabla: np.ndarray
    
    def __init__(self,tamaño:1000,Fcarga=0.7):
        self.__tamaño = self.getPrimo(tamaño/Fcarga)
        self.__tabla = np.empty(self.__tamaño,dtype=object)
        for i in range(self.__tamaño):
            self.__tabla[i] = ListaEnlazada()
            
# Operaciones Abstractas    
    def division(self,clave):
        return clave % self.__tamaño
    
    def extraccion(self,clave):
        return int(clave[-3:])
    
    def alfanumerico(self,clave):
        sum = 0
        for char in str(clave):
            sum += ord(char)
        return sum % self.__tamaño
    
    def insertar(self,clave):
        i = self.hash(clave)
        self.__tabla[i].insertar(clave)
        
    def buscar(self,clave):
        i = self.hash(clave)
        aux = self.__tabla[i].getCabeza()
        encontrado = False
        intentos = 1
        
        while aux != None and aux.getDato() != clave:
            aux = aux.getSiguiente()
            intentos += 1
            
        if aux != None:
            encontrado = True
            print(f"Se encontro el valor {clave} en el indice {i} en {intentos}")
        else:
            print("No se encontro el valor")
            
        return encontrado
    
"""--- Metodos Primos---"""
    
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
    
""" Digrafo Secuencial"""
#TAD
class Digrafo:
    __vertices:int
    __matriz: np.ndarray
    
    def __init__(self,N):
        self.__vertices = N
        self.__matriz = np.zeros((N,N),dtype=int)
        
# Operaciones Abstractas
    def insertar(self,u,v): # Agregar Aristas    
        if self.__matriz[u][v] == 0:
            self.__matriz[u][v] = 1
        else:
            print("La arista ya existe")
            
    def adyacentes(self,u): # Adyacentes de un vertice
        adyacentes = []
        for v in range(self.__vertices):
            if self.__matriz[u][v] == 1:
                adyacentes.append(v)
        return adyacentes
    
    def dos_Vertices_son_adyacentes(self,u,v): # 2 vertices si son adyacentes
        if 0 <= u < self.__vertices and 0 <= v < self.__vertices:
            if self.__matriz[u][v] == 1 or self.__matriz[v][u] == 1:
                print(f"{u} y {v} son adyacentes")
            else:
                print(f"{u} y {v} no son adyacentes")
                
    def g_entrada(self,u): # Cantidad de aristas que llegan al vertice u
        c=0
        for v in range(self.__vertices):
            if self.__matriz[v][u] == 1:
                print(v)
                c+=1
        return c   
            
    def g_salida(self,u): # Cantidad de aristas que salen del vertice u
        c = 0
        for v in range(self.__vertices):
            if self.__matriz[u][v] == 1:
                print(v)
                c+=1
        return c        
        
    def nodosSumideros(self,u): # Verifica todos los nodos del digrafo si son sumideros
        for v in range(self.__vertices):
            if self.g_salida(u) == 0 and self.g_entrada(u) > 0:
                print(v)
            else:
                print("No hay nodos sumideros")
                
    def nodosFuentes(self,u):  # Verifica todos los nodos del digrafo si son fuentes
        for v in range(self.__vertices):
            if self.g_entrada(u)==0 and self.g_salida(u) > 0:
                print(v)
            else:
                print("No hay nodos fuentes")
    