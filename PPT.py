jugador1 = input("Hola jugador 1, elije piedra papel o tijera: ")
jugador2 = input("Hola jugador 2, elije piedra papel o tijera: ")

if jugador1 == jugador2:
    print("empate")
elif (jugador1 == "piedra" and jugador2 == "tijera") or \
     (jugador1 == "papel" and jugador2 == "piedra") or \
     (jugador1 == "tijera" and jugador2 == "papel"):
    print("Jugador 1 gana")
else:
    print("Jugador 2 gana")