import random

# Sorteando todos os nomes informados

alunos = []

for i in range(1,6):
    nome = input('Digite o nome do aluno {}: '.format(i))
    alunos.append(nome)

# Shuffle vai embaralhar os nomes dentro da lista
ordem = random.shuffle(alunos)

print('Ordem sorteada dos alunos: \n')

# "Enumerate" vai repetir os nomes que foram embaralhados na lista e o "start" vai ser o numero inicial que nosso "for" vai começar, por exemplo: se tivermos 5 alunos e o start começar em 5 ele vai até o 10, se começar em 1 vai até o 5.
for indice, aluno in enumerate(alunos, start=1):
    print('{}. {}'.format(indice,aluno))
