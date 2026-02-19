"""
# 1. COMENTARIOS EN PYTHON

# 2. IMPRIMIR HOLA MUNDO
print('Hola Mundo!')   

# 3. VERSION DE PYTHON
import sys             
print(sys.version)

# 4. VARIABLES
saludo = 'Hola'        
nombre = 'Juan'
print(saludo,nombre)  # Imprime las variables declaaradas

fruta = 'Manzana'
print('Me gusta la',fruta) # Imprime cadenas de texto y variables

# 5. EJERCICIO 1
# Solicita al usuario ingresar la longitud y el ancho del rectángulo
longitud = float(input("Ingrese la longitud del rectángulo: "))  # Pedir al usuario (input), float tipo de dato
ancho = float(input("Ingrese el ancho del rectángulo: "))

area = longitud * ancho   # Operacion

print("El área del rectángulo es:", area) # Imprime el resultado

# 6. EJERCICIO 2:
# Imagina que eres un estudiante y deseas calcular tu promedio en tres exámenes que has realizado en una materia específica. 
# Puedes utilizar este programa para ingresar las calificaciones de tus tres exámenes y obtener de inmediato el promedio.

nota1 = float(input("Ingrese la nota # 1: "))
nota2 = float(input("Ingrese la nota # 2: "))
nota3 = float(input("Ingrese la nota # 3: "))

notas = nota1 + nota2 + nota3
promedio = notas / 3

print("El promedio de la materia es:",promedio)

# 7. TIPOS DE DATOS EN PYTHON
# Enteros (int): Numeros enteros tanto positivos como negativos
numero1 = 14
print(numero1)

# Decimales (Float): Numeros decimales tanto positivos como negativos
numero2 = 3.1416
print(numero2)

# Cadena (str): Representa texto
texto = 'Hola Mundo!'
print(texto)

# Booleano (bool): representa verdadero (true) o falso (false)
isOpen = True
print(isOpen)

# Utilizando la funcion incorporada (type) indicara el tipo de expresion
print(type(numero1))
print(type(numero2))
print(type(texto))
print(type(isOpen))

# 8. CONVERTIR TIPOS DE OBJECTOS
# Convertir de entero (int) a decimal (float) => float()
x = 128
print('Numero:', x ,type(x))

x = float(x)
print('Numero:', x ,type(x))

# Convertir de decimal (float) a entero (int) => int()
y = 458.26
print('Numero:', y ,type(y))

y = int(y)
print('Numero:', y ,type(y))

# Convertir cadena (str) a entero (int) o decimales (float,) si la cadena es de numeros
z = '12584'
print('Cadena:',z,type(z))

z = int(z)
print('Numero:',z,type(z))

# Si la cadena no es de numeros se obtendra un error
#a = 'Hola 123'
#print('Cadena:',a,type(a))

#a = int(a)                   # invalid literal for int() with base 10: 'Hola 123'
#print("Result:",a,type(a))  

# Convertir enteros (int) a cadenas (str) => str()
b = 259
print('Numero:',b,type(b))

b = str(b)
print('Cadena:',b,type(b))

# 9. EJERCICIO: TIPOS
# Tipo de datos de 6 / 2
print(type(6/2))   # Float

# Tipo de datos de 6 // 2
print(type(6//2))  # Int

# 10. EXPRESIONES
# Expresiones => Operaciones matematicas (suma, resta, multiplicacion y division) 
valor1 = 5
valor2 = 4

print('Suma:',(valor1 + valor2))
print('Resta:',(valor1 - valor2))
print('Multiplicacion:',(valor1 * valor2))
print('Division:',(valor1 / valor2))
print('Division redondeada:',(valor1 // valor2))

# 11. EJECICIO EXPRESIONES
# Calcular cuantas horas hay en 160 min
minutos = 160
horas = minutos / 60
print(minutos,'minutos son',horas, 'horas')

operacion = 30 + 2 * 60    # Sigue el orden de jerarquia osea primero multiplica 2 * 60 y luego le suma 30 
print(operacion)

operacion2 = (30 + 2) * 60  # Resecta parentensis como prioridad
print(operacion2)

"""
