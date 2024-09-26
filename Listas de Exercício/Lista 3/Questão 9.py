magia = int(input("Diga qual a habilidade do mago você quer usar: "))

match magia:
    case 1:
        print("Usar a habilidade de fogo")
    case 2:
        print("Usar a hábilidade de água")
    case 3:
        print("Usar a hábilidade de terra")
    case _:
        print("Você deve usar outra hábilidade")