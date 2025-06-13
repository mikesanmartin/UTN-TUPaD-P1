# Actividad 1)
contador = 0

for contador in range(101): 
    print(contador)
    contador += 1

# Actividad 2)
numero = input("Por favor, ingrese un numero entero: ")
contador_digitos = 0

for numero in range(len(numero)):
    contador_digitos += 1

print("La cantidad de digitos correspondiente al numero ingresado es: ", contador_digitos)

# Actividad 3)
num_inicial = int(input("Por favor, ingrese el numero inicial: "))
num_final = int(input("Por favor, ingrese el numero final: "))
acumulador = num_inicial
valor_total = 0

for acumulador in range(num_inicial, num_final - 1):
    acumulador += 1
    valor_total = valor_total + acumulador
    
print(f"La sumatoria de los numeros comprendidos entre:{num_inicial} y {num_final}, sin incluirlos, es:", valor_total)

# Actividad 4)
numero_usuario = int(input("Por favor, ingrese un numero: "))
acumulador = 0

while numero_usuario != 0:
    acumulador += numero_usuario
    numero_usuario = int(input("Por favor, ingrese un numero: "))

print("El total acumulado es: ", acumulador)


# Actividad 5)
import random

numero_random = random.randint(0,9)
contador_intentos = 0
numero_usuario = int(input("Por favor, ingrese un numero: "))

while numero_random != numero_usuario:
    print("El numero es incorrecto, vuelve a intentarlo.")
    contador_intentos += 1
    numero_usuario = int(input("Por favor, ingrese un numero: "))

print(f"Felicidades! Has adivinado, y solo te tomo {contador_intentos} intentos!")

# Actividad 6)
numero = 100

for numero in range (100, 0, -1):
    if numero % 2 == 0:
        print(numero)
    numero -= 1

# Actividad 7)
acumulador = 0
sumatoria = 0
numero_usuario = int(input("Por favor, ingrese un numero: "))

while numero_usuario <= 0:
    print("El numero ingresado no es valido, por favor intente nuevamente: ")
    numero_usuario = int(input())
else:
    for acumulador in range (0, numero_usuario + 1):
        sumatoria += acumulador
                
print("La sumatoria de numeros total es: ", sumatoria)

# Actividad 8)
# Informo la cantidad de numeros que podra ingresar el usuario.
cant_numeros = 100

# Defino los contadores para estados posibles, par, impar, positivo y negativo
contador_pares = 0
contador_impares = 0
contador_positivos = 0
contador_negativos = 0

for i in range (cant_numeros):
    numero_usuario = int(input("Por favor, ingrese un numero: "))

    # Evaluo el numero
    if (numero_usuario >= 0):
        contador_positivos += 1
        if(numero_usuario % 2 == 0):
            contador_pares += 1
        else:
            contador_impares += 1
    else:
        contador_negativos += 1
        if(numero_usuario % 2 == 0):
            contador_pares += 1
        else:
            contador_impares += 1

print("De acuerdo a los numeros ingresados: ")
print("La cantidad de numeros pares es: ", contador_pares)
print("La cantidad de numeros impares es: ", contador_impares)
print("La cantidad de numeros positivos es: ", contador_positivos)
print("La cantidad de numeros negativos es: ", contador_negativos)

# Actividad 9)
# Informo la cantidad de numeros que podra ingresar el usuario.
cant_numeros = 3
acumulador = 0
media = 0


for i in range(cant_numeros):
    numero_usuario = int(input("Por favor, ingrese un numero: "))
    acumulador += numero_usuario

media = (acumulador / cant_numeros)

print("La media de los numeros ingresados es: ", media)

# Actividad 10)
numero_usuario = input("Por favor ingrese un numero: ")
cant_digitos = len(numero_usuario)

print(f"El numero {numero_usuario} invertido es: ", end="")

for i in range(cant_digitos, 0, -1):
    print(numero_usuario[i -1], end="")