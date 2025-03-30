from flask import Flask, jsonify
import os



app = Flask(__name__)


@app.route('/')
def hello_world():
    return jsonify('Streaming de vídeos')


@app.route('/video/<video_name>/<file_name>')
def stream(video_name, file_name):
    return jsonify(f'Seu vídeo estará em: /video/{video_name}/{file_name}')

@app.route('/filmes-lista')
def lista_de_filmes():
    return jsonify('lista de todos os filmes:')


if __name__ == '__main__':
    app.run()
