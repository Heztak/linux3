# Importa el módulo requests
## Lian Valenzuela || Juan Narria
import requests

# Define la URL del servidor
SERVER_URL = "http://192.168.10.222:8080"

# Define una función para ingresar un ID
def ingresar_id(prompt):
    id = input(prompt)
    return id

# Define una función para consultar si un juego está disponible
def consultar_juego_disponible():
    response = requests.get(f"{SERVER_URL}/api/game/available")
    data = response.json()
    if data['state'] == "available":
        print("Juego disponible")
    else:
        print("No hay juego disponible en este momento")

# Define una función para realizar una jugada
def realizar_jugada():
    id_jugador = ingresar_id("Ingrese el ID del jugador: ")
    id_juego = ingresar_id("Ingrese el ID del juego: ")
    valor_jugada = input("Ingrese el valor de la jugada: ")

    payload = {
        "player_id": id_jugador,
        "game_id": id_juego,
        "move_value": valor_jugada
    }

    response = requests.post(f"{SERVER_URL}/api/move", json=payload)
    if response.status_code == 200:
        print("Jugada realizada con éxito")
    else:
        print(f"Error al realizar la jugada, código de estado: {response.status_code}")


## Lian Valenzuela || Juan Narria

# Define una función para consultar el resultado del juego
def consultar_resultado_juego():
    response = requests.get(f"{SERVER_URL}/api/game/result")
    data = response.json()
    print("Nombre de los jugadores:", data["jugadores"])
    print("Valores de las jugadas:", data["valores_jugadas"])
    print("Jugador ganador:", data["jugador_ganador"])
    print("Puntaje acumulado de los jugadores:", data["puntaje_acumulado"])

## Lian Valenzuela || Juan Narria

# Bucle principal para interactuar con el usuario
while True:
    print("------MENU------")
    print("1. Ingresar el ID del jugador")
    print("2. Ingresar el ID del juego")
    print("3. Consultar juego disponible")
    print("4. Realizar jugada")
    print("5. Consultar estado del juego")
    print("6. Salir")
    opcion = input("Seleccione una opcion: ")

    if opcion == '1':
        id_jugador = ingresar_id("Ingrese el ID del jugador: ")
        print("ID del jugador ingresado: ", id_jugador)
    elif opcion == '2':
        id_juego = ingresar_id("Ingrese el ID del juego: ")
        print("ID del juego ingresado: ", id_juego)
    elif opcion == '3':
        consultar_juego_disponible()
    elif opcion == '4':
        realizar_jugada()
    elif opcion == '5':
        consultar_resultado_juego()
    elif opcion == '6':
        print("Saliendo del programa")
        break
    else:
        print("Opción no válida, selecciona una opción válida")
