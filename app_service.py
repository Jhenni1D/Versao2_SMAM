import datetime
from datetime import date
import json


def pegar_data_formatada():
    data_atual = date.today()  # date é a lib
    return "{}/{}/{}".format(data_atual.day, data_atual.month,data_atual.year)  # formatando a data contatenar dados


def pegar_hora_formatada():
    now = datetime.datetime.now()  # agora pegar a hora
    return str(now.hour) + ":" + str(now.minute) + ":" + str(now.second)  # concatenar o foamato da hora

def registrar_dado_no_bd(dados, sensor):
    post(link_bd.format(sensor), json=dados)