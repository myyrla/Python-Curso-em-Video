salario=float(input('Qual é o salário do funcionário? R$'))
novosal=salario+(salario*15/100)
input(f'O funcionário que ganhava R${salario:.2f}, com os 15% de aumento, passa a receber R${novosal:.2f}')
