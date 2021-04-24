#!/usr/bin/python3
# Autor: Pablo J. Santos --> @jaysaints
# Está aplicação é desenvolvida utilizando a API de Dados do site Mercado Biticoin
# Para maiores informações segue o link https://www.mercadobitcoin.com.br/api-doc/


import requests
import os
import json
import time
from datetime import datetime



moeda = 'BTC'
valor = 283000.10

# Tempo em segunda para atualizar o valor
atualiza = 5

# Url da API passa os dados
urlTicker = f'https://www.mercadobitcoin.net/api/{moeda}/ticker'

# Faz uma requisição a pagina com o metodo GET
r = requests.get(urlTicker)

print(f'\tMOEDA: {moeda}' + ' '*8 + f'VALOR ESTIMADO PARA VENDA $ {valor}\n')
#print("Máxima 24H: " + getValues['ticker']['high'])
#print("Mínima 24H: " + getValues['ticker']['low'])
#print("Último Preço: " + getValues['ticker']['last'])
#print(f"Último Preço: {ultimoPreco}")
#print("Volume 24H: " + getValues['ticker']['vol'])
#print("Maior preço de oferta 24H: " + getValues['ticker']['buy'])
#print("Menor preço de oferta 24H: " + getValues['ticker']['sell'])
#print("Data e Hora 24H: " + getValues['ticker']['date'])

flag = 0
while True:
    datahora = datetime.now()
    strfdata = datahora.strftime('%d/%m/%Y-%H:%M:%S')
    page = requests.get(urlTicker)
    getValues = page.json()
    ultimoPreco = float(getValues['ticker']['last'])
    # Verifica estabilidade do valor por 10 seg
    if ultimoPreco >= valor:
        flag += 1
    if flag == 2:
        print(f'''
        #######################################
        #           >>> VENDER <<<            #
        #          $ {ultimoPreco}            #
        #             {strfdata}              #
        #######################################''')
        break
    time.sleep(atualiza)
    print(f'[{strfdata}] $ {ultimoPreco} ')
