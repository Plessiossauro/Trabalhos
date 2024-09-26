Nota1 = int(input('Digite a primeira nota: '))
Nota2 = int(input('Digite a segunda nota: '))
Media = (Nota1 + Nota2) / 2

if Media >= 6:
    print('Você foi aprovado')
elif Media <= 6:
    print('Você foi reprovado')
else:
    print('Erro no sistema')
