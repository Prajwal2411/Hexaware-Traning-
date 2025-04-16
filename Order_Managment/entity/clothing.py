from entity.product import Product

class Clothing(Product):
    def __init__(self, productid=None, productname=None, description=None, price=None, quantityinstock=None, size=None, color=None):
        super().__init__(productid, productname, description, price, quantityinstock, type="clothing")
        self.size = size
        self.color = color

    def __str__(self):
        return super().__str__() + f", Size: {self.size}, Color: {self.color}"
