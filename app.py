from flask import Flask, request, jsonify

# Instancia de Flask
app = Flask(__name__)

# Base de datos para películas
movies_db = []

#------------------------------------Endpoint para agregar una película------------------------------------
@app.route('/api/new-movie', methods=['POST'])
def agregar_movie():
    data = request.get_json()

    # Revisa que data sea una lista
    if not isinstance(data, list):
        return jsonify({'message': 'Formato de datos incorrecto'}), 400

    for movie_data in data:
        # Accede a cada película en la lista
        movie = {
            'movieId': movie_data['movieId'],
            'name': movie_data['name'],
            'genre': movie_data['genre']
        }
        # Se agrega a la base de datos 
        movies_db.append(movie)
    # Se muestra el mensaje que las peliculas fueron ingresadas con exito
    return jsonify({'message': 'Película(s) agregada(s) con éxito'}), 201 # 201: Se ha creado un nuevo recurso

#------------------------------------Endpoint para obtener todas las películas por género------------------------------------
@app.route('/api/all-movies-by-genre/<genre>', methods=['GET'])
######## En la url <genre> se debe sustituir por el genero que deso buscar:
def get_movies_by_genro(genre):
    # Lista compresionada
    filtered_movies = [movie for movie in movies_db if movie['genre'].lower() == genre.lower()]
    # Devuelve la concidencia de genero, de lo contrario no muestra nada
    return jsonify({'movies': filtered_movies})

#------------------------------------Endpoint para actualizar una película------------------------------------
@app.route('/api/update-movie', methods=['PUT'])
def actualizar_movie():
    data = request.get_json()

    for movie in movies_db:
        # Verifica las claves de la base de datos:
        if movie['movieId'] == data['movieId']:
            movie['name'] = data['name']
            movie['genre'] = data['genre']
            return jsonify({'message': 'Película actualizada con éxito'})

    # Mensaje si no encuentra ninguna pelicula en la base de datos
    return jsonify({'message': 'Película no encontrada'}), 404 # El servidor no pudo encontrar el contenido solicitado

# inicio del programa:
if __name__ == '__main__':
    app.run(debug=True)
