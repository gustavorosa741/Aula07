par = []

while True:
    numero = int(input("Digite um numero: "))
    if numero < 0:
        print("Numero negativo" \
        "\nSaindo...")
        break
    elif numero %2 ==0:
        par.append(numero)
        print("Numeros par:", par)
    if par:
        media = sum(par) / len(par)
        print("Media:", media)
    else:
        ("nenhum numero")

    