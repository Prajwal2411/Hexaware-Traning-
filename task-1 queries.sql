
CREATE DATABASE TechShop;

USE TechShop;

CREATE TABLE Customers (
    CustomerID INT IDENTITY(1,1) PRIMARY KEY,
    FirstName VARCHAR(50) NOT NULL,
    LastName VARCHAR(50) NOT NULL,
    Email VARCHAR(100) UNIQUE NOT NULL,
    Phone VARCHAR(15),
    Address VARCHAR(255)
);

CREATE TABLE Products (
    ProductID INT IDENTITY(1,1) PRIMARY KEY,
    ProductName VARCHAR(100) NOT NULL,
    Description TEXT,
    Price DECIMAL(10,2) NOT NULL CHECK (Price >= 0)
);

CREATE TABLE Orders (
    OrderID INT IDENTITY(1,1) PRIMARY KEY,
    CustomerID INT NOT NULL,
    OrderDate DATETIME DEFAULT GETDATE(),
    TotalAmount DECIMAL(10,2) DEFAULT 0,
    FOREIGN KEY (CustomerID) REFERENCES Customers(CustomerID) ON DELETE CASCADE
);

CREATE TABLE OrderDetails (
    OrderDetailID INT IDENTITY(1,1) PRIMARY KEY,
    OrderID INT NOT NULL,
    ProductID INT NOT NULL,
    Quantity INT CHECK (Quantity > 0),
    FOREIGN KEY (OrderID) REFERENCES Orders(OrderID) ON DELETE CASCADE,
    FOREIGN KEY (ProductID) REFERENCES Products(ProductID)
);


CREATE TABLE Inventory (
    InventoryID INT IDENTITY(1,1) PRIMARY KEY,
    ProductID INT NOT NULL UNIQUE,
    QuantityInStock INT DEFAULT 0 CHECK (QuantityInStock >= 0),
    LastStockUpdate DATETIME DEFAULT GETDATE(),
    FOREIGN KEY (ProductID) REFERENCES Products(ProductID)
);

INSERT INTO Customers (FirstName, LastName, Email, Phone, Address)
VALUES 
    ('John', 'Doe', 'john.doe@example.com', '1234567890', '123 Main St'),
    ('Jane', 'Smith', 'jane.smith@example.com', '0987654321', '456 Oak St'),
    ('Alice', 'Johnson', 'alice.johnson@example.com', '1122334455', '789 Pine St'),
    ('Bob', 'Williams', 'bob.williams@example.com', '2233445566', '321 Elm St'),
    ('Charlie', 'Brown', 'charlie.brown@example.com', '3344556677', '654 Birch St'),
    ('David', 'Davis', 'david.davis@example.com', '4455667788', '987 Cedar St'),
    ('Emma', 'Wilson', 'emma.wilson@example.com', '5566778899', '741 Maple St'),
    ('Frank', 'Miller', 'frank.miller@example.com', '6677889900', '852 Spruce St'),
    ('Grace', 'Moore', 'grace.moore@example.com', '7788990011', '963 Walnut St'),
    ('Hannah', 'Taylor', 'hannah.taylor@example.com', '8899001122', '159 Chestnut St');

INSERT INTO Products (ProductName, Description, Price)
VALUES
('Laptop', 'High-performance laptop with Intel i7 and SSD', 95000.00),
('Smartphone', 'Latest 5G smartphone with AMOLED display', 65000.00),
('Tablet', 'Lightweight tablet with stylus support', 40000.00),
('Smartwatch', 'Feature-rich smartwatch with SpO2 monitor', 20000.00),
('Wireless Earbuds', 'Noise-cancelling earbuds with deep bass', 12000.00),
('Gaming Console', 'Next-gen gaming console with 1TB storage', 35000.00),
('Monitor', '4K UHD monitor with HDR support', 25000.00),
('Keyboard', 'RGB mechanical gaming keyboard', 8000.00),
('Mouse', 'Ergonomic wireless mouse with high DPI', 4000.00),
('Headphones', 'Studio-quality over-ear headphones', 18000.00);



INSERT INTO Orders (CustomerID, OrderDate, TotalAmount)
VALUES 
    (1, '2024-03-01', 20000.00),
    (2, '2024-03-02', 7000.00),
    (3, '2024-03-03', 1500.00),
    (4, '2024-03-04', 15250.00),
    (5, '2024-03-05', 80025.00),
    (6, '2024-03-06', 1230.00),
    (7, '2024-03-07', 800.00),
    (8, '2024-03-08', 300.00),
    (9, '2024-03-09', 700.00),
    (10, '2024-03-10', 9700.00);

INSERT INTO OrderDetails (OrderID, ProductID, Quantity)
VALUES 
    (1, 1, 10),
    (2, 2, 1),
    (3, 3, 12),
    (4, 4, 8),
    (5, 5, 3),
    (6, 6, 1),
    (7, 7, 2),
    (8, 8, 1),
    (9, 9, 2),
    (10, 10, 1);

INSERT INTO Inventory (ProductID, QuantityInStock)
VALUES 
    (1, 8),
    (2, 0),
    (3, 5),
    (4, 6),
    (5, 3),
    (6, 1),
    (7, 2),
    (8, 0),
    (9, 2),
    (10, 25);

