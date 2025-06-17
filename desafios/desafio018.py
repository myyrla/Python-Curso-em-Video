from math import sin, cos, tan, radians
angulo = float (input("Digite o ângulo: "))
angulo_rad = radians(angulo)
seno = sin(angulo_rad)
coseno = cos(angulo_rad)
tangente = tan (angulo_rad)
print(f'Com o ângulo {angulo}, conseguimos identificar o seno {seno:.2f}, coseno {coseno:.2f} e a tangente {tangente:.2f}')