'''

 2- Desenvolva um programa que lê os dados de um arquivo CSV e imprime cada linha na tela.
Para isso:

 * Solicite ao usuário o nome do arquivo CSV a ser lido.
 * Utilize o módulo `csv` para abrir o arquivo e ler os dados.
 * Exiba cada linha completa como uma lista.
 * Trate erros como arquivo inexistente ou problemas na leitura.

 Dica: Use `csv.reader()` para ler e percorrer as linhas do arquivo.
'''
import csv
def ler_dados_csv(nome_arquivo):
    try:
        with open(nome_arquivo, mode='r', newline='', encoding='utf-8') as arquivo_csv:
            leitor_csv = csv.reader(arquivo_csv)
            for linha in leitor_csv:
                print(linha)  
    except FileNotFoundError:
        print(f"O arquivo '{nome_arquivo}' não foi encontrado.")
    except Exception as e:
        print(f"Ocorreu um erro ao ler o arquivo: {e}")
nome_arquivo = input("Digite o nome do arquivo CSV a ser lido (ex: dados_pessoas.csv): ")
ler_dados_csv(nome_arquivo)


