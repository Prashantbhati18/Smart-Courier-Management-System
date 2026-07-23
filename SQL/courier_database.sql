-- Create Database
CREATE DATABASE IF NOT EXISTS CourierDB;

USE CourierDB;

CREATE TABLE Customers (
    customer_id INT AUTO_INCREMENT PRIMARY KEY,
    customer_name VARCHAR(100) NOT NULL,
    phone VARCHAR(15),
    email VARCHAR(100),
    address VARCHAR(255)
);

CREATE TABLE Branches (
    branch_id INT AUTO_INCREMENT PRIMARY KEY,
    branch_name VARCHAR(100) NOT NULL,
    city VARCHAR(100),
    state VARCHAR(100)
);

CREATE TABLE Shipments (
    shipment_id INT AUTO_INCREMENT PRIMARY KEY,

    customer_id INT,
    branch_id INT,

    origin VARCHAR(100),
    destination VARCHAR(100),

    weight DECIMAL(8,2),

    booking_date DATE,
    expected_delivery DATE,
    actual_delivery DATE,

    status VARCHAR(30),

    shipping_cost DECIMAL(10,2),

    FOREIGN KEY (customer_id)
        REFERENCES Customers(customer_id),

    FOREIGN KEY (branch_id)
        REFERENCES Branches(branch_id)
);



INSERT INTO Customers
(customer_name, phone, email, address)
VALUES
('Rahul Sharma','9876543210','rahul@gmail.com','Delhi'),
('Priya Singh','9123456789','priya@gmail.com','Mumbai'),
('Amit Kumar','9988776655','amit@gmail.com','Chandigarh');


INSERT INTO Branches
(branch_name, city, state)
VALUES
('Delhi Hub','Delhi','Delhi'),
('Mumbai Hub','Mumbai','Maharashtra'),
('Chandigarh Hub','Chandigarh','Punjab');


INSERT INTO Shipments
(
customer_id,
branch_id,
origin,
destination,
weight,
booking_date,
expected_delivery,
actual_delivery,
status,
shipping_cost
)

VALUES

(1,1,'Delhi','Mumbai',5.5,'2026-07-20','2026-07-25',NULL,'Pending',330),

(2,2,'Mumbai','Delhi',8.0,'2026-07-18','2026-07-23','2026-07-22','Delivered',480),

(3,3,'Chandigarh','Jaipur',3.2,'2026-07-21','2026-07-26',NULL,'In Transit',192);