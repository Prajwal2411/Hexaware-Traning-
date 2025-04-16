from entity.product import Product

class Electronics(Product):
    def __init__(self, productid=None, productname=None, description=None, price=None, quantityinstock=None, brand=None, warrantyperiod=None):
        super().__init__(productid, productname, description, price, quantityinstock, type="electronics")
        self.brand = brand
        self.warrantyperiod = warrantyperiod

    def __str__(self):
        return super().__str__() + f", Brand: {self.brand}, Warranty: {self.warrantyperiod} months"
