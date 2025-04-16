from dao.order_processor import OrderProcessor
from entity.user import User
from entity.electronics import Electronics
from entity.clothing import Clothing


def main():
    print("Starting Order Management System...")
    try:
        processor = OrderProcessor()  # Initialize the OrderProcessor
        print("Database connection established successfully.")
    except Exception as e:
        print(f"Error initializing OrderProcessor: {e}")
        return  # Exit if the database connection fails

    while True:
        print("\n--- Order Management System ---")
        print("1. Create User")
        print("2. Create Product")
        print("3. Create Order")
        print("4. Cancel Order")
        print("5. Get All Products")
        print("6. Get Orders by User")
        print("7. Show All Users")
        print("8. Show Product Details by ID")
        print("9. Cancel/Delete User")  # New option
        print("10. Delete Product")  # New option
        print("11. Exit")

        try:
            choice = input("Enter your choice: ").strip()

            if choice == "1":
                # Create User
                print("\n--- Create User ---")
                username = input("Enter username: ").strip()
                password = input("Enter password: ").strip()
                role = input("Enter role (admin/user): ").strip().lower()

                if role not in ["admin", "user"]:
                    print("Invalid role. Please enter 'admin' or 'user'.")
                    continue

                user = User(username=username, password=password, role=role)
                processor.create_user(user)
                print("User created successfully.")

            elif choice == "2":
                # Create Product
                print("\n--- Create Product ---")
                product_name = input("Enter product name: ").strip()
                description = input("Enter description: ").strip()
                try:
                    price = float(input("Enter price: ").strip())
                    quantity_in_stock = int(input("Enter quantity in stock: ").strip())
                except ValueError:
                    print("Invalid input for price or quantity. Please enter valid numeric values.")
                    continue
                product_type = input("Enter type (electronics/clothing): ").strip().lower()

                if product_type == "electronics":
                    brand = input("Enter brand: ").strip()
                    try:
                        warranty_period = int(input("Enter warranty period (in months): ").strip())
                    except ValueError:
                        print("Invalid input for warranty period. Please enter a numeric value.")
                        continue
                    product = Electronics(
                        productname=product_name,
                        description=description,
                        price=price,
                        quantityinstock=quantity_in_stock,
                        brand=brand,
                        warrantyperiod=warranty_period
                    )
                elif product_type == "clothing":
                    size = input("Enter size: ").strip()
                    color = input("Enter color: ").strip()
                    product = Clothing(
                        productname=product_name,
                        description=description,
                        price=price,
                        quantityinstock=quantity_in_stock,
                        size=size,
                        color=color
                    )
                else:
                    print("Invalid product type. Please choose either 'electronics' or 'clothing'.")
                    continue

                # Validate admin user
                admin_username = input("Enter admin username: ").strip()
                admin_password = input("Enter admin password: ").strip()
                user = User(username=admin_username, password=admin_password, role="admin")

                try:
                    processor.create_product(user, product)
                    print("Product created successfully.")
                except PermissionError as e:
                    print(e)
                except Exception as e:
                    print(f"Error creating product: {e}")

            elif choice == "3":
                # Create Order
                print("\n--- Create Order ---")
                try:
                    user_id = int(input("Enter user ID: ").strip())
                except ValueError:
                    print("Invalid user ID. Please enter a numeric value.")
                    continue

                user = User(userid=user_id)
                try:
                    num_products = int(input("Enter number of products to order: ").strip())
                except ValueError:
                    print("Invalid number of products. Please enter a numeric value.")
                    continue

                products = {}
                for _ in range(num_products):
                    try:
                        product_id = int(input("Enter product ID: ").strip())
                        quantity = int(input("Enter quantity: ").strip())
                        products[product_id] = quantity
                    except ValueError:
                        print("Invalid product ID or quantity. Please enter numeric values.")
                        continue

                try:
                    processor.create_order(user, products)
                    print("Order created successfully.")
                except Exception as e:
                    print(f"Error creating order: {e}")

            elif choice == "4":
                # Cancel Order
                print("\n--- Cancel Order ---")
                try:
                    user_id = int(input("Enter user ID: ").strip())
                    order_id = int(input("Enter order ID to cancel: ").strip())
                except ValueError:
                    print("Invalid input for user ID or order ID. Please enter numeric values.")
                    continue

                try:
                    processor.cancel_order(user_id, order_id)
                    print(f"Order {order_id} cancelled successfully.")
                except Exception as e:
                    print(f"Error cancelling order: {e}")

            elif choice == "5":
                # Get All Products
                print("\n--- Get All Products ---")
                try:
                    products = processor.get_all_products()
                    if products:
                        for product in products:
                            print(product)
                    else:
                        print("No products found.")
                except Exception as e:
                    print(f"Error fetching products: {e}")

            elif choice == "6":
                # Get Orders by User
                print("\n--- Get Orders by User ---")
                try:
                    user_id = int(input("Enter user ID: ").strip())
                    user = User(userid=user_id)
                    orders = processor.get_orders_by_user(user)
                    if orders:
                        for order in orders:
                            print(order)
                    else:
                        print("No orders found for this user.")
                except Exception as e:
                    print(f"Error fetching orders: {e}")

            elif choice == "7":
                # Show All Users
                print("\n--- Show All Users ---")
                try:
                    users = processor.get_all_users()  # New DAO method to retrieve all users
                    if users:
                        for user in users:
                            print(user)
                    else:
                        print("No users found.")
                except Exception as e:
                    print(f"Error fetching users: {e}")

            elif choice == "8":
                # Show Product Details
                print("\n--- Show Product Details by ID ---")
                try:
                    product_id = int(input("Enter product ID: ").strip())
                    product = processor.get_product_by_id(product_id)  # New DAO method for product details
                    if product:
                        print(product)
                    else:
                        print(f"No product found with ID {product_id}.")
                except Exception as e:
                    print(f"Error fetching product details: {e}")


            elif choice == "9":
                # Cancel/Delete User
                print("\n--- Cancel/Delete User ---")
                try:
                    user_id = int(input("Enter user ID to delete: ").strip())
                except ValueError:
                    print("Invalid user ID. Please enter a numeric value.")
                    continue
                try:
                    processor.delete_user(user_id)
                    print(f"User with ID {user_id} deleted successfully.")
                except Exception as e:
                    print(f"Error deleting user: {e}")
            elif choice == "10":
                # Delete Product
                print("\n--- Delete Product ---")
                try:
                    product_id = int(input("Enter product ID to delete: ").strip())
                except ValueError:
                    print("Invalid product ID. Please enter a numeric value.")
                    continue
                try:
                    processor.delete_product(product_id)
                    print(f"Product with ID {product_id} deleted successfully.")
                except Exception as e:
                    print(f"Error deleting product: {e}")

            elif choice == "11":
                # Exit
                print("Exiting the system...")
                processor.close_connection()
                break

            else:
                print("Invalid choice. Please try again.")

        except Exception as e:
            print(f"An unexpected error occurred: {e}")


if __name__ == "__main__":
    try:
        main()
    except Exception as e:
        print(f"An error occurred: {e}")
