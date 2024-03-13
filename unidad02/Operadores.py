#-Operadores de comparación: Se utilizan para comparar dos valores, el resultado va a ser True o False
primer_numero = 5
segundo_numero = 9

primer_segundo_iguales = primer_numero == segundo_numero
print("Los números son iguales? ", primer_segundo_iguales)

nuemeros_distintos = primer_numero != segundo_numero
print("Son los números distintos? ", nuemeros_distintos)

primero_es_mayor = primer_numero > segundo_numero
print("El primer número es mayor? ", primero_es_mayor)

primer_mayor_o_igual = primer_numero >= segundo_numero
print("El primer número es mayor o igual: ", primer_mayor_o_igual)

#Ejercicio: crear dos variables con distintos números y comparar si el primer número
#es menor al segundo, imprimir el resultado.
#Crear dos variables de tipo string y comparar si son iguales o distintas.
#Imprimir el resultado.

#-Operadores lógicos: Se utilizan para evaluar expresiones booleanas
#para este tipo de operadores vamos a utilizar una estructura de control if

#Si yo tengo éstos valores
valor1 = 3
valor2 = 5
valor3 = 9
#Quiero saber si el número del medio (valor2) está entre el primer y último valor
#Utilicemos el operador lógico and
#Vamos a escribir lo siguiente utilizando un if:

if valor1 < valor2 and valor2 < valor3:
    print("El segundo valor está entre el primero y el último valor")
else:
    print("El segundo valor no se encuentra entre el primer y último valor")

#Cómo vamos a leer la estructura anterior:
#SI (if) el primer valor (valor1) es menor
#al segundo valor (valor2) Y (and) el segundo valor (valor2) es menor al tercer valor (valor3) entonces (:)
#que se imprima "El segundo valor está entre el primero y el último valor", de lo contrario (else)
#que se imprima "El segundo valor no se encuentra entre el primer y último valor"

#Vamos a usar ahora el operador or
#Para ello voy a pedir ingresar un número y si ese número es par o mayor de 5
#me lo va a indicar en la terminal

numero = int(input("Ingrese un número: "))
#Con la función input yo espero que el usuario ingrese un valor por teclado
#ese valor siempre va a ser del tipo de dato string, es por eso que yo voy a convertirlo
#al tipo de dato int para trabajar en este ejemplo

if numero % 2 == 0 or numero > 5:
    print("El número ingresado es par o mayor a 5")
else:
    print("El número ingresado es impar y menor a 5")

#Cómo vamos a leer la estructura anterior:
#Si (if) el número ingresado es par (recordemos que el operador % me da el resto de la división,
# si al dividir por 2 el resto es 0, sabemos que el número es par) O (or) mayor a 5 entonces (:)
#que se imprima "El número ingresado es par o mayor a 5", de lo contrario (else)
#que se imprima "El número ingresado es impar y menor a 5"

#Por último vamos a ver el operador not: se utiliza para saber si la expresión que yo le indico
#es falsa, es decir si no se cumple esa condición, veamos
#Voy a pedir que el usuario ingrese una letra
letra = input("ingrese una letra: ")

#Si esa letra no es una vocal entonces se imprime que esa letra es una consonante,
#de lo contrario se imprime que la letra es una vocal
if not(letra == "a" or letra == "e" or letra == "i" or letra =="o" or letra == "u"):
    print("La letra es una consonante")
else:
    print("La letra es una vocal")

#Ejercicio: Pedir ingresar un número y si no es un número impar o menor a 10 imprimir
#"El número ingresado es un número par o es mayor a 10"
#de lo contrario imprimir "El número ingresado es impar o menor a 10"

#Ejercicio: Pedir ingresar 3 números e indicar si el primer número ingresado es menor o igual
# a los otros. Imprimir por pantalla "El número ingresado: " " es menor a los otros números"
# de lo contrario "El número ingresado: " " puede no ser menor a todos los otros número"
