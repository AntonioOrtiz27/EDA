from Nodo import Nodo
#TAD Arbol Binario de Busqueda        
class ArbolBinario:
    __raiz:Nodo
    
    def __init__(self):
        self.__raiz = None
        
    def getRaiz(self):
        return self.__raiz
        
    def setRaiz(self,x):
        self.__raiz = x
        
    def vacio(self):
        return self.__raiz == None
    
    def insertarRecursivo(self,valor:int, nodo:None):
        if self.vacio():
            self.__raiz = Nodo(valor)           
        elif valor < nodo.getDato():                        
            if nodo.getIzquierda() is None:                  
                nodo.setIzquierda((Nodo(valor)))
            else:
                self.insertarRecursivo(valor, nodo.getIzquierda())
        elif valor > nodo.getDato(): 
            if nodo.getDerecha() is None:
                nodo.setDerecha((Nodo (valor)))
            else:
                self.insertarRecursivo(valor, nodo.getDerecha())
        else:
            print(f"Erorr el Valor {valor} ya se encuentra en el arbol")
            
    def inorden(self, nodo):                                                    #Muestra los nodos en orden ascendente(del nodo mas chico al nodo mas grande)
        if  nodo is not None:
            self.inorden(nodo.getIzquierda())                                   #Recorre recurtsivamente el arbol izquierdo
            print(nodo.getDato(),end=" ")                                      #Imprime el nodo
            self.inorden(nodo.getDerecha())                                     #Recorre recursivamente el arbol derecho
        
    def preorden(self, nodo):                                                   #muestra primero la raiz del arbon, luego el hijo izquierdo y por ultimo el derecho
        if nodo is not None:
            print(nodo.getDato(), end=" ")                                     #Imprime el nodo
            self.preorden(nodo.getIzquierda())                                  #Recorre recurtsivamente el arbol izquierdo
            self.preorden(nodo.getDerecha())                                    #Recorre recursivamente el arbol derecho
        
    def postorden(self, nodo):                                                  #muestra primero los hijos izquierdo, derecho y luego la raiz
        if nodo is not None:
            self.postorden(nodo.getIzquierda())                                 #Recorre recurtsivamente el arbol izquierdo
            self.postorden(nodo.getDerecha())                                   #Recorre recursivamente el arbol derecho
            print(nodo.getDato(), end=" ")                                     #Imprime el nodo

    
    def getMinimo(self,nodo):                                                                
        if self.__raiz is None:                                 #Si la raiz no existe entonces retorna null
            return None                                                                            
        elif nodo.getIzquierda() is None:                       #Cuando no puede avanzar mas ese nodo es el minimo 
            return nodo
        else:
            return self.getMinimo(nodo.getIzquierda())          #Mientras haya nodo o hijo izquierdo avanza hacia ese nodo
        
    def getMaximo(self, nodo):
        if self.__raiz is None:                                 #Si la raiz no existe entonces retorna null
            return None
        elif nodo.getDerecha() is None:                         #Cuando no puede avanzar mas ese nodo es el maximo
            return nodo
        else:
            return self.getMaximo(nodo.getDerecha())            #Mientras haya nodo o hijo derecho avanza hacia ese nodo
    
    def eliminar(self, nodo, valor):
        """
            Verificación del árbol vacío:
                Primero, el método verifica si el árbol está vacío mediante self.vacio(). Si el árbol está vacío, imprime un mensaje y no realiza ninguna operación adicional.

            Recursión hacia el subárbol izquierdo o derecho:
                Aquí el método compara el valor que se desea eliminar con el valor del nodo actual:
                    Si valor es menor que el valor del nodo actual, el método recurre hacia el subárbol izquierdo (nodo.getIzquierda()), buscando el valor en ese subárbol.
                    Si valor es mayor, recurre al subárbol derecho (nodo.getDerecha()) en busca del valor en el lado derecho.
                    Esta recursión continúa hasta encontrar el nodo que contiene el valor que queremos eliminar.

            Nodo encontrado (valor coincidente):
            Caso 1: El nodo es una hoja (no tiene hijos):
                Si el nodo no tiene hijos (ambos subárboles izquierdo y derecho son None), simplemente se devuelve None, lo que efectivamente elimina el nodo de su posición en el árbol.

            Caso 2: El nodo tiene un solo hijo:
                Si el nodo solo tiene un hijo (izquierdo o derecho), el método devuelve ese hijo, reemplazando el nodo actual en su posición en el árbol.

            Caso 3: El nodo tiene dos hijos:
                En este caso, se necesita reemplazar el nodo con su sucesor en orden (el menor valor del subárbol derecho). Esto se hace en tres pasos:
                    Se encuentra el sucesor llamando a self.getMinimo(nodo.getDerecha()), que devuelve el nodo con el menor valor en el subárbol derecho.
                    Se actualiza el valor del nodo actual con el valor del sucesor (nodo.setValor(sucesor.getValor())).
                    Finalmente, se elimina el sucesor del subárbol derecho mediante una llamada recursiva a self.eliminar para evitar duplicados.
            
            Devolución del nodo actualizado:
                Después de actualizar el nodo (o eliminarlo si es un nodo hoja), el método devuelve el nodo actualizado para que la estructura del árbol permanezca consistente. Esto permite que el árbol se actualice correctamente en todos los niveles de recursión.

            Este método garantiza que el árbol permanezca ordenado tras la eliminación del nodo y que el BST conserve sus propiedades tras la operación.
        """
        
        if self.vacio():
            print("El arbol esta vacio")                                                                    
        
        if valor < nodo.getDato():                                                            #Si el valor a eliminar es menor que el valor del nodo actual(valor de la raiz),
            nodo.setIzquierda(self.eliminar(nodo.getIzquierda(),valor))                       #Buscar en el subárbol izquierdo
                
        elif valor > nodo.getDato():                                                         #Si el valor a eliminar es mayor que el valor del nodo actual,
            nodo.setDerecha(self.eliminar(nodo.getDerecha(),valor))                           #Buscar en el subárbol derecho
                                                                                                    
        else:                                                                                 #Si el valor es igual al valor del nodo actual, este es el nodo a eliminar
            
            if nodo.getIzquierda() is None and nodo.getDerecha() is None:                     #Caso 1: Nodo hoja, no tiene hijos.
                return None
            
            if nodo.getIzquierda() is None:                                                   #Caso 2: Nodo con 1 hijo
                return nodo.getDerecha()
            if nodo.getDerecha() is None:
                return nodo.getIzquierda()
                                                                                              #Caso 3: Nodo con 2 hijos
            sucesor = self.getMinimo(nodo.getDerecha())                                       #Encontrar el sucesor (el menor valor en el subárbol derecho)
            nodo.setDato(sucesor.getDato())                                                 #Copiar el valor del sucesor al nodo actual
            nodo.setDerecha(self.eliminar(nodo.getDerecha(), sucesor.getDato()))             #Eliminar el sucesor del subárbol derecho
        return nodo

    #metodo para visualizar el arbol en consola
    def mostrarArbol(self, nodo, nivel):
        if nodo is not None:
            self.mostrarArbol(nodo.getDerecha(), nivel + 1)
            print("    " * nivel + str(nodo.getDato()))
            self.mostrarArbol(nodo.getIzquierda(), nivel + 1)
            
    def buscar(self,nodo:Nodo,valor:int):
        if nodo is None:
            print(f"No se encontro el numero {valor}")
            encontrado = None    
        else:
            if nodo.getDato() == valor:
                print(f"Se encontro el numero {valor} ")
                encontrado = nodo
            elif valor < nodo.getDato():
                encontrado = self.buscar(nodo.getIzquierda(),valor)
            else:
                encontrado = self.buscar(nodo.getDerecha(),valor)
    
        return encontrado
    
    def hoja(self,nodo:Nodo,valor:int):
        hojita = self.buscar(nodo,valor)
        es_hoja=True
        if hojita.getDerecha() is None and hojita.getIzquierda() is None:
            print(f"{hojita.getDato()} es Hoja")
        else:
            print(f"{hojita.getDato()} no es hoja")
                  
    # Padre e Hijo
    def padre(self, padre : int, hijo : int):
        nodo_padre = self._busqueda(padre)
        es_padre = False
        
        if nodo_padre is None:
            print(f"{padre} no esta en el arbol")
        elif nodo_padre.getIzquierda() != None and nodo_padre.getIzquierda().getDato() == hijo:
                print(f"{padre} es padre de {hijo}")
                es_padre = True
        elif nodo_padre.getDerecha() != None and nodo_padre.getDerecha().getDato()==hijo:
                print(f"{padre} es padre de {hijo}")
                es_padre = True
        else:
            print(f"{padre} no es padre de {hijo}")
    
        return es_padre
    
    def hijo(self, hijo : int, padre : int):
        nodo_padre = self._busqueda(padre)
        es_hijo = False
        
        if nodo_padre is None:
            print(f"{padre} no esta en el arbol")
            es_hijo = None
        elif nodo_padre.getIzquierda() != None and nodo_padre.getIzquierda().getDato() == hijo:
            print(f"{hijo} es hijo de {padre}")
            es_hijo = True
        elif nodo_padre.getDerecha() != None and nodo_padre.getDerecha().getDato()==hijo:
            print(f"{hijo} es hijo de {padre}")
            es_hijo = True
        else:
            print(f"{hijo} no es hijo de {padre}")
    
        return es_hijo
    
    def _busqueda(self,valor:int):
        return self.buscarHijoYPadre(self.__raiz,valor)
    
    def buscarHijoYPadre(self,nodo:Nodo,valor:int):
        if nodo is None:
            encontrado = None
        else:
            if nodo.getDato() == valor:
                encontrado = nodo
            elif valor < nodo.getDato():
                encontrado = self.buscarHijoYPadre(nodo.getIzquierda(),valor)
            else:
                encontrado = self.buscarHijoYPadre(nodo.getDerecha(),valor)
    
        return encontrado

    def _nivel(self,nodo:Nodo,valor:int,nivel):
        if nodo is None:
            print(f"No lo encontro al nodo {valor}")
            aux = None
        elif nodo.getDato() == valor:
            print(f"El nivel del nodo {valor} es {nivel}")
            aux = nivel
        elif valor < nodo.getDato():
            aux = self._nivel(nodo.getIzquierda(),valor,nivel+1)
        else:
            aux = self._nivel(nodo.getDerecha(),valor,nivel+1)

        return aux

    def nivel(self,raiz,valor):
        return self._nivel(raiz,valor,1)
    
    
    def nodosNivel(self,raiz,nivel):
        if raiz != None:
            if nivel == 1:
                print(raiz.getDato(), end=" ")
            elif nivel > 1:
                self.nodosNivel(raiz.getIzquierda(), nivel - 1)
                self.nodosNivel(raiz.getDerecha(), nivel - 1)
    
    def _altura(self,nodo):
        if nodo is None:
            aux = 0
        else: 
            aux = 1 + max(self._altura(nodo.getDerecha()), self._altura(nodo.getIzquierda()))
        return aux
    
    def altura(self):
        h = self._altura(self.__raiz)
        print(f"La Altura del arbol es {h}")
        return h
    
    def buscarCamino(self,nodo:Nodo,valor:int):
        if nodo is None:
            encontrado = 0       
        else:
            if nodo.getDato() == valor:
                encontrado = nodo
            elif valor < nodo.getDato():
                encontrado = self.buscarCamino(nodo.getIzquierda(),valor)
            else:
                encontrado = self.buscarCamino(nodo.getDerecha(),valor)
    
        return encontrado
    
    def _buscar(self,valor):
        return self.buscarCamino(self.__raiz,valor)

    def antecesor(self,x : int,z : int):
        es_antecesor = False
        if self.buscarCamino(self._buscar(x),z) != None:
            es_antecesor = True
        return es_antecesor
        
    def camino(self,inicio : int,fin : int):
        es_antecesor = self.antecesor(inicio, fin)
        camino = []
        if es_antecesor == True:
            nodo_actual = self._buscar(inicio)
            while nodo_actual != None and nodo_actual.getDato() != fin:
                if fin < nodo_actual.getDato():
                    camino.append(0)
                    nodo_actual = nodo_actual.getIzquierda()
                else:
                    camino.append(1)
                    nodo_actual = nodo_actual.getDerecha()
        return camino

    def gradoNodo(self,raiz, valor:int):
        nodo = self.buscar(raiz, valor)
        if nodo is None:
            aux = None
        else:
            print(f"El grado del nodo {valor} es: {nodo.grado()}")
            aux= nodo.grado()
        return aux
    
    def gradoArbol(self,nodo):
        if nodo is None:
            aux = None
        else:
            aux = nodo.grado()
            print(f"Grado del arbol: {aux}")
            
    # una función donde se ingresan dos claves, 
    # decir si la segunda clave es descendiente directo de la primera clave.

    def Dosclaves(self,padre,hijo):
        nodo_padre= self.buscar(self.__raiz,padre)
        bandera=False
        
        if nodo_padre is not None:
            izq= nodo_padre.getIzquierda()
            der= nodo_padre.getDerecha()
            bandera= ((izq!=None and izq.getDato()==hijo) or (der!=None and der.getDato()==hijo))
            
        return bandera
    
    # una función que imprima todos los nodos hojas. (preorder)
    def nodosHojas(self,nodo):
        if nodo != None:
            if nodo.grado() == 0:
                print(nodo.getDato())
            self.nodosHojas(nodo.getIzquierda())
            self.nodosHojas(nodo.getDerecha())
            
    # --una función que retorne la cantidad de descendientes de una clave que se ingresa por teclado.
    def inorder(self,nodo):
        
        c = 0
        if nodo != None:
            if nodo.grado() >= 1:
                c+=1
            c += self.inorder(nodo.getIzquierda())
            c += self.inorder(nodo.getDerecha())
        
        return c
    
    def descendientes(self,raiz,clave_ingresada):
        Nodo_buscado = self.buscar(raiz,clave_ingresada)
        
        if Nodo_buscado is not None:
            c = self.inorder(Nodo_buscado)
            print(f"Nodos descendientes de {clave_ingresada}: {c}")
            
            
