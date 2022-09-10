#||||||||||||||||||||||||||||||||||||-NOTAS DE PYTHON-||||||||||||||||||||||||||||||||||||
#El siguiente programa contiene la mayoria de los conocimientos sobre python 3.
#El programa esta dividido en temas cuyos titulos se encuentran en ingles para facilitar su busqueda.
#Cada tema tiene un codigo de ejemplo junto con un comentario en español que explica el primero.
#El objetivo de esta bibliografia es que sea utilizada como metodo de repaso o como lugar de consulta en caso
#de olvidarnos alguna sintaxis o funcion aprendida previamente
#Si no se cuenta con ningun conocimiento en la materia se recomienda aprender primero en algunos de los sitios 
#detallados en el archivo Bibliografias.txt adjuntado
#Si encuentra algun typo o tiene alguna recomendacion se agradece el feedback en:
#Creado por Valentino Amato Roberts
#Ultima edicion: 18/5/2022
#|||||||||||||||-COMENTARIOS-|||||||||||||||
#Metodo 1 de comentario
'''Metodo 2 de comentario'''
#||||||||||||||||||||||||||||||||||||-DATA TYPES-|||||||||||||||||||||||||||||||||||| 
#|||||||||||||||-INT-|||||||||||||||
a = 1          #Creamos una variable de tipo int con un entero       
b = 2323       #Creamos otra variable de tipo int con otro entero
c = -234       #Creamos otra variable de tipo int con un entero negativo
print(a,b,c)   #Imprimimos las tres variables
print(type(a)) #Imprimimos el tipo de dato de la primera variable (int)
print(type(b)) #Imprimimos el tipo de dato de la segunda variable (int)
print(type(c)) #Imprimimos el tipo de dato de la tercera variable (int)
#|||||||||||||||-FLOAT-|||||||||||||||
a = 1.0        #Creamos una variable de tipo float con un numero con punto decimal   
b = 2323.56    #Creamos otra variable de tipo float con otro numero con punto decimal
c = -234.43    #Creamos otra variable de tipo float con un numero negativo con punto decimal
d = 342e1      #Creamos otra variable de tipo float con un numero multiplicado por 10^1
e = -12e2      #Creamos otra variable de tipo float con un numero negativo multiplicado por 10^2
f = 56e-8      #Creamos otra variable de tipo float con un numero multiplicado por 10^-8
g = -34.4e-4   #Creamos otra variable de tipo float con un numero negativo con punto decimal multiplicado por 10^-4
print(b,f,g)   #Imprimimos algunas de las variables
print(type(a)) #Imprimimos el tipo de dato de la variable a (float)
print(type(a)) #Imprimimos el tipo de dato de la variable f (float)
print(type(g)) #Imprimimos el tipo de dato de la variable g (float)
#|||||||||||||||-COMPLEX-|||||||||||||||
a = 1j         #Creamos una variable de tipo complex con un numero complejo
b =  -4j       #Creamos otra variable de tipo complex con otro numero complejo
c = 4+5j       #Creamos otra variable de tipo complex con otro numero complejo
d = -3.34-0.23j#Creamos otra variable de tipo complex con otro numero complejo
print(b,c,d)   #Imprimimos algunas de las variables
print(type(b)) #Imprimimos el tipo de dato de la variable b (complex)
print(type(c)) #Imprimimos el tipo de dato de la variable c (complex)
print(type(d)) #Imprimimos el tipo de dato de la variable d (complex)
#|||||||||||||||-BOOL-|||||||||||||||
a = True       #Creamos una variable de tipo bool con un estado verdadero
b = False      #Creamos una variable de tipo bool con un estado falso
print(a,b)     #Imprimimos las dos variables
print(type(a)) #Imprimimos el tipo de dato de la variable a (bool)
print(type(b)) #Imprimimos el tipo de dato de la variable b (bool)
#||||||||||||||||||||||||||||||||||||-STRING-|||||||||||||||||||||||||||||||||||| 
String_1 = "Mas"                    #Declaramos el valor del primer string
String_2 = 'que'                    #Declaramos el valor del segundo string
String_3 = "Hola\nMundo\nCruel"     #Primera forma de crear saltos de linea
String_4 = """                      #Segunda forma (Las dos generan la misma salida)
Hola
Mundo
Cruel"""

#Si queremos evitar saltos de lineas entre distintos prints pordemos hacer lo siguiente
print("Hello",end=" ")              #Agregando un segundo argumento: end, podemos envitar que el proximo print aparasca en otra linea
print("World")                      #"World" se imprimira en la misma linea que "Hello" separados por un espacio (end=" ")

Lista1 = ["Hola","Mundo"]           #Declaramos dos o mas strings
String5,String6 = Lista1            #Con ayuda de una lista
print(String_3,String_4)
Frase = (String_1 + " amargo " + String_2 + " la hiel")              #Metodo 1 de concatenacion de Strings
Frase = "%s amargo %s la hiel" %(String_1, String_2)                 #Metodo 2 de concatenacion de Strings
Frase = "{} amargo {} la hiel".format(String_1, String_2)            #Metodo 3 de concatenacion de Strings
Frase = "{a} amargo {b} la hiel".format(b = String_1,a = String_2)   #Metodo 4 de concatenacion de Strings
Frase = f"{String_1} amargo {String_2} la hiel"                      #Metodo 5 de concatenacion de Strings
Frase = Frase.lower()               #Cambia es string poniendo todo en minusculas
Frase = Frase.upper()               #Cambia es string poniendo todo en mayusculas
Frase = Frase.title()               #Cambia es string poniendo en mayuscula la primer letra de cada palabra
Frase = Frase.capitalize()          #Convierte la primera letra del string en mayuscula 
Frase = Frase.strip()               #Remueve las mayusculas, si las hay, de el inicio y el final del string
Frase = Frase.swapcase()            #Convierte todas las letras mayusculas en minusculas y viceversa 

Frase = Frase[0:4]                  #Imprime los caracteres seleccionados del string
Frase = Frase[::-1]                 #invierte el orden del string

Busqueda = Frase.find("Mas")        #Busca en el string la "palabra" entre comillas de izquierda a derecha. Si no lo encuentra, retorna un -1
Busqueda = Frase.rfind("Mas")       #Busca en el string la "palabra" entre comillas de derecha a izquierda. Si no lo encuentra, retorna un -1
Busqueda = Frase.index("A")         #Busca en el string la "palabra" entre comillas de izquierda a derecha. Si no lo encuentra, genera un error
Busqueda = Frase.rindex("A")        #Busca en el string la "palabra" entre comillas de derecha a izquierda. Si no lo encuentra, genera un error

Cuenta = Frase.count("a")           #Cuenta las veces que se repite el caracter o "palabra" entre comillas en el string
Remplazo = Frase.replace("a","b")   #Remplaza todos los caracteres "a" por "b" en el string
Separar = Frase.split(" ")          #Divide el string cada vez que se encuentre el valor entre las comillas

print(Frase.startswith("a"))        #Retorna True si el string empieza con el operando, False si no es asi
print(Frase.endswith("a"))          #Retorna True si el string termina con el operando, False si no es asi

print(Frase.isalnum())              #Retorna True si todos los caracteres del string son numeros, False si no es asi
print(Frase.isalpha())              #Retorna True si todos los caracteres del string pertenecen al alfabeto, False si no es asi
print(Frase.islower())              #Retorna True si todas las letras del string son minusculas, False si no es asi
print(Frase.isupper())              #Retorna True si todas las letras del string son mayusculas, False si no es asi
print(Frase.isspace())              #Retorna True si todo el string esta compuesto por espacion vacios, False si no es asi


print(Frase, Busqueda, Cuenta, Remplazo, Separar)
del Frase                           #Elimina el string
#|||||||||||||||-RAW STRING-|||||||||||||||
#Un raw string o string crudo es un tipo de string en el que podemos usar "\" sin que se generen errores, esto es muy util a la hora
#De indicar un directorio cuando usamos algun tipo de libreria o modulo
print(r"C:\Usuarios\Valentino Amato\Escritorio")#Usamos un raw string para imprimir un directorio
#Tambien tenemos otras opciones para hacer lo mismo:
print("C:\\Usuarios\\Valentino Amato\\Escritorio")
print(r"C:/Usuarios/Valentino Amato/Escritorio")
#||||||||||||||||||||||||||||||||||||-LIST-|||||||||||||||||||||||||||||||||||| 
#Una lista es una secuencia ordenada de elementos facilmente modificable
Lista = ["hola", "mundo", 17, True] #Creamos una lista
Lista2 = ["Hola","Como","Estas?",3] #Creamos otra lista
Lista_numerica2 = [22, 24]          #Creamos otra lista
Lista3 = [["hola","aloh"],[12,34]]  #Creamos una lista que contiene listas dentro
Lista.append("palabra")             #Añade un dato al final de la lista
Lista.insert(2,"cruel")             #Inserta un dato en la lista en la posicion indicada en el primer valor
Lista.remove(True)                  #Borra el dato de la lista que se elija
Lista_pop = Lista.pop(3)            #Toma el dato indicado de la lista y lo almacena en la nueva variable, predeterminadamente toma el ultimo dato(si se dejan los parentesis en blanco)
Lista2.clear()                      #Borra todos los elementos de la lista deseada
Nueva_lista = Lista.copy()          #Creamos una nueva lista con el los elementos de otra, pero que son independientes entre si
Lista.reverse()                     #Invierte el orden de los datos en la lista
print(Lista.count("mundo"))         #Imprime la cantidad de elementos con un valor dado          
print(Lista.index("mundo",0,20))    #Imprime el indice mas bajo en el que se encuentra un elemento dado en una lista
#El primer operando ("mundo") es el dato a buscar, el segundo (0) es opcional y indica desde donde comenzar la busqueda y el tercero (20), tambien opcional, indica donde terminarla  
print(Lista[0])                     #Imprime el dato de la lista que se elija
print(Lista[0:3])                   #Imprime los datos de la lista que se elijan
print(Lista[::-1])                  #Imprime los todos los datos de la lista pero con order invertido
Lista_numerica=[1,3,67,3,124,2,45,7]#Declaramos una lista con valores numericos
Lista_numerica.sort()               #Ordena los numeros de la lista de menor a mayor
Lista_numerica.sort(reverse=True)   #Ordena los numeros de la lista de mayor a menor
Tipo_de_dato= type(Lista[0])        #Devuelve el tipo de dato de un objeto de la lista 
Lista_numerica.append(Lista_numerica2)#Añade al final de la primer lista, la segunda en forma de un solo elemento. La longitud de la lista solo se incrementa en 1
Lista_numerica.extend(Lista_numerica2)#Añade al final de la primer lista, todos los elementos de la segunda por separado. La longitud de la lista se incrementa segun la cantidad de elementos en la segunda lista
a = slice(1,10,2)                    #Creamos un objeto slice que nos sirve para retornar una seccion deseada de una secuencia (lista, tupla, string, etc)
#El primer numero (1) expresa desde donde comienza la seccion, el segundo numero (10) expresa donde termina y el tercero (2) indica el intervalo entre los datos que se toman
print(Lista_numerica[a])             #Imprimimos la seccion deseada de Lista_numerica usando el objeto slice anteriormente creado
print(Lista_numerica[1:10:2])        #Imprimimos la misma seccion de Lista_numerica sin usar el objeto slice
#Los tres numero que se ingresan en la anterior linea tienen el mismo orden y significado que los usados para en la creacion del objeto slice
print(Lista3[1][0])                  #Imprimimos un elemento dentro de una lista que a su vez esta destro de otra lista. El primer numero indica la lista "exterior", y el segundo numero, la "interior"
print(Lista_numerica)                #Imprimimos una lista
print(Lista, Lista_pop, Tipo_de_dato)#Imprimimos el tipo de dato de una lista
#||||||||||||||||||||||||||||||||||||-TUPLE-||||||||||||||||||||||||||||||||||||
#Una tupla es practicamente una lista inmutable
Tupla = (4, "String_x", True, 8)     #Creamos una tupla
print(Tupla[1])                      #Imprimimos un dato de la tupla
print(Tupla[1:4])                    #Imprimimos todos los datos de la tupla que se encuentren entre los dos valores
print(Tupla)                         #Imprimimos la tupla creada
Tupla2 = tuple(("hola",2,5,True))    #Creamos otra tupla usando el metodo tuple
print(Tupla2)                        #Imprimimos la segunda tupla
#||||||||||||||||||||||||||||||||||||-RANGE-||||||||||||||||||||||||||||||||||||
#El tipo de dato range es una secuencia de numeros en cierto rango y toma numeros con un determinado intervalo
#Al igual que los frozensets, este tipo de dato solo puede ser creado mediante un metodo, el metodo range()
#Dicho metodo recibe tres parametros el numero donde empieza la secuencia, el numero donde termina, y el intervalo
#Podemos entender al intervalo como si se debe tomar un numero cada un numero, un numero cada dos, uno cada tres, etc
#Variable = range(inicio, fin, pasos)
r1 = range(3,10,2)  #Creamos un range que contiene la siguiente cadena de numeros: 3,5,7,9
r2 = range(4,12)    #Creamos un range que contiene la siguiente cadena de numeros: 4,5,6,7,8,9,10,11
r3 = range(4)       #Creamos un range que contiene la siguiente cadena de numeros: 0,1,2,3
print(r1,r2,r3)     #Si imprimimos las anteriores variables solo veremos los numeros que forman al range
#Es decir que en ves de verse la secuencia de numeros se ven los numeros correspondientes al inicio, fin y a los pasos del range
#Podemos usar un bucle for para ver la secuencia de numeros:
for _ in r1:        #Recorremos la secuencia de numeros de r1 y la variable "_" toma el valor de cada uno de los numeros de la secuencia
    print(_)        #Imprimimos los numeros de la secuencia
#||||||||||||||||||||||||||||||||||||-DICTIONARIES-|||||||||||||||||||||||||||||||||||| 
#Un diccionario es una tipo de dato mutable pero que a diferencia de una lista que se encuentra indexada por numeros
#el diccionario se encuentra indexado en base a llaves. A cada llave le corresponde un valor
#Las llaves de un diccionario son inmutables y no se puede encontrar duplicador
llaves = ["hola","como","estas"]                        #Creamos una lista que contendra las llaves de un diccionario
valores = ["estoy","muy","bien"]                         #Creamos una lista que contendra los valores de un diccionario
Diccionario = {'a' : "String 1",'b' : "String 2",4 : "Numero",(2,5) : "Tupla"} #Creamos un Diccionario
Diccionario2 = {'d':"valor_d",'e':"valor_c"}            #Creamos otro diccionario
Diccionario['a'] = "valor_a"                            #Modifica el valor de una clave existente
Diccionario['c'] = "valor_c"                            #Si la clave no existe la crea con el valor escrito
Valor = Diccionario['a']                                #Devuelve como resultado el valor de la clave entre los corchetes
Valor = Diccionario.get('x', "No se encontro la clave") #Devuelve como resultado el valor de la clave entre los corchetes, si no lo encuentra devuelve el segundo dato

del Diccionario[4]                                      #Elimina una clave del diccionario
print(Diccionario.pop("a"))                             #Elimina una llave especifica del diccionario y la retorna, si no existe, retorna un error
print(Diccionario.popitem())                            #Elimina el ultimo par llave-valor ingresado y la retorna

New_dict = dict.fromkeys(llaves,valores)                #Crea un diccionario. Recibe dos argumentos, el primero son las llaves y el segundo son los valores (opcional)
New_dict2 = New_dict.copy()                             #Retorna una copia devinculada de un diccionario 

Claves = Diccionario.items()                            #Devuelve las parejas del diccionario
Claves = list(Diccionario.items())                      #Devuelve las parejas del diccionario en forma de lista
Claves = tuple(Diccionario.items())                     #Devuelve las parejas del diccionario en forma de tupla

