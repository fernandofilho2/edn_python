'''
Crie um programa que  acesse a API  para buscar um usuário fictício aleatório. exibindo o nome, e-mail e país desse usuário, caso houver erro na conexão, mostre uma mensagem de falha.
'''
import requests
def buscar_usuario_aleatorio():
    url = "https://randomuser.me/api/"
    try:
        resposta = requests.get(url)
        resposta.raise_for_status()  # Verifica se houve erro na requisição
        dados = resposta.json()
        usuario = dados['results'][0]
        nome = f"{usuario['name']['first']} {usuario['name']['last']}"
        email = usuario['email']
        pais = usuario['location']['country']
        return nome, email, pais
    except requests.exceptions.RequestException as e:
        print("Falha na conexão:", e)
        return None
resultado = buscar_usuario_aleatorio()
if resultado:

    nome, email, pais = resultado
    print(f"Nome: {nome}\nE-mail: {email}\nPaís: {pais}")
else:
    print("Não foi possível obter os dados do usuário.")
