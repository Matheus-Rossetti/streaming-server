from flask import Flask, jsonify
import os



app = Flask(__name__)


@app.route('/')
def hello_world():
    return jsonify('Streaming de vídeos')


@app.route('/video/<video_name>/<file_name>')
def stream(video_name, file_name):

    #TODO criar link temporario usando a API do S3 e retornar o link ao app

    return jsonify(f'Seu vídeo estará em: /video/{video_name}/{file_name}')

@app.route('/filmes-lista')
def lista_de_videos():

    # TODO requisição pro S3 para pegar todos os diretorios dentro do bucker
    # TODO deve retornar uma lista, contar a lista e retornar a quantidade de filmes e seus nomes

    return jsonify('lista de todos os filmes:')

@app.route('/upload')
def upar_video():

    # TODO verificar o tipo de arquivo
    # TODO enviar arquivo para o micro-serviço com ffmpeg

    # TODO ffmpeg vai guardar os arquivos gerados no S3
    return

if __name__ == '__main__':
    app.run()
