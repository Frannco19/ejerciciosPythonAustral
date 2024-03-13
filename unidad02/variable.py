#Vamos a ver tipos de datos que puede contener una variable

tipo_texto_string = "Hola Mundo" #si quiero escribir texto uso comillas dobles o simples
num_entero = 3 #si quiero escribir números enteros
num_decimal = 3.5 #si quiero escribir números con decimales separo con punto
num_complejo = 3 + 9j #si quiero escribir números complejos indico con la j la parte imaginaria
tipo_bool = True #si quiero indicar que algo es true o false utilizo un tipo de dato bool

#si quiero agrupar varios datos
lista = [2, "José", 3.5]  #sus datos pueden modificarse
tupla = ("Amarillo", 5, 9.7) #sus datos no pueden modificarse
diccionario = {"Nombre" : 'Juan', "Edad" : 24} #tiene que haber una par "clave":valor

#vamos a imprimir todos esos datos en la terminal haciendo uso del nombre de la variable
#uso la palabra print y entre paréntesis coloco todo lo que quiero que se imprima
#al correr el programa.
print(tipo_texto_string, num_entero, num_decimal, num_complejo, lista, tupla, diccionario)

# Uso el "\n" para que me imprima los datos con un salto de línea
print(tipo_texto_string,"\n", num_entero, "\n", num_decimal, "\n", num_complejo, "\n", lista, "\n", tupla, "\n", diccionario)

#Si quiero saber cuál es el tipo de dato que se encuentra en la variable puedo utilizar la función Type
print(tipo_texto_string, ' su tipo de dato es: ', type(tipo_texto_string), "\n", num_entero, ' su tipo de dato es: ', type(num_entero), "\n", num_decimal, ' su tipo de dato es: ', type(num_decimal),)


#Ejercicio: Ingresá los datos de 5 compañeros e imprimilos
#Nombre, edad, hobby, usá el tipo de dato que creas apropiado.


#¿Qué pasa si tomo una variable que tiene una asignación y le asigno otro valor? veamos
variable_ejemplo = "Hola"
variable_ejemplo = 2

print(variable_ejemplo) #podemos ver en la terminal cuál es el valor que quedó guardado

#Vamos a sumar tipos de datos

valor1 = 4
valor2 = 3.5

total_suma_valores = valor1 + valor2 #en este caso sumo un valor entero con uno decimal y al resultado lo guardo en la variable

print('El total de la suma es: ',total_suma_valores) #al total de la operación anterior la imprimo para conocer el resultado

#¿Qué pasa si quiero sumar datos que no son numéricos?

valor3 = 'Hola '
valor4 = '2023'

suma_string = valor3 + valor4

print('La suma de strings es: ', suma_string)
#Al imprimir el resultado podemos ver que se hace una concatenación de caracteres,
#incluso se respetan los espacios vacíos como el que se encuentra al final del dato de valor3

#Ejercicio: creá una variable para alojar la suma de los nombre de tus 5 compañeros concatenados y otra para la suma de sus edades 
#imprimí los resultados.
