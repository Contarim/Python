from math import hypot

#Calculado a hipotenusa de um triângulo retângulo a partir das medidas dos catetos com ajuda da função 'HYPOT' própria para calcular a hipotenusa a partir dos valores dos catetos.

ca=float(input('Digite o comprimento do cateto oposto: '))
co=float(input('Digite o comprimento do cateto adjacente: '))
hipotenusa= hypot(co, ca)

print('O comprimento da hipotenusa é: {:.2f}'.format(hipotenusa))

