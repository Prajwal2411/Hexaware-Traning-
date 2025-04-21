class OrderItem:
    def __init__(self, orderid=None, productid=None, quantity=None):
        self.orderid = orderid
        self.productid = productid
        self.quantity = quantity

    def __str__(self):
        return f"OrderID: {self.orderid}, ProductID: {self.productid}, Quantity: {self.quantity}"
