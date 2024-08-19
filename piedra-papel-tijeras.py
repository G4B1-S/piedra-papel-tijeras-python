jugador1 = input("¡Hola Jugador1! ¿Que eliges? ¿Piedra,Papel o Tijeras: ")
jugador2 = input("¡Hola Jugador2! ¿Que eliges? ¿Piedra,Papel o Tijeras: ")


if jugador1 == jugador2:
    print("¡Han empatado!")
elif (jugador1 == "piedra" and jugador2 == "tijeras") or (jugador1 == "papel" and jugador2 == "piedra") or (jugador1 == "tijeras" and jugador2 == "papel"):
    print('Ha ganado el jugador 1')
else:
    print('Ha ganado el jugador 2')

