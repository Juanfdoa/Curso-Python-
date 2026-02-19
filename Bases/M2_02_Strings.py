
# 1. CADENAS O STRING
# se pueden usar comillas simples o dobles y almacenar cualquier tipo de texto

cadena1 = 'Hola Mundo'
cadena2 = "Hola Mundo"
cadena3 = 'Hola Mundo 1234'

# 2. INDEXING
# Es un numero que indica la posicion del caracter dentro de la cadena, se usa el []
name = 'Juan Acevedo'
print(name[2])    #a

# 3. INDEXING NEGATIVO
# Similar al indexing pero en negativo y visceversa
print(name[-2])   #d

# 4. LONGITUD -> Tamaño de la cadena
# usando (len) podremos saber el tamaño de la cadena
print(len(name))

# 5. SLICING
# El operador (slice) se puede usar para acceder a subcadenas dentro de una cadena
print(slice(name[5:12]))   #Devuelve la cadena desde la posicion 5 hasta la 12 (Acevedo)

# 6. CONCATENAR STRINGS
# Se usa el operador (+) para concatenar cadenas
lastname = 'Patiño'
fullname = name + ' ' + lastname
print(fullname)

# 7. ESCAPE SEQUENCES
# Las barra invertidas comienzan la secuecia de escape
print(" FUNDAMENTOS IA MINTIC \n CURSO INTRODUCTORIO" ) # \n Salto de linea
print(" FUNDAMENTOS IA MINTIC \t CURSO INTRODUCTORIO" ) # \t Espaciado mayor

# 8. STRING OPERATIONS
# upper -> convierte cadenas de minusculas a mayusculas
minus = 'juan acevedo'
mayus = minus.upper()
print(mayus)

# replace -> reemplaza un segmento de la cadena
a = 'Juan Acevedo'
b = a.replace('Acevedo', 'Patiño')
print(b)

# find -> busca una subcadena, retorna la posicion donde empieza
c = 'Primeros pasos con python'
d = c.find('py')
print(d)