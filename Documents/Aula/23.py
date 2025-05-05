nome = "Anna"
idade = 20
nota = 8.5


sql = "INSERT INTO alunos (nome, idade, nota) VALUES (%s, %s, %s) "
val = (nome, idade, nota,)

cursor.execute(sql, val)
