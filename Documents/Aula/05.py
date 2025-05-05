from xmlrpc.client import boolean


cidade = str(input("Qual sua cidade?: "))
nascimento = int(input("Qual sua data de nascimento?: "))
altura = float(input("Qual sua altura?: "))
gosta = boolean(input("Você gosta de programar?: "))

print(f"\nA cidade {cidade} é maravilhosa!")
print(f"Você nasceu em: {nascimento}")
print(f"Sua altura é: {altura}")
if gosta == True:
    print("É otimo saber que gosta de programar :)")
else:
    print("É uma pena que não goste de programar :(")