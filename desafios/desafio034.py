salario = float(input("Digite o seu salário atual em reais: "))
if salario <= 1.250:
    print( f'Com o aumento de 10%, o seu salário atual é {salario * 1.10} reais!')
else:
    print(f'Com o aumento de 15%, o seu salário atual é {salario * 1.15} reais!')


#existe a opção de calcular o salario como - salario + (salario * 15/100)
