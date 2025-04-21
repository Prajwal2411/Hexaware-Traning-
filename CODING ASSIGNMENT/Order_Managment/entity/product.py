class Product:
    def __init__(self, productid=None, productname=None, description=None, price=None, quantityinstock=None, type=None):
        self.productid = productid
        self.productname = productname
        self.description = description
        self.price = price
        self.quantityinstock = quantityinstock
        self.type = type

    def __str__(self):
        return (f"ProductID: {self.productid}, Name: {self.productname}, Description: {self.description}, "
                f"Price: {self.price}, Quantity: {self.quantityinstock}, Type: {self.type}")
