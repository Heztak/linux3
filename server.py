## Lian Valenzuela || Juan Narria

# Importa los módulos necesarios
from flask import Flask, request, jsonify

# Crea una nueva aplicación Flask
app = Flask(__name__)

# Inicializa una lista para almacenar las jugadas
jugadas = []

# Define una ruta para comprobar si un juego está disponible
@app.route('/api/game/available', methods=['GET'])
def game_available():
    # Puedes cambiar esto para reflejar el estado actual del juego
    estado_juego = 'disponible'
    return jsonify({'state': estado_juego, 'game_id': 123})

# Define una ruta para recibir jugadas
@app.route('/api/move', methods=['POST'])
def receive_move():
    # Obtiene los datos enviados con la solicitud
    data = request.json
    # Añade los datos a la lista de jugadas
    jugadas.append(data)
    # Devuelve una respuesta para indicar que la jugada fue recibida
    return jsonify({'message': 'Move received'})

## Lian Valenzuela || Juan Narria

# Define una ruta para obtener los resultados del juego
@app.route('/api/game/result', methods=['GET'])
def get_game_result():
    # Estos son sólo ejemplos, deberías reemplazarlos con los valores reales
    jugadores = ['Jugador 1', 'Jugador 2', 'Jugador 3']
    # Calcula los valores de las jugadas basándose en los datos almacenados
    valores_jugadas = [j['move_value'] for j in jugadas]
    # Encuentra el jugador ganador basándose en los valores de las jugadas
    jugador_ganador = jugadores[valores_jugadas.index(max(valores_jugadas))]
    # Calcula el puntaje acumulado de las jugadas
    puntaje_acumulado = sum(valores_jugadas)

    # Devuelve los resultados del juego como una respuesta JSON
    return jsonify({
        'jugadores': jugadores,
        'valores_jugadas': valores_jugadas,
        'jugador_ganador': jugador_ganador,
        'puntaje_acumulado': puntaje_acumulado
    })

## Lian Valenzuela || Juan Narria

# Ejecuta la aplicación si este script se ejecuta directamente
if __name__ == '__main__':
    app.run(host='192.168.159.132', port=8080)
