titulo = "Python Basico"
autor = "João Silva"
ano = 2023

sql = "INSET INTO livros (titulo, autor, ano) VALUES (%s, %s, %s)"
val = (titulo, autor, ano)

cursor.execute(sql, val)

