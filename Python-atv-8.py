n1=int(input('Digite um valor: '))
n2=int(input('Digite outro valor'))

#Teste com os operadores artiméticos 

s= n1 + n2
m= n1 * n2
d= n1 / n2
di= n1 // n2
e= n1 ** n2

print('A Soma é {}, A multiplicação é {}, a divisão é {}, a Divisão inteira é {}'.format(s,m,d,di), end=' ')
print('e a potência é {}'.format(e))