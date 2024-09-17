from datetime import datetime

class History:
    def __init__(self, price, dateTime=None, product_id=None, link=None):
        self.price = price
        self.product_id = product_id
        self.link = link
        if dateTime != None:
            self.dateTime = dateTime.strftime('%d/%m/%Y')

class Product:
    def __init__(self, id=None, name=None, brand=None, category=None):
        self.id = id
        self.name = name
        self.brand = brand
        self.category = category
        self.history = []  # Inicializa uma lista vazia para o histórico

    def add_history(self, price, dateTime):
        # Adiciona um novo objeto History à lista de histórico
        self.history.append(History(price, dateTime))

    def __str__(self, format_type='simple'):
        if format_type == 'simple':
            return f"ID: {self.id} - Product: {self.name} - Brand: {self.brand} - Category: {self.category}"
        elif format_type == 'historic':
            # Formata a string para exibir o histórico de preços
            result = f"Product: {self.name}\n"
            for h in self.history:
                result += f"Price: {h.price} - Date: {h.dateTime}\n"
            return result
