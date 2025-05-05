# Actividad 1)
edad = int(input("Por favor ingrese su edad: "))

if edad >= 18:
    print("Es mayor de edad.")

# Actividad 2)
nota = int(input("Por favor, ingrese su nota: "))

if nota >= 6:
    print("Aprobado")
else:
    print("Desaprobado")

# Actividad 3)
valor = int(input("Por favor, ingrese un valor par valido: "))

if (valor % 2 == 0):
    print("Ha ingresado un numero par.")
else:
    print("Por favor, ingrese un numero par.")

# Actividad 4)
edad = int(input("Por favor, ingrese su edad: "))

if edad >= 0 and edad < 12:
    print("Niño/a")
elif edad >=12 and edad < 18:
    print("Adolescente")
elif edad >= 18 and edad < 30:
    print("Adulto/a joven")
elif edad >= 30: 
    print("Adulto/a")
else:
    print("Valor invalido, por favor intente nuevamente.")

# Actividad 5)
# Se decidio usar getpass para ocultar caracteres al usuario a modo de complemento en el ejercicio.
import getpass

password = getpass.getpass("Por favor, ingrese una contraseña: ")

longitud_password = len(password)

if longitud_password >= 8 and longitud_password <= 14:
    print("Ha ingresado una contraseña correcta.")
else:
    print("Por favor, ingrese una contraseña de entre 8 y 14 caracteres.")

# Actividad 6)
import random
from statistics import mode, median, mean

numeros_aleatorios = [random.randint(1,100) for i in range(50)]

moda = mode(numeros_aleatorios)
mediana = median(numeros_aleatorios)
media = mean(numeros_aleatorios)

if media > mediana > moda:
    print("Sesgo positivo")
elif media < mediana < moda:
    print("Sesgo negativo")
elif media == mediana == moda:
    print("Sin sesgo")
else:
    print("No aplica")

# Actividad 7)
texto_usuario = input("Por favor, ingrese una frase o palabra: ")

terminacion_texto = texto_usuario[-1]

if terminacion_texto in "aAeEiIoOuU":
    print(texto_usuario + "!")
else:
    print(texto_usuario)

# Actividad 8)
nombre_usuario = input("Por favor, ingrese su nombre: ")

opcion_usuario = input("Por favor, ingrese una opcion sobre como escribir vuestro nombre, siendo: 1) Mayuscula, 2) Minuscula o 3) La primera letra mayuscula. ")

if opcion_usuario == "1":
    print(nombre_usuario.upper())
elif opcion_usuario == "2":
    print(nombre_usuario.lower())
elif opcion_usuario == "3":
    print(nombre_usuario.title())
else:
    print("Ha ingresado una opcion invalida, por favor intente nuevamente.")

# Actividad 9)
magnitud_terremoto = int(input("Por favor, ingrese la magnitud del terremoto: "))

if magnitud_terremoto >= 7:
    print("Extremo")
elif 7 > magnitud_terremoto >= 6:
    print("Muy fuerte")
elif 6 > magnitud_terremoto >= 5:
    print("Fuerte")
elif 5 > magnitud_terremoto >= 4:
    print("Moderado")
elif 4 > magnitud_terremoto >= 3:
    print("Leve")
else:
    print("Muy leve")

# Actividad 10)
lugar = input("Por favor, ingrese la inicial del hemisferio en que se encuentra N = Norte, S = Sur ").upper()
mes = int(input("Por favor, ingrese el mes del año de forma numerica: "))
dia = int(input("Por favor, ingrese el dia del mes: "))

if (mes == 12 and dia >= 20) or (1 <= mes <= 2) or (mes == 3 and dia <= 20):
    if lugar == "N":
        print("Usted se encuentra en la estacion de invierno.")
    elif lugar == "S":
        print("Usted se encuentra en la estacion de verano.")
    else:
        print("Lugar/hemisferio invalido, por favor intente nuevamente.")
elif (mes == 3 and dia >= 21) or (4 <= mes <= 5) or (mes == 6 and dia <= 20):
    if lugar == "N":
        print("Usted se encuentra en la estacion de primavera.")
    elif lugar == "S":
        print("Usted se encuentra en la estacion de otono.")
    else:
        print("Lugar/hemisferio invalido, por favor intente nuevamente.")
elif (mes == 6 and dia <= 21) or (7 <= mes <= 8) or (mes == 9 and dia <= 20):
    if lugar == "N":
        print("Usted se encuentra en la estacion de verano.")
    elif lugar == "S":
        print("Usted se encuentra en la estacion de invierno.")
    else:
        print("Lugar/hemisferio invalido, por favor intente nuevamente.")
elif (mes == 9 and dia <= 21) or (10 <= mes <= 11) or (mes == 12 and dia <= 21):
    if lugar == "N":
        print("Usted se encuentra en la estacion de otono.")
    elif lugar == "S":
        print("Usted se encuentra en la estaion de primavera.")
    else:
        print("Lugar/hemisferio invalido, por favor intente nuevamente.")