Claves = Diccionario.keys()                             #Devuelve las llaves del diccionario
Claves = list(Diccionario.keys())                       #Devuelve las llaves del diccionario en forma de lista
Claves = tuple(Diccionario.keys())                      #Devuelve las llaves del diccionario en forma de tupla

Valores = Diccionario.values()                          #Devuelve los valores del diccionario
Valores = list(Diccionario.values())                    #Devuelve los valores del diccionario en forma de lista
Valores = tuple(Diccionario.values())                   #Devuelve los valores del diccionario en forma de tupla

print(Diccionario.setdefault("a","hola"))               #Retorna el valor de la llave indicada en el primer operando ("a")
print(Diccionario.setdefault("v","hola"))               #Si la llave no exite en el diccionario, la crea y le da como valor el segundo operando ("hola").

Diccionario.update(Diccionario2)                        #Añade al primer diccionario el contenido del segundo
Diccionario2.clear()                                    #Elimina todo el contenido del diccionario
print(Valores, Claves, Valor, Diccionario)
#||||||||||||||||||||||||||||||||||||-SETS-|||||||||||||||||||||||||||||||||||| 
#Un set es una secuencia mutable de datos unicos sin orden 
set1 = {"hola",1,2,3}                                    #Creamos un set
set2 = {"hola","chau"}                                   #Creamos otro set
set3 = {1,2,4,2,2}                                       #Creamos otro set
set1.add(True)                                           #Añadimos un dato a el set1
set3.clear()                                             #Borramos todos los elementos del set3
set4 = set1.copy()                                       #Creamos un nuevos set con los elemetos del set1

set3 = set1.difference(set2)	                         #Retorna un set con las diferencias entre dos o mas sets
set3 = set1.difference_update(set2)	                     #Remueve los elementos del set1 que se encuentran en el set2 

set3 = set1.intersection(set2)      	                 #Retorna un set que esta compuesto por la insterseccion de los elementos del set1 y el set2
set3 = set1.intersection_update(set2)	                 #Remueve los elementos del set1 que no se encuentran en el set2 

set3 = set1.isdisjoint(set1)	                         #Retorna True si los dos sets no poseen ninguna interseccion, False si no es asi
set3 = set1.issubset(set2)      	                     #Retorna True si todos los elementos del set1 se encuentran en el set2

set4 = set4.pop()	                                     #Remueve un elemento aleatorio de un set y lo retorna
set3 = set2.remove("hola")                               #Remueve el elemento especificado de el set
set3 = set1.symmetric_difference(set2)	                 #Retorna un set con las diferencias simetricas entre los dos sets
set3 = set1.symmetric_difference_update(set2)            #Retorna None, pero actualiza el contenido del primer set(set1) con las diferencias simetricas entre los sets  
set3 = set1.union(set2)	                                 #Retorna un set que contiene la union de los dos sets 
set3 = set1.update(set2)	                             #Actualiza el set con los datos de un itarable
print(type(set1))                                        #Imprimimos el tipo de dato del set
print(set1)                                              #Imprimimos el set

#||||||||||||||||||||||||||||||||||||-FROZENSETS-||||||||||||||||||||||||||||||||||||                               
#Un frozenset es un set inmutable
#Tienen la caracteristica de que solo pueden ser declarados mediante la funcion frozenset() 
#A diferencia de los anteriores tipos de datos que pueden ser declarados normalmente
Lista = ["Hola","Como","Estas",4,True,4.45]             #Creamos una lista 
FrozenSet = frozenset(Lista)                            #Creamos un frozen set con los elementos de la anterior lista
print(FrozenSet)                                        #Imprimimos el frozenset
print(type(FrozenSet))                                  #Imprimimos el tipo de dato del frozenset
#|||||||||||||||-BYTES-|||||||||||||||
#|||||||||||||||-BYTEARRAY-|||||||||||||||
#|||||||||||||||-MEMORYVIEW-|||||||||||||||
#||||||||||||||||||||||||||||||||||||-IF-ELIF-ELSE-||||||||||||||||||||||||||||||||||||
a = 3
b = 4
c = 5
d = None
if a == 1:         #Si a es igual a uno 
    print(a)       #Imprime a
elif b == 2:       #Si el anterior condicional no se cumple pero b es igual a 2
    print(b)       #Imprime b
elif c == 3:       #Si el anterior condicional no se cumple pero c es igual a 3
    print(c)       #Imprime c
else:              #Si nada de lo anterior se cumple
    print("error") #Imprime "error"
Mensaje = "Hola mundo" if a > 0 else "Adios mundo"#Si a>0 Mensaje = "Hola mundo",de lo contratio Mensaje = "Adios mundo"
print(Mensaje)
if d:              #Si la Variable, String, Lista, Tupla o Diccionario contiene algun dato(No es igual a cero) 
    print(True)    #Implime True
else:              #Si la Variable, String, Lista, etc, no contiene datos, es igual a 0 o a None
    print(False)   #Imprime False
if a and b > 1:    #Si a y b son mas grandes que 1
    print(True)    #Imprime True
if a or b > 1:     #Si a o b es mas grande que 1
    print(True)    #Imprime True
if not a == -3:    #Si a negado (-a) es igual a -3
    print(True)    #Imprime True
#||||||||||||||||||||||||||||||||||||-OPERATORS-||||||||||||||||||||||||||||||||||||
#|||||||||||||||--COMPARISON OPERATORS-|||||||||||||||
# == Igual que
# <  Menor que
# >  Mayor que
# <= Menor o igual que
# >= Mayor o igual que
# != Distinto que
#|||||||||||||||-ARITHMETIC OPERATORS-|||||||||||||||
# +  Suma
# -  Resta
# *  Multiplicacion
# ** Exponente
# /  Division
# // Division entera
# %  Modulo (Devuelve el resto de la division entre los dos operandos)
#|||||||||||||||-LOGICAL OPERATORS-|||||||||||||||
# and Si a y b...
# or  Si a o b...
# not Negador
#|||||||||||||||-ASSIGNMENT OPERATORS-|||||||||||||||
# =   Ejemplo: x = 10    Es lo mismo que: x = 10
# +=  Ejemplo: x += 10   Es lo mismo que: x = x + 10
# -=  Ejemplo: x -= 10   Es lo mismo que: x = x - 10
# *=  Ejemplo: x *= 10   Es lo mismo que: x = x * 10
# /=  Ejemplo: x /= 10   Es lo mismo que: x = x / 10
# %=  Ejemplo: x %= 10   Es lo mismo que: x = x % 10
# //= Ejemplo: x //= 10  Es lo mismo que: x = x // 10
# **= Ejemplo: x **= 10  Es lo mismo que: x = x ** 10
# &   Ejemplo: x &= 10   Es lo mismo que: x = x & 10
# |=  Ejemplo: x |= 10   Es lo mismo que: x = x | 10
# ^=  Ejemplo: x ^= 10   Es lo mismo que: x = x ^ 10
# >>= Ejemplo: x >>= 10  Es lo mismo que: x = x >> 10
# <<= Ejemplo: x <<= 10  Es lo mismo que: x = x << 10
#|||||||||||||||-IDENTITY OPERATORS-|||||||||||||||
# is     Devuelve True si dos variables son el mismo objeto      Ejemplo: a is b
# is not Devuelve True si dos variables no son el mismo objeto   Ejemplo: a is not b
#Devuelve el valor absoluto de un numero
#|||||||||||||||-MEMBERSHIP OPERATORS-|||||||||||||||
# in     Devuelve True si una secuencia con un valor especifico esta presente en un objeto    Ejemplo: a in b
# not in Devuelve True si una secuencia con un valor especifico no esta presente en un objeto Ejemplo: a not in b
#|||||||||||||||-BITWISE OPERATORS-|||||||||||||||
# &  AND                    El operador copia un bit 1 a el resultado si hay un bit 1 en los dos operandos
# |  OR                     El operador copia un bit 1 a el resultado si hay un bit 1 en alguno de los dos operandos
# ^  XOR                    El operador copia un bit 1 a el resultado si hay un bit 1 en solo uno de los dos operandos
# ~  Binary ones complement En muy resumidas cuentas hace el siguiente calculo -a-1, es decir que cambia el signo del operando y le resta 1
# << Binary left shift      Los bits del primer operando se desfasan a la izquierda la cantidad de lugares indicados por el segundo operando
# >> Binary right shift     Los bits del primer operando se desfasan a la derecha la cantidad de lugares indicados por el segundo operando
#EJEMPLOS:
a = 60            # 60 = 0011 1100 
b = 13            # 13 = 0000 1101 
c = 0

# &  AND 
c = a & b   #00111100 & 00001101 = 00001100
#c es igual a 12 que es igual a 0000 1100 en binario

# |  OR
c = a | b   #00111100 | 00001101 = 00001100     
#c es igual a 61 que es igual a 0011 1101 en binario 

# ^  XOR
c = a ^ b   #00111100 ^ 00001101 = 00110001       
#c es igual a 49 que es igual a 0011 0001 en binario

# ~  Binary ones complement
c = ~a      #-00111100 -1 = -0b111101   
#c es igual a -61 que es igual a -0b111101 en binario

# << Binary left shift
c = a << 2  #00111100 << 2 = 11110000      
#c es igual a 240 que es igual a 1111 0000

# >> Binary right shift
c = a >> 2  #00111100 >> 2 = 00001111    
#c es igual a 15 que es igual a 0000 1111 en binario

#||||||||||||||||||||||||||||||||||||-WHILE-||||||||||||||||||||||||||||||||||||
Contador = 0                       #Creamos una variable para contar las iteraciones de un bucle
A = 1                              #Creamos una variable con un entero
B = 1                              #Creamos una variable con un entero
Bandera = True                     #Creamos una variable booleana
while Contador < 15:               #Mientras Contador sea menor a 15
    Contador += 1                  #Contador = Contador + 1
    print(Contador)                #Imprimimos contador
    if Contador == 10:             #Si contador es igual a 10
        print("CONTADOR = 10")     #Imprimimos "Contador = 10"
        continue                   #Continuamos con el while
    if Contador == 13:             #Si contador es igual a 13
        print("Contador = 13")     #Imprimimos "Contador = 13"
        break                      #Terminamos el while
else:                              #Si Contador es mayor a 15
    print("Fin del While")         #Imprimimos "Fin del While" y terminamos el while
#Nota: a += 1 es lo mismo que: a = a + 1 | a -= 1 es lo mismo que: a = a - 1
while Bandera:                     #Mientras Bandera sea igual a True
    Contador -= 1                  #Contador = Contador - 1
    print(Contador)                #Imprimimos contador
    if Contador == 10:             #Si contador es igual a 10
        print("CONTADOR = 10")     #Imprimimos "Contador = 10"
        continue                   #Continuamos con el while
    if not Contador:               #Si contador es igual a 0
        Bandera = False            #Bandera es igual a False
else:                              #Bandera es igual a False 
    print("Fin del While")         #Imprimimos "Fin del While" y terminamos el while

#BREAK, CONTINUE AND PASS STATEMENTS
#Los tres declaraciones superiores se utilizan para controlar el comportamiento de bucles, funciones y mas
# BREAK: Termina el bucle en el que se encuentra
# CONTINUE: Ignora todas las intrucciones posteriores y pasa a la proxima iteracion del bucle
# PASS: Se usa cuando se necesita sintacticamente de declaracion que no altere el programa. No hace nada
#A continuacion ejemplos y demostraciones del funcionamiento de los tres

A = 0                      #Cambiamos el valor de la variable A
while True:                #Creamos un bucle while que se ejecuta indefinidamente
    A+=1                   #Incrementamos el valor de A en 1
    if A<5:                #Si A es menor a 5
        print("A",A)       #Imprimimos la letra A y el valor de la variable A
        pass               #Usamos PASS para no hacer nada
        print("pass")      #Imprimimos pass
    elif A<10:             #Si A no es menor a 5 pero es menor a 10
        print("B",A)       #Imprimimos la letra B y el valor de la variable A
        continue           #Usamos CONTINUE para pasar a la siguiente iteracion del bucle
        print("continue")  #Como pasamos a la siguiente iteracion esta linea nunca se va a ejecutar
    elif A<15:             #Si A no es menor a 10 pero es menor a 15
        print("C",A)       #Imprimimos la letra C y el valor de la variable A
        break              #Usamos BREAK para terminar completamente el bucle while
        print("break")     #Como terminamos el bucle esta linea nunca se va a ejecutar
#|||||||||||||||-ITER-|||||||||||||||
lista = [66, "kasdifhqrewihg", True, {3 : "m"}, [4, 5 ,6 ,7 ,8], ("hola", "mundo")] #Creamos una lista que contenga cualquier tipo de datos
a = iter(lista)                    #Transformamos la lista en un objeto que puede ser iterado 
b = iter(lista)                    #Transformamos la lista en otro objeto que puede ser iterado de forma independiente al anterior
print(next(a))                     #Imprimimos el primer objeto de la lista
print(next(a))                     #Imprimimos el segundo objeto de la lista
print(next(b))                     #Imprimimos el primer elemento de la lista
print(next(a))                     #Imprimimos el tercer objeto de la lista
print(next(a))                     #Imprimimos el cuarto objeto de la lista
print(next(b))                     #Imprimimos el segundo objeto de la lista
print(next(a))                     #Imprimimos el cuarto objeto de la lista
print(next(a))                     #Imprimimos el ultimo objeto de la lista
#||||||||||||||||||||||||||||||||||||-FOR-||||||||||||||||||||||||||||||||||||
lista_1 = [1,2,3,4,5,6,7,8,9,0]
for numeros1 in lista_1:           #numeros1 se iguala a todos los elementos en la lista_1 de uno a uno
    print(numeros1)                #Imprimimos cada elemento de la lista
else:                              #Cuando terminamos el loop for
    print("Fin")                   #Imprimimos "Fin"

for numeros2 in lista_1:           #numeros2 recorre todos los elementos en la lista_1
    print(numeros2)                #Imprimimos todos los valores de la lista_1
    if numeros2 == 2:              #Si numeros2 es igual a 2 
        print("if_1")              #Imprimimos "if_1"
        pass                       #Continuamos con normalidad usando "PASS"
    if numeros2 == 4:              #Si numeros2 es igual a 4
        print("if_2")              #Imprimimos "if_2"
        continue                   #Esquivamos el resto del codigo en el loop y continuamos con el proximo ciclo usando "CONTINUE"
    if numeros2 == 8:              #Si numeros2 es igual a 8
        print("if_3")              #Imprimimos "if_3"
        break                      #Terminamos completamente con el loop for sin pasar por el else usando "BREAK"
else:                              #Si el loop for termina sin intervencion de "BREAK"
    print("Fin del for loop")      #Imprimimos "Fin del for loop"
Rango = range(2, 20, 2)            #Creamos una secuencia de numeros usando RANGE, el primer numero indica el numero donde empieza la secuencia
                                   #El segundo numero indica hasta donde se extiende la secuencia.Y el tercero indica cada cuantos caracteres se toma un numero
for numeros3 in Rango:             #Recorremos todos los numeron en Rango
    print(numeros3)                #Los imprimimos
for a,b in enumerate(Rango):       #Recorremos todos los valores en Rango
    print(a,b)                     #Imprimimos el numero de dato que se esta leyendo de la lista
for a,b in enumerate(lista_1):     #"ENUMERATE" devuelve dos variables:En la segunda se escriben los datos de la lista
    print(a,b)                     #Y en la primera se enumeran los datos que se recorren en la lista.Empieza en 0 y va aumentando de uno en uno a medida que se obtienen los datos de la lista en la segunda variable
for c in range(0, len(lista_1)):   #Recorre todos los datos entre 0 y la longitud de la lista
    print(c)                       #Imprimimos los datos
                                   #Notas: "LEN" devuelve la longitud de un string, lista, tupla o diccionario
for a in Diccionario.items():      #Recorremos todos los items del diccionario
    print(a)                       #Los imprimimos           
