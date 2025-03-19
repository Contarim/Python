import random

# Sorteando todos os nomes informados

alunos = []

for i in range(1,5):
    nome = input('Digite o nome do aluno {}: '.format(i))
    alunos.append(nome)

# Shuffle vai embaralhar os nomes dentro da lista
ordem = random.shuffle(alunos)

print('Ordem sorteada dos alunos: \n')

# "Enumerate" vai repetir os nomes que foram embaralhados na lista e o "start" vai ser o numero inicial que nosso "for" vai começar
for indice, aluno in enumerate(alunos, start=1):
    print('{}. {}'.format(indice,aluno))
