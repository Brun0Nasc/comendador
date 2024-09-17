from config.config import connect_database
from models.product import Product, History

def list_categories():
    conn = connect_database()

    with conn.cursor() as cur:
        cur.execute("SELECT * FROM t_categoria_produto;")
        list = cur.fetchall()
        for row in list:
            print(row)
    
    conn.close()

def list_products():
    conn = connect_database()

    with conn.cursor() as cur:
        cur.execute("""SELECT TP.id,
                           TP.nome,
                           TP.descricao marca,
                           TCP.nome categoria
                    FROM t_produto TP
                    JOIN t_categoria_produto TCP ON TP.categoria_id = TCP.id
                    ORDER BY TP.id;""")
        list = cur.fetchall()

        products = []

        for row in list:
            product = Product(row[0], row[1], row[2], row[3])
            products.append(product)
        
        for p in products:
            print(p.__str__())
    
    conn.close()

def list_product_history(product_id: int):
    conn = connect_database()

    with conn.cursor() as cur:
        cur.execute(f"""SELECT TP.nome, 
                               THP.preco, 
                               THP.data_criacao
                        FROM t_produto TP
                        JOIN t_historico_preco THP ON TP.id = THP.produto_id
                        WHERE TP.id = {product_id}
                        ORDER BY THP.data_criacao DESC;""")
        list = cur.fetchall()

        if len(list) == 0:
            print("Product not found.")
            return

        p = Product()
        for row in list:
            if p.name == None:
                p.name = row[0]
            p.add_history(row[1], row[2])
        print(p.__str__('historic'))
    
    conn.close()

def create_product(product: Product):
    conn = connect_database()

    with conn.cursor() as cur:
        cur.execute(f"""INSERT INTO t_produto (nome, descricao, categoria_id)
                       VALUES ('{product.name}', '{product.brand}', {product.category});""")
        conn.commit()
    
    conn.close()

def register_price(history: History):
    conn = connect_database()

    with conn.cursor() as cur:
        cur.execute(f"""INSERT INTO t_historico_preco (preco, produto_id, link)
                        VALUES ({history.price}, {history.product_id}, '{history.link}');""")
        conn.commit()
    
    conn.close()