larg=float(input('Qual a largura da parede: '))
alt=float(input('Qual a altura da parede: '))
area=larg*alt
input(f'Sua parede tem a dimensão de {larg}x{alt} e sua área é de {area}m²')
tinta=area/2
input(f'Para pintar sua parede, será necessário {tinta:.2f}L de tinta')