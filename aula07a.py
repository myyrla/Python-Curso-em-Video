nome=input('Digite o seu nome: ')
print(f'Prazer em te conhecer, {nome:=^20}')

n1=int(input('Um valor: '))
n2=int(input('Outro valor: '))
s=n1+n2
m=n1*n2
d=n1/n2
di=n1//n2
e=n1**n2
print(f'A soma é {s}, \n o produto é {m} e a \n divisão é {d:.3f}', end=" ")
#o \n faz a quebra da linha e o end='' junta os dois prints
print(f'a divisão inteira é {di} e a potência é {e}')