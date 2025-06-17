import random
alunos = input ("Digite o nome dos alunos que participarão do sorteio, sepadandos por vírgula: ")
lista_alunos = [nome.strip() for nome in alunos.split(",")]
aluno_random = random.choice(lista_alunos)
print(f'O aluno sorteado é: {aluno_random}')