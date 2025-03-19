import math

# Calculando o "Seno", "Cosseno" e "Tangente" a partir de um ângulo informado

angulo = float(input('Digite um ângulo: '))

# Radians converte o valor do ângulo para graus radianos
angulo_rad = math.radians(angulo)

# "sin", "cos" e "tan" calculam o valor convertido em graus radianos para encontrar o Seno, Cosseno e Tangente
seno = math.sin(angulo_rad)
cosseno = math.cos(angulo_rad)
tangente = math.tan(angulo_rad)

print('Seno : {:.2f}'.format(seno))
print('Cosseno : {:.2f}'.format(cosseno))
print('Tangente : {:.2f}'.format(tangente))