import json
import time

import requests

url = 'http://api.openweathermap.org/data/2.5/weather?id=3451189&units=metric&lang=pt&appid=ea064b5e8f9165abed56acaa801885ee'

puxar_dados_pagina = requests.post(url, json={'key': 'value'})
content = puxar_dados_pagina.json()

direcao_do_vento = (content['wind']['deg'])
temperatura_minima = (content['main']['temp_min'])
temperatura_maxima = (content['main']['temp_max'])
cidade = (content['name'])
nascer_do_sol = (content['sys']['sunrise'])
por_do_sol = (content['sys']['sunset'])

def direcao_vento():
    if direcao_do_vento == 0:
        return('Norte')
    if (direcao_do_vento > 0) and (direcao_do_vento < 90):
        return('Nordeste')
    if direcao_do_vento == 90:
        return('Leste')
    if (direcao_do_vento > 90) and (direcao_do_vento < 180):
        return('Sudeste')
    if direcao_do_vento == 180:
        return('Sul')
    if (direcao_do_vento > 180) and (direcao_do_vento < 270):
        return('Sudoeste')
    if direcao_do_vento == 270:
        return('Oeste')
    if (direcao_do_vento > 270) and (direcao_do_vento < 360):
        return('Noroeste')

direcao = (direcao_vento())
nascente = (time.strftime("%D %H:%M", time.localtime(int(nascer_do_sol))))
poente = (time.strftime("%D %H:%M", time.localtime(int(por_do_sol))))

print('')
print(cidade)
print(f'Temperatura Mínima: ', (temperatura_minima), 'ºC')
print(f'Temperatura Máxima: ', (temperatura_maxima), 'ºC')
print(f'Direção do Vento:',(direcao_vento()))
print(f'Nascer do Sol: ', (nascente))
print(f'Por do Sol: ',(poente))
print('')
print('Informações geradas na tela inserida e carregada em dados_clima.json')

dados_clima = {"Cidade": cidade, 'Temperatura minima': temperatura_minima, 'Temperatura maxima': temperatura_maxima, 'Direcao do vento': direcao, 'Nascer do Sol': nascente, 'Por do Sol': poente}

def gerar_json(content, dados_clima):
    with open('dados_clima.json', 'w') as f:
        json.dump(dados_clima, f)

print(json.dumps(dados_clima, indent = 4))

gerar_json(content, dados_clima)