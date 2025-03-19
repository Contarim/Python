import random

# Sorteando um nome

alunos = []

for i in range(1,5):
    nome = input('Digite o nome do aluno {}: '.format(i))
    alunos.append(nome)

escolhido = random.choice(alunos)

print('O aluno sorteado foi: {}'.format(escolhido))
