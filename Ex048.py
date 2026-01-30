cont = soma = conta_numeros = 0
while cont < 500: #ele vai fazer loop enquanto o cont for menor que 500
    cont += 1 #a cada loop o cont é incrementado com +1 para nao ficar no loop infinito

    if cont % 2 == 1: #aqui estou usando o if para verificar quais numeros sao IMPARES

        if cont % 3 == 0: #aqui estou usando o if para verificar quais numeros sao multiplos de 3

            print(cont) #aqui vai ser exibido apenas os numeros impares e os multiplos de 3

            soma += cont #a variavel soma é responsavel por somar todos os numeros impares e multiplos de 3
            conta_numeros += 1 #estou usando essa variavel para deposi exibir quantos numeros foram somados

print(f'Foram somados ao todo {conta_numeros} e a soma entre eles é de {soma}')
