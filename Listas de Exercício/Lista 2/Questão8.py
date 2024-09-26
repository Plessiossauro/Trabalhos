Valor = float(input('Valor da compra: '))
Desconto_10 = Valor - (0.1 * Valor)
Desconto_05 =  Valor - (0.05 * Valor)

if Valor >= 100:
    print(f"O valor da sua compra foi de {Valor}, com um desconto de 10%, totalizando R${Desconto_10}")
elif Valor >= 50 < 100:
    print(f"O valor da sua compra foi de {Valor}, com um desconto de 5%, totalizando R${Desconto_05}")
else:
    print(f"O valor de sua compra não foi elegivel a desconto.")