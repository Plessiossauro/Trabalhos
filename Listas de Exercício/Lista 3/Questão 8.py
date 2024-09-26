missoes = int(input('Informe quantas vitórias o cavaleiro tem: '))

if missoes > 10:
    print('O cavaleiro recebeu mais 100 moedas de ouro pelas suas conquistas!')
elif 5 <= missoes <= 10:
    print('O cavaleiro recebeu mais 50 moedas de ouro pelas suas conquistas!')
elif 1 <= missoes <= 5:
    print('O cavaleiro recebeu mais 10 moedas de ouro pelas suas conquistas!')
elif missoes == 0:
    print('O cavaleiro não possui vitórias para receber moedas de ouro do seu rei.')
else:
    print('Informe outro número de vitórias')