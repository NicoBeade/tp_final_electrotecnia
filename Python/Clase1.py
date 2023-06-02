#Input output

#x = input("Ingrese una palabra")
print("Hola")

#Variables

c = 0
x = 1.0
y = "Hola"
print("C = ", c)
print("Type(c) = ", type(c))
print("x = ", x)
print("Type(x) = ", type(x))
print("y = ", y)
print("Type(y) = ", type(y))

z = True
print("z = ", z)
print("Type(z) = ", type(z))

print(8 + 4)
print(8 / 5)
print(8 % 2)
print(8 ** 2)   #8**2 == 8^2

#Casteo explicito
print("Casteo implicito: ", 8/5)
print("Casteo explicito: ", int(8/5))
print("Casteo explicito: ", bool(12/5))


#Control de Flujo

if 8/5 < 2:
    print("8/5 < 2")
    print("Hola")
elif 4%5 == 6:
    print("IA carrea la clase")
else:
    print("No se programar")

#Funciones
def f(x, y):
    z = x + y
    return z**2

z = True
print(f(3, 5))


#Estructuras de datos
#Listas
#a = [a0, a1, a2 ...]

lista_vacia = []
lista_con_elementos = [1,2,3,"True", False, 5.5, ["Complicado"]]

for indice in range(len(lista_con_elementos)):  #range(7) = 0,1,2,3,4,5,6 NO ME DEVUELVE EL 7
    print(lista_con_elementos[indice])

for indice in range(1, 6, 2):
    print(lista_con_elementos[indice])

#Ranged based for
for elemento in lista_con_elementos:
    if type(elemento) == type(1):
        print(elemento)

indice = 0
while indice < len(lista_con_elementos):
    print(lista_con_elementos[indice])
    indice += 1

#Operaciones con listas
print(lista_con_elementos)
lista_con_elementos.append("Final")
print(lista_con_elementos)
del lista_con_elementos[4]
print(lista_con_elementos)

#slicing
print(lista_con_elementos[1:4])
print(lista_con_elementos[1:6:2])
print(lista_con_elementos[:4])
print(lista_con_elementos[3:])
print(lista_con_elementos[::-1])            #Inversion de lista


numeros = [5,8,1,6,78,100,69]
print(numeros)
numeros.sort()
print(numeros)

#Remove
numeros.remove(78)
print(numeros)

#Preguntar por ocurrencias dentro de la lista
if 100 in numeros:
    print("Habia un 100")

#Tuplas
tupla = (16, 6, 8)
print(tupla)
print(tupla[1])

def vector(x):
    return x, 2*x, 3*x

x, y, z = vector(5)
print(x, y, z)


#Diccionarios
#diccionario = {clave: valor, clave2: valor2}
diccionario = {'nombre': 'Pepe', 'edad': 20, 'sexo': 'M'}
print(diccionario)
print(diccionario['edad'])