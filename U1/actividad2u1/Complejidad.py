""""
1 -Calcular e indicar el Orden de Complejidad correspondiente a:
a. T1(n)(producto)
b. T2(n)(Suma)
c. T3(n)(Incremento)
2-Ejecute cada código dado agregando un contador en cada uno para contar el tiempo de ejecución
3-Determinar para cada uno de los ítems del punto anterior el valor de n0 a partir del cual se cumple que:
 t(n) <=c.f(n)para algún valor constante de c ϵ R
"""


def producto():
    print("Producto")
    m=0
    c=0

    n = int(input("Ingrese un número:"))
    m = n * n
    c+=1
    print("Resultado del producto:", m)
    
    return c

def Suma():
    print("Suma")
    n = int(input("Ingrese un número: "))
    m = 0
    c=0
    for i in range(n):
        m = m + n
        c+=1
    print("Resultado de suma:", m)
    return c

def incremento():
    print("Incremento")
    n = int(input("Ingrese un número:"))
    m=0
    c=0
    for i in range(n):
        for j in range(n):
            m = m + 1
            c+=1
    print("Resultado del incremento:",m)
    return c
    
# Inciso 2.
def total(p,sum,i):
    print("Tiempo de ejecucion de la funcion Producto:", p)
    print("Tiempo de ejecucion de la funcion suma:", sum)
    print("Tiempo de ejecucion de la funcion incremento:",i)
    
if __name__ == "__main__":
    p=producto()
    s=Suma()
    i=incremento()
    print("\n\n")
    total(p,s,i)

# Inciso 1.   
# Complejidad de la funcion producto: T1(n) = O(1)
# Complejidad de la funcion suma: T2(n) = O(n)
# Complejidad de la funcion incremento: T3(n) = O(n²)

# Inciso 3.
# Producto: t(n)= 1 ≤ c*1 ---> Se cumple para 𝑐≥1. El valor de n0​=1
# Suma: t(n)= n ≤ c*n --> Se cumple para 𝑐≥1. El valor de n0​=1
# Incremento: t(n)= n^2 ≤ c*n^2 --> Se cumple para 𝑐≥1. El valor de n0​=1
# Conclusión: Para estos algoritmos simples, la cota asintótica se cumple desde el primer valor de 𝑛.