d=int(input('Digite quantos dias ficou com o carro: '))
km=float(input("Digite quantos Km você andou com o carro: "))
total= (d * 60) + (km * 0.15)

#Função para calcular o alugel de um veículo
print('\nO preço do alugel diário é de R$60,00 e o preço por Km rodado é de R$0,15\n\n')
print('Você ficou {} Dias com o carro e andou {} Km.\n\no valor do alugel ficou em R${} sendo R${} da quantidade de dias e R${} da quantidade de Km rodados'.format(d,km,total,d*60,km*0.15))
