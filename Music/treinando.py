
import mysql.connector

#conectar banco de dados
mydb = mysql.connector.connect(
    host="localhost",
    user="root",
    password="Bender@1",
    database="Alunos")

#dar comandos para dentro do banco de dados
mycursor = mydb.cursor()
mycursor.execute ("USE Alunos")

cadastrar_aluno = []


def cadastrar_aluno():
    cadastrar_nome = (input("\nDigite o nome do aluno: "))
    cadastrar_idade = int(input("Digite a idade do aluno: "))
    cadastrar_curso = (input("DIgite o curso do aluno: "))
    print("\nAluno cadastrado com sucesso!\n")
    sql = "INSERT INTO alunos (nome, idade, curso) VALUES (%s,%s,%s)"
    val = (cadastrar_nome, cadastrar_idade, cadastrar_curso,)
    mycursor.execute(sql,val)
    mydb.commit()


cadastro_livro = ["robin", "andre", 2255, 2]


def cadastrar_livro():
    cadastro_livro.append(input("Digite o título do livro:"))
    cadastro_livro.append(input("Digite o autor do livro:"))
    cadastro_livro.append(input("Digite o codigo de identificação do livro:"))
    cadastro_livro.append(input("Digite quantos livros há em estoque:"))
    print("livro cadastrado com sucesso!")

def livros_cadastrados():
    livro = input("Digite o nome do livro que deseja procurar: ")
    if livro in cadastro_livro:
        indice = cadastro_livro.index(livro)
        dados_livro = cadastro_livro[indice:indice+4]
        rotulo_livro = ["\n\nNome do livro", "Autor do livro", "Codigo do livro", "Quantidade em estoque"]

        for rotulo_livro, dados_livro in zip(rotulo_livro, dados_livro):
            print(f"{rotulo_livro}: {dados_livro}")



    #print(cadastro_livro)



cadastro_emprestimo = []


def cadastrar_emprestimo():
    cadastro_emprestimo.append(input("Digite o nome do aluno:"))
    cadastro_emprestimo.append(input("Digite o livro que será emprestado:"))
    cadastro_emprestimo.append(input("Digite data do emprestimo:"))
    print("Emprestimo cadastrado com sucesso!\n")

def verificar_emprestimos():
    nome = input("Digite o nome do aluno que deseja verificar os emprestimos: ")
    if nome in cadastro_emprestimo:
        indice = cadastro_emprestimo.index(nome)
        dados = cadastro_emprestimo[indice:indice+3]
        rotulo = ["\nNome do aluno","Nome do livro","Data do emprestimo"]

        for rotulo, dados in zip(rotulo, dados):
            print(f"{rotulo}: {dados}")


    else:
        print("Aluno não encontrado.")

        
    
def sair():
    print("Saindo")
    exit()


while True:
    print("\nDigite 1 para cadastrar um livro")
    print("Digite 2 para ver os livros cadastrados")
    print("Digite 3 para cadastrar um emprestimo")
    print("Digite 4 para verificar todos os emprestimos")
    print("Digite 5 para cadastrar um aluno")
    print("Digite 9 para sair")

    opcao = input("escolha uma opção:")

    if opcao == "1":
        cadastrar_livro()

    elif opcao == "2":
        livros_cadastrados()

    elif opcao == "3":
        cadastrar_emprestimo()

    elif opcao == "4":
        verificar_emprestimos()

    elif opcao == "5":
        cadastrar_aluno()

    elif opcao == "9":
        sair()
    else:
        print("\nOpção invalida!")














