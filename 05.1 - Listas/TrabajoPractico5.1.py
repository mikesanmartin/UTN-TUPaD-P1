# Actividad 1)
# Declaro array vacio
array_numeros = []

for i in range (0, 101):
    # Evaluo la condicion para agregar numeros al array
    if (i % 4 == 0):
        array_numeros.append(i)

# Imprimo resultado
print(array_numeros)

# Actividad 2)
# Defino el array
mi_array = ["Ferrari", "Mercedes", "Alpine", "Aston Martin", "Mc Laren"]

# Muestro el anteultimo elemento
print(mi_array[-2])

# Actividad 3)
mi_array = []

mi_array.append("Ford")
mi_array.append("Chevrolet")
mi_array.append("Fiat")

print(mi_array)

# Actividad 4)
# Se define el array
animales = ["perro", "gato", "conejo", "pez"]

# Se imprime para verificar
# print(animales)

# Ingreso cambios en el array
animales[1] = "loro"
animales[-1] = "oso"

# Imprimo para verificar cambios
print(animales)

# Actividad 5)
# El programa informado declara inicialmente un array de numeros.
# Luego elimina el valor mas gande que se encuentre en ese array.
# Primero declara el remove() y luego adentro busca el mayor valor con max().
# Imprime el array por pantalla una vez removido el elemento que fue identificado con el mayor valor.

# Actividad 6)
# Defino array
mi_array = []

# Ingreso criterio para agregar numeros
for i in range(10, 31, 5):
    mi_array.append(i)

# Imprime solamente los 2 primeros valores
print(mi_array[0:2])

# Actividad 7)
# Defino array
autos = ["sedan", "polo", "suran", "gol"]

# Actualizo valores
autos[1] = "vento"
autos[2] = "tiguan"

# Imprimo lista para verificar
print(autos)

# Actividad 8)
# Defino array
dobles = []

# Actualizo valores
dobles.append(5*2)
dobles.append(10*2)
dobles.append(15*2)

# Imprimo lista para verificar
print(dobles)

# Actividad 9)
# Defino array
compras = [["pan", "leche"], ["arroz", "fideos", "salsa"],
["agua"]]

# Modificaciones
# a) Agregar "jugo" a la lista del tercer cliente usando append. 
compras[2].append("jugo")

# b) Reemplazar "fideos" por "tallarines" en la lista del segundo cliente.
compras[1][1] = "tallarines"

# c) Eliminar "pan" de la lista del primer cliente.
compras[0].remove("pan")

# d) Imprimir la lista resultante por pantalla
print(compras)

# Actividad 10)
# Defino array vacio
lista_anidada = []

# Agrego elementos
lista_anidada.append(15)
lista_anidada.append(True)
lista_anidada.append([])
lista_anidada[2].append(25.5)
lista_anidada[2].append(57.9)
lista_anidada[2].append(30.6)
lista_anidada.append(False)

# Imprimo lista
print(lista_anidada)
