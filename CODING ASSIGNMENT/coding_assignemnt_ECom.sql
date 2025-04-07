create database Store1; 


use Store1;

-- Customers table
create table customers (
    customer_id INT PRIMARY KEY,
    name VARCHAR(255),
    email VARCHAR(255) UNIQUE,
    password VARCHAR(255)
);

-- Products table
CREATE TABLE products (
    product_id INT PRIMARY KEY,
    name VARCHAR(255),
    price DECIMAL(10,2),
    description TEXT,
    stockQuantity INT
);

-- Cart table
create table cart (
    cart_id INT PRIMARY KEY,
    customer_id INT,
    product_id INT,
    quantity INT,
    FOREIGN KEY (customer_id) REFERENCES customers(customer_id),
    FOREIGN KEY (product_id) REFERENCES products(product_id)
);

-- Orders table
create table orders (
    order_id INT PRIMARY KEY,
    customer_id INT,
    order_date DATE,
    total_price DECIMAL(10,2),
    shipping_address TEXT,
    FOREIGN KEY (customer_id) REFERENCES customers(customer_id)
);

-- Order_items table
create table order_items (
    order_item_id INT PRIMARY KEY,
    order_id INT,
    product_id INT,
    quantity INT,
    itemAmount DECIMAL(10,2),
    FOREIGN KEY (order_id) REFERENCES orders(order_id),
    FOREIGN KEY (product_id) REFERENCES products(product_id)
);


-- Values to add in the table: 

-- 1) into product table.

insert into  products (product_id, name, price, description, stockQuantity) VALUES
(1, 'Laptop', 800.00, 'High-performance laptop', 10),
(2, 'Smartphone', 600.00, 'Latest smartphone', 15),
(3, 'Tablet', 300.00, 'Portable tablet', 20),
(4, 'Headphones', 150.00, 'Noise-canceling', 30),
(5, 'TV', 900.00, '4K Smart TV', 5),
(6, 'Coffee Maker', 50.00, 'Automatic coffee maker', 25),
(7, 'Refrigerator', 700.00, 'Energy-efficient', 10),
(8, 'Microwave Oven', 80.00, 'Countertop microwave', 15),
(9, 'Blender', 70.00, 'High-speed blender', 20),
(10, 'Vacuum Cleaner', 120.00, 'Bagless vacuum cleaner', 10);

select * from products;

-- 2) into customer table.

insert into customers (customer_id, name, email, password) VALUES
(1, 'John Doe', 'johndoe@example.com', 'password123'),
(2, 'Jane Smith', 'janesmith@example.com', 'password456'),
(3, 'Robert Johnson', 'robert@example.com', 'password789'),
(4, 'Sarah Brown', 'sarah@example.com', 'password321'),
(5, 'David Lee', 'david@example.com', 'password654'),
(6, 'Laura Hall', 'laura@example.com', 'password987'),
(7, 'Michael Davis', 'michael@example.com', 'password159'),
(8, 'Emma Wilson', 'emma@example.com', 'password753'),
(9, 'William Taylor', 'william@example.com', 'password852'),
(10, 'Olivia Adams', 'olivia@example.com', 'password369');

select * from customers;

-- 3) into order table .

insert into orders (order_id, customer_id, order_date, total_price, shipping_address) VALUES
(1, 1, '2023-01-05', 1200.00, '123 Main St, City'),
(2, 2, '2023-02-10', 900.00, '456 Elm St, Town'),
(3, 3, '2023-03-15', 300.00, '789 Oak St, Village'),
(4, 4, '2023-04-20', 150.00, '101 Pine St, Suburb'),
(5, 5, '2023-05-25', 1800.00, '234 Cedar St, District'),
(6, 6, '2023-06-30', 400.00, '567 Birch St, County'),
(7, 7, '2023-07-05', 700.00, '890 Maple St, State'),
(8, 8, '2023-08-10', 160.00, '321 Redwood St, Country'),
(9, 9, '2023-09-15', 140.00, '432 Spruce St, Province'),
(10, 10, '2023-10-20', 1400.00, '765 Fir St, Territory');

select * from orders;


-- 4) into order items table.

insert into order_items (order_item_id, order_id, product_id, quantity, itemAmount) VALUES
(1, 1, 1, 2, 1600.00),
(2, 1, 3, 1, 300.00),
(3, 2, 2, 3, 1800.00),
(4, 3, 5, 2, 1800.00),
(5, 4, 4, 4, 600.00),
(6, 4, 6, 1, 50.00),
(7, 5, 1, 1, 800.00),
(8, 5, 2, 2, 1200.00),
(9, 6, 10, 2, 240.00),
(10, 6, 9, 3, 210.00);

select * from  order_items;

-- 5) into cart table.

insert into cart (cart_id, customer_id, product_id, quantity) VALUES
(1, 1, 1, 1),
(2, 2, 3, 2),
(3, 3, 5, 1),
(4, 4, 2, 1),
(5, 5, 7, 3),
(6, 6, 8, 2),
(7, 7, 4, 1),
(8, 8, 6, 2),
(9, 9, 9, 1),
(10, 10, 10, 1);

select * from cart;



-- Questiones to solve :

-- 1. Update refrigerator product price to 800.
update products set price = 800 where name = 'Refrigerator';

-- 2. Remove all cart items for a specific customer.
delete from cart where customer_id = 5;

-- 3. Retrieve Products Priced Below $100.
select * from products where price < 100;

-- 4. Find Products with Stock Quantity Greater Than 5.
select * from products where stockQuantity > 5;

-- 5. Retrieve Orders with Total Amount Between $500 and $1000.
select * from orders where total_price between 500 and 1000;

-- 6. Find Products which name end with letter 'r'.
select * from products where name LIKE '%r';


-- 7. Retrieve Cart Items for Customer 5.    (the customer with the id 5 hase been removed from the cart for query number 2)
select * from cart where customer_id = 5;


-- 8. Find Customers Who Placed Orders in 2023.
select * from customers where customer_id in (select customer_id from orders where year(order_date) = 2023);


-- 9. Determine the Minimum Stock Quantity for Each Product Category.
select min(stockQuantity)as low_stock from products;



-- 10. Calculate the Total Amount Spent by Each Customer.
select customer_id, sum(total_price) as total_spent from orders group by customer_id;


-- 11. Find the Average Order Amount for Each Customer.
select customer_id, avg(total_price) as avg_order from orders group by customer_id;


-- 12. Count the Number of Orders Placed by Each Customer.
select customer_id, count(order_id) as order_count from orders group by customer_id;


-- 13. Find the Maximum Order Amount for Each Customer.
select customer_id, max(total_price) as max_order from orders group by customer_id;


-- 14. Get Customers Who Placed Orders Totaling Over $1000.
select customer_id from orders group by customer_id having sum(total_price) > 1000;



-- 15. Subquery to Find Products Not in the Cart.
select * from products where product_id not in (select product_id from cart);



-- 16. Subquery to Find Customers Who Haven't Placed Orders.
select * from customers where customer_id not in (select customer_id from orders);



-- 17. Subquery to Calculate the Percentage of Total Revenue for a Product.
select product_id, (sum(itemamount) / (select sum(total_price) from orders)) * 100 as revenue_percentage from order_items  
group by product_id;



-- 18. Subquery to Find Products with Low Stock.
select * from products where stockquantity < 5;


-- 19. Subquery to Find Customers Who Placed High-Value Orders.
select distinct customer_id from orders where total_price > 1000;

