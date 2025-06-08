import random

numero_secreto = random.randint(1, 100)
cantidad_intentos = 0
cantidad_max = 3
adivinado = False

print("¡Bienvenido al juego de adivinanza con límite de intentos!")

while not adivinado and cantidad_intentos < cantidad_max:
    numero = input("Introduce un número entre 1 y 100: ")
    
    try:
        entrada = int(numero)
    except ValueError:
        print("Por favor, introduce un número válido.")
        continue

    if entrada == numero_secreto:
        print("¡Felicidades! Has adivinado el número secreto.")
        adivinado = True
    elif entrada < numero_secreto:
        print("El número secreto es mayor.")
    else:
        print("El número secreto es menor.")
    
    cantidad_intentos += 1

if not adivinado:
    print("Lo siento, has agotado tus intentos. El número secreto era", numero_secreto)
