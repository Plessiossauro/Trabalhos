Temperatura = float(input('Digite a temperatura ambiente atual (ºC): '))

print(Temperatura)

if Temperatura < 15:
    print('O clima está frio')
elif 15 <= Temperatura <= 25:
    print('O clima está ameno')
else:
    print('O clima está quente')