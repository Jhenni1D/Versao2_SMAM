from flask import Flask, render_template, request
import pandas as pd

from app_service import pegar_data_formatada, pegar_hora_formatada

# cria uma instância do Flask
app = Flask(__name__)

# define uma rota para a página inicial
@app.route('/')
def index():
    return 'Olá, mundo! Este é um site simples criado com Flask.'

@app.route('/visualizar-dados')
def visualizar_dados():
    return 'Dados em json'

@app.route('/dados',methods=['POST'])  # dizer o metodo da rota, nesse caso é post
def receber():  # o tipo da função
  dado = request.json  # requisitando um arquivo json
  dado_armazenar = {"medicao": dado["medicao"]}  # dicionario ou objeto
  dado_armazenar["data"] = pegar_data_formatada()
  dado_armazenar["hora"] = pegar_hora_formatada()
  dado["datahora"] = dado_armazenar["data"] + "_" + dado_armazenar["hora"]
  print(f"\nDado armazenado: {dado_armazenar} - Sensor: {dado['sensor']}")
  registrar_dado_no_bd(dado_armazenar, dado["sensor"])
  io.emit("insert_queue", dado)
  return "deu tudo certo"

# executa o aplicativo Flask
if __name__ == '__main__':
    app.run(debug=True)