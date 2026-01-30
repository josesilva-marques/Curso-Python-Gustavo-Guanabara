num = int(input('Digite um numero para ver a sua tabuada: '))

for c in range(0,11):
    print('{} X {} = {}'.format(num ,c,(num * c)))