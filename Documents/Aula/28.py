cargo = "gerente"

cursor.execute(f"UPDATE funcionarios set salario = salario * 500 where cargo = %s", (cargo))