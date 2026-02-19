# CONDICIONALES EN PYTHON

# 1. DECLARACIONES CONDICIONALES -> IF - ELIF - ELSE
# IF -> Se utiliza para ejecutar un bloque de codigo si la condicion es verdadera
edad = 18

if edad >= 18:
    print("Eres mayor de edad.")

# ELIF -> Se utiliza para agregar mas condiciones, ejecuta la primera cuya condicion sea verdadera
puntuacion = 85

if puntuacion >= 90:
    print("Tienes una A.")
elif puntuacion >= 80:
    print("Tienes una B.")
elif puntuacion >= 70:
    print("Tienes una C.")
else:
    print("Tienes una D.")

# ELSE -> Se utiliza si no hay condiciones verdaderas
edad = 16
if edad >= 18:
    print("Eres mayor de edad.")
else:
    print("Eres menor de edad.")

# EJERCICIO 1

temperatura = float(input("Ingresa la temperatura actual en grados Celsius: "))
if temperatura < 10:
    print('Recomendamos usar ropa abrigada')
elif temperatura >= 10 and temperatura < 20:
    print('Recomendamos usar ropa de entretiempo')
elif temperatura >= 20:
    print('Recomendamos ropa ligera')

# EJERCICIO 2

a = float(input("Ingresa el primer número: "))
b = float(input("Ingresa el segundo número: "))
operacion = input("Elige una operación (+, -, *, /): ")
resultado = 0

if operacion == '+':
    resultado = a + b
    print('El resultado de la suma es: ' + resultado)
elif operacion == '-':
    resultado = a - b
    print('El resultado de la resta es: '+ resultado)
elif operacion == '*':
    resultado = a - b
    print('El resultado de la Multiplicacion es: '+ resultado)
elif operacion == '/':
    resultado = a - b
    print('El resultado de la division es: '+ resultado)
else :
    print('La operacion ingresada no es correcta')