for a in Diccionario.keys():       #Recorremos todos los keys del diccionario
    print(a)                       #Los imprimimos   
for a in Diccionario.values():     #Recorremos todos los values del diccionario
    print(a)                       #Los imprimimos    
#|||||||||||||||-LIST COMPRENHENSION-|||||||||||||||
lista3 = [None]                    #Creamos una lista vacia con "[]" o [None]
for x in range(50):                #Recorremos todos los valores entre 0 y 49
    lista3.append(x)               #Agregamos los estos valores a lista3
print(lista3)                      #Imprimimos la lista
lista4 = [x for x in range(50) if x % 2 == 0]#Crea una lista con todos los valores pares entre 0 y 49
#NOTA: primero ingresamos la variable de la cual la lista saca los valores, luego el bucle y luego el condicional(opcional)
print(lista4)                      #Imprimimos la lista4 con estos valores
tupla = tuple([x for x in range(50) if x % 2 == 0])#Agregamos "tuple" para transformar el resultado en una tupla
print(tupla)                       #Imprimimos la tupla
Diccionario = {x : y for x, y in enumerate(lista3) if x > 40}#Con enumerate recibimos dos valores y los usamos para crear un diccionario y agregamos un condicional que solo toma los resultados en los que x es mayor a 40
print(Diccionario)                 #Imprimimos el diccionario
#||||||||||||||||||||||||||||||||||||-FUNCTIONS-||||||||||||||||||||||||||||||||||||
a = 5
def potencia():          #Creamos una funcion. Una funcion permite crear una pieza de codigo y ejecutarla  cuando se desee y cunatas veces de desee
    b = a ** 2           #El codigo en la funcion hace la potencia cuadrada de a
    print(b)             #Y lo imprime
potencia()               #Llamamos a la funcion para que se ejecute

def potencia2(a):        #Esta vez ingresamos una variable para poder ingresar datos al llamar a la funcion
    b = a ** 2           #El codigo en la funcion hace la potencia cuadrada de a
    print(b)             #Y lo imprime
potencia2(5)             #Llamamos a la funcion para que se ejecute y le damos un valor a la variable a

def potencia3(a):        #Ingresamos una variable para poder ingresar datos al llamar a la funcion
    b = a ** 2           #El codigo en la funcion hace la potencia cuadrada de a
    return(b)            #Y devolvemos ese dato cuando de llame la funcion
Retorno = potencia3(6)   #Llamamos a la funcion para que se ejecute y le retorne b
print(Retorno)           #Imprimimos el retorno de la funcion

def funcion(b,n,m):      #Ingresamos una multiples variables para poder ingresar datos al llamar a la funcion
    return(b+n+m)        #Y devolvemos la suma de todas las variables
print(funcion(2,4,5))    #Llamamos a la funcion, le damos valores a las variables  y imprimimos el retorno de la funcion

def funcion0(b,n,m):     #Ingresamos una multiples variables para poder ingresar datos al llamar a la funcion
    return(b+n+m)        #Y devolvemos la suma de todas las variables
retorno2 = funcion0(b = 3,n = 8,m = 23)  #Llamamos a la funcion, le damos un dato especifico a casa variable y almacenamos el retorno de la funcion en retorno2
print(retorno2)          #Imprimimos el retorno de la funcion

def funcion1(b,n = 5,m = 10):        #Podemos asignar un valor a la variable para que lo tome en caso de que no se lo demos
    return(b+n+m)                    #Devolvemos la suma de todas las variables
print(funcion1(2,4))                 #Llamamos a la funcion sin darle el valor de la variable m, para que se tome el valor predeterminado ("10")

def funcion2():                      #Creamos una funcion
    return "hola","mundo",True,34    #Retorna una serie de datos prescritos
retorno0 = funcion2()                #Almacenamos todos los datos en una variable 
a = retorno0[0]                      #Guardamos un dato especifico de la variable anterior en un nueva variable
b = retorno0[1]                      #Guardamos otro dato especifico de la variable anterior en otra nueva variable
c = retorno0[2]                      #Guardamos otro dato especifico de la variable anterior en otra nueva variable
d = retorno0[3]                      #Guardamos otro dato especifico de la variable anterior en otra nueva variable
print(a,b,c,d)                       #Imprimimos todos los datos

def funcion3():                      #Creamos una funcion
    return "hola","mundo",True,34    #Retorna una serie de datos prescritos
A,B,C,D = funcion3()                 #Almacenamos cada dato en una variable distinta
print(A,B,C,D)                       #Imprimimos cada dato retornado por separado
y = list(funcion3())                 #Transformamos el retorno de la funcion en una lista 
print(y)                             #Y la imprimimos
x = funcion3()                       #Almacenamos la salida de la funcion en x
print(x)                             #Lo imprimimos en forma de tupla
print(list(funcion3()))              #Imprimimos el retorno de la funcion en forma de lista directamente

def funcion4(funcion):               #Creamos una funcion que recibe el nombre de otra funcion
    print(funcion(4,7,1))            #Ejecuta esta segunda funcion, le da 3 numeros e imprime el retorno
nuevaFuncion = funcion4              #Declaramos que funcion4 tambien responda a nuevaFuncion, es decir, que podemos llamar a la funcion tanto como funcion4, como nuevaFuncion
nuevaFuncion(funcion0)               #Ejecutamos nuevaFuncion(funcion4) y le damos una funcion(funcion0) para que sea ejecutada en la funcion4

def funcion5(z):                     #Creamos una funcion
    return z > 10                    #Si z > 10 retornamos True, si no es asi, retornamos False
print(funcion5(11))                  #Imprimimos el retorno de la funcion para z = 11
#Podemos usar la siguiente sintaxis para funciones cortas y sencillas:
def doblar(num): return num*2        #Cuando se llama a la funcion con un numero devuelve ese numero multiplicado por 2
print(doblar(4))
#||||||||||||||||||||||||||||||||||||-SCOPE-|||||||||||||||||||||||||||||||||||| 
def subrutina():           #3 La funcion se ejecuta
    a = 2                  #4 Declara LOCALMENTE un nuevo valor de a (que solo afecta a la funcion y no cambia el valor de a fuera de esta)
    print(a)               #5 Imprimimos el valor de a LOCAL
    return                 #6 Terminamos la funcion
a = 5                      #1 Le asignamos a la varieble a un valor de 5
subrutina()                #2 Llamamos a la funcion subrutina
print(a)                   #7 Imprimimos el valor de a, que es 5 ya que solo lo cambiamos LOCALMENTE(dentro de la funcion), no GLOBALMENTE

def subrutina1():          #3 Se ejecuta la funcion
    def sub_subrutina():   #6 Se ejecuta la funcion
        print(a1)          #7 Imprime el valor LOCAL de a1(3)
        return             #8 Termina la funcion sub_subrutina
    a1 = 3                 #4 Declaramos un nuevo valor LOCAL de a1
    sub_subrutina()        #5 Llamamos a la funcion sub_subrrutina
    print(a1)              #9 Imprimimos nuevamente el valor LOCAL de a1(3)
    return                 #10 Terminamos la funcion
a1 = 4                     #1 Le asignamos a la varieble a1 un valor de 4
subrutina1()               #2 Llamamos a la funcion subrutina1
print(a1)                  #11 Imprimimos el valor de a1, que es 4 ya que solo lo cambiamos LOCALMENTE(dentro de la funcion), no GLOBALMENTE
#|||||||||||||||GLOBAL|||||||||||||||
a2 = 5                     #1 Declaramos la variable a2 con un valor de 5
def subrutina2():          #3 Se ejecuta la funcion
    global a2              #4 Declaramos la variable a2 como GLOBAL permitiendo alterar el valor de a2 desde dentro de la funcion
    print(a2)              #5 Imprimimos a2(5)
    a2 = 1                 #6 Cambiamos GLOBALMENTE el valor de a2 de 5 a 1
    return                 #7 Terminamos la funcion
subrutina2()               #2 Llamamos a la funcion subrutina2
print(a2)                  #8 Imprimimos el valor de a2(1)
#|||||||||||||||NONLOCAL|||||||||||||||
def subrutina3():          #3 Se ejecuta la funcion
    def sub_subrutina2():  #6 Se ejecuta la funcion
        nonlocal a3        #7 Declaramos a la variable a3 como NO LOCAL, esto nos permite alterar los valores de la variable en niveles superiores sin alterar a las variables globales
        print(a3)          #8 Imprimimos a3(3)
        a3 = 1             #9 Cambiamos el valor de a3 a 1 de manera NO LOCAL
        return             #10 Terminamos la funcion
    a3 = 3                 #4 Le asignamos a a3 un valor LOCAL de 3
    sub_subrutina2()       #5 Llamamos a la funcion sub_subrutina2
    print(a3)              #11 Imprimimos a3 que es igual a 1 ya que fue alterado en un nivel mas bajo de manera NO LOCAL
    return                 #12 Terminamos la funcion
a3 = 4                     #1 Le asignamos a la variable a4 el valor de 4
subrutina3()               #2 Llamamos a la funcion subrutina3
print(a3)                  #13 Imprimimos a3 GLOBAL que sigue siendo igual a 4 ya que no se ve afectado por cambios NO LOCALES en niveles bajos
"""NOTAS: 
Una VARIABLE LOCAL es aquella cuyo ámbito se restringe a la función que la ha declarado. 
Esto implica que esa variable sólo va a poder ser manipulada en dicha sección, y no se podrá hacer referencia fuera de dicha sección.
Una VARIABLE GLOBAL es aquella cuyo ámbito pertenecen al programa principal.
Puede utilizarse en cualquier función que la declare como global.
Una VARIABLE NO LOCAL es aquella que pertenece a un ámbito superior al de la subrutina, pero que no son globales."""
print("-------------------") #1 Imprimimos un separador para distinguir los datos del siguiente ejemplo
def rutina1():               #4 Se ejecuta la funcion
    def rutina2():           #7 Se ejecuta la funcion
        def rutina3():       #10 Se ejecuta la funcion
            nonlocal a3      #11 Declaramos a a3 como una variable NO LOCAL
            print(a3)        #12 Imprimimos el valor de a3(2)
            a3 = 7           #13 Cambiamos el valor de a3 de manera NO LOCAL a 7
            return           #14 Terminamos la funcion     
        a3 = 2               #8 Cambiamos el valor de a3 LOCALMENTE a 2 
        rutina3()            #9 Llamamos a la funcion rutina3()
        print(a3)            #15 Imprimimos el valor de a3, que es 7, por que lo cambiamos NO LOCALMENTE en el punto #13
        return               #16 Terminamos la funcion
    a3 = 3                   #5 Cambiamos el valor de a3 LOCALMENTE a 3 
    rutina2()                #6 Llamamos a la funcion rutina2()
    print(a3)                #17 Imprimimos el valor de a3, que es 3, por que no se vio afectado por el cambio NO LOCAL de la variable en el punto #13
    return                   #18 Terminamos la funcion
a3 = 4                       #2 Declaramos la variable a3 y la igualamos a 4
rutina1()                    #3 Llamamos a la funcion rutina1()
print(a3)                    #17 Imprimimos el valor de a3, que es 4, por que no se vio afectado por el cambio NO LOCAL de la variable en el punto #13  

print("-------------------") #1 Imprimimos un separador para distinguir los datos del segundo ejemplo
def rutina01():              #4 Se ejecuta la funcion
    def rutina02():          #7 Se ejecuta la funcion
        def rutina03():      #10 Se ejecuta la funcion
            global a4        #11 Declaramos a a4 como una variable GLOBAL
            print(a4)        #12 Imprimimos el valor de a4 que es 4, ya que al declarar a4 como GLOBAL, hacemos que el valor de a4 fuera de las funciones(Punto #2, Linea 333) sea el mismo que el que se encuentra dentro de la funcion rutina03 (Punto #10, Linea 320)
            a4 = 7           #13 Cambiamos el valor de a4 de manera GLOBAL a 7
            return           #14 Terminamos la funcion     
        a4 = 2               #8 Cambiamos el valor de a4 LOCALMENTE a 2 
        rutina03()           #9 Llamamos a la funcion rutina03()
        print(a4)            #15 Imprimimos el valor de a4, que es 2, por que lo cambiamos no se vio afectado por al cambio GLOBAL en el punto #13
        return               #16 Terminamos la funcion
    a4 = 3                   #5 Cambiamos el valor de a4 LOCALMENTE a 3 
    rutina02()               #6 Llamamos a la funcion rutina02()
    print(a4)                #17 Imprimimos el valor de a4, que es 3, por que no se vio afectado por el cambio GLOBAL de la variable en el punto #13
    return                   #18 Terminamos la funcion
a4 = 4                       #2 Declaramos la variable a4 y la igualamos a 4
rutina01()                   #3 Llamamos a la funcion rutina01()
print(a4)                    #17 Imprimimos el valor de a4, que es 7, por que se vio afectado por el cambio GLOBAL de la variable en el punto #13  
#|||||||||||||||-ARGUMENTS-|||||||||||||||
#*ARGS (Non-Keyword Arguments)
#Se usan para pasar a una funcion un numero variable de argumentos que se encuentran indexados mediante numeros (Non-Keyword Arguments)
#El siguiente programa realiza una suma de una cantidad n de numeros que se le provean
def suma(*argumentos):              #2 Se ejecuta la funcion.El asterisco antes del argumento permite que ingresen n cantidad de argumentos y se transformen en tupla
    print(argumentos)               #3 Imprime los argumentos que recibio la funcion en forma de tupla
    resultado = 0                   #4 Creamos una variable local para almacenar la suma de los argumentos
    for valor in argumentos:        #5 Creamos un loop for en el que "valor" toma el valor de los argumentos de uno en uno
        resultado += valor          #6 Sumamos cada valor de "valor" a resultado y asi logramos sumar todos los datos del argumento sin importar cuantos sean
    return resultado                #7 Retornamos el resultado de la suma de todos los argumentos
resultado = suma(1,3,5,23,6,8,2)    #1 Llamamos a la funcion suma y le damos una cantidad n de numeros
print(resultado)                    #8 Imprimimos el retorno de la funcion

#**KWARGS (Keyword Arguments)
#Se usan para pasar a una funcion un numero variable de argumentos que se encuentran indexados mediante llaves (Keyword Arguments)
def funcion6 (**diccionario):                   #Se ejecuta la funcion.El doble asterisco antes del argumento permite que ingresen n cantidad de argumentos y se transformen en diccionario
    print(diccionario)                          #Imprimimos los argumentos recibidos en forma de diccionario
    print(f"valor2 es: {diccionario['valor2']}")#Imprimimos el valor de la llave valor2
    for Llaves in diccionario.keys():           #Con un bucle for iteramos todas las llaves de los argumentos recibidos
        print(Llaves)                           #Imprimimos las llaves una por una
    for Valores in diccionario.values():        #Con un bucle for iteramos todos los valores de los argumentos recibidos       
        print(Valores)                          #Imprimimos los valores uno por uno
    for Items in diccionario.items():           #Con un bucle for iteramos todos las items de los argumentos recibidos
        print(Items)                            #Imprimimos los items uno por uno
funcion6(valor1 = "palabra",valor2 = 33,valor3 = True,valor4 = 43)#Llamamos a la funcion6

#Si se quiere usar simultaneamente varios de los argumentos anteriores 
#Se debe seguir un orden especifico:
#Primero se deben declarar los argumentos normales, luego los *ARGS y por ultimo los **KWARGS
def funcion (a,b,c,d=True,*args,**kwargs):#2 Se ejecuta la funcion.El doble asterisco antes del argumento permite que ingresen n cantidad de argumentos y se transformen en diccionario
    print(a)                              #Imprimimos el argumento a que recibe el dato "hola"
    print(b)                              #Imprimimos el argumento b que recibe el dato 12
    print(c)                              #Imprimimos el argumento c que recibe el dato 4
    print(d)                              #Imprimimos el argumento d que recibe el dato False
    print(args)                           #Imprimimos los *args 
    print(kwargs)                         #Imprimimos los **kwargs 
