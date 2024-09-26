porta = int(input("Diga qual a porta que você deseja abrir: "))

match porta:
    case 1:
        print("Você abriu a porta 1")
    case 2:
        print("Você abriu a porta 2")
    case 3:
        print("Você abriu a porta 3")
    case 4:
        print("Você abriu a porta 4")
    case 5:
        print("Você abriu a porta 5")
    case _:
        print("Você deve escolher outra porta")
        