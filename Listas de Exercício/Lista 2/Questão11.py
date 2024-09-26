Lado_1 = int(input("Digite o lado do triângulo: "))
Lado_2 = int(input("Digite o lado do triângulo: "))
Lado_3 = int(input("Digite o lado do triângulo: "))

if Lado_1 == Lado_2 == Lado_3:
    print("Este triângulo é equilátero")
elif Lado_1 == Lado_2:
    print("Este triângulo é isoceles")
elif Lado_2 == Lado_3:
    print("Este triângulo é isoceles")
elif Lado_3 == Lado_1:
    print("Este triângulo é isoceles")
else:
    print("Este triângulo é escaleno")