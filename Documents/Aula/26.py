id_cliente = 100

cursor.execute(f"DELETE * FROM cliente WHERE id_cliente = %s", (id_cliente))