if __name__ == "__main__":
    arbol = ArbolBinario()
    for x in [15, 10, 20, 8, 12, 17, 25]:
        arbol.insertarRecursivo(x,arbol.getRaiz())
    
    #Visualizar arbol en terminal
    print("Visualizar nodos del arbol en el orden que fueron insertados.\n")
    arbol.mostrarArbol(arbol.getRaiz(),0)
    
    # Recorridos del árbol
    print("\n\nRecorrido Inorden (debe mostrar valores en orden ascendente):")
    arbol.inorden(arbol.getRaiz())
    
    print("\nRecorrido Preorden (raíz, izquierda, derecha):")
    arbol.preorden(arbol.getRaiz())
    
    print("\nRecorrido Postorden (izquierda, derecha, raíz):")
    arbol.postorden(arbol.getRaiz())
    print("\n")
        
    # Prueba de eliminar un valor (en este caso 10)
    arbol.eliminar(arbol.getRaiz(),10)
    print("-"*45)
    print("Se elimino el nodo que contiene el valor 10")
    print("-"*45)

    # Recorrido Inorden después de eliminar
    print("\nRecorrido Inorden luego de eliminar el 10:")
    arbol.inorden(arbol.getRaiz())
    print("\nRecorrido Preorden luego de eliminar el 10:")
    arbol.preorden(arbol.getRaiz())
    print("\nRecorrido Postorden luego de eliminar el 10:")
    arbol.postorden(arbol.getRaiz())
    
    print("\n")
    print("Visualizar el arbol con el numero 10 suprimido")
    print("\n")
    
    #Visualizar arbol en terminal
    arbol.mostrarArbol(arbol.getRaiz(),0)

    # Prueba de obtener minimo y maximo
    print("\nValor minimo en el arbol:", arbol.getMinimo(arbol.getRaiz()).getDato())
    print("Valor maximo en el arbol:", arbol.getMaximo(arbol.getRaiz()).getDato())
    
    #Buscar elemento
    print("\nBUSCAR el numero 8")
    arbol.buscar(arbol.getRaiz(),8)
    print("\nBUSCAR el numero 10 que fue suprimido")
    arbol.buscar(arbol.getRaiz(),10)
    

    #Hoja
    print("\nVerificamos si 8 y 20 son HOJAS.")
    arbol.hoja(arbol.getRaiz(),8)
    arbol.hoja(arbol.getRaiz(),20)

    #Hijo
    print("\n¿8 es HIJO de 12?")
    arbol.hijo(8,12)
    print("\n¿17 es HIJO de 20?")
    arbol.hijo(17,20)
    print("\n¿12 es HIJO de 8?")
    arbol.hijo(12,8)
    print("\n¿20 es HIJO de 17?")
    arbol.hijo(20,17)
    print("\n¿100 esta en el arbol?")
    arbol.hijo(100,100)
    
    #Padre
    print("\n¿12 es PADRE de 8?")
    arbol.padre(12,8)
    print("\n¿20 es PADRE de 17?")
    arbol.padre(20,17)
    print("\n¿8 es PADRE de 12?")
    arbol.padre(8,12)
    print("\n¿17 es PADRE de 20?")
    arbol.padre(17,20)

        
    #Nivel
    print("\nIndicar el nivel de un nodo")
    arbol.nivel(arbol.getRaiz(),8)
    arbol.nivel(arbol.getRaiz(),20)
    print()
    
    print("\nMostrar nodos de acuerdo a nivel ingresado")
    niv = int(input("ingrese nivel para mostrar que nodos hay:"))
    arbol.nodosNivel(arbol.getRaiz(),niv)
    print()
    
    #Altura del arbol
    print("\nAltura del arbol")
    arbol.altura()
    
    #Camino
    print("\nCaminos en el árbol")
    print("\nCamino de 15 a 17")
    print(arbol.camino(15, 17))
    print("\nCamino de 15 a 25")
    print(arbol.camino(15, 25))
    print("\nCamino de 15 a 8")
    print(arbol.camino(15, 8))
    print()
    
    # Grado de un nodo
    print("\nGrado de un nodo")
    arbol.gradoNodo(arbol.getRaiz(),15)
    arbol.gradoNodo(arbol.getRaiz(),10)
    arbol.gradoNodo(arbol.getRaiz(),8)
    arbol.gradoNodo(arbol.getRaiz(),12)
    print()
    
    # Grado del arbol
    arbol.gradoArbol(arbol.getRaiz())
    print()
    
    # Verificar si la segunda clave es descendiente directo de la primer clave
    hijo= int(input("Ingrese la clave hijo:"))
    padre= int(input("Ingrese la clave padre:"))
    print(f"¿{hijo} es hijo de {padre}?",arbol.Dosclaves(padre,hijo))
    print()
    
    # una función que imprima todos los nodos hojas. (preorder)
    print("Todos los nodos hojas del arbol")
    arbol.nodosHojas(arbol.getRaiz())
    
    # --una función que retorne la cantidad de descendientes de una clave que se ingresa por teclado.
    nodo = int(input("Ingrese nodo para ver cuantos descendientes tiene:"))
    arbol.descendientes(arbol.getRaiz(),nodo)
    
print("\n---Fin TAD de Arbol Binario de Busqueda y sus Operaciones Básicas---")
        