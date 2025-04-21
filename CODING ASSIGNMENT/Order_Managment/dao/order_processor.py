import pyodbc
from dao.i_order_management_repository import IOrderManagementRepository
from exception.user_not_found_exception import UserNotFoundException
from exception.order_not_found_exception import OrderNotFoundException
from exception.product_not_found_exception import ProductNotFoundException
from util.db_conn_util import DBConnUtil


class OrderProcessor(IOrderManagementRepository):
    def __init__(self):
        self.conn = DBConnUtil.get_connection()

    def create_user(self, user):
        cursor = self.conn.cursor()
        query = "INSERT INTO Users (username, password, role) VALUES (?, ?, ?)"
        try:
            cursor.execute(query, user.username, user.password, user.role)
            self.conn.commit()
            print("User created successfully.")
        except Exception as e:
            print("Error in create_user:", e)

    def create_product(self, user, product):
        if user.role.lower() != "admin":
            raise PermissionError("Only admins can create products.")
        cursor = self.conn.cursor()
        if product.type.lower() == "electronics":
            query1 = "INSERT INTO Product (productname, description, price, quantityinstock, type) VALUES (?, ?, ?, ?, ?)"
            query2 = "INSERT INTO Electronics (productid, brand, warrantyperiod) VALUES (?, ?, ?)"
            try:
                cursor.execute(query1, product.productname, product.description, product.price, product.quantityinstock,
                               product.type)
                self.conn.commit()
                product_id = cursor.lastrowid  # Get the ID of the inserted product
                cursor.execute(query2, product_id, product.brand, product.warrantyperiod)
                self.conn.commit()
                print("Electronics product created successfully.")
            except Exception as e:
                print("Error in create_product (electronics):", e)
        elif product.type.lower() == "clothing":
            query1 = "INSERT INTO Product (productname, description, price, quantityinstock, type) VALUES (?, ?, ?, ?, ?)"
            query2 = "INSERT INTO Clothing (productid, size, color) VALUES (?, ?, ?)"
            try:
                cursor.execute(query1, product.productname, product.description, product.price, product.quantityinstock,
                               product.type)
                self.conn.commit()
                product_id = cursor.lastrowid  # Get the ID of the inserted product
                cursor.execute(query2, product_id, product.size, product.color)
                self.conn.commit()
                print("Clothing product created successfully.")
            except Exception as e:
                print("Error in create_product (clothing):", e)
        else:
            print("Invalid product type.")

    def create_order(self, user, products):
        cursor = self.conn.cursor()
        # Check if the user exists
        check_user_query = "SELECT COUNT(*) FROM Users WHERE userid = ?"
        cursor.execute(check_user_query, user.userid)
        if cursor.fetchone()[0] == 0:
            raise UserNotFoundException("User not found.")
        # Insert the order
        order_query = "INSERT INTO Orders (userid) VALUES (?)"
        try:
            cursor.execute(order_query, user.userid)
            self.conn.commit()
            order_id = cursor.lastrowid  # Get the newly created order ID
            print(f"Order {order_id} created successfully for user {user.userid}.")
            # Insert each product into the OrderItems table
            order_items_query = "INSERT INTO OrderItems (orderid, productid, quantity) VALUES (?, ?, ?)"
            for product_id, quantity in products.items():
                cursor.execute(order_items_query, order_id, product_id, quantity)
            self.conn.commit()
            print(f"Order items added successfully to order {order_id}.")
        except Exception as e:
            print("Error in create_order:", e)

    def cancel_order(self, userid, orderid):
        cursor = self.conn.cursor()
        # Check if the order exists and belongs to the user
        check_order_query = "SELECT COUNT(*) FROM Orders WHERE orderid = ? AND userid = ?"
        cursor.execute(check_order_query, orderid, userid)
        if cursor.fetchone()[0] == 0:
            raise OrderNotFoundException("Order not found or does not belong to the user.")
        # Cancel the order
        cancel_order_query = "UPDATE Orders SET status = 'cancelled' WHERE orderid = ?"
        try:
            cursor.execute(cancel_order_query, orderid)
            self.conn.commit()
            print(f"Order {orderid} cancelled successfully.")
        except Exception as e:
            print("Error in cancel_order:", e)

    def get_all_products(self):
        cursor = self.conn.cursor()
        query = "SELECT * FROM Product"
        try:
            cursor.execute(query)
            rows = cursor.fetchall()
            products = []
            for row in rows:
                products.append({
                    "productid": row.productid,
                    "productname": row.productname,
                    "description": row.description,
                    "price": row.price,
                    "quantityinstock": row.quantityinstock,
                    "type": row.type
                })
            return products
        except Exception as e:
            print("Error in get_all_products:", e)
            return []

    def get_orders_by_user(self, user):
        cursor = self.conn.cursor()
        # Check if the user exists
        check_user_query = "SELECT COUNT(*) FROM Users WHERE userid = ?"
        cursor.execute(check_user_query, user.userid)
        if cursor.fetchone()[0] == 0:
            raise UserNotFoundException("User not found.")
        # Retrieve the user's orders
        orders_query = "SELECT o.orderid, o.orderdate, o.status, oi.productid, oi.quantity FROM Orders o " \
                       "INNER JOIN OrderItems oi ON o.orderid = oi.orderid WHERE o.userid = ?"
        try:
            cursor.execute(orders_query, user.userid)
            rows = cursor.fetchall()
            orders = []
            for row in rows:
                orders.append({
                    "orderid": row.orderid,
                    "orderdate": row.orderdate,
                    "status": row.status,
                    "productid": row.productid,
                    "quantity": row.quantity
                })
            return orders
        except Exception as e:
            print("Error in get_orders_by_user:", e)
            return []

    def get_all_users(self):
        cursor = self.conn.cursor()
        query = "SELECT userid, username, role FROM Users"
        try:
            cursor.execute(query)
            rows = cursor.fetchall()
            users = []
            for row in rows:
                users.append(f"UserID: {row.userid}, Username: {row.username}, Role: {row.role}")
            return users
        except Exception as e:
            print("Error in get_all_users:", e)
            return []

    def get_product_by_id(self, product_id):
        cursor = self.conn.cursor()
        query = "SELECT * FROM Product WHERE productid = ?"
        try:
            cursor.execute(query, product_id)
            row = cursor.fetchone()
            if row:
                return {
                    "ProductID": row.productid,
                    "Name": row.productname,
                    "Description": row.description,
                    "Price": row.price,
                    "QuantityInStock": row.quantityinstock,
                    "Type": row.type
                }
            return None
        except Exception as e:
            print("Error in get_product_by_id:", e)
            return None

    def delete_product(self, product_id):
        cursor = self.conn.cursor()
        # Check if the product exists
        check_product_query = "SELECT COUNT(*) FROM Product WHERE productid = ?"
        cursor.execute(check_product_query, product_id)
        if cursor.fetchone()[0] == 0:
            raise ProductNotFoundException(f"Product with ID {product_id} not found.")

        # Delete the product (including related entries in Electronics/Clothing)
        delete_electronics_query = "DELETE FROM Electronics WHERE productid = ?"
        delete_clothing_query = "DELETE FROM Clothing WHERE productid = ?"
        delete_product_query = "DELETE FROM Product WHERE productid = ?"
        try:
            cursor.execute(delete_electronics_query, product_id)  # Attempt to delete from Electronics
            cursor.execute(delete_clothing_query, product_id)  # Attempt to delete from Clothing
            cursor.execute(delete_product_query, product_id)  # Delete base product
            self.conn.commit()
            print(f"Product with ID {product_id} deleted successfully.")
        except Exception as e:
            print("Error in delete_product:", e)

    def delete_user(self, user_id):
        cursor = self.conn.cursor()
        try:
            # Delete orders linked to the user
            delete_orders_query = "DELETE FROM Orders WHERE userid = ?"
            cursor.execute(delete_orders_query, user_id)
            self.conn.commit()

            # Delete the user
            delete_user_query = "DELETE FROM Users WHERE userid = ?"
            cursor.execute(delete_user_query, user_id)
            self.conn.commit()

            print(f"User with ID {user_id} and their associated orders have been deleted successfully.")
        except Exception as e:
            print("Error in delete_user:", e)

    def close_connection(self):
        self.conn.close()
