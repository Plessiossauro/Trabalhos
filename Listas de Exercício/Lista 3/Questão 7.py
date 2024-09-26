altura_da_planta = float(input('Informe a altura da planta em metros: '))

if altura_da_planta < 1:
    print('A planta foi classificada como pequena')
elif 1 <= altura_da_planta <= 3:
    print('A planta foi classificada como média')
else:
    print('A planta foi classificada como grande')