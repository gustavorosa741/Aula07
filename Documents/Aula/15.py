n1 = int(input("Digite o primeiro numero: "))
n2 = int(input("Digite o segundo numero:"))
operacao = str(input("Digite a operação desejada: "))

if operacao == "+" :
    print(n1 + n2)
elif operacao == "-":
    print(n1 - n2)
elif operacao == "*":
    print(n1 * n2)
elif operacao == "/":
    print(n1 // n2)
else:
    print("Opção invalida")