funcion("hola",12,4,False,"arg1","arg2","arg3",valor1 = "palabra",valor2 = 33,valor3 = True,valor4 = 43)#Llamamos a la funcion
#|||||||||||||||-LAMBDAS-|||||||||||||||
#Sirven para realizar funciones simples y cortas
lambda1 = lambda valor5, valor6 : valor5 + valor6 #Creamos una lambda que toma dos valores y los suma
print(lambda1(4,5))                               #Llamamos a la lambda, le damos dos valores y imprimimos su retorno
lambda2 = lambda string : string[::-1]            #Creamos una lambda que toda un string y lo invierte
print(lambda2("automovil"))                       #Llamamos a la lambda, le damos un string y imprimimos su retorno
lambda3 = lambda string0 : "¿"+string0+"?"        #Creamos una lambda que toma un string y le añade signos de pregunta
lambda3 = lambda string0 : "¿{}?".format(string0) #Hacemos lo mismo con ".format"
print(lambda3("Como estas"))                      #Llamamos a la lambda, le damos un string y imprimimos su retorno
lambda4 = lambda : 32                             #Creamos una lambda que retorna un valor especifico(32)
print(lambda4())                                  #Imprimimos el retorno de la funcion
lambda5 = lambda : print("Sin retorno")           #Creamos una lambda que no tiene retorno, sino que ejecuta una accion especifica
lambda5()                                         #Llamamos a la lambda5
lambda6 = lambda num: num%2 != 0                  #Creamos una lambda que analiza si el numero que le damos es inpar o par y devuelve True o False respectivamente en cada caso()
print(lambda6(8))                                 #Imprimimos el retorno de la funcion
#||||||||||||||||||||||||||||||||||||-DECORATORS-|||||||||||||||||||||||||||||||||||| 
#Un decorador es el nombre de un patrón de diseño. Los decoradores alteran de manera dinámica la funcionalidad de una función,
#método o clase sin tener que hacer subclases o cambiar el código fuente de la clase decorada.
def Decorador(funcion):                           #3 Se ejecuta el decorador
    def wrapper ():                               #5 Se ejecuta el wrapper
        print("Antes de ejecutar la funcion ")    #6 Se ejecuta el codigo antes de la ejecucion de la funcion decorada
        funcion()                                 #7 Se ejecuta la funcion decorada
        print("Despues de ejecutar la funcion")   #8 Se ejecuta el codigo despues de la ejecucion de la funcion decorada
    return wrapper                                #4 Llamamos a la funcion anidada wrapper
@Decorador                                        #2 La funcion7 esta decorada
def funcion7():                                   #7 Se ejecuta la funcion decorada
    print("Se ejecuto la funcion7")               #7 Se ejecuta la funcion decorada
funcion7()                                        #1 Llamamos a la funcion7
#Si queremos que la funcion decorada reciba y retorne valores:
def Decorador1(funcion):                          #3 Se ejecuta el decorador
    def wrapper1 (*args, **kwargs):               #5 Se ejecuta el wrapper1
        print("Antes de ejecutar la funcion ")    #6 Se ejecuta el codigo antes de la ejecucion de la funcion decorada
        funcion(*args, **kwargs)                  #7 Llamamos a la funcion decorada(funcion8), con los argumentos correpondientes
        print("Despues de ejecutar la funcion")   #12 Se ejecuta el codigo despues de la ejecucion de la funcion decorada
    return wrapper1                               #4 Llamamos a la funcion anidada wrapper1
@Decorador1                                       #2 La funcion8 esta decorada
def funcion8(a,b):                                #8 Se ejecuta la funcion decorada    
    resultado = a + b                             #9 Sumamos los argumentos a y b y almacenamos el resultado en una variable
    print(resultado)                              #10 Imprimimos la variable 
    print("Se ejecuto la funcion8")               #11 Imprimimos un mensaje indicando que se ejecuto la funcion  
funcion8(20, 30)                                  #1 Llamamos a la funcion8
#Si queremos ingresar un argumento extra:
def Decorador2(Argumento_extra):                  #3 Se ejecuta el decorador
    def wrapper_1 (Funcion_a_decorar):            #5 Se ejecuta el wrapper 1
        def wrapper_2(*args, **kwargs):           #7 Se ejecuta el wrapper 2
            print("Antes de ejecutar la funcion") #8 Imprime un mensaje 
            print(Argumento_extra)                #9 Imprime el argumento extra
            Funcion_a_decorar(*args, **kwargs)    #10 Llamamos a la funcion9 con sus respectivos argumentos
            print("Luego de ejecutar la funcion") #15 Imprimimos un mensaje un vez ejecutada la funcion
        return wrapper_2                          #6 Llamamos al wrapper 2
    return wrapper_1                              #4 Llamamos al wrapper 1
@Decorador2("Argumento extra")                    #2 La funcion 2 se encuentra decorada, llamamos al decorador y le damos un argumento
def funcion9(a,b):                                #11 Se ejecuta la funcion
    resultado = a + b                             #12 La funcion suma sus argumentos y almacena los resultados en una variable
    print(resultado)                              #13 Imprime esa variable
    print("Se ejecuto la funcion9")               #14 Imprime un mensaje
funcion9(20, 30)                                  #1 Llamamos a la funcion9 
#||||||||||||||||||||||||||||||||||||-GENERATORS-||||||||||||||||||||||||||||||||||||
#Un generador se comporta parecido a una lista, en el sentido que puede ser recorrida con un iterador.
#La diferencia es que los valores no están almacenados en una colección, sino que se generan en el momento de uno en uno. 
#Con esto se logra ocupar el mínimo de espacio en la memoria y podemos generar listas de millones de elementos sin necesidad de almacenarlos previamente.
def generador(*args):                             #2 El generador recibe los argumentos y se ejecuta 
    for valor in args:                            #3 Recorre los argumentos recibidos de uno en uno y los guarda en valor
        yield valor + 5                           #4 Envia valor + 5 sin terminar la funcion usando la palabra reservada yield
for valor in generador(0,1,2,3,4,5,6,7,8,9):      #1 Creamos un loop que llama al generador.Una vez ejecutado este recorre los datos que entrega y los guarda de uno en uno en valor
    print(valor)                                  #5 Imprimimos los datos generados de uno en uno
#|||||||||||||||-DOCSTRINGS-|||||||||||||||
#En Python todos los objetos cuentan con una variable especial llamada doc gracias a la que podemos describir para qué sirven y cómo se usan los objetos.
#Estas variables reciben el nombre de docstrings, cadenas de documentación.
def funcion10():                                  #2 Se ejecuta la funcion10
    """Este es el docstring de la funcion10,      #3 Establecemos docstring de la funcion
en el que podemos describir su funcionamiento,
entre otras cosas"""
    print("Este es el codigo de la funcion10")    #4 Imprimimos un mensaje
funcion10()                                       #1 Llamamos a la funcion10              
print(funcion10.__doc__)                          #5 Imprimimos el docstring de la funcion                  
print(funcion10.__name__)                         #6 Imprimimos el nombre  de la funcion
#||||||||||||||||||||||||||||||||||||-MODULES-|||||||||||||||||||||||||||||||||||| 
#Un módulo  permite organizar lógicamente código, agrupando código relacionado dentro de un módulo
#hace el código mas fácil de entender y usar. Un módulo es un objeto de Python con atributos, nombres arbitrarios 
#que puede enlazar y hacer referencia.
#Simplemente, un módulo es no es otra cosa sino un archivo con extensión .py. 
#Un módulo puede definir funciones, clases y variables, también puede incluir código ejecutable.
#De la siguiente manera podemos importar un modulo:
from asyncio import DatagramTransport
import Modulo                                      #Importa todo el modulo
import Modulo as Mi_Modulo                         #Importa todo el modulo y nos permite llamarlo de otra manera
from Modulo import suma                            #Importa una funcion especifica del modulo 
from Modulo import suma as adicion                 #Importa una funcion especifica del modulo con otro nombre
from Modulo import suma,resta,multiplicacion,division#Importa varias funcion del modulo 
from Modulo import (suma,resta,multiplicacion,division)#Importa varias funcion del modulo
from Modulo import *                               #Importa todas las funciones del modulo
Modulo.suma(10,20)                                 #Si importamos el modulo por completo(Ejemplo:linea 444.445) usamos esta sintaxis
suma(10,20)                                        #Si importamos la funcion especifica usamos esta sintaxis
#help(Modulo)                                      #Solicitamos informacion sobre el modulo 
#dir(Modulo)                                       #Muestra los atributos del modulo
#help(division)                                    #Solicitamos informacion sobre una funcion especifica en el modulo
print(Modulo.__doc__)                              #Imprimimos el docstring del modulo
#print(Modulo.__datos__)                           #Imprimimos un dato declarado en el modulo
print(Modulo.__name__)                             #Imprimimos el nombre del modulo
print(variable_x)                                  #Imprimimos una variable declarada en el modulo
if __name__ == "__main__":                         #Si este es el script principal
    print("Este es el script principal")           #Imprimimos "Este es el script principal"
#|||||||||||||||-PACKAGES-|||||||||||||||
#Un paquete es una carpeta que contiene varios modulos, dicha carpeta debe contener, ademas de los modulos 
#Un archivo llamado "__init__.py" en el cual podemos introducir un codigo que sera ejecutado el importar el paquete
from paquete_de_prueba.Modulo1 import funcion_m    #Importamos una funcion que contiene un modulo dentro de nuestro paquete
funcion_m()                                        #Hacemos que la funcion se ejecute
#A su vez pueden haber paquetes dentro de paquetes, llamados subpaquetes
#Estos requieren la misma estructura y tambien necesitan tener una archivo __init__.py
#La sintaxis para acceder a una funcion, clase o variable de un subpaquete es la siguiente:
from paquete_de_prueba.subpaquete_de_prueba.Modulo2 import funcion_a
funcion_a()
#||||||||||||||||||||||||||||||||||||-EXCEPTIONS-|||||||||||||||||||||||||||||||||||| 
#Las excepciones son bloques de código que nos permiten continuar con la ejecución de un programa pese a que ocurra un error.

try:                                               #Intenta correr el siguiente codigo:
    print(10/0)                                    #Intenta imprimir 10/0 lo cual genera un error
except:                                            #Si y solo si se genera un error en el bloque try se ejecuta el bloque except
    print("A ocurrido un error")                   #Imprime que ha habido un error

try:                                               #Intenta correr el siguiente codigo:
    print(10/0)                                    #Intenta imprimir 10/0 lo cual genera un error de tipo ZeroDivisionError
except ZeroDivisionError as error:                 #Si y solo si se genera el error especificado(En este caso: ZeroDivisionError) se ejecuta el bloque except y guarda el error en una variable(En este caso "error")
    print("Error:",error)                          #Imprime hubo un error del tipo ZeroDivisionError

try:                                               #Intenta correr el siguiente codigo:
    print(10/0)                                    #Intenta imprimir 10/0 lo cual genera un error de tipo ZeroDivisionError
except ZeroDivisionError as error:                 #Si y solo si se genera el error especificado(En este caso: ZeroDivisionError) se ejecuta el bloque except y guarda el error en una variable(En este caso "error")
    print("Error:",error)                          #Imprime hubo un error del tipo ZeroDivisionError
except IndexError as error:                        #Si el error no es de tipo ZeroDivisionError, sino IndexError, se ejecuta el bloque except y guarda el error en una variable(En este caso "error")
    print("Error:",error)                          #Imprime hubo un error del tipo IndexError

try:                                               #Intenta correr el siguiente codigo:
    print(10/0)                                    #Intenta imprimir 10/0 lo cual genera un error de tipo ZeroDivisionError
except Exception as error:                         #Si se genera algun error se ejecuta el bloque except y guarda el error en una variable(En este caso "error")
    print("Error:",error)                          #Imprime hubo un error y indica su tipo

try:                                               #Intenta correr el siguiente codigo:
    print(10/2)                                    #Intenta imprimir 10/0 lo cual genera un error de tipo ZeroDivisionError
except ZeroDivisionError as error:                 #Si y solo si se genera el error especificado(En este caso: ZeroDivisionError) se ejecuta el bloque except y guarda el error en una variable(En este caso "error")
    print("Error:",error)                          #Imprime hubo un error del tipo ZeroDivisionError
else:                                              #Si no se ejecuta el bloque except(No hay errores), se ejecuta el bloque else:
    print("No se detectaron errores")              #Imprime que no se detectaron errores

try:                                               #Intenta correr el siguiente codigo:
    print(10/0)                                    #Intenta imprimir 10/0 lo cual genera un error de tipo ZeroDivisionError
except Exception as error:                         #Si se genera cualquier tipo de error se ejecuta el bloque except y guarda el error en una variable(En este caso "error")
   print("Error:",error)                           #Imprime hubo un error del tipo ZeroDivisionError
else:                                              #Si no se ejecuta el bloque except(No hay errores), se ejecuta el bloque else:
    print("No se detectaron errores")              #Imprime que no se detectaron errores
finally:                                           #Independientemente se si hubieron errores o no, una vez que se ejecutan los bloques anteriores, o no, se ejecuta el bloque finally:(Este bloque siempre se ejecuta)
    print("Fin del script")                        #Imprime fin del script
#|||||||||||||||-RAISE-|||||||||||||||
#La declaracion raise() nos permite forzar que ocurra una excepcion determinada.
try:                                               #Intenta correr el siguiente codigo:
    raise SyntaxError("Error de sintaxis")         #Levantamos una excepcion del tipo SyntaxError con un mensaje personalizado
except SyntaxError as SError:                      #Recoge el anterior error y lo guarda como SError
    print(SError)                                  #Imprimimos el error
#||||||||||||||||||||||||||||||||||||-ASSERTIONS-|||||||||||||||||||||||||||||||||||| 
#Las aserciones son un metodo de generar una excepcion cuando una expresion es verdadera, o se cumple cierto
#requisito(segun como se programe la asercion)
#Ademas podemos agregar un texto que se mostrara en el error si se ejecuta la asercion
"""try:                                             #Comentamos el ejemplo para no tener que identar el resto del codigo debido al uso del except para recoger el AssertionError que se genera
    print(1)                                        #Imprime un mensaje
    assert 1 == 2                                   #Creamos una asercion. Como 1 no es igual a 2 crea una excepcion
    print(2)                                        #Esta parte del codigo no se ejecuta ya que el asercion a generado un error
except AssertionError:                              #Usamos except para recojer la excepcion de la asercion y asi continuar con el programa
    i = 0                                           #Declaramos una variable
    while True:                                     #Iniciamos un bucle while
        i += 1                                      #Sumamos 1 a la variable i
        assert i < 9                                #Creamos una asercion que crea un error si i es mayor o igual a 9
        print(i)                                    #Imprimimos el valor de i"""

a = 1                                               #Creamos una variable
b = 2                                               #Creamos otra variable
assert a<b, "a es mas grande que b"                 #Si a es mas grande que b se crea un error y se muestra el mensaje: "a es mas grande que b"

