preco = "preco" <= 50

cursor.execute(f"SELECT nome, preco FROM produtos where preco = %s", (preco))