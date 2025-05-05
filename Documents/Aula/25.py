data_pedido = 20230101

cursor.execute(f"DELETE * FROM pedidos WHERE data_pedido = %s",(data_pedido))
