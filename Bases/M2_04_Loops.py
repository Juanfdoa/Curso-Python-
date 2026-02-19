# LOOPS -> BUCLES
''' 
# 1. RANGE(start,stop,step)
range(3)
range(3,8)
range(3,8,2)

for numero in range(0, 20, 2):
    print(numero)

# 2. BUCLE FOR
# Se usa para iterar sobre una secuencia
    
dates = [1982,1980,1973]
N = len(dates)

# Iterar la lista
for i in range(N):
    print(dates[i])

for year in dates:
    print(year)


colores = ["rojo", "verde", "azul"]
for color in colores:
    print("Color:", color)

for i, color in enumerate(colores): #i = indice , color = color en cada iteración
    print(i, color)

# 3. BUCLE WHILE
# Se utiliza para ejecutar un conjunto de instrucciones mientras se cumple la condicion dada

# Imprimir números del 1 al 5 usando un bucle while
numero = 1
while numero <= 5:
    print("Número:", numero)
    numero += 1 # incrementa 1 a numero en cada iteracion



'''