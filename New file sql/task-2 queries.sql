
use TechShop;
-- 1. Retrieve names and emails of all customers
SELECT FirstName, LastName, Email FROM Customers;
GO

-- 2. List all orders with order dates and corresponding customer names
SELECT o.OrderID, o.OrderDate, c.FirstName, c.LastName 
FROM Orders o
JOIN Customers c ON o.CustomerID = c.CustomerID;


-- 3. Insert a new customer
INSERT INTO Customers (FirstName, LastName, Email, Phone, Address) 
VALUES ('Geoge', 'Can', 'george1.can@example.com', '9998887766', '123 Washington Ave');


-- 4. Increase prices of all products by 10%
UPDATE Products 
SET Price = Price * 1.10;


-- 5. Delete a specific order and its associated order details (Input OrderID)
DECLARE @OrderIDToDelete INT = 1;
DELETE FROM OrderDetails WHERE OrderID = @OrderIDToDelete;
DELETE FROM Orders WHERE OrderID = @OrderIDToDelete;


-- 6. Insert a new order
INSERT INTO Orders (CustomerID, OrderDate, TotalAmount) 
VALUES (2, GETDATE(), 650.00);


-- 7. Update customer contact info (Input CustomerID)
DECLARE @CustomerIDToUpdate INT = 3;
UPDATE Customers 
SET Email = 'newemail@example.com', Address = 'Updated Address' 
WHERE CustomerID = @CustomerIDToUpdate;


-- 8. Recalculate and update total order cost
UPDATE Orders 
SET TotalAmount = (
    SELECT SUM(p.Price * od.Quantity) 
    FROM OrderDetails od
    JOIN Products p ON od.ProductID = p.ProductID
    WHERE od.OrderID = Orders.OrderID
);


-- 9. Delete all orders for a specific customer
DECLARE @CustomerIDToDelete INT = 5;
DELETE FROM OrderDetails WHERE OrderID IN (SELECT OrderID FROM Orders WHERE CustomerID = @CustomerIDToDelete);
DELETE FROM Orders WHERE CustomerID = @CustomerIDToDelete;


-- 10. Insert a new product
INSERT INTO Products (ProductName, Description, Price) 
VALUES ('Apple Mac', 'Immersive Performance oriented', 750000.00);

