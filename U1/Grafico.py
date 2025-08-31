import matplotlib.pyplot as plt
"""
4 -Representar gráficamente en un mismo eje cartesiano, la evolución del costo temporal en función del tamaño de
n, de cada una de las funciones halladas en el punto 1.
#5- Realizar un análisis del gráfico anterior y determinar qué algoritmo es asintóticamente más eficiente que los
otros, para distintos tamaños de la entrada. 
"""
#Inciso 4.
n_values = list(range(1, 51))
producto_values = [1 for n in n_values]      # O(1)
suma_values = [n for n in n_values]         # O(n)
incremento_values = [n*n for n in n_values] # O(n^2)

plt.plot(n_values, producto_values, label="Producto O(1)")
plt.plot(n_values, suma_values, label="Suma O(n)")
plt.plot(n_values, incremento_values, label="Incremento O(n^2)")
plt.xlabel("n")
plt.ylabel("Costo (operaciones)")
plt.title("Evolución del costo temporal según n")
plt.legend()
plt.grid(True)
plt.show()
#Inciso 5.
"""
Producto (O(1)) → Siempre más eficiente, sin importar 𝑛.

Suma (O(n)) → Crece linealmente, eficiente para 𝑛 pequeños o medianos.

Incremento (O(n²)) → Ineficiente para valores grandes de 𝑛, 
se vuelve mucho más lento que las otras dos funciones.

Conclusión:
Para entradas grandes, el producto es el más eficiente, seguido de la suma.
El incremento es claramente el menos eficiente debido a su crecimiento cuadrático.
"""