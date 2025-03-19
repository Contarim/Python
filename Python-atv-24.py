from math import sqrt

#Calculado a hipotenusa de um triângulo retângulo a partir das medidas dos catetos

ca=int(input('Digite o comprimento do cateto oposto: '))
co=int(input('Digite o comprimento do cateto adjacente: '))
hipotenusa= sqrt(co**2 + ca**2)

print('O comprimento da hipotenusa é: {:.2f}'.format(hipotenusa))