#A continuacion un listado de excepciones que podemos encontrar en python:
#BaseException
#Exception
#ArithmeticError
#FloatingPointError
#OverflowError
#ZeroDivisionError
#AssertionError
#AttributeError
#BufferError
#EOFError
#ImportError
#ModuleNotFoundError
#LookupError
#IndexError
#KeyError
#MemoryError
#NameError
#UnboundLocalError
#OSError
#BlockingIOError
#ChildProcessError
#ConnectionError
#BrokenPipeError
#ConnectionAbortedError
#ConnectionRefusedError
#ConnectionResetError
#FileExistsError
#FileNotFoundError
#InterruptedError
#IsADirectoryError
#NotADirectoryError
#PermissionError
#ProcessLookupError
#TimeoutError
#ReferenceError
#RuntimeError
#NotImplementedError
#RecursionError
#StopIteration
#StopAsyncIteration
#SyntaxError
#IndentationError
#TabError
#SystemError
#TypeError
#ValueError
#UnicodeError
#UnicodeDecodeError
#UnicodeEncodeError
#UnicodeTranslateError
#Warning
#BytesWarning
#DeprecationWarning
#FutureWarning
#ImportWarning
#PendingDeprecationWarning
#ResourceWarning
#RuntimeWarning
#SyntaxWarning
#UnicodeWarning
#UserWarning
#GeneratorExit
#KeyboardInterrupt
#SystemExit
#||||||||||||||||||||||||||||||||||||-CLASSES-|||||||||||||||||||||||||||||||||||| 
#Una clase es una plantilla para la creación de objetos de datos según un modelo predefinido. 
#Las clases se utilizan para representar entidades o conceptos, como los sustantivos en el lenguaje. 
#Cada clase es un modelo que define un conjunto de variables -el estado, y métodos apropiados para operar con dichos datos -el comportamiento.
#Cada objeto creado a partir de la clase se denomina instancia de la clase.
#ATRIBUTOS:A efectos prácticos los atributos no son muy distintos de las variables,
#la diferencia fundamental es que sólo existen dentro del objeto.
#OBJETOS:Son instancias de la clase, y su definicion viene dada por esta.Son independientes, si alteramos un atributo
#de un objeto, los demas objetos no se ven afectados
class Lapicera0:                                   #Creamos una clase
    color = "Transparente"                         #Creamos un atributo(color)  
    color_tinta = "Azul"                           #Creamos otro atributo
    trazo = "Fino"                                 #Creamos otro atributo
    tapa = False                                   #Creamos otro atributo   
Lapicera1 = Lapicera0()                            #Creamos un objeto
Lapicera2 = Lapicera0()                            #Creamos otro objeto
Lapicera3 = Lapicera0()                            #Creamos otro objeto
print(Lapicera1.tapa,Lapicera2.tapa)               #Imprimimos el atributo(tapa) de ambos objetos
Lapicera0.material = None                          #Tambien podemos crear un nuevo atributo desde afuera de la clase
Lapicera3.borrador = None                          #Tambien podemos crear un nuevo atributo desde un objeto afuera de la clase 
Lapicera1.tapa = True                              #Cambiamos el valor del atributo tapa en el objeto Lapicera1
print(Lapicera1.tapa,Lapicera2.tapa)               #Imprimimos el atributo(tapa) de ambos objetos y vemos que el objeto Lapicera2 no se vio afetado por el cambio en Lapicera1 en la linea 529
#METODOS:Son subrutinas cuyo codigo se escribe dentro de una clase.
#Podemos llamarlas desde los objetos
class Lapicera:                                    #Creamos una clase
    color = "Transparente"                         #Creamos un atributo(color)  
    color_tinta = "Azul"                           #Creamos otro atributo
    trazo = "Fino"                                 #Creamos otro atributo
    tapa = False                                   #Creamos otro atributo          
    def tapa1(self):                               #Creamos un metodo, con argumento self para indicarle el objeto que lo esta invocando
        return self.tapa                           #Retorna el valor de tapa y termina la funcion.Usamos self para poder acceder a un atributo desde un metodo
    def escribir(self):                            #Creamos otro metodo, con argumento self para indicarle el objeto que lo esta invocando
        print("Lapicera esta escribiendo")         #Imprime un mensaje
    def guardar(self):                             #Creamos otro metodo, con argumento self para indicarle el objeto que lo esta invocando
        if self.tapa1():                           #Si tapa es igual a True.Usamos self para poder acceder a un metodo desde otro metodo
            print("Lapicera guardada")             #Imprime "Lapicera guardada"
        else:                                      #Si tapa no es igual a True
            print("No hay tapa")                   #Imprime "No hay tapa"
Lapicera1 = Lapicera()                             #Creamos un objeto
print(Lapicera1.tapa)                              #Imprimimos el atributo tapa de Lapicera1
Lapicera1.tapa1()                                  #Llamamos al metodo tapa1
Lapicera1.guardar()                                #Llamamos al metodo guardar
Lapicera1.tapa = True                              #Cambiamos el valor del atributo tapa de Lapicera1
Lapicera1.guardar()                                #Volvemos a llamar a el metodo guardar
Lapicera1.tinta = True                             #Tambien podemos crear un atributo desde un objero fuera de la clase, pero a este solo podra
print(Lapicera1.tinta)                             #Acceder la instancia que lo crea (Lapicera1)
Lapicera.borrador = True                           #Creamos un atributo desde fuera de la clase al que se puede acceder desde todos los objetos
print(Lapicera.borrador)                           #Imprimimos el atributo
Lapicera3 = Lapicera()                             #Cremos otra instancia de la clase
print(Lapicera3.borrador)                          #Imprimimos el anterior atributo desde la nueva instancia
#SELF:En python se tiene herencia múltiple, no siendo posible saber a priori en qué orden buscar
#el método a ejecutar sin conocer la instancia en concreto que lo están invocando. 
#De ahí que sea importante indicar la instancia, por convenio como self.
#Debido a esto, cuando ejecutamos un método desde un objeto (y no desde una clase), enviamos un primer
#argumento implícito que hace referencia al propio objeto.
#|||||||||||||||||||||||||||-MAGIC METHODS-|||||||||||||||||||||||||||
#Los metodos magicos son aquellos que empiezan y terminan con doble guion bajo("__"). Los metodos magucos nos permiten principalmente
#Crear o modificar funcionalidades de una clase, a continuacion vemos algunos:
#|||||||||||||||-__init__-|||||||||||||||
#El método __init__ es un método especial de una clase en Python.
#El objetivo fundamental del método __init__ es inicializar los atributos del objeto que creamos.
#El método __init__ se llama automáticamente al crear un objeto.
class Clase:                                       #Creamos una clase
    def __init__(self):                            #Definimos el metodo __init__
        self.atributo0 = 0                         #Establecemos atributos con valores predeterminados
        self.atributo1 = 1                         #Establecemos atributos con valores predeterminados
        self.atributo2 = 2                         #Establecemos atributos con valores predeterminados
Clase1 = Clase()                                   #Creamos un objeto, que recibe los atributos definidos en el metodo __init__
print(Clase1.atributo0)                            #Imprimimos el valor del atributo0

class Clase0:                                       #Creamos una clase
    def __init__(self,atributo0,atributo1,atributo2):#Definimos el metodo __init__
        self.atributo0 = atributo0                 #Establecemos atributos sin valores(para luego darselos al crear un objeto)
        self.atributo1 = atributo1                 #Establecemos atributos sin valores(para luego darselos al crear un objeto)
        self.atributo2 = atributo2                 #Establecemos atributos sin valores(para luego darselos al crear un objeto)
Clase1 = Clase0(0,1,2)                             #Creamos un objeto y definimos el valor de sus atributos
print(Clase1.atributo0)                            #Imprimimos el valor del atributo0

class Clase2:                                      #Creamos una clase
    def __init__(self,at0=0,at1=1,at2=2):          #Definimos el metodo __init__.Predeterminamos valores para los atributos en caso de que no se brinden al crear el objeto
        self.at0 = at0                             #Establecemos atributos con un valor predeterminado(dado en la linea 592) que se toma solo si no le damos otro al crear un objeto
        self.at1 = at1                             #Establecemos atributos con un valor predeterminado(dado en la linea 592) que se toma solo si no le damos otro al crear un objeto
        self.at2 = at2                             #Establecemos atributos con un valor predeterminado(dado en la linea 592) que se toma solo si no le damos otro al crear un objeto
Clase1 = Clase2(44,45,46)                          #Creamos un objeto y definimos el valor de sus atributos(de no hacerlo se tomarian sus valores predeterminados)
print(Clase1.at0)                                  #Imprimimos el valor del atributo0
#|||||||||||||||-__new__-|||||||||||||||
class Clase25():                                   #Cremos una clase
    def __new__(cls):                              #2-Se ejecuta el metodo __new__
        print("Este metodo se ejecuta primero")    #3-Se imprime un mensaje
        return super().__new__(cls)                
    def __init__(self):                            #5-Se ejecuta el metodo __init__
        print("Este metodo se ejecuta segundo")
objeto6 = Clase25()                                #1-Creamos un objeto
print(objeto6.__new__(Clase25))                    
#|||||||||||||||-__str__ - __repr__-|||||||||||||||
#Al intentar imprimir una instancia de una clase solo nos encontraremos con informacion sobre su lugar en la memoria
#Los metodo magicos __str__ y __repr__  cambian esto al permitirnos ejecutar un codigo cuando se trata de imprimir un objeto de una clase.
#El método __str__ debe usarse para crear los mensajes que serán presentados al usuario final por lo que deben ser fácilmente legibles. 
#Mientras que el método __repr__ se usa para depuración y desarrollo, por lo que sus mensajes ha de ser inequívocos.
class Clase19:                                     #Creamos un clase
    def __str__(self):                             #Creamos un metodo magico __str__
        print("Este metodo se ejecuta cuando")     #Al tratar de imprimir una instacia ya no vemos su lugar en la memoria, sino que se ejecuta 
        return"Intentamos imprimir un objeto"      #El codigo en el metodo y luego retorna un string
objeto3 = Clase19()                                #Cremos un objeto
print(objeto3)                                     #Imprimimos el objeto
print(str(objeto3))                                #Llamamos al metodo __str__
print(objeto3.__str__())                           #Llamamos al metodo __str__

class Clase21:                                     #Creamos un clase
    def __repr__(self):                            #Creamos un metodo magico __repr__
        print("Este metodo se ejecuta cuando")     #Al tratar de imprimir una instacia ya no vemos su lugar en la memoria, sino que se ejecuta 
        return"Intentamos imprimir un objeto"      #El codigo en el metodo y luego retorna un string
objeto4 = Clase21()                                #Cremos un objeto
print(objeto4)                                     #Imprimimos el objeto
print(repr(objeto4))                               #Llamamos al metodo __repr__
print(objeto4.__repr__())                          #Llamamos al metodo __repr__

class Clase22:                                     #Creamos un clase
    def __repr__(self):                            #Creamos un metodo magico __repr__
        return"Se ejecuto el metodo magico __repr__"#Retornamos un string cuando se ejecute el metodo
    def __str__(self):                             #Creamos un metodo magico __str__
        return"Se ejecuto el metodo magico __str__"#Retornamos un string cuando se ejecute el metodo
objeto5 = Clase22()                                #Cremos un objeto
print(objeto5)                                     #Imprimimos el objeto
print(repr(objeto5))                               ##Llamamos al metodo __repr__
print(str(objeto5))                                ##Llamamos al metodo __str__  
#|||||||||||||||-__getattr__ or __getattribute__-|||||||||||||||
#El metodo magico __getattr__ o __getattribute__ nos permite ejecutar un codigo cuando llamamos a un atributo
#Que no existe, y asi evitar que se generen errores.
class Clase20:                                     #Creamos un clase
    def __getattr__(self, nombre):                 #Creamos un metodo magico __getattr__ o __getattribute__
        print("Atributo Inexistente")              #Al tratar de imprimir un atributo inexistente ya no genera un error, sino que ejecuta el codigo en el metodo 
objeto3 = Clase20()                                #Cremos un objeto
print(objeto3.Atributo_Inexistente)                #Tratamos de imprimir un atributo inexistente 
#|||||||||||||||-PRIVATE METHODS AND ATRIBUTES-|||||||||||||||
#Son metodos o atributos a los que solo se pueden desde la clase y no desde una instancia
class Clase3:                                      #Creamos una clase
    def __init__(self,usuario,contraseña):         #Definimos un metodo __init__ para declarar los atributos de los objetos
        self.usuario = usuario                     #Declaramos el atributo "usuario" 
        self.__contraseña = contraseña             #Declaramos el aributo "contraseña" como privado.Esto hace que al intentar acceder a este desde un objeto se genere un error, por ende solo podemos acceder a el desde la clase
    def encriptador(self):                         #Creamos un metodo
        return self.__contraseña[::-1]             #El metodo retorna la contraseña al revez.Esto es posible a pesar de que "contraseña" sea un atributo privado ya que accedemos a el desde dentro de la clase
usuario0 = Clase3("Valentino","12345678")          #Creamos un objeto y definimos el valor de sus atributos
usuario0.__contraseña = "Contraseña"               #No se puede modificar un atributo privado de esta manera, al intentarlo creamos otro atributo totalmente distinto con el valor dado
print(usuario0.__contraseña)                       #Imprimimos el atributo creado en la linea 652
print(usuario0.encriptador())                      #Imprimimos el retorno de la funcion "encriptador"

class Clase4:                                      #Creamos una clase
    def __init__(self,usuario,contraseña):         #Definimos un metodo __init__ para declarar los atributos de los objetos
        self.usuario = usuario                     #Declaramos el atributo "usuario" 
        self.__contraseña = contraseña             #Declaramos el aributo "contraseña" como privado.Esto hace que al intentar acceder a este desde un objeto se genere un error, por ende solo podemos acceder a el desde la clase
    def __encriptador(self):                       #Creamos un metodo privado, que solo puede ser llamado desde la clase
        return self.__contraseña[::-1]             #El metodo retorna la contraseña al revez.Esto es posible a pesar de que "contraseña" sea un atributo privado ya que accedemos a el desde dentro de la clase
    def retorno3(self):                            #Creamos un metodo 
        return self.__encriptador()                #Retorna el retorno del metodo "__encriptador".Esto es posible a pesar de que el metodo "__encriptador" sea privado por que llamamos a la funcion desde un ,metodo dentro de la clase
usuario0 = Clase4("Valentino","12345678")          #Creamos un objeto y definimos el valor de sus atributos
print(usuario0.retorno3())                         #Imprimimos el retorno de la funcion "retorno3"
#NOTA:Un carácter de guión bajo único (_) antes de un nombre se utiliza para especificar que el nombre 
#debe tratarse como una variable, función, método o clases "privado" o "interno"
#|||||||||||||||-PROPERTIES-|||||||||||||||
class Clase6:                                      #Creamos una clase
    def __init__(self,user,password):              #Defimimos un metodo __init__
        self.user = user                           #Inicializa un atributo("user")
        self.__password = password                 #Inicializa un atributo privado("__password")
    @property                                      #Decoramos la metodo password con  @property
    def password(self):                            #Creamos un metodo 
        return self.__password                     #Retorna el valor de __password
objeto0 = Clase6("Valentino","password")           #Creamos un objeto con ciertos atributos
print(objeto0.password)                            #Llamamos al metodo password. El uso del decorador @property nos permite llamarlo como si de un atributo de tratase, es decir, sin tener que usar parentesis luego de el metodo(por lo que podemos escribir "print(objeto0.password)"" en vez de "print(objeto0.password())"")
#|||||||||||||||-CLASSMETHOD-|||||||||||||||
#Nos permite crear un metodo que recibe como argumento la propia clase y puede ser llamado desde esta 
class Clase7:                                      #Creamos una clase
    @classmethod                                   #Decoramos un metodo con @classmethod para hacerlo un metodo de clase
    def Classmethod(cls, numero):                  #El metodo recibe como argumento la clase (cls) y un numero
        return numero ** 2                         #El metodo retorna el cuadrado del numero que recibe
print(Clase7.Classmethod(10))                      #Llamamos al metodo por medio de una clase y le damos un argumento
#|||||||||||||||-STATICMETHOD-|||||||||||||||
#Los metodos estaticos no reciben como argumento la clase ni el objeto.
class Clase8:                                      #Creamos una clase
    @staticmethod                                  #Decoramos un metodo con @staticmethod para hacerlo un metodo de clase
    def Staticmethod(numero):                      #El metodo solo recibe como argumento un numero
        return numero ** 2                         #El metodo retorna el cuadrado del numero que recibe
