"Criar um código que registre as notas de alunos e calcular a média da turma.


def calcular_media_turma():
    numero_alunos = int(input("Digite o número de alunos na turma: "))
    notas = []

    for i in range(numero_alunos):
        nota = float(input(f"Digite a nota do aluno {i + 1}: "))
        notas.append(nota)

    media = sum(notas) / numero_alunos
    return f"A média da turma é: {round(media, 2)}"

print(calcular_media_turma())
