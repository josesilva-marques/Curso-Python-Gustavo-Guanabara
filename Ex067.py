while True:
    n = int(input('Digite um número para ver sua tabuada: '))
    print('-' * 30)
    if n < 0:
        break
    for c in range(1, 11):
        print(f'{n} x {c} = {n * c}')
    print('-' * 30)
print('Programa de tabuada encerrado. Volte sempre!')