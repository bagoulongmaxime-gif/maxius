class Product:
    current_id = 0

    def __init__(self, id, name, category, date, price):
        Product.current_id += 1
        self.id = Product.current_id
        self.name = name
        self.category = category
        self.date = date
        self.price = price
        self.quantity = 1

    
    def updateProduct(self, price=None, quantity=None):
        if (price == None and quantity == None):
            raise ValueError
        
        if (quantity == None and price > 0):
            self.price = price
        
        if (price == None and quantity > 0):
            self.quantity = quantity

    
    @property
    def details(self):
        return (self.id, self.name, self.category, self.date, self.price, self.quantity)