print(Clase8.Staticmethod(10))                     #Llamamos al metodo por medio de una clase y le damos un argumento
#|||||||||||||||-ISINSTANCE-|||||||||||||||
#La función isinstance() verifica un objeto (primer argumento) es una instancia o subclase de una clase(segundo argumento).
i = 2                                              #Declaramos una variable
print(isinstance(i,int))                           #Imprimimos True si la anterior variable es un numero entero, False si no lo es

j = 2.32                                           #Declaramos una variable
print(isinstance(j,float))                         #Imprimimos True si la anterior variable es un numero decimal, False si no lo es

k = "hola"                                         #Declaramos una variable
print(isinstance(k,(float,int)))                   #Imprimimos True si la anterior variable es un numero entero o decimal, False si no lo es

class Clase5:                                      #Declaramos una clase
    atributo3 = (44,34,67)                         #Declaramos un atributo
objeto = Clase5()                                  #Creamos un objeto
print(isinstance(objeto.atributo3,list))           #Imprimimos True si el atributo es una lista, False si no lo es
print(isinstance(objeto.atributo3,tuple))          #Imprimimos True si el atributo es una tupla, False si no lo es
print(isinstance(objeto.atributo3,dict))           #Imprimimos True si el atributo es un diccionario, False si no lo es
print(isinstance(objeto,Clase5))                   #Imprimimos True si el atributo es una instancia de la clase "Clase5", False si no lo es
#|||||||||||||||-SETTERS-GETTERS-DELETERS-|||||||||||||||
#Los setters, getters y deleters son metodos de una clase que usamos para setear el valor de un atributo, verlo y destruirlo respectivamente

class Empleados:                                   #Creamos una clase 
    def __init__(self, nombre, apellido):          #Cremos un metodo __init__ para poder crear objetos
        self.nombre = nombre                       #Creamos un atributo que contendra el nombre de un empleado
        self.apellido = apellido                   #Creamos un atributo que contendra el apellido de un empleado
    @property                                      #Creamos un getter usando el decorador @property para poder llamar a el metodo como un atributo
    def NombreCompleto(self):                      #Cremos un metodo
        return f"{self.nombre} {self.apellido}"    #El metodo retorna el nombre y apellido del empleado cuando el llamado
    @NombreCompleto.setter                         #Creamos el setter mediante el decorador .setter para poder configurar el nombre completo de un empleado
    def NombreCompleto(self, nombrecompleto):      #Creamos un metodo que recibe el nombre completo del empleado
        nombre, apellido = nombrecompleto.split(" ")#Separamos el nombre completo que recibe el metodo y lo separamos en nombre y apellido
        self.nombre = nombre                       #Actualizamos el valor de nombre
        self.apellido = apellido                   #Actualizamos el valor de apellido
        print("Fullname setted correctly")         #Imprimimos un mensaje
    @NombreCompleto.deleter                        #Creamos el deleter mediante el decorador .deleter para poder eliminar el nombre completo del empleado
    def NombreCompleto(self):                      #Creamos el metodo del deleter, el cual solo recibe self como argumento
        self.nombre = None                         #Eliminamos los datos de nombre
        self.apellido = None                       #Eliminamos los datos de nombre
        print("Fullname deleted correctly")        #Imprimimos un mensaje
Empleado1 = Empleados("Valentino", "Amato")        #Creamos un objeto 
print(Empleado1.nombre)                            #Imprimimos el nombre del empleado1
print(Empleado1.apellido)                          #Imprimimos el apellido del empleado1
print(Empleado1.NombreCompleto)                    #Imprimimos el nombre completo del empleado1
Empleado1.NombreCompleto = ("Roberto Cantos")      #Cambiamos el nombre completo del empleado1 usando el setter
print(Empleado1.nombre)                            #Imprimimos el nuevo nombre del empleado1
print(Empleado1.apellido)                          #Imprimimos el nuevo apellido del empleado1
print(Empleado1.NombreCompleto)                    #Imprimimos el nuevo nombre completo del empleado1
del Empleado1.NombreCompleto                       #Borramos el nombre del empleado1 usando el deleter
print(Empleado1.nombre)                            #Imprimimos el nuevo nombre del empleado1(El cual ha sido borrado por el deleter)
print(Empleado1.apellido)                          #Imprimimos el nuevo nombre del empleado1(El cual ha sido borrado por el deleter)
print(Empleado1.NombreCompleto)                    #Imprimimos el nuevo nombre del empleado1(El cual ha sido borrado por el deleter)
#|||||||||||||||-INHERITANCE-|||||||||||||||
#Cuando tenemos dos o mas clases que contienen mismos atributos y clases usamos la herencia para poder reducir el codigo repetido
#Para esto creamos una clase padre en la que se encuentran atributos y metodos publicos que pueden ser heredados por otras clases hijas
class Animales:                                    #Creamos una primer clase padre de la que se heredaran metodos y atributos PUBLICOS 
    Vida = True                                    #No se puede hacer lo mismo con metodos o atributos privados ya que generara un error
    @property                                      #Creamos una propiedad a la que podran acceder todas las clases que lo hereden
    def Patas(self):                               #Cremos el metodo a decorar
        return True                                #El metodo retorna True cuando es llamado
class Felinos(Animales):                           #Cremos una clase, que en este caso, hereda los atributos y metodos publicos 
    Pelaje = True                                  #De la clase padre: "Animales" (Esto lo hacemos poniendo la clase padre en los 
    @property                                      #Parentesis posteriores a la clase).
    def Uñas_Retractiles(self):                    #Heredar los datos mencionados nos permite tratarlos como si pertenecieran a la clase hija 
        return True                                #Es decir que podemos llamar los metodos y atributos heredaros desde instancias de esta clase
class Gato(Felinos):                               #Creamos una nueva clase llamada "Gato" que hereda los atributos y metodos publicos de la 
    pass                                           #Clase "Felinos".Como "Felinos" es clase hija de "Animales", "Gato" hereda todos los metodos
class Jaguar(Felinos):                             #Y atributos publicos de "Animales" y "Felinos", por lo tanto, puede acceder a estos desde
    pass                                           #Una de sus instancias
Gato1 = Gato()                                     #Cremos una instancia de la clase Gato que puede acceder a todos los atributos y metodos
Jaguar1 = Jaguar()                                 #Heredados de su clase padre ("Felinos") incluyendo los que su padre hereda de su padre ("Animales") 
print(Gato1.Vida,Gato1.Patas)                      #Imprimimos todos los atributos y metodos de las clases "Animales" y "Felinos" desde una instancia
print(Gato1.Pelaje,Gato1.Uñas_Retractiles)         #De la clase hija que los hereda
print(Jaguar1.Vida,Jaguar1.Patas)                  #Imprimimos todos los atributos y metodos de las clases "Animales" y "Felinos" desde una instancia
print(Jaguar1.Pelaje,Jaguar1.Uñas_Retractiles)     #De otra clase hija que los hereda
#|||||||||||||||-MULTIPLE INHERITANCE-|||||||||||||||
#Una clase puede heredar metodos y atributos privados de dos o mas clases padres
class Clase9:                                      #Creamos una clase 
    x1 = 1                                         #Creamos un atributo publico
class Clase10:                                     #Creamos una clase
    y1 = 1                                         #Creamos un atributo publico
class Clase11:                                     #Creamos una clase
    z1 = 1                                         #Creamos un atributo publico
class Clase12(Clase9,Clase10,Clase11):             #Creamos una clase que hereda los metodos y atributos publicos de todas la clases que se
    pass                                           #Escriban entre los parentesis posteriores a la clase
Objeto = Clase12()                                 #Creamos una instancia de la Clase12
print(Objeto.x1,Objeto.y1,Objeto.z1)               #Imprimimos todos los atributos que hereda la Clase12
#|||||||||||||||-SUPER-|||||||||||||||
#La función super() nos permite invocar y conservar un método o atributo de una clase padre (primaria) desde una clase hija (secundaria)
#Sin tener que nombrarla explícitamente. Esto nos brinda la ventaja de poder cambiar el nombre de la clase padre (base) o hija (secundaria)
#Cuando queramos y aún así mantener un código funcional, sencillo  y mantenible.
class Clase23():                                   #Cremos una clase padre
    def __init__(self, x):                         #Creamos un metodo __init__ 
        print("Clase23")                           #Imprimimos un mensaje 
        self.x = x*2                               #Creamos un atributo 
        print(self.x)                              #Imprimimos x
class Clase24(Clase23):                            #Cremos una clase hija, que hereda de la Clase23 
    def __init__(self, y):                         #Creamos un metodo __init__
        self.y = y                                 #Creamos un atributo
        print("Clase24")                           #Imprimimos un mensaje
        super().__init__(y)                        #Llamamos al metodo __init__ mediante super(), evitando nombrar a la clase
        Clase23.__init__(self,y)                   #Esta linea hace lo mismo que la anterior, pero sin usar el metodo super()
objeto = Clase24("String")                         #Padre(Clase23) donde se encuentra el metodo que queremos llamar: Clase23.__init__(self, y)
print(objeto.y,objeto.x)                           #Imprimimos x, y de las clases 23 y 24 respectivamente                       #Imprimimos los atributos del objeto
#|||||||||||||||-OVERRIDE-|||||||||||||||
#La sobrescritura de metodos o override nos permite agregar funcionalidades a un metodo de clase que hereda una clase hija
class Clase13:                                     #6 Si el metodo no se hallase en la Clase15 se buscaria en esta clase
    def Metodo(self):                              #7 Si el metodo se encontrase en esta clase se ejecutaria
        print("Metodo de la Clase13 ejecutado")    #8 Si el metodo no se hallase ni en la Clase15 ni en la Clase13, se buscaria en la Clase14
class Clase14:                                     #9 Si el metodo no se hallase ni en la Clase15 ni en la Clase13, buscaria en esta clase
    def Metodo(self):                              #10 Si el metodo se encontrase en esta clase se ejecutaria
        print("Metodo de la Clase14 ejecutado")    #11 Si el metodo no se hallara en esta ultima clase surgiria un error 
class Clase15(Clase13,Clase14):                    #3 Python busca primero el metodo en la clase a la que pertenece la intancia
    def Metodo(self):                              #4 Si el metodo se encuentra en la clase, lo ejecuta
        print("Metodo de la Clase15 ejecutado")    #5 Si no se encuentra en la clase lo busca en las clases padres de izquierda a derecha (Primero Clase13, Luego Clase14, etc)
Objeto1 = Clase15()                                #1 Cremos una instancia de la Clase15
Objeto1.Metodo()                                   #2 Llamamos al metodo "Metodo" desde la instancia
#Cuando usando herencia, ciertos metodos de distintas clases compraten nombre, Python comienza a buscar ese metodo y una vez que lo encuentra 
#Lo ejecuta. Cabe destacar que solo se ejecuta el primer metodo encontrado, es decir, que en el ejemploo anterior solo se ejecuta el metodo en la Clase15
#Por mas de que herede metodos con el mismo nombre.
#Si deseamos que tambien se ejecuten estos metodos heredados podemos llamarlos desde el metodo que SI se ejecuta
#Y de ese modo añadir una funcionalidad deseada a un metodo heredado:
class Clase16:                                     #6 Accedemos a el metodo mediante la clase
    def Metodo(self):                              #7 Se ejecuta el metodo
        print("Metodo de la Clase16 ejecutado")    #8 Imprime un mensaje
class Clase17:                                     #10 Accedemos a el metodo mediante la clase
    def Metodo(self):                              #11 Se ejecuta el metido
        print("Metodo de la Clase17 ejecutado")    #12 Imprime un mensaje
class Clase18(Clase13,Clase14):                    #3 El metodo se busca en la clase a la que pertenece el objeto
    def Metodo(self):                              #4 El metodo se encientra y se ejecuta
        Clase16.Metodo(self)                       #5 Llamamos a otro metodo con el mismo nombre que se encuentra en la Clase16
        Clase17.Metodo(self)                       #9 Llamamos a otro metodo con el mismo nombre que se encuentra en la Clase17
        print("Metodo de la Clase18 ejecutado")    #13 Imprime un mensaje 
Objeto2 = Clase18()                                #1 Creamos una instancia de una clase
Objeto2.Metodo()                                   #2 Llamamos a un metodo. 
#De esta manera podemos agregar funcionalidades a un metodo heredado como si de un decorador se tratara

#||||||||||||||||||||||||||||||||||||-REGEX-||||||||||||||||||||||||||||||||||||
#Las expresiones regulares (regular expressions) o regex son una secuencia de caracteres
#Usadas para verificar si un patron existe en un string o no
import re                                          #Importamos la libraria re que nos permite usar regex

string1 = "Helicoptero"                            #Creamos un string
string2 = "Heli"                                   #Creamos otro string
 
#Usamos la funcion match para saber si el primer string se encuentra en el segundo
print(re.match(string1,string2))                   #Como el string1(Helicoptero) no se encuentra en el string2(Heli) retorna None
print(re.match(string1,string1))                   #Como el string1(Helicoptero) se encuentra en el string1(Helicoptero) retorna un objeto con informacion

#Usamos la funcion search para buscar una secuencia o un string en otro string
#Usamos la funcion group para conseguir el string coincidente

print(re.search(r"Co.k.e","Cookie").group())       #Busca el primer string en el segundo y si lo encuentra imprime la coincidencia
                                                   #Los puntos en "Co.k.e" conciden con cualquier caracter que no sea un salto de linea (\n)
                                                   
print(re.search(r'^Hola', "Hola mundo").group())   #Busca si el segundo sting comienza con el primero, si es asi imprime la coincidencia                                             
                                                   #El caracter "^" permite buscar si el segundo string comienza con una cierta sentencia

print(re.search(r'mundo$', "Hola mundo").group())  #Busca si el segundo sting termina con el primero, si es asi imprime la coincidencia                                             
                                                   #El caracter "$" permite buscar si el segundo string termina con una cierta sentencia


print(re.search(r'[nmñ]',"nx").group())            #Busca la letra "n", "m" o "ñ", imprime la primera coincidencia que encuentra
                                                   #"[nñm]" coincide con una "n", "m" o "ñ"

print(re.search(r'[492]',"98").group())            #Busca el numero 4,9 o 2 imprime la primera coincidencia que encuentra
                                                   #"[492]" coincide con un 4,9 o 2
                                                   
print(re.search(r'[a-z]',"n").group())             #Busca una letra entre "a" y "z", imprime la primera coincidencia que encuentra
                                                   #"[a-z]" coincide con una letra minuscula entre la a y la z

print(re.search(r'[a-zA-Z0-9]',"n5j7A").group())   #Busca una caracter entre "a" y "z", "A" y "Z" o entre 0 y 9; imprime la primera coincidencia que encuentra
                                                   #"[a-zA-Z0-9]" permite buscar un caracter en una rango de letras en minuscula, en mayuscula y numeros 

print(re.search(r'[^a-z]',"n5j7A").group())        #Busca una caracter que no este entre "a" y "z", imprime la primera coincidencia que encuentra
                                                   #"[^a-z]" coincide con un caracter que no sea una letra minuscula entre la "a" y la "z"

print(re.search(r'[^nmg][2-7]',"n5j7A").group())   #Busca una letra que no sea "n", "m" o "g" que este seguido con un numero entre el 2 y el 7, imprime la primer coincidencia
                                                   #"[^ngm][2-7]" permite buscar una caracter que no sea "n", "m" o "g" que este seguido con un numero entre el 2 y el 7


#El caracter "\" acompañado de ciertas letras forman un metacaracter
print(re.search(r'hola\sjuan',"hola juan").group())         #"\s" concide con un espacio. Entonces "hola\sjuan" concide con "hola juan"

#Si se quiere ignorar el uso del metacaracter, se añade otro "\"
print(re.search(r'hola\\sjuan',"hola\\sjuan").group())      #"\\s" concide con "\s". Entonces "hola\\sjuan" concide con "hola\sjuan"

