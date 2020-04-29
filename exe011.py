n1 = float(input('Qual a altura da parede? '))
n2 = float(input('Qual a largura da parede? '))
quad = n1*n2
print('Com a altura de {} e a largura de {} você tem uma área de {}m².'.format(n1, n2, quad))
tot = quad / 2
print('Para pintar a área acima você precisará de {}L de tinta.'.format(tot))
