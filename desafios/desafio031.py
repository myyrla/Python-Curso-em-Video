dist = float(input('Digite a distância você vai percorrer em (KM): '))
if dist <= 200:
    print(f'Você deverá pagar uma passagem de {dist*0.50:.2f} reais.')
else:
    print(f'Você deverá pagar uma passagem de {dist*0.45:.2f} reais.')
