numeros = []

for i in range(3):
    numero = int(input(f"Digite o numero{i+1}: "))
    numeros.append(numero)

numeros.sort()

print("Os numeros em ordem são: ", numeros)