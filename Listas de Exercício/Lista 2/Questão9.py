Hora_extra = int(input('Quantidade de horas extras que o funcionário fez: '))
Horas_faltas = int(input('Quantidade de horas que o funcionário faltou : '))

if Hora_extra > Horas_faltas:
    print("Bônus de R$500,00")
else:
    print("Sem bônus")