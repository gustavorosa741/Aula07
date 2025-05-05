codigo = int(input("Digite o codigo do produto: "))

match codigo:
    case 1:
        print("Eletronico")
    case 2:
        print("Roupas")
    case 3:
        print("Alimentos")
    case 4:
        print("Livros")
    case 5:
        print("Brinquedos")
    case _:
        print("Codigo invalido")
