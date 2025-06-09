print("Bienvenido al juego de penales. Puede elejir entre izquierda, derecha o medio")

cantidad_penales = 3
cantidad_pateados = 0
golesA = 0
golesB = 0


for i in range(cantidad_penales):
    print("Patea A, ataja B")
    
    pateadorA = input("Elije entre izquierda derecha o medio: ")
    pateadorB = input("Elije entre izquierda derecha o medio: ")

    if pateadorA == pateadorB:
        print("ATAJO")
    else:
        print("GOL! Cantidad de goles",golesA + 1, ".Cantidad de penales pateados ", cantidad_pateados + 1)
        golesA += 1
    cantidad_pateados += 1

    print("Patea B, ataja A")
    pateadorB = input("Elije entre izquierda derecha o medio: ")
    pateadorA = input("Elije entre izquierda derecha o medio: ")
    if pateadorB == pateadorA:
        print("ATAJO!")
    else:
        print("GOL! Cantidad de goles ", golesB + 1, ". Cantidad de penales pateados ", cantidad_pateados + 1)
        golesB += 1
    cantidad_pateados += 1

print("Penales finalizados")

if golesA > golesB:
    print("El equipo A gana con", golesA, "goles")
elif golesB > golesA:
    print("El equipo B gana con", golesB, "goles")
else:
    print("Empate, ambos equipos anotaron", golesA, "goles")