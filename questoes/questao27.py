'''
 3- Desenvolva um programa que cria um dicionário com dados de uma pessoa e salva esses dados em um arquivo JSON.
Em seguida, o programa deve ler o mesmo arquivo e exibir o conteúdo.
Para isso:

 * Crie um dicionário com pelo menos três campos (ex: nome, idade, cidade).
 * Solicite ao usuário o nome do arquivo JSON.
* Salve os dados no arquivo usando o módulo `json`.
 * Após salvar, leia o mesmo arquivo e imprima os dados carregados.
 * Trate possíveis erros como ausência do arquivo ou problemas na escrita.

 Dica: Use `json.dump()` para escrever e `json.load()` para ler o arquivo.

'''
import json
def salvar_dados_json(nome_arquivo, dados):
    try:
        with open(nome_arquivo, 'w', encoding='utf-8') as arquivo_json:
            json.dump(dados, arquivo_json, ensure_ascii=False, indent=4)
        print(f"Dados salvos com sucesso no arquivo: {nome_arquivo}")
    except Exception as e:
        print(f"Ocorreu um erro ao salvar o arquivo: {e}")
def ler_dados_json(nome_arquivo):
    try:
        with open(nome_arquivo, 'r', encoding='utf-8') as arquivo_json:
            dados = json.load(arquivo_json)
            print("Dados carregados do arquivo:")
            print(dados)
    except FileNotFoundError:
        print(f"O arquivo '{nome_arquivo}' não foi encontrado.")
    except Exception as e:
        print(f"Ocorreu um erro ao ler o arquivo: {e}")
dados_pessoa = {
    'nome': 'João Pereira',
    'idade': 30,
    'cidade': 'São Paulo'
}
nome_arquivo = input("Digite o nome do arquivo JSON para salvar os dados (ex: dados_pessoa.json): ")
salvar_dados_json(nome_arquivo, dados_pessoa)
ler_dados_json(nome_arquivo)
