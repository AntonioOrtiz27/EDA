from nodo import Nodo
        
class ListaEnlazada:
    __cabeza : Nodo
    def __init__(self):
        self.__cabeza = None
        
    def __str__(self):
        actual = self.__cabeza
        elementos = []
        while actual:
            elementos.append(str(actual.getElem()))  # convertimos a string ya que join funciona solo para
            actual = actual.getSig()
        return " -> ".join(elementos)

    def insertar(self, valor: str) -> None:
        nuevo = Nodo(valor)
        actual = self.__cabeza
        repetido = False

        if not actual:
            self.__cabeza = nuevo
        else:
            while actual.getSig() != None:
                if actual.getElem() == valor:
                    repetido = True
                actual = actual.getSig()
            if actual.getElem() == valor:
                repetido = True
                print(f"el elemento {valor} no se inserto ya esta en la tabla")
            if not repetido:
                actual.setSig(nuevo)

    def getCabeza(self):
        return self.__cabeza