print(re.search(r'\d peras',"4 peras").group())             #"\d" concide con un numero del 0 al 9. Entonces "\d peras" concide con "4 peras"

print(re.search(r'p\Sras',"peras").group())                 #"\S" concide con cualquier caracter que no sea un espacio. Entonces "p\Sras" concide con "peras"


#|||||-REPETITIONS-|||||
print(re.search(r'4+ peras',"444 peras").group())           #"+" chequea si el caracter anterior aparece una o mas veces empezando de esa posicion.
                                                            #Entonces "4+" coincide con "4", "44", "444", etc.

print(re.search(r'4* peras',"555 peras").group())           #"*" chequea si el caracter anterior aparece cero o mas veces empezando de esa posicion.
                                                            #Entonces "4*" coincide con "", "4", "44", etc.

print(re.search(r'4? peras',"666 peras").group())           #"?" chequea si el caracter anterior aparece cero o una vez empezando de esa posicion.
                                                            #Entonces "4?" coincide con "" y "4".

print(re.search(r'4{3}',"444 peras").group())               #"{x}" chequea si el caracter anterior aparece x veces. 
                                                            #Entonces "4{3}" coincide con "444".

print(re.search(r'4{3,6}',"444 peras").group())             #"{x,y}" chequea si el caracter anterior aparece entre x e y veces. 
                                                            #Entonces "4{3,6}" coincide con "444", "4444", "44444" y "444444"

print(re.search(r'4{3,}',"444 peras").group())              #"{x,}" chequea si el caracter anterior aparece un minimo de x veces. 
                                                            #Entonces "4{3,}" coincide con "444", "4444", "44444", etc.
                                                        
print(re.search(r'4{,3}',"444 peras").group())              #"{,y}" chequea si el caracter anterior aparece un maximo de y veces. 
                                                            #Entonces "4{,3}" coincide con "", "4", "44" y "444".

#Tambien podemos usar lo anterior para repetir metacaracteres:
print(re.search(r'.? peras',"666 peras").group())           #"?" chequea si el caracter anterior aparece cero o una vez empezando de esa posicion.
                                                            #Entonces ".?" coincide con cualquier caracter que no sea un salto de linea (\n) y que aparesca 0 o 1 vez.

print(re.search(r'.* peras',"666 peras").group())           #"*" chequea si el caracter anterior aparece cero o mas veces empezando de esa posicion.
                                                            #Entonces ".*" coincide con cualquier caracter que no sea un salto de linea (\n) y que aparesca 0 o mas veces.

print(re.search(r'.{3} peras',"666 peras").group())         #"{3}" chequea si el caracter anterior aparece exactamente 3 veces empezando de esa posicion.
                                                            #Entonces ".{3}" coincide con cualquier caracter que no sea un salto de linea (\n) y que aparesca 3 veces.

#Se puede anular el efecto de los repetidores y de varios metacaracteres agregando un "\" delande de ellos:
print(re.search(r'4\? peras',"4? peras").group())           #"\" anula el efecto del metacaracter "?".
                                                            #Entonces "4\? peras" coincide con "4? peras".

print(re.search(r'4\{3,6}',"4{3,6}").group())               #"\" anula el efecto del repetidor "{3.6}". 
                                                            #Entonces "4\{3,6}" coincide con "4{3,6}".


#|||||-GROUPING-|||||
#En regex podemos separar en grupos el string coincidente que retorna una busqueda.
#Estos grupos se delimitan mediante el uso de parentesis ()

oracion = "Pepe compra manzanas"                            #Cremos un string en el cual buscaremos concidencias.
x=(re.search(r'(\w+)\s+(\w+)\s+(\w+)', oracion))            #Buscamos en el string tres grupos de letras separados por una cantidad indeterminada de espacios.
                                                            #"\w+" coincide con un string de una o mas letras.
                                                            #"\s+" coincide con uno o mas espacios en blanco.
                                                            #Entonces '(\w+)\s+(\w+)\s+(\w+)' concide con 'Pepe compra manzanas', 'Hola Como Estas', etc.

print(f'La coincidencia completa es: {x.group()}')          #Imprimimos la coincidencia completa: "Pepe compra manzanas"                                
print(f'El primer grupo es: {x.group(1)}')                  #Imprimimos el primer grupo de la coincidencia : "Pepe"                
print(f'El segundo grupo es: {x.group(2)}')                 #Imprimimos el segundo grupo de la coincidencia : "compra"
print(f'El tercer grupo es: {x.group(3)}')                  #Imprimimos el tercer grupo de la coincidencia : "manzanas"

print(f'Imprimimos todos los grupos: {x.groups()}')         #Usamos groups() para imprimir todos los grupos menos el 0
                                                            #Entonces groups() retorna los grupos 1,2 y 3 en una tupla:
                                                            #('Pepe', 'compra', 'manzanas')
                                                    
#El anterior metodo de agrupacion es facil y sencillo.
#Pero puede ser caotico a medida que aumenta el tamaño del codigo y la cantidad de grupos.
#Para solucionar eso podemos asignar NOMBRES a los grupos, en vez de numeros.
#A continuacion se volvera a realizar el ejerplo anterior pero asignando nombres a los grupos:

oracion2 = "Pepe compra manzanas"                            #Cremos un string en el cual buscaremos concidencias.

#En el anterior ejemplo separabamos los grupos mediante parentesis.
#Para asignar nombres, debemos separar los grupos con la siguiente sintaxis: (?P<nombre>...)
#Nombre es el nombre del grupo. Los "..." son remplazados por el patron a buscar
x=(re.search(r'(?P<oracion>(?P<sujeto>\w+)\s+(?P<accion>\w+)\s+(?P<objeto>\w+))', oracion2))     
                                                            #Los grupos creados son identicos a los del ejemplo anterior
                                                            #El grupo "oracion" engloba la coincidencia completa
                                                            #Los grupos "sujeto", "accion" y "objeto" son respectivamente los anteriores grupos 1, 2 y 3.

print(f'La coincidencia completa es: {x.group("oracion")}') #Imprimimos el grupo "oracion": "Pepe compra manzanas"                                
print(f'El primer grupo es: {x.group("sujeto")}')           #Imprimimos el grupo "sujeto" : "Pepe"                
print(f'El segundo grupo es: {x.group("accion")}')          #Imprimimos el grupo "accion": "compra"
print(f'El tercer grupo es: {x.group("objeto")}')           #Imprimimos el grupo "objeto" : "manzanas"


#|||||-GREEDY AND NON-GREEDY-|||||
#Cuando un patron coincide con lo maximo posible en un string se le llama una busqueda codiciosa o greedy match:
#Para hacer una busqueda codiciosa usamos la combinacion de metacaracteres '.*' que coincide con 0 o mas caracteres que no sean espacios.
print(re.search(r'<.*>',"<hola<como>estas>").group())       #'<.*>' busca el string mas grande que se entuentre entre "<" y ">".
                                                            #Entonces '<.*>' coincide con '<hola<como>estas>'.

#Cuando un patron coincide con lo minimo posible en un string se le llama una busqueda no codiciosa o non-greedy match:
#Para hacer una busqueda no codiciosa usamos la combinacion de metacaracteres '.*?' que coincide con 0 o mas caracteres que no sean espacios.
print(re.search(r'<.*?>',"<hola<como>estas>").group())      #'<.*?>' busca el string mas pequeño posible que se entuentre entre la primera aparicion de "<" y  un ">".
                                                            #Entonces '<.*?>' coincide con '<hola<como>'.


#|||||-REGEX FUNCTIONS-|||||
#A continuacion veremos una definicion mas completa de las funciones usadas anteriormente, asi como otras funciones nuevas:

#COMPILE() nos permite crear un objeto o patron regex que podemos buscar en varios strings dinstintos
#Esto lo hace una buena idea cuando tenemos que buscar una expresion muchas veces en un mismo programa

patron = re.compile(r"pepe")                                #Creamos el patron 'pepe' con compile()
secuencia = "pepe trabaja mucho"                            #Creamos un string en el que luego buscaremos un regex o expresion regular
print(patron.search(secuencia).group())                     #Buscamos el objeto regex que creamos en el string secuencia
print(patron.search("pepe esta durmiendo").group())         #De esta manera podemos agilizar la busqueda de un mismo patron en varios strings distintos

#MATCH() busca un patron y retorna la primera ocurrencia en forma de un objeto 'match'
#Busca el patron solo en el inicio del string por lo que si la ocurrencia se encuentra en otra posicion del string
#match() retornara none. Usando .group() podemos transformar el objeto 'match' en un string que contiene la ocurrencia
#Si usamos .group() y no hay ninguna ocurrencia (el retorno es none) ocurrira un error

print(re.match("hola","hola como estas").group())           #Buscamos el patron "hola" en "hola como estas" y usamos .group(). El retorno es 'hola'
print(re.match("hola","como estas hola"))                   #Buscamos 'hola' en 'como estas hola'. Como el patron 'hola' no esta en el inicio del string
                                                            #No hay coincidencia y retorna none. Si entonces usaramos .group() generariamos un error

#SEARCH() busca un patron y retorna la primera ocurrencia en forma de un objeto 'match'
#A diferencia de match(), search() busca el la ocurrencia en todo el string
#Si no hay una coincidencia o match, search() retornara none
#Usando .group() podemos transformar el objeto 'match' en un string que contiene la ocurrencia
#Si usamos .group() y no hay ninguna ocurrencia (el retorno es none) ocurrira un error.

print(re.search("hola","hola como estas").group())           #Buscamos el patron "hola" en "hola como estas" y usamos .group(). El retorno es 'hola'
print(re.search("hola","como estas hola").group())           #Buscamos 'hola' en 'como estas hola'. Como search() busca en todo el string, el retorno es 'hola
print(re.search("chau","como estas hola"))                   #Buscamos 'hola' en 'como estas hola'. Como el patron 'hola' no esta en el string
                                                             #No hay coincidencia y retorna none. Si entonces usaramos .group() generariamos un error

#FINDALL() busca un patron y retorna la todas las ocurrencias en el texto en forma de lista
#A diferencia de match(), findall() busca las ocurrencias en todo el string
#Si no hay una coincidencia o match, findall() retornara una lista vacia 
#Si usamos .group() ocurrira un error.

print(re.findall("hola","hola hola chau"))                   #Buscamos el patron "hola" en "hola hola chau". El retorno es ['hola','hola']
print(re.findall("hola","chau hola hola"))                   #Buscamos 'hola' en 'chau hola hola'. Como findall busca en todo el string, el retorno es ['hola','hola']
print(re.findall("chau","hola hola hola"))                   #Buscamos 'chau' en 'hola hola hola'. Como el patron 'chau' no esta en el string, el retorno es []

#FINDITER() busca un patron y retorna la todas las ocurrencias en el texto 
#A diferencia de findall(), finditer() retorna las ocurrecias en forma de match objects dentro de un iterable 
#Por lo anterior, para ver las ocurrencias individualmente debemos iterar el retorno de finditer()
#Usar finditer() es una buena idea cuando queremos mas informacion que la que entrega findall()
#Los objetos match retornados por finditer() no solo contienen el texto coincidiente 
#Sino que tambien contiene su respectiva posicion en el texto original

a = re.finditer("hola","hola hola chau")                     #Buscamos ocurrencias con finditer y guardamos el retorno en una variable a
for objetosmatch in a:                                       #Iteramos el retorno de finditer que contiene los objetos match correspondientes a las ocurrencias
    print(objetosmatch)                                      #Imprimimos los objetos match de las ocurrencias:
                                                             #<re.Match object; span=(0, 4), match='hola'> <re.Match object; span=(5, 9), match='hola'>

b = re.finditer("hola","chau hola hola")                     #Buscamos ocurrencias con finditer y guardamos el retorno en una variable b
print(next(b))                                               #Iteramos el retorno de finditer y imprimimos el primer objeto match:
                                                             #<re.Match object; span=(5, 9), match='hola'>
print(next(b))                                               #Iteramos el retorno de finditer y imprimimos el segundo objeto match:
                                                             #<re.Match object; span=(10, 14), match='hola'>

c = re.finditer("chau","hola hola hola")                     #Buscamos ocurrencias con finditer y guardamos el retorno en una variable a
for objetosmatch in c:                                       #Iteramos el retorno de finditer que contiene los objetos match correspondientes a las ocurrencias
    print(objetosmatch)                                      #Como no hubo ninguna ocurrencia no se imprime ningun objeto match


#MATCH OBJECTS los objetos match que retornan las funciones match(), search(), finditer(), etc, contienen una variedad de datos:
x=[]                                                         #Cremos una lista donde guardaremos los objetos match que retornara finditer()
y = re.finditer("hola","chau hola hola")                     #Buscamos ocurrencias con finditer y guardamos el retorno en una variable y
for _ in y:                                                  #Iteramos el retorno de finditer que contiene objetos match correspondientes a las ocurrencias
    x.append(_)                                              #Guardamos dichos objetos match en la lista x
print(x)                                                     #Imprimimos la lista

#SPAN() retorna en una tupla la posicion donde inicia y termina una ocurrencia de un objeto match:
print(x[0].span())                                           #Imprimimos la posicion de la ocurrencia del primer match de la lista x: (5, 9)

#STRING retorna el string en el que se busco la ocurrencia de un objeto match: 
print(x[0].string)                                           #Imprimimos el string en el que se busco la ocurrencia del primer match de la lista x: "chau hola hola"

#GROUP() retorna la ocurrencia de un objeto match:
print(x[0].group())                                          #Imprimimos la ocurrencia del primer match de la lista x: "hola"


#EXPAND() sirve para inyectar en un string cualquiera los grupos de una ocurrencia
a = re.search(r"(\d*)\s*(\d*)","234 34")                     #Buscamos coincidencias y las agrupamos
print(a.group())                                             #Imprimimos la concidencia completa
print(a.groups())                                            #Imprimimos todos los grupos

b = a.expand("La concidencia completa es \g<0>, el primer grupo es \g<1>, el segundo es \g<2>")#Usamos expand() para insertar los grupos en un string
                                                             #Los grupos se ingresan en el string usando '\g<x>' donde x es el numero del grupo
print(b)                                                     #Imprimimos el string con los grupos insertados:
                                                             #"La concidencia completa es 234 34, el primer grupo es 234, el segundo es 34"

#SPLIT() sirve para dividir un string mediante el uso de caracteres o patrones
print(re.split("/","hola/como/estas"))                       #Usamos split() para dividir un string cada vez que aparece el caracter "/"
                                                             #split() retorna una lista con cada division realizada: ['hola', 'como', 'estas']
print(re.split("-","hola/como/estas"))                       #Si el caracter o patron buscado no se encuentra en el string
                                                             #split() retorna una lista que contiene el string completo en donde se busco: ['hola/como/estas']

#SUB() busca un caracter o patron en un string, si lo encuentra lo remplaza por otro string
#sub() toma 4 argumentos en el siguiente orden: 
#1-patron a buscar, 2-remplazo, 3-string en el que se busca y 4-banderas
print(re.sub("\s","-","hola como estas"))                    #Usamos sub() para buscar espacios en "hola como estas". Si se encuentran se remplazan por "-"
                                                             #El resultado es "hola-como-estas"            
print(re.sub("X","-","hola como estas"))                     #Usamos sub() para buscar "X" en "hola como estas". Si se encuentran se remplazan por "-"
                                                             #Si no se encuentra "X" no se modifica el string: "hola como estas"       

#SUBN() busca un caracter o patron en un string, si lo encuentra lo remplaza por otro string
#A diferencia de sub(), subn() retorna en una tupla el string modificado y el numero de remplazos realizados  
#La sintaxis es identica a la de sub()
print(re.subn("\s","-","hola como estas"))                   #Usamos subn() para buscar espacios en "hola como estas". Si se encuentran se remplazan por "-"
                                                             #El resultado es la tupla ("hola-como-estas" ,2). Dicha tupla contiene el string modificado y el numero de remplazos             
