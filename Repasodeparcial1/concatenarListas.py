class Nodo:
    def __init__(self, dato):
        self.__dato = dato
        self.__siguiente = None

    def obtener_dato(self):
        return self.__dato

    def set_dato(self, dato):
        self.__dato = dato

    def obtener_siguiente(self):
        return self.__siguiente

    def set_siguiente(self, siguiente):
        self.__siguiente = siguiente

class ListaEncadenada:
    def __init__(self):
        self.__cabeza = None
        self.__cantidad = 0

    def vacia(self):
        return self.__cantidad == 0

    def obtener_cantidad(self):
        return self.__cantidad
    def insertar(self, x, p):
        if 1>p> self.__cantidad + 1:
            print("Error: Posición inválida.")
            return
        
        nuevo = Nodo(x)
        if p == 1 and self.vacia():
            nuevo.set_siguiente(self.__cabeza)
            self.__cabeza = nuevo
        else:
            actual = self.__cabeza
            for _ in range(1, p - 1):
                if actual is not None:
                    actual = actual.obtener_siguiente()
                else:
                    print("Error: Posición inválida.")
                    return
            
            if actual is not None:
                nuevo.set_siguiente(actual.obtener_siguiente())
                actual.set_siguiente(nuevo)
            else:
                print("Error: Posición inválida.")
                return
        
        self.__cantidad += 1

    def suprimir(self, p):
        if 1>p > self.__cantidad:
            print("Error: Posición inválida.")
            return
        
        if p == 1:
            # Eliminar el primer nodo
            self.__cabeza = self.__cabeza.obtener_siguiente()
        else:
            # Navegar hasta el nodo anterior al que se quiere eliminar
            actual = self.__cabeza
            for _ in range(1, p - 1):
                if actual is not None:
                    actual = actual.obtener_siguiente()
                else:
                    print("Error: Posición inválida.")
                    return
            
            if actual is not None and actual.obtener_siguiente() is not None:
                actual.set_siguiente(actual.obtener_siguiente().obtener_siguiente())
            else:
                print("Error: Posición inválida.")
                return
        
        self.__cantidad -= 1


    def recuperar(self, p):
        if 1>p > self.__cantidad:
            print("Error: Posición inválida.")
            return None
        
        actual = self.__cabeza
        for _ in range(1, p):
            if actual is not None:
                actual = actual.obtener_siguiente()
            else:
                print("Error: Posición inválida.")
                return None

        if actual is not None:
            return actual.obtener_dato()
        print("Error: Posición inválida.")
        return None


    def buscar(self, x):
        actual = self.__cabeza
        pos = 0
        band = False
        while actual is not None and not band:
            if actual.obtener_dato() == x:
                band = True
            actual = actual.obtener_siguiente()
            pos += 1
        if band:
            return pos
        else:
            print("Error: Elemento no encontrado.")
            return None

    def primer_elemento(self):
        if not self.vacia():
            return self.__cabeza
        else:
            print("Error: La lista está vacía.")
            return None

    def ultimo_elemento(self):
        actual = self.__cabeza
        if not self.vacia():
            while actual.obtener_siguiente() is not None:
                actual = actual.obtener_siguiente()
            return actual
        else:
            print("Error: La lista está vacía.")
            return None

    def siguiente_posicion(self, p):
        if 1 <= p < self.__cantidad:
            return p + 1
        print("Error: No hay posición siguiente.")
        return None


    def anterior_posicion(self, p):
        if 1 < p <= self.__cantidad:
            return p - 1
        print("Error: No hay posición anterior.")
        return None


    def recorrer(self):
        actual = self.__cabeza
        while actual is not None:
            print(actual.obtener_dato(), end=" ")
            actual = actual.obtener_siguiente()
        print()

# Ejecutar las pruebas
if __name__ == "__main__":
    L1 = ListaEncadenada()
    L2 = ListaEncadenada()
    L1.insertar(1,1)
    L1.insertar(2,2)
    L1.insertar(3,3)
    L2.insertar(4,1)
    L2.insertar(5,2)
    L2.insertar(6,3)
    print("l1",L1.recorrer()  )# Salida esperada: 1 2 3
    print("l2",L2.recorrer()  )# Salida esperada: 1 2 3
    print(L1.ultimo_elemento())
    print(L2.primer_elemento())

    L1.ultimo_elemento().set_siguiente(L2.primer_elemento())
    
    
    
    print("l1",L1.recorrer()  )# Salida esperada: 1 2 3 4 5 6
