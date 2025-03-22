import math

#Importando e utilizando biblioteca pela primeira vez!

n = int(input('Digite um número: '))

raiz = math.sqrt(n)

print('A raiz de {} é igual a {}'.format(n,raiz))
print('A raiz de {} é igual a {:.2f}'.format(n,raiz))
print('A raiz de {} é igual a {}'.format(n,math.ceil(raiz)))
print('A raiz de {} é igual a {}'.format(n,math.floor(raiz)))

