"""Criar um código que serve para analisar números digitados pelo usuário,
classificando-os como pares ou ímpares e contabilizando quantos de cada tipo foram 
inseridos. """

def analisar_numeros():
    quantidade_numeros = int(input("Quantos números você deseja analisar? "))
    pares = 0
    impares = 0

    for _ in range(quantidade_numeros):
        numero = int(input("Digite um número: "))
        if numero % 2 == 0:
            pares += 1
        else:
            impares += 1

    return f"Números pares: {pares}, Números ímpares: {impares}"
print(analisar_numeros())
