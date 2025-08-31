# EDA
ESTRUCTURAS DE DATOS Y ALGORITMOS  
PRACTICO Nº2 - Parte 1 : PILA 
 
 
Teniendo en cuenta la complejidad y eficiencia de los algoritmos, realice los 
siguientes ejercicios.  
Ejercicio 1:  
Implementar el TDA Pila, con sus operaciones Abstractas en Representación secuencial y 
encadenada. 
Ejercicio 2:  
Realizar un programa que implemente la conversión de un número decimal a su 
representación binaria utilizando el método de las divisiones sucesivas. 
Ejercicio 3: 
Las escaleras normalmente se pueden subir de 1 o 2 peldaños a la vez.  
Implementar un algoritmo no recursivo, utilizando una pila para simular el funcionamiento de 
la recursión, que liste todas las formas diferentes posibles de subir una escalera de ‘n’ 
peldaños. 
Ejercicio 4:  
Realizar un programa que simule el juego de las torres de 
Hanoi. 
 
El juego de las tres torres de Hanoi consiste en una 
configuración de tres pilas numeradas como 1, 2 y 3, con ‘n’ 
discos de tamaño creciente. Los discos se representarán 
mediante enteros. Los discos más grandes utilizarán valores 
mayores y los discos más pequeños valores menores. 
 
El objetivo del juego es trasladar los discos de la pila 1, a la pila 3, usando la pila 2 como 
auxiliar. Para realizar este traslado se deben cumplir siempre los siguientes requisitos: 
a) Solo se puede mover una pieza cada vez; y para tomar una segunda pieza se 
debe dejar primero la anterior en alguna torre.  
b) Solo puede apilar una pieza encima de una más grande.  
 
Se deberá ingresar el número de discos con el que se va a jugar y mostrar por pantalla el 
estado inicial del juego (todas las piezas colocadas en la pila 1 y las pilas 2 y 3 vacías).  
A partir de ahí, pedirá sucesivamente pares de números indicando la pila origen desde la 
que tomará la pieza y la pila destino a la que se quiere realizar el movimiento. El programa 
analizará si la jugada es factible. Si el resultado del análisis es positivo, moverá la ficha de 
una pila a otra. Si no lo es indicará que es una jugada imposible, indicando el porqué y 
pedirá un nuevo movimiento. 
 
El juego terminará cuando las pilas 1 y 2 estén vacías y todos los discos se encuentren en 
la pila 3, mostrando el número de jugadas realizadas y el número mínimo de jugadas (2n–1) 
en el que se podría haber realizado. 
 
ESTRUCTURAS DE DATOS Y ALGORITMOS  
PRACTICO Nº2 - Parte 2 :  COLA 
 
 
Ejercicio 5: 
Implementar el TDA Cola, con sus operaciones Abstractas en Representación secuencial y 
encadenada. 
Ejercicio 6: 
Modificar problema anterior de la escalera (resuelto utilizando un algoritmo no recursivo), 
pero que use una cola en lugar de pila. Compare las salidas de ambos programas.  
Ejercicio 7: 
El Laboratorio de Computación tiene una única impresora, a la cual llegan trabajos para 
imprimir de cualquiera de las máquinas.  Los trabajos a imprimir tienen asociado la cantidad 
de páginas (se aceptan, como máximo, trabajos de 100 páginas).  
Considerando que los trabajos llegan en promedio cada 5 minutos a la cola de impresión y 
que la impresora imprime a una velocidad de 10 ppm:  
Se requiere simular el comportamiento de dicha cola, teniendo en cuenta que la impresora 
tiene un tiempo máximo para procesar cada trabajo de 3 minutos. El trabajo que no se 
terminó de imprimir porque excedía su tiempo de proceso ingresa nuevamente a la cola con 
la cantidad de páginas que restan por imprimir. 
 
Suponer el tiempo de simulación de 1 hora y que la cantidad de páginas del trabajo es 
aleatoria.  Se pide:  
a) Informar cantidad de trabajos que quedaron sin atender.  
b) Indicar el promedio de espera de los trabajos impresos. 
Ejercicio 8: 
Un banco cuenta con 3 cajeros disponibles para atender a clientes que desean realizar 
depósitos. El tiempo de atención del cajero 1 es de 5 minutos, el del cajero 2 es de 3 
minutos, y el del cajero 3 es de 4 minutos en promedio. El tiempo promedio de llegada de 
los clientes es de 2 minutos. El tiempo durante el cual se desea realizar la simulación es de 
2 horas. Cada cajero tiene una cola de clientes distinta. Si un cliente llega y uno o más 
cajeros están disponibles, sin cola de espera, la elección es aleatoria. Si todos los cajeros 
están ocupados, los clientes eligen la cola más corta. Si las colas más cortas tienen el 
mismo número de clientes, la elección es aleatoria.  
Realizar en un algoritmo que permita determinar:  
a) El tiempo máximo de espera de los clientes en la cola.  
b) Cantidad de clientes atendidos.  
c) Cantidad de clientes que quedaron sin atender.  
d) Promedio de espera de los clientes atendidos.  
e) Promedio de espera de los clientes sin atender 
