from Abierto import TablaHashA
from encadenamiento import TablaHashE

if __name__=="__main__":
    tabla_encadenada= TablaHashE(100)    
    tabla_direccionamiento = TablaHashA(100)
    claves = [66,467,566,735,285,87,66]
    
    print("----TABLA HASH DIRECCIONAMIENTO ABIERTO-----")
    for clave in claves:
        tabla_direccionamiento.insertar(clave)
        
    tabla_direccionamiento.buscar(467)
    tabla_direccionamiento.buscar(400)
    
    tabla_direccionamiento.mostrarDireccionamiento()
    
    print("\n----TABLA HASH ENCADENADA----")
    for clave in claves:
        tabla_encadenada.insertar(clave)
    
    tabla_encadenada.buscar(700)
    tabla_encadenada.buscar(735)
    
    tabla_encadenada.mostrarEncadenamiento()
    
    
    
    

    
    