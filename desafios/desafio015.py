dias=float(input('Quantos dias o carro foi alugado? '))
km=float(input('Quantos Km rodados? '))
custdia=dias*60
custkm=km*0.15
custot=custdia+custkm
input(f'O valor a pagar é de R${custot:.2f}')