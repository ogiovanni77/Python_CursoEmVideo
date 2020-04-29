day = int(input('Quantos dias o carro foi alugado? '))
km = float(input('Quantos Km rodados? '))
calc = day * 60 + km * 0.15
print('O total do aluguel do carro é: R${:.2f}'.format(calc))
