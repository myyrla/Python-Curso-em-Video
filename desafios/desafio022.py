nome = str(input('Digite seu nome completo: ')).strip()
print('Analisando seu nome...')
print(f'Seu nome completo em maiúsculo é {nome.upper()}')
print (f'Seu nome completo em minúsculo é {nome.lower()}')
print(f'O seu nome tem ao todo {len(nome) - nome.count(" ")} letras')
primeiro_nome = nome.split()[0]
print(f'O seu primeiro nome é {primeiro_nome} tem {len(primeiro_nome)} letras')

