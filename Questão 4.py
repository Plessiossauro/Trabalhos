real_1 = int(input("Quantidades de moedas de 1 real: "))
centavos_50 = int(input("Quantidade de moedas de 50 centavos: "))
centavos_25 = int(input("Quantidade de moedas de 25 centavos: "))

Total = (real_1 * 1) + (centavos_50 * 0.5) + (centavos_25 * 0.25)

print(f"O valor total das moedas é : R${Total:.2f}")