'''
- Crie um programa que consulte informações de um  na API , retorne logradouro, bairro, cidade e estado do CEP digitado, caso o CEP não existir ou houver erro na requisição, mostre uma mensagem de falha.

'''
import requests
def buscar_cep(cep):
    url = f"https://viacep.com.br/ws/{cep}/json/"
    try:
        resposta = requests.get(url)
        resposta.raise_for_status()  # Verifica se houve erro na requisição
        dados = resposta.json()
        if 'erro' in dados:
            print("CEP não encontrado.")
            return None
        logradouro = dados.get('logradouro', 'N/A')
        bairro = dados.get('bairro', 'N/A')
        cidade = dados.get('localidade', 'N/A')
        estado = dados.get('uf', 'N/A')
        return logradouro, bairro, cidade, estado
    except requests.exceptions.RequestException as e:
        print("Falha na conexão:", e)
        return None 
cep_digitado = input("Digite o CEP (somente números): ")
resultado = buscar_cep(cep_digitado)
if resultado:
    logradouro, bairro, cidade, estado = resultado
    print(f"Logradouro: {logradouro}\nBairro: {bairro}\nCidade: {cidade}\nEstado: {estado}")
else:
    print("Não foi possível obter os dados do CEP.")
    