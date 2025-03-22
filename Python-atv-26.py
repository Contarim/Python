from random import choice

# Sorteando um nome

alunos = []

for i in range(1,5):
    nome = input('Digite o nome do aluno {}: '.format(i))
    #APPEND vai pegar os valores guardados na variável 'nome' e jogar para a lista da variável 'alunos'
    alunos.append(nome)
#CHOICE vai escolher aleatóriamente 1 dos nomes que estiver dentro da lista 'alunos'
escolhido = choice(alunos)

print('O aluno sorteado foi: {}'.format(escolhido))
