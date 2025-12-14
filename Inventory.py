from Product import Product

class Inventory:

    productList = []


    @staticmethod
    def createProduct(product):
        Inventory.productList.append(product)


    @staticmethod
    def deleteProduct(id):
        for i, product in enumerate(Inventory.productList):
            if (product.id == id):
                Inventory.productList.remove(i)
                print(f"Le produit d'id {id} a bien été supprimé")
                return
            print(f"Le produit d'id {id} est introuvable")

    
    @staticmethod
    def getDetails(id=None, name=None):
        if (id == None and name == None):
            raise ValueError
        
        if (id == None):
            for product in Inventory.productList:
                if (product.name == name):
                    return product.details
                
        if (name == None):
            for product in Inventory.productList:
                if (product.id == id):
                    return product.details