print(re.subn("X","-","hola como estas"))                    #Usamos subn() para buscar "X" en "hola como estas". Si se encuentran se remplazan por "-"
                                                             #Como no hay "X" en "hola como estas", subn() retorna la tupla ('hola como estas', 0)  

#|||||-COMPILATION FLAGS-|||||
#En regex podemos modificar el comportamiento de una expresion usando una bandera o flag especifica:

#IGNORECASE(I) permite hacer una busqueda que no distinga entre mayusculas y minusculas
print(re.search("HOLA","hola chau",re.IGNORECASE).group())   #Usamos IGNORECASE para realizar una busqueda que no distinga mayusculas de minusculas
                                                             #Como usamos IGNORECASE, "HOLA" coincide con "hola" y viceversa 
print(re.search("HOLA","hola chau",re.I).group())            #Tambien podemos usar la abreviacion de la bandera (I) para obtener el mismo resultado
                                                             #Como usamos IGNORECASE, "HOLA" coincide con "hola" y viceversa 

#DOTALL(S) permite que el metacaracter "." coincida con cualquier caracter y saltos de linea (\n)
print(re.search(".*","hola\nchau",re.DOTALL).group())        #Usamos DOTALL para que el "." coincida con cualquier caracter y saltos de linea (\n)
                                                             #Como usamos DOTALL, ".*" coincide con "hola\nchau" 
print(re.search(".*","hola\nchau",re.S).group())             #Tambien podemos usar la abreviacion de la bandera (S) para obtener el mismo resultado
                                                             #Como usamos DOTALL, ".*" coincide con "hola\nchau"  

#MULTILINE(M) modifica el funcionamiento de los metacaracteres "^" y "$"
#Por defecto "^" busca un patron en el comienzo de un string y "$" lo busca en el final
#Con MULTILINE(M) estos dos metacaracteres tambien buscan  en cada salto de linea:
#"^" busca un patron en el inicio del string y despues de cada salto de linea (\n)
#"$" busca un patron en el final del string y antes de cada salto de linea (\n)
string = "arbol rojo claro\nsilla azul oscuro"               #Creamos un string con un salto de linea

a=re.findall("^\w*",string,re.MULTILINE)                     #Usamos MULTILINE para que "^" tambien busque en los saltos de linea (\n)  
print(a)                                                     #Imprimimos la coincidencia: ['arbol', 'silla']

b=re.findall(r"\w+$",string,re.M)                            #Usamos la abreviacion de MULTILINE(M) para que "$" tambien busque en los saltos de linea (\n)  
print(b)                                                     #Imprimimos la coincidencia: ['claro', 'oscuro']

#VERBOSE(X) permite añadir espacios y comentarios dentro de una expresion regular 
#Al usar VERBOSE(X) se ignoran todos los espacios dentro del patron excepto dentro de metacaracteres o cuando se encuentran luego de una barra (\)
#Tambien se ignorara todo lo que de encuentre entre un "#" (inicio del comentario) y el final de la linea
correos = "Carlos Zurich repara computadoras"

print(re.search(r"""              #Usamos VERBOSE(X) para poder hacer una expresion mas limpia y facil de leer
[A-Z][a-z]+                       #Buscamos una palabra de longitud mayor a cero que empieze con una mayuscula
[ ]                               #Como los espacios son ignorados usamos '[ ]' para poner un espacio en el patron
[A-Z][a-z]+                       #Buscamos una palabra de longitud mayor a cero que empieze con una mayuscula
\                                 #Ponemos otro espacio usando la expresion '\ '
[a-z]+                            #Buscamos una palabra en minuscula de longitud mayor a cero 
""",correos,re.VERBOSE).group())  #El anterior patron imprime la siguiente coincidencia 'Carlos Zurich repara'


correos = "Pedro Trunis come   ravioles"

a=(re.search(r"""                 #Usamos VERBOSE(X) para poder hacer una expresion mas limpia y facil de leer
[a-z]+                            #Buscamos una palabra de longitud mayor a cero que empieze con una mayuscula
[ ]                               #Como los espacios son ignorados usamos '[ ]' para poner un espacio en el patron
[A-Z][a-z]+                       #Buscamos una palabra de longitud mayor a cero que empieze con una mayuscula
\                                 #Ponemos otro espacio mediante '\ '
[a-z]+                            #Buscamos una palabra en minuscula de longitud mayor a cero 
[ ]+                              #Buscamos una cantidad de espacios mayor a cero 
[a-z]+                            #Buscamos una palabra en minuscula de longitud mayor a cero 
""",correos,re.X | re.I).group()) #Mediante el uso de '|' podemos usar varias banderas a la vez. En este caso usamos VERBOSE(X) y IGNORECASE(I)
print(a)                          #Imprimimos la coincidencia del anterior patron: 'Pedro Trunis come   ravioles'


#|||||-LOOKAROUNDS: LOOKAHEAD AND LOOKBEHIND-|||||
#En regex podemos usar lookahead y lookbehind para agregar una condicion en la busqueda de un patron
#Con lookahead podemos hacer que un patron coincida con una parte del string solo si es seguido por otro patron x
#Con lookbehind podemos hacer que un patron coincida con una parte del string solo si antes de este se encuentra otro patron x

#LOOKAHEAD: La sintaxis de lookahead es X(?=Y), donde 'X' es el patron que se busca e 'Y' es la condicion
#Usando lookahead, el patron 'X' coincidira en el string solo si le sigue 'Y':
string1 = "4 casas son mas grandes que 3 apartamentos"        
a = re.search(r"\d(?= apartamentos)",string1)                #Buscamos un digito (0-9) en string1, con la condicion de que ese numero este seguido por " apartamentos"
print(a.group())                                             #Imprimimos la ocurrencia: Un digito seguido por un espacio y la palabra "apartamento" (3)

#LOOKAHEAD NEGATIVO: La sintaxis de lookahead negativo es X(?!Y), donde 'X' es el patron que se busca e 'Y' es la condicion
#Usando lookahead negativo, el patron 'X' coincidira en el string solo si NO le sigue 'Y':
string1 = "hay 4 remeras y 5 pantalones "        
a = re.search(r"\d(?! remeras)",string1)                     #Buscamos un digito (0-9) en string1, con la condicion de que ese numero NO este seguido por " remeras"
print(a.group())                                             #Imprimimos la ocurrencia: Un digito seguido por cualquier cosa que NO sea " remeras" (5)

#LOOKBEHIND: La sintaxis de lookbehind es (?<=Y)X, donde 'X' es el patron que se busca e 'Y' es la condicion
#Usando lookahead, el patron 'X' coincidira en el string solo si se encuentra despues de 'Y':
string1 = "A: 34, B: 76, C: 12"        
a = re.search(r"(?<=A: )\d{2}",string1)                      #Buscamos dos digitos (00-99) en string1, con la condicion de que dichos digitos se encuentren despues de "A: "
print(a.group())                                             #Imprimimos la ocurrencia: Dos digitos que se encuentran despues de "A: " (34)

#LOOKAHEAD NEGATIVO: La sintaxis de lookbehind negativo es (?<!Y)X, donde 'X' es el patron que se busca e 'Y' es la condicion
#Usando lookahead, el patron 'X' coincidira en el string solo si NO se encuentra despues de 'Y':
string1 = "lista 3=(A: 34, B: 76, C: 12)"        
a = re.search(r"(?<![A-Z]: )\d+",string1)                     #Buscamos un digito o mas en string1, con la condicion de que dichos digitos NO se encuentren despues de  "[A-Z]: "
print(a.group())                                              #Imprimimos la ocurrencia: Un digito seguido por cualquier cosa que NO sea "[A-Z]: " (3)


#|||||||||||||||-REGEX METACHARACTERS TABLE-|||||||||||||||
#A continuacion un resumen de los metacaracteres mas usados en regex:

# []  Coincide con los caracteres que especifiquen dentro:  "[am4]"	
# \   Dependiendo de que caracter le siga puede formar un metacaracter o a su vez removerle el significado especial:  "\d"	
# .	  Coincide con cualquier caracter que no sea un salto de linea (\n):  "he..o"	
# ^	  Busca un patron al principio de un string:  "^hello"	
# $	  Busca un patron al fin de un string:  "planet$"	
# *	  Chequea si el anterior caracter se repite cero o mas veces:  "he.*o"	
# +	  Chequea si el anterior caracter se repite una o mas veces:  "he.+o"	
# ?	  Chequea si el anterior caracter se repite cero o una vez:  "hel.?o"	
# {}  Chequea si el anterior caracter se repite un numero dado de veces:  "hel{2}o"	
# |	  Sirve para usar mas de una bandera	
# ()  Sirve para crear grupos al hacer una busqueda 

# \A  Busca un patron al inicio de un string, a diferencia de "^", no se ve afectado por MULTILINE(M):  "\AStart"	
# \b  Busca que los caracteres especificados se encuentren al inicio o al final de una palabra:  "\bstart", "end\b"
# \B  Busca que los caracteres especificados NO se encuentren al inicio o al final de una palabra:  "\bstart", "end\b"	
# \d  Coincide con un caracter que sea un digito (0-9):  "\d"	
# \D  Coincide con un caracter que NO sea un digito (0-9):  "\D"	
# \s  Coincide con un espacio en blanco:  "\s"	
# \S  Coincide con un caracter que NO sea un espacio en blanco:  "\S"	
# \w  Coincide con una letra mayuscula o minuscula (a-z,A-Z):  "\w"	
# \W  Coincide con un caracter que NO sea una letra mayuscula o minuscula (a-z,A-Z):  "\W"	
# \Z  Busca un patron al final de un string, a diferencia de "$", no se ve afectado por MULTILINE(M):  "Spain\Z"


#||||||||||||||||||||||||||||||||||||-BUILT-IN MODULES-||||||||||||||||||||||||||||||||||||
#|||||||||-OS-|||||||||
import os                                   #Importamos la libreria os
os.path.dirname(os.path.realpath(__file__)) #Brinda el directorio en el que se encuentra el ejecutable actual
#os.remove()                                #Elimima el archivo requerido
#os.rmdir()                                 #Elimima la carpeta vacia requerida
#shutil.rmtree()                            #Elimima la carpeta requerida y todo su contenido
#|||||||||-RANDOM-|||||||||
import random                               #Importamos la libreria random
Numero_aleatorio = random.randint(0,20)     #Elige un numero aleatorio entre los valores dados, incluyendolos 
Dato = random.choice(Lista)                 #Elige un dato aleatorio de una lista selecionada 
random.shuffle(Lista)                       #Reordena aleatoriamente los datos de una lista selecionada 
print(Numero_aleatorio,Dato,Lista)          #Imprimimos las variables declaradas
#|||||||||-DATETIME-|||||||||
import datetime                             #Importamos la libreria datetime
x = datetime.datetime.now()                 #Guardamos la fecha actual en una variable
print(x)                                    #Imprimimos la fecha actual

y = datetime.datetime(2022,6,14,7,45,58,263578)#Creamos una nueva fecha
#Los operandos ingresador corresponden a los siguientes datos respectivamente: Año, Mes, Dia, Hora, Minuto, Segundo, Microsegundos
print(y)                                      #Imprimimos la fecha creada

#Podemos usar el metodo strftime() para transformar una fecha a string y en el proceso recortar o modificar algunos de los datos 
print(type(y.strftime("%B")))               #Imprimimos solo el mes de la fecha y

print(datetime.datetime.now().strftime("%A"))#Imprimimos el dia de la semana actual
#Strftime recibe un operando que determina los datos de la fecha que se retornan
#A continuacion todos los operandos disponibles:
#OPERANDO        FUNCION                                               EJEMPLO
# %a	  Weekday, short version	                                    Wed	
# %A	  Weekday, full version	                                        Wednesday	
# %w	  Weekday as a number 0-6, 0 is Sunday	                        3	
# %d	  Day of month 01-31	                                        31	
# %b	  Month name, short version	                                    Dec	
# %B	  Month name, full version          	                        December	
# %m	  Month as a number 01-12	                                    12	
# %y	  Year, short version, without century	                        18	
# %Y	  Year, full version	                                        2018	
# %H	  Hour 00-23	                                                17	
# %I	  Hour 00-12	                                                05	
# %p	  AM/PM	                                                        PM	
# %M	  Minute 00-59	                                                41	
# %S	  Second 00-59                      	                        08	
# %f	  Microsecond 000000-999999         	                        548513	
# %z	  UTC offset	                                                +0100	
# %Z	  Timezone	                                                    CST	
# %j	  Day number of year 001-366        	                        365	
# %U	  Week number of year, Sunday as the first day of week, 00-53	52	
# %W	  Week number of year, Monday as the first day of week, 00-53	52	
# %c	  Local version of date and time	                            Mon Dec 31 17:41:00 2018	
# %C	  Century	                                                    20	
# %x	  Local version of date	                                        12/31/18	
# %X	  Local version of time                                     	17:41:00	
# %G	  ISO 8601 year	                                                2047
# %u	  ISO 8601 weekday (1-7)	                                    1	
# %V	  ISO 8601 weeknumber (01-53)	                                01

#|||||||||-MATH-|||||||||
import math             #Importamos el modulo math
x = 4.5                 #Creamos una variable de tipo float
y = -3.5                #Creamos una variable de tipo float
z = 3                   #Creamos una variable de tipo int
a = -5                  #Creamos una variable de tipo int

print(math.ceil(x))     #CEIL() retorna el numero entero superior mas proximo a la variable x. (5)
print(math.floor(x))    #FLOOR() retorna el numero entero inferior mas proximo a la variable x. (4)

print(math.copysign(x,y))#COPYSIGN retorna una variable flotante con la magnitud del primer operando y el signo del segundo operando. (-4.5)

print(math.factorial(3))#FACTORIAL() retorna el factorial de un numero entero positivo. Genera un error si el operando es de tipo float o negativo. (6)

print(math.sqrt(4))     #SQRT() retorna la raiz cuadrada de el operando. (2)

print(math.gcd(10,25,5))#GDC() retorna el divisor comun maximo de los enteros dados. (5)
print(math.lcm(6,3,12)) #LCM() retorna el minimo comun multiplo de los enteros dados. (12)

print(math.pi)          #PI retorna el valor de pi. (~3.14159)
print(math.e)           #E retorna el valor de e. (~2.71828)
 
print(math.degrees(3.1))#DEGREES() retorna el angulo en grados equivalente al valor en radianes del operando
print(math.radians(180))#RADIANS() retorna el valor en radianes equivalente al angulo en grados del operando

print(math.isclose(x,y,rel_tol=1,abs_tol=1))#Retorna True si los operandos son cercanos y False si no lo son. (False)
#La determinacion de si los operandos (x,y) son o no cercanos depende de los ultimos dos operandos(rel_tol y abs_tol)
#Rel_tol determina la tolerancia relativa. 1 equivale a 100%
#Abs_tol determina la tolerancia relativa. 1 equivale a 1

#||||||||||||||||||||||||||||||||||||-BUILT-IN FUNCTIONS-||||||||||||||||||||||||||||||||||||
#|||||||||-BIN-|||||||||
#La funcion integrada bin() permite convertir un numero decimal a binario
a = 13        #Declaramos una variable que contiene un numero decimal
print(bin(a)) #Imprimimos el equivalente en binario 

#|||||||||-ABS-|||||||||
q = -5         #Creamos una variable con un numero entero negativo
print(abs(q))  #Usamos abs para imprimir el valor absoluto de la variable (5)

#|||||||||-MIN-MAX-|||||||||
a = [1,4,6,45.5,-4,-45.5] #Creamos una lista con numeros
print(min(a))             #Imprimimos el numero menor de la lista con min
print(max(a))             #Imprimimos el numero mayor de la lista con max

#|||||||||-THINGS-TO-ADD-|||||||||

