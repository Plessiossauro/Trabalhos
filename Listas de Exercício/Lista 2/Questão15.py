velocidade = float(input('Diga a velocidade do carro registrada em (km/h): '))
multa_valor = 5
multa = (velocidade - 80) * multa_valor

if velocidade < 80:
    print('Você está dentro do limite de velocidade.')
else:
    print(f'Você está acima da velocidade e sua multa será de R${multa}')