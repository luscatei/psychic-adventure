from math import sin, tan, cos, radians
import time

angulo = float(input('Digite um angulo: '))
seno = sin(radians(angulo))
tangente = tan(radians(angulo))
cosseno = cos(radians(angulo))
print('Processando...')
time.sleep(0.5)

print(f'O angulo {angulo} tem o seno {seno:.2f}, tangente {tangente:.2f}, cosseno {cosseno:.2f}')