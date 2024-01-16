/* 
    Oracle SQL - PL/SQL
    Car dealership @ The future is in the past
*/

/* 1. Data Definition Language */

// Create Manufacturers Table
CREATE TABLE Manufacturers (
    manufacturer_id NUMBER PRIMARY KEY,
    manufacturer_name VARCHAR2(100) UNIQUE NOT NULL,
    manufacturer_country VARCHAR2(50)
);

// Create Cars Table
CREATE TABLE Cars (
    car_id NUMBER PRIMARY KEY,
    manufacturer_id NUMBER,
    model_name VARCHAR2(100) NOT NULL,
    year NUMBER(4) NOT NULL,
    price NUMBER(10, 2) NOT NULL,
    color VARCHAR2(50),
    mileage NUMBER(10, 2),
    fuel_type VARCHAR2(50),
    CONSTRAINT fk_manufacturer FOREIGN KEY (manufacturer_id) REFERENCES Manufacturers(manufacturer_id)
);

// Create Customers Table
CREATE TABLE Customers (
    customer_id NUMBER PRIMARY KEY,
    first_name VARCHAR2(50) NOT NULL,
    last_name VARCHAR2(50) NOT NULL,
    email VARCHAR2(100) UNIQUE NOT NULL,
    phone_number VARCHAR2(15),
    citizenship_id NUMBER
);

// Create Employees Table
CREATE TABLE Employees (
    employee_id NUMBER PRIMARY KEY,
    first_name VARCHAR2(50) NOT NULL,
    last_name VARCHAR2(50) NOT NULL,
    position VARCHAR2(50),
    hire_date DATE
);

// Create Sales Table
CREATE TABLE Sales (
    sale_id NUMBER PRIMARY KEY,
    car_id NUMBER,
    customer_id NUMBER,
    employee_id NUMBER,
    sale_date DATE NOT NULL,
    sale_price NUMBER(10, 2) NOT NULL,
    CONSTRAINT fk_car FOREIGN KEY (car_id) REFERENCES Cars(car_id),
    CONSTRAINT fk_customer FOREIGN KEY (customer_id) REFERENCES Customers(customer_id),
    CONSTRAINT fk_employee FOREIGN KEY (employee_id) REFERENCES Employees(employee_id)
);

// Create Rentals Table
CREATE TABLE Rentals (
    rental_id NUMBER PRIMARY KEY,
    car_id NUMBER,
    customer_id NUMBER,
    employee_id NUMBER,
    start_date DATE NOT NULL,
    end_date DATE NOT NULL,
    rental_price_per_day NUMBER(10, 2) NOT NULL,
    CONSTRAINT fk_car_rental FOREIGN KEY (car_id) REFERENCES Cars(car_id),
    CONSTRAINT fk_customer_rental FOREIGN KEY (customer_id) REFERENCES Customers(customer_id),
    CONSTRAINT fk_employee_rental FOREIGN KEY (employee_id) REFERENCES Employees(employee_id)
);

// ALTER integrity constraint
ALTER TABLE Customers
ADD CONSTRAINT phone_number_unique UNIQUE (phone_number);

// New column for Cars table 
ALTER TABLE Cars
ADD gearbox_type VARCHAR2(50);

// Modify datatype lengtn for a column of Customers table
ALTER TABLE Customers
MODIFY phone_number VARCHAR2(20);

// Rename Table
ALTER TABLE Manufacturers
RENAME TO Make;

// Remove all the tables
DROP TABLE Rentals;
DROP TABLE Sales;
DROP TABLE Cars;
DROP TABLE Customers;
DROP TABLE Employees;
DROP TABLE Manufacturers;
-- DROP TABLE MAKE;