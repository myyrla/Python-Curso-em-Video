preço = float(input('Qual o valor do produto? R$'))
novopreco = preço-(preço*5/100)
input(f'Com o desconto de 5% o valor de R${preço:.2f} cai para R${novopreco:.2f}')
