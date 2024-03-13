#Si es necesario yo puedo transformar un tipo de dato, veamos un ejemplo
#En este ejemplo voy a crear un tipo de dato int y lo voy a transformar en float
numero_entro = 32 
numero_decimal = float(numero_entro)

print("Este es el número; ", numero_entro, " Es de tipo: ", type(numero_entro),'\n', 
"Este es el número: ",numero_decimal, " Es de tipo: ", type(numero_decimal))

#Veamos un ejemplo con un dato del tipo string y lo voy a transformar en entero
variable_string = "4"
de_string_a_entero = int(variable_string)

print('Este es el string: ', variable_string, type(variable_string),'\n',
'Transformada a número entero: ', de_string_a_entero, type(de_string_a_entero))

#¿Qué pasa si quiero transformar un string con caracteres alfanuméricos a número?
#string = "Hola 4"
#transformacion = int(string)
#print(transformacion) #saltará un error, porque solo puede transformar números no caracteres alfabéticos

#Hagamos un ejemplo más, esta vez vamos a transformar un tipo de dato numérico a string
numero = 500.67
numero_a_string = str(numero)

print('Este es el número: ', numero, type(numero),'\n',
'Esete es el string: ', numero_a_string, type(numero_a_string))

#Ejercicio: Escribir una variable de tipo string y transformarla en float,
#Escribir una variable de tipo float y transformarla en entero
#imprimir ambos resultados

#¿Para qué necesito transformar los tipos de datos?
#Depende del resultado que quieras obtener de una operación, veamos un ejemplo
precio_producto1 = 3
precio_producto2 = 6
resultado = float(precio_producto1) + float(precio_producto2)
print('El precio total es: ', resultado)

#Si el dato ingresado está en un tipo de dato y quiero realizar una operación con él
año_de_nacimiento = '2015'
año_actual = 2023
edad = año_actual - int(año_de_nacimiento)
print('Su edad es: ', edad)

#Ejercicio: Escribir dos variables de tipo float, sumarlas y asignar ese valor a otra variable convertida
#en entero
#Escribir una variable de tipo entero y una de tipo string, sumarlas para obtener un resultado 
# tipo string y otro resultado tipo entero, asignando esos resultados a otras variables
#imprimir ambos resultados

#¿Qué otros operadores aritméticos además del + - existen?
multiplicación = 3 * 2
print('Resultado de usar el operador * para multiplicar: ',multiplicación)

potencia = 3 ** 2
print('Resultado de usar el operador ** para potencia: ', potencia)

potencia2 = pow(3,2)
print('Resultado de usar el operador pow para potencia: ', potencia2)

division = 30 / 5
print('Resultado de usar el operador /, el resultado siempre es tipo float: ', division)

division_entera = 30 // 4
print('Resultado de usar el operador //, el resultado es tipo entero: ', division_entera)

modulo = 3 % 2
print('Resultado de usar el operador %, nos dá el resto de la división: ', modulo)

#Ejercicio: realizar una operación con cada operador utilizando un número float y ver
#qué resultado se obtiene
