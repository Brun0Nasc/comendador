import psycopg
import os
from dotenv import load_dotenv
from product import Product

def load_config():
    load_dotenv("creds.env")  # Load environment variables from .env file

    dbName = os.getenv("DB_NAME")
    dbUser = os.getenv("DB_USER")
    dbPass = os.getenv("DB_PASSWORD")
    dbHost = os.getenv("DB_HOST")
    dbPort = os.getenv("DB_PORT")

    return f"dbname={dbName} user={dbUser} host={dbHost} password={dbPass} port={dbPort}"

def connect_database():
    conn = psycopg.connect(load_config())
    return conn

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

def get_price_history(product_id):
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

print("Choose an option:")
print("1 - List categories")
print("2 - List products")
print("3 - Get price history")
option = input("Option: ")

if option == "1":
    list_categories()
elif option == "2":
    list_products()
elif option == "3":
    product_id = input("Product ID: ")
    get_price_history(product_id)
