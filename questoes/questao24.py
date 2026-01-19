''' Crie um programa que realize consultas a  em relação ao Real (BRL) usando a API mostre valor atual, máxima, mínima e data/hora da última atualização, caso a moeda não existir ou houver erro na requisição, retorne uma mensagem de erro.
'''
import requests 
def consultar_cotacao_moeda(moeda):
    url = f"https://economia.awesomeapi.com.br/json/last/{moeda}-BRL"
    try:
        resposta = requests.get(url)
        resposta.raise_for_status()  # Verifica se houve erro na requisição
        dados = resposta.json()
        chave_moeda = f"{moeda}BRL"
        if chave_moeda not in dados:
            print("Moeda não encontrada.")
            return None
        cotacao = dados[chave_moeda]
        valor_atual = cotacao['bid']
        valor_maximo = cotacao['high']
        valor_minimo = cotacao['low']
        data_hora_atualizacao = cotacao['create_date']
        return valor_atual, valor_maximo, valor_minimo, data_hora_atualizacao
    except requests.exceptions.RequestException as e:
        print("Falha na conexão:", e)
        return None
moeda_digitada = input("Digite a sigla da moeda (ex: USD, EUR, GBP): ").upper()
resultado = consultar_cotacao_moeda(moeda_digitada)
if resultado:
    valor_atual, valor_maximo, valor_minimo, data_hora_atualizacao = resultado
    print(f"Cotação da moeda {moeda_digitada} em relação ao BRL:")
    print(f"Valor Atual: R$ {valor_atual}")
    print(f"Valor Máximo: R$ {valor_maximo}")
    print(f"Valor Mínimo: R$ {valor_minimo}")
    print(f"Data/Hora da Última Atualização: {data_hora_atualizacao}")
else:
    print("Não foi possível obter os dados da moeda.")
    