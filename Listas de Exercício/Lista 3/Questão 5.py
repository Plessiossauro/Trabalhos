agua_disponivel = float(input("Quantidade de água disponivel (litros): "))

distancia = float(input("Distância ate o oásis (km): "))

agua_necessaria = distancia * 2

if agua_disponivel >= agua_necessaria:
    print("A quantidade de água e suficiente para chegar ao oásis.")

else:
    print("A quantidade água não é suficiente, será necessário mais água.")