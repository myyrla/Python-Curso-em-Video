n1 = float (input('Digite sua primeira nota: '))
n2 = float (input('Digite sua segunda nota: '))
m = (n1 + n2) / 2
print(f'Sua média foi {m:.1f}')
if m >= 6.0:
    print('Sua média foi boa, parabéns!')
else:
    print('Sua média foi ruim, estude mais!')

#Tem a opção de colocar print('Parabens' if m >= 6 else 'Estude mais')