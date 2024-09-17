from models.product import Product, History
from repository.products import *

print("Choose an option:")
print("1 - List categories")
print("2 - List products")
print("3 - Get price history")
print("4 - Create product")
print("5 - Register product price")

option = int(input("Option: "))

if option == 1:
    list_categories()
elif option == 2:
    list_products()
elif option == 3:
    try:
        product_id =int(input("Product ID: "))
        list_product_history(product_id)
    except ValueError as e:
        print("Invalid option:", e.__str__())
elif option == 4:
    name = input("Product name: ")
    brand = input("Product brand: ")
    list_categories()
    category = int(input("Category ID: "))
    product = Product(name=name, brand=brand, category=category)
    create_product(product)
elif option == 5:
    try:
        list_products()
        product_id = int(input("\nProduct ID: "))
        price = float(input("Price: "))
        link = input("Link: ")
        history = History(price, product_id=product_id, link=link)
        register_price(history)
    except ValueError as e:
        print("Invalid option:", e.__str__())