from random import randint
from time import sleep

print('-=-'*30)
print('Vou pensar em um numero Tente adivinhar ! '.center(80))
print('-=-'*30)

numero = int(input('Digite um numero: '))

print('Hummm Estou analisando o numero....')

sleep(3)


escolhido = randint(0,5)

if numero == escolhido:
    print('PARABENS')
else:
    print('ERROU')