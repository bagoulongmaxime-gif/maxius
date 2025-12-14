from Product import Product
from Inventory import Inventory

class Order:

    def __init__(self, date):
        self.elements = []
        self.date = date


    def createOrder(self):
        for product in Inventory.productList:
            for element in self.elements:
                if (product.name == element[0] and product.quantity >= element[1]):
                    product.quantity -= element[1]



    def processOrder(self, name, newQantity):
        for element in self.elements:
            if (element[0] == name and newQantity <= element[1]):
                element[1] = 