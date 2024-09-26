salario_mensal = float(input('Informe o seu salário mensal: '))

if salario_mensal <= 2000:
    print('Você está isento do imposto de renda!')
elif 2000.01 <= salario_mensal <= 3500:
    print('O seu imposto de renda será de 10%.')
else:
    print('O seu imposto de renda será de 15%.')