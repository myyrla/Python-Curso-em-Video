#Fatiamento, análise, transformação, divisão e junção. 
frase = 'Curso em Vídeo Python'
print (frase)
print (frase[3])
print (frase[3:13])
print (frase[:13])
print (frase[2::8])
print (frase.count('o'))
print (frase.upper().count('o'))
print (len(frase))
print (len(frase.strip()))
print(frase.find('Vídeo'))
print (frase.lower().find('vídeo'))
dividido = frase.split()
print(dividido)
print(dividido[0])
print(dividido[2] [3])


#print(frase.replace('Python','Android'))
#não muda de forma efetiva, muda apenas na instancia. Caso queira mostrar novamente, aí fazer o print(frase) novamente, com a atualização.

#Quando eu tenho uma frase muito grande e quero que ela fique dividida, coloco 3" no começo e no final, o python fatia sozinho.
print ("""Lorem Ipsum is simply dummy text of the printing and typesetting industry. Lorem Ipsum has been the industry's standard dummy text ever since the 1500s, when an unknown printer took a galley of type and scrambled it to make a type specimen book. It has survived not only five centuries, but also the leap into electronic typesetting, remaining essentially unchanged. It was popularised in the 1960s with the release of Letraset sheets containing Lorem Ipsum passages, and more recently with desktop publishing software like Aldus PageMaker including versions of Lorem Ipsum.""") 