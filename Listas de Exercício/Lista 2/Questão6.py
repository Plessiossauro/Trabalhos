numero_conta = int(input('Número da conta do cliente: '))
saldo = float(input('Saldo da conta do cliente: '))
debito = float(input('Débito da conta do cliente: '))
credito = float(input('Crédito da conta do cliente: '))
saldo_atual = saldo - debito + credito

print(numero_conta)

if saldo_atual >= 0:
    print('O saldo está positivo')
else:
    print('O saldo está negativo')

print(saldo_atual)