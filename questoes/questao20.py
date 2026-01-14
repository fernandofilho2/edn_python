
"""Crie uma função que calcule a idade de uma pessoa em dias,
baseada no ano de nascimento."""   



def calcular_idade_em_dias(ano_nascimento, ano_atual):
    idade_anos = ano_atual - ano_nascimento
    idade_dias = idade_anos * 365  
    return idade_dias
ano_nascimento = int(input("Digite o ano de nascimento: "))
ano_atual = int(input("Digite o ano atual: "))
idade_em_dias = calcular_idade_em_dias(ano_nascimento, ano_atual)
print(f"A idade em dias é: {idade_em_dias} dias")
