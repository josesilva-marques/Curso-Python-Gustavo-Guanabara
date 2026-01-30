nota1 = float(input('Primeira nota: '))
nota2 = float(input('Segunda nota: '))
media = (nota1 + nota2) / 2
print('Tirando {} e {}, a média do aluno é {:.1f}'.format(nota1, nota2, media))
if media < 5:
    print('REPROVADO. NÃO DESISTA PEQUENO GAFANHOTO!')
elif media > 5 and media <= 6.9:
    print('RECUPERAÇÃO, SE ESFORCE MAIS.')
elif media >= 7:
    print('APROVADISSIMO, BOA GAROTÃO!')