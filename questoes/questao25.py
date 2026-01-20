''' Crie um programa que escreve dados de pessoas (nome, idade e cidade) em um arquivo CSV.
Para isso:

 * Crie uma lista de listas com dados fictícios de pelo menos três pessoas.
 * Solicite ao usuário o nome do arquivo CSV onde os dados serão salvos.
 * Escreva os dados usando o módulo `csv`, com cabeçalhos apropriados.
 * Confirme a gravação exibindo uma mensagem com o nome do arquivo.
 * Trate possíveis erros de escrita de arquivo.

 Dica: Use `csv.writer()` para escrever os dados linha por linha.

'''
import csv
def escrever_dados_csv(nome_arquivo, dados):
    try:
        with open(nome_arquivo, mode='w', newline='', encoding='utf-8') as arquivo_csv:
            escritor_csv = csv.writer(arquivo_csv)
            escritor_csv.writerow(['Nome', 'Idade', 'Cidade']) 
            escritor_csv.writerows(dados)  
        print(f"Dados gravados com sucesso no arquivo: {nome_arquivo}")
    except Exception as e:
        print(f"Ocorreu um erro ao escrever o arquivo: {e}")

dados_pessoas = [
    ['Ana Silva', 28, 'São Paulo'],
    ['Carlos Oliveira', 35, 'Rio de Janeiro'],
    ['Mariana Santos', 22, 'Belo Horizonte']
]
nome_arquivo = input("Digite o nome do arquivo CSV para salvar os dados (ex: dados_pessoas.csv): ")
escrever_dados_csv(nome_arquivo, dados_pessoas)
