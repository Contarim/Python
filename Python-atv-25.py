from math import radians,sin,cos,tan

# Calculando o "Seno", "Cosseno" e "Tangente" a partir de um ângulo informado

angulo = float(input('Digite um ângulo: '))

# Radians converte o valor do ângulo para graus radianos

seno = sin(radians(angulo))
cosseno = cos(radians(angulo))
tangente = tan(radians(angulo))

# "sin", "cos" e "tan" calculam o valor convertido em graus radianos para encontrar o Seno, Cosseno e Tangente

print('O ângulo {} tem o Seno de {:.2f}'.format(angulo,seno))
print('O ângulo {} tem o Cosseno : {:.2f}'.format(angulo,cosseno))
print('O ângulo {} tem o Tangente : {:.2f}'.format(angulo,tangente))