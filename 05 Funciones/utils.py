import math

# Funciones auxiliares
def saludar(nombre = "Mundo"):
    saludo = f"Hola {nombre}!"
    print(saludo)

def imprimir_mensaje(mensaje):
    print(mensaje)

def solicitar_input_usuario(campo):
    valor = input(f"Por favor ingrese {campo}:")   
    return valor

def solicitar_numero_usuario(numero):
    valor = int(solicitar_input_usuario(numero))
    return valor

# Funciones actividades
# Actividad 1)
def imprimir_hola_mundo():
    return saludar()

# Actividad 2)
def saludar_usuario(nombre):
    return saludar(nombre)

# Actividad 3)
def imprimir_informacion_personal(nombre, apellido, edad, residencia):
    mensaje_informacion = f"Soy {nombre} {apellido}, tengo {edad} años y vivo en {residencia}"
    print(mensaje_informacion)

# Actividad 4)
def calcular_area_circulo(radio):
    calcular_perimetro_circulo(radio)
    area_circulo = (math.pi)*(radio ** 2)

    imprimir_mensaje(f"El area del circulo es:{area_circulo}")

def calcular_perimetro_circulo(radio):
    perimetro_circulo = 2*(math.pi)*radio
    imprimir_mensaje(f"El perimetro del circulo es: {perimetro_circulo}")
    #return(perimetro_circulo)