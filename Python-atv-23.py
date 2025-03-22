from math import floor

# Mostrando a porção inteira de um número real utilizando a biblioteca MATH

n=float(input('Digite um número real: '))

print('\nUtilizando função "floor" da biblioteca MATH\nO número digitado foi {} e a porção inteira dele é {}'.format(n,floor(n)))

print('\nUtilizando a função "int" nativa do Python\nO número digitado foi {} e a porção inteira dele é {}'.format(n,int(n)))


