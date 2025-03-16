n=int(input('Digite um numero para a tabuada: '))

print('O número escolhido foi {} abaixo teremos a tabuada dele'.format(n))

# Função para calcular a tabuada com a estrutura de repetição "FOR"
for i in range(1,11):
    print(f"{n} x {i} = {n * i}")