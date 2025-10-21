class NodoHuffman:
   __str : str
   __frecuencia : int
   __izquierda : object
   __derecha : object
   
   def __init__(self, str, frecuencia):
      self.__str = str
      self.__frecuencia = frecuencia
      self.__izquierda = None
      self.__derecha = None
      
   def getStr(self):
      return self.__str
   
   def getFrecuencia(self):
      return self.__frecuencia
   
   def getIzquierda(self):
      return self.__izquierda
   
   def getDerecha(self):
      return self.__derecha
   
   def setIzquierda(self, izquierda):
      self.__izquierda = izquierda
   
   def setDerecha(self, derecha):
      self.__derecha = derecha
      
def analizarCadena(cadena: str) -> list:
   lista = []
   while cadena != "":
      letra = cadena[0]
      frecuencia = cadena.count(letra)
      for i in range(len(cadena)):
         cadena = cadena.replace(letra, "", -1)
      lista.append(NodoHuffman(letra, frecuencia))
   return lista

def ordenarLista(lista: list) -> list:
   lista.sort(key = lambda x: x.getFrecuencia())
   return lista

def armarArbol(lista: list) -> NodoHuffman:
   while len(lista) > 1:
      nodo1 = lista.pop(0)
      nodo2 = lista.pop(0)
      frecuencia = nodo1.getFrecuencia() + nodo2.getFrecuencia()
      nodo = NodoHuffman(nodo1.getStr() + nodo2.getStr(), frecuencia)
      nodo.setIzquierda(nodo1)
      nodo.setDerecha(nodo2)
      lista.append(nodo)
      lista = ordenarLista(lista)
   return lista[0]

def codificar(arbol: NodoHuffman, cadena: str) -> str:
   codificacion = ""
   for letra in cadena:
      nodo = arbol
      while nodo.getStr() != letra:
         if letra in nodo.getIzquierda().getStr():
            codificacion += "0"
            nodo = nodo.getIzquierda()
         else:
            codificacion += "1"
            nodo = nodo.getDerecha()
      codificacion += " "
   return codificacion

if __name__=="__main__":
    
    cadena1 = input("Ingrese la cadena que desee comparar: ")
    cadena2 = input("Ingrese la cadena con la que desee comparar: ")

    print("La longitud de la cadena 1 es: ", len(cadena1))
    print("La longitud de la cadena 2 es: ", len(cadena2))