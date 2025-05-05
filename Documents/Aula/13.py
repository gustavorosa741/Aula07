idade = int(input("Digite sua idade: "))
valor = int(input("Digite o valor do ingresso: "))
estudante = str(input("Você é estudante? "))

final = []

if idade <=12:
    print(f"Você tem 50% de desconto, totaliznado {valor * 0.5}")
elif idade >= 60:
    print(f"Você tem 30% de desconto, totalizando {valor * 0.3}")
elif estudante == "sim":
    print(f"Você tem 10% de desconto, totalizando: {valor * 0.1}")

else:
    print("você não tem desconto.")


