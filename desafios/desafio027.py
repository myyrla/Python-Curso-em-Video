nome = str(input('Digite o seu nome completo: ')).strip()
nome_dividido = nome.split()
print(f'O seu primeiro nome é {nome_dividido[0]}')
print(f'O seu último nome é {nome_dividido[-1]}')