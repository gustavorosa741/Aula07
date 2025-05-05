id_pedido = 500

cursor.execute(f"UPDATE status INTO pedidos WHERE id_pedido = %s", (id_pedido))
