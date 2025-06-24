vel = float (input('Qual a velocidade que o seu carro estava? KM/h '))
multa = (vel - 80) * 7
if vel > 80:
    print(f'O seu carro foi multado e deverá pagar uma multa de {multa} reais.')
else:
    print('Parabéns, você está em uma ótima velocidade.')
