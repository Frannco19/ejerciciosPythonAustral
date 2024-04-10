"""
Ejercicio 16

¿Cuál es el problema asociado al siguiente programa? ¿Cómo lo solucionaría?

x = 0
while x < 5:
    print(x)
"""

"""
Ejercicio 17

Escriba un programa que dado un valor umbral, reciba una secuencia de números por input y vaya
sumando los números de la secuencia hasta que la suma alcance el umbral.

Resultados esperados:

umbral = 21
# valores : 3 5 4 4 5
# suma: 21

umbral = 31
# valores 3 5 4 4 5 5 3 5
# suma: 34
"""

"""
Ejercicio 18

Escriba un programa equivalente al siguiente, pero sin usar continue:

suma = 0
i = 1
while i < 100:
    if i % 2 == 0:
        continue
    suma = suma + i

Luego del cambio, reemplazar el bucle while por un bucle for que haga lo mismo.
"""
"""
Ejercicio 19

Escriba un programa que pida al usuario ingresar una frase,
y que luego la muestre por consola caracter por caracter,
y se detenga si alguno de los caracteres es numérico

Ayuda: Utilice la función isnumeric() de los strings.
"""

"""
Ejercicio 20

Escriba un programa que solicite un número entero positivo al usuario y compute la suma de todos
los números naturales menores a él. Este programa debe ser interactivo. Es decir, el programa solicita
un número al usuario, devuelve la suma, y solicita un nuevo número. Esto continúa así hasta que el
usuario ingresa "salir", determinando que el programa debe terminar. Ejemplos:

Ingrese un numero o ' salir ' para terminar : 10
La suma es 45
Ingrese un numero o ' salir ' para terminar : 50
La suma es 1225
Ingrese un numero o ' salir ' para terminar : salir
"""
''' numero = (input("Ingrese un numero o salir para terminar :"))
suma = 0
while numero.lower() != "salir":
    numero = int(numero)
    for i in range(1,numero):
        suma = suma + i
    print(f"La suma de los numeros positivos menores a {numero} es {suma}")
    suma = 0
    numero = (input("Ingrese un numero o salir para terminar :")) '''
""" 
Ejercicio 21

Una mañana ponés un billete en la vereda al lado del Monumento a la Bandera. Cada día volvés y
duplicás la cantidad de billetes, apilándolos prolijamente. ¿Cuánto tiempo pasa antes de que la pila de
billetes sea más alta que la del Monumento? Considere los siguientes valores para comenzar a resolver
el problema:

grosor_billete = 0.11 * 0.001 # grosor de un billete en metros
altura_monumento = 70 # metros

billetes_en_la_pila = 1
dias_transcurridos = 1
"""

"""
Ejercicio 22

Ingrese dos números, compute cuántos múltiplos del primero son menores que el segundo.

a. Implementarla utilizando un bucle for.
b. Implementarla utilizando un bucle while.
"""

"""
Ejercicio 23

Repita el ejercicio de la sucesión de Fibonacci,
pero esta vez vaya computando los cocientes consecutivos de la secuencia `fib_n / fib_n_menos_1`.
Detenga el programa cuando `abs(1.618 - cociente) < 0.001`.
O sea, cuando el cociente se aproxime a φ = 1,618... el número áureo.

Opcional: Cambie los valores iniciales, para que en vez de ser 0 y 1, sean otros.
¿Qué pasa con el número al que el cociente se aproxima?
"""

"""
Ejercicio 24

Escriba un programa que imprima una secuencia infinita de números primos.
Este programa va a colgar su terminal, puede detener el programa utilizando Ctrl + C, o Command + C en Mac.
"""

"""
Ejercicio 25

El problema 3x + 1, o la Conjetura de Collatz, es un problema simple pero no resuelto de la matemática.

Propone lo siguiente:
Sea un proceso iterativo que toma un número natural como entrada.
En cada paso se divide al número en 2 si es par, o se le aplica 3x + 1 si es impar.
Entonces para todo número natural el proceso iterativo llega a 1 eventualmente.

No sabemos si esto es verdad, pero funcionó para todos los números probados. Técnicamente podrían
existir números naturales muy grandes, para los cuáles el proceso no termine. Se han estudiado tanto
la cantidad de pasos que toma para cada número, como el número máximo que alcanza el proceso.

Escriba un programa que simule este problema, o sea, que tome un número como entrada, realice este
proceso, y termine solamente cuando llega a 1. Registre e imprima al término del proceso la cantidad
de pasos y el número máximo alcanzado.
"""