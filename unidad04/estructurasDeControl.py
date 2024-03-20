#########################################################################
# Ejercicio 1: Escriba un programa que pregunte al usuario su edad y muestre
# por pantalla si es mayor de edad o no (18 años)
""" edad = int(input("ingrese su edad:"))
if edad>=18:
    print("sos mayor de edad!")
else:
    print("no sos mayor de edad!") """
#########################################################################
# Ejercicio 2: Escriba un programa que pida al usuario ingresar un año y 
# determine si es bisiesto o no. (Ayuda: Un año es bisiesto si es divisible entre 4, 
# pero no entre 100, o si es divisible entre 400)
""" anio = int(input("ingrese un año : "))
if anio % 4 == 0 and (anio % 100 != 0 or anio % 400 == 0):
	print("Es bisiesto")
else:
	print("No es bisiesto") """
########################################################################
# Ejercicio 3: Escribir un programa para una empresa que tiene salas de juegos
# para todas las edades y quiere calcular de forma automática el precio que 
# debe cobrar a sus clientes por entrar. El programa debe preguntar al usuario 
# la edad del cliente y mostrar el precio de la entrada. Si el cliente es 
# menor de 4 años puede entrar gratis, si tiene entre 4 y 18 años debe pagar 
# $500, y si es mayor de 18 años $1.000
""" edadCkiente = int(input("ingrese la edad para los juegos : "))
if edadCkiente < 4:
    print("entras gratis!")
elif edadCkiente >= 4 and edadCkiente <= 18:
    print("debes pagar $500 dolares")
else:
    print("debes pagar $1000 dolares") """
#########################################################################
# Ejercicio 4: Escribe un programa para saber si el número ingresado es de 1 dígito,
# 2 dígitos, 3 dígitos o más de 3 dígitos
numero = len(int(input("Ingrese un numero : ")))
if len(numero) == 1:
    print("numero de 1 digito!")
elif len(numero) == 2:
    print("numero de 2 digitos")
elif len(numero) == 3:
    print("numero de 3 digitos")
else:
    print("numero de mas de 3 digitos")
########################################################################
# Ejercicio 5: Pedir al usuario que ingrese una oración y una letra, 
# imprimir si la letra se encuentra en la oración y cuántas veces aparece, 
# en el caso de no estar, imprimir que no se encuentra

########################################################################
# Ejercicio 6: Pedir al usuario que ingrese una oración y mostrar por pantalla si tiene 
# más de una palabra y en ese caso, cuántas palabras tiene, de lo contrario, 
# decir que tiene una sola palabra.

########################################################################
# Ejercicio 7: Una pizzería ofrece pizzas vegetarianas y no vegetarianas a sus
# clientes. Todas las pizzas tienen como base muzzarella y se pueden elegir 
# los ingredientes adicionales para cada tipo de pizza, aparecen a continuación.
#   Ingredientes vegetarianos: Pimiento y tofu.
#   Ingredientes no vegetarianos: Peperoni, Jamón y Salmón.
# Escribir un programa que pregunte al usuario si quiere una pizza vegetariana 
# o no, y en función de su respuesta le muestre un menú con los ingredientes 
# disponibles para que elija. Solo se puede elegir un ingrediente. Al final se 
# debe mostrar por pantalla si la pizza elegida es vegetariana o no y todos 
# los ingredientes que lleva.

#########################################################################
# Ejercicio 8: Pida al usuario que ingrese las medidas de tres lados de un triángulo
# e imprima si los lados ingresados corresponden a un triángulo equilátero, 
# un triángulo escaleno o un triángulo isósceles. 
# (Ayuda: los triángulos equiláteros tienen todos sus lados iguales, 
# en los triángulos escalenos los tres lados son distintos y los triángulos isósceles tienen
# solo dos lados iguales)

#########################################################################
# Ejercicio 9: Un vendedor de juguetes ofrece tres tipos de juguetes: 
# juguetes a baterías, juguetes a cuerda y juguetes de carga eléctrica. 
# El vendedor ofrece un descuento del 10 % en los pedidos de juguetes 
# a base de baterías si el pedido supera los 1000 productos. 
# En pedidos de más de 100 para juguetes a cuerda, se otorga un descuento del 5 %, 
# y se otorga un descuento del 10 % en pedidos de juguetes de carga eléctrica 
# superior a 500. Suponga que los códigos numéricos 1, 2 y 3 se usan para
# juguetes con batería, juguetes a cuerda y juguetes de carga eléctrica, respectivamente. 
# Escriba un programa que lea el código del producto y la cantidad del pedido e 
# imprima la cantidad neta por la que el cliente debe pagar después del descuento.


# Ejercicio: Elabore un script en Python que solcite al usuario el ingreso 
# una edad, y muestre un mensaje por consola diciendo "La persona es menor de edad."
# si la edad menor a 18, "La persona es mayor de edad." si la edad 
# está entre 18 y menor a 65, y "La persona es mayor de edad y jubilado." a partir de
# los 65 años de edad.


age = int(input("Ingrese la edad de la persona: "))

if age < 18:
    print("La persona es menor de edad.")
elif age < 65:
    print("La persona es mayor de edad.")
else:
    print("La persona es mayor de edad y jubilado.")
    
    
# Ejercicio: Elabore un script en Python que solcite al usuario el ingreso 
# de 2 números (pueden contener decimales). Sume ambos números y muestre por
# consola el resultado como entero.

numeroUno = input("Ingrese un número decimal: ")
numeroDos = input("Ingrese otro número decimal: ")
numeroUnoFloat = float(numeroUno)
numeroDosFloat = float(numeroDos)
resultado = numeroUnoFloat + numeroDosFloat
print("resultado casteado a entero:  ", int(resultado))
print("resultado sin castear a entero: ", resultado)
print(type(resultado))