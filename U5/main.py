from Abierto import TablaHashA
from encadenamiento import TablaHashE

if __name__=="__main__":
    
    # Utilizando el metodo de las divisiones sucesivas

    tabla_encadenada= TablaHashE(5)    
    tabla_direccionamiento = TablaHashA(10)
    claves = [66,467,566,735,285,87,66]
    
    print("----TABLA HASH DIRECCIONAMIENTO ABIERTO-----")
    for clave in claves:
        tabla_direccionamiento.insertar(clave)
        
    tabla_direccionamiento.buscar(467)
    tabla_direccionamiento.buscar(66)
    tabla_direccionamiento.buscar(285)
    
    tabla_direccionamiento.mostrarDireccionamiento()
    
    print("\n----TABLA HASH ENCADENADA----")
    for clave in claves:
        tabla_encadenada.insertar(clave)
    
    tabla_encadenada.buscar(700)
    tabla_encadenada.buscar(735)
    
    tabla_encadenada.mostrarEncadenamiento()
    
    # Utilizando un metodo alfanumerico

    print("---- TABLA HASH DIRECCIONAMIENTO ABIERTO CON EQUIPOS DE ARGENTINA -----")
    
    t_direccionamiento = TablaHashA(13.5)
    equipos = ['Boca','River','Racing','San Lorenzo','Velez']
    # el 13.5 redondea a 20 claves, el motivo del valor es para simular la liga.
    
    # Insertar
    for equipo in equipos:
        t_direccionamiento.insertarClubes(equipo)
        
    # Mostrar tabla
    t_direccionamiento.mostrarDireccionamiento()
    
    # Buscar equipo
    t_direccionamiento.buscarClubes('Boca')

    print("---- TABLA HASH ENCADENADA CON EQUIPOS DE ARGENTINA -----")
    
    t_encadenada = TablaHashE(13.5)
    clubes = [
    'Boca', 'River', 'Racing', 'San Lorenzo', 'Velez',
    'Argentinos Juniors', 'Arsenal', 'Atlético Tucumán', 'Banfield', 'Barracas Central',
    'Belgrano', 'Central Córdoba (SdE)', 'Defensa y Justicia', 'Deportivo Riestra', 'Estudiantes (LP)',
    'Gimnasia (LP)', 'Godoy Cruz', 'Huracán', 'Independiente', 'Instituto',
    'Lanús', 'Newells Old Boys', 'Platense', 'Rosario Central', 'Sarmiento (J)',
    'Talleres (C)', 'Tigre', 'Unión (SF)', 'Vélez Sarsfield', 'Colón'
    ]
    
    # Insertar
    for club in clubes:
        t_encadenada.insertarEquipos(club)
        
    # Mostrar tabla
    t_encadenada.mostrarEncadenamiento()

    # Buscar equipo
    t_encadenada.buscarEquipos('Velez')


    
    
    
    

    
    