from time import sleep 
print('-=-'*20)
print('Analisador de triângulos')
print('-=-'*20)
med_1 = float (input('Primeiro segmento: '))
med_2 = float (input ('Segundo segmento: '))
med_3 = float (input ('Terceiro segmento: '))
print('Processando...')
sleep(3)
if med_1 < med_2 + med_3 and med_2 < med_1 + med_3 and med_3 < med_1 + med_2:
    print('Os seguimentos podem formar um triângulo!')
else: 
    print('Os segmentos não podem formar um triângulo.')