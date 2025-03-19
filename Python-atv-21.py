from math import sqrt, ceil, floor

#Importando e utilizando biblioteca pela primeira vez!

n = int(input('Digite um número: '))

raiz = sqrt(n)

print('A raiz de {} é igual a {}'.format(n,raiz))
print('A raiz de {} é igual a {:.2f}'.format(n,raiz))
print('A raiz de {} é igual a {}'.format(n,ceil(raiz)))
print('A raiz de {} é igual a {}'.format(n,floor(raiz)))
