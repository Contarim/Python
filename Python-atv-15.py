l=float(input('Digite a largura da parede: '))
a=float(input('Digite a altura da parede: '))

#função para calcular a área de local e a quantidade de tinta para pintar essa área
print('Sua parece tem uma área de {} m2 considerando que 1 litro de tinta conseguimos pintas 2 metros quadrados, você precisa de {} Litros de tinta para pintar a sua parede.'.format(l*a,(l*a)/2))
