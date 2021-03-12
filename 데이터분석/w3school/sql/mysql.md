### sql 

https://www.w3schools.com/sql/default.asp

#### query 

SELECT * FROM Customers;    
SELECT DISTINCT Country FROM Customers;  
select count(distinct customerName) from customers;  

SELECT * FROM Customers WHERE Country='Germany' AND City='Berlin';  

SELECT * FROM Customers ORDER BY Country ASC, CustomerName DESC;  

select * FROM Customers WHERE addressline2 IS NULL;  

SELECT * FROM Customers LIMIT 3;  

SELECT MAX(buyPrice) AS LargestPrice FROM Products;  
min,max,sum,avg,count  

SELECT * FROM Customers WHERE CustomerName NOT LIKE '%_or%';  

SELECT * FROM Customers WHERE City LIKE '[!bsp]%';   
[a-c],[s_s%ss%] ...  

SELECT * FROM Customers WHERE Country NOT IN ('Germany', 'France', 'UK');  

SELECT * FROM Products WHERE Price BETWEEN 10 AND 20;  

#### join 

SELECT Orders.OrderID, Customers.CustomerName, Orders.OrderDate FROM Orders INNER JOIN Customers ON Orders.CustomerID=Customers.CustomerID;   

SELECT City FROM Customers UNION SELECT City FROM offices;  

SELECT COUNT(customername), Country FROM Customers GROUP BY Country;  

SELECT count(distinct e.LastName), COUNT(o.OrderID) AS NumberOfOrders FROM Orders as o INNER JOIN employees as e ON o.EmployeeID = e.EmployeeID WHERE LastName = 'Davolio' OR LastName = 'Fuller' GROUP BY LastName HAVING COUNT(o.OrderID) > 25;  
        

#### manipulate 

INSERT INTO Customers (CustomerName, City, Country)
VALUES ('Cardinal', 'Stavanger', 'Norway');  

UPDATE Customers SET ContactName='Juan' WHERE Country='Mexico';   

DELETE FROM Customers WHERE CustomerName='Alfreds Futterkiste';   
DELETE FROM table_name;  

#### definition 

CREATE DATABASE testDB;  

DROP DATABASE testDB;  

BACKUP DATABASE testDB TO DISK = 'D:\backups\testDB.bak';  


