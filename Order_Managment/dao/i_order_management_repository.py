from abc import ABC, abstractmethod

class IOrderManagementRepository(ABC):
    @abstractmethod
    def create_user(self, user):
        pass

    @abstractmethod
    def create_product(self, user, product):
        pass

    @abstractmethod
    def create_order(self, user, products):
        pass

    @abstractmethod
    def cancel_order(self, userid, orderid):
        pass

    @abstractmethod
    def get_all_products(self):
        pass

    @abstractmethod
    def get_orders_by_user(self, user):
        pass

    @abstractmethod
    def get_all_users(self):
        pass

    @abstractmethod
    def get_product_by_id(self, product_id):
        pass

    @abstractmethod
    def delete_product(self, product_id):
        pass

    @abstractmethod
    def delete_user(self, user_id):
        pass


