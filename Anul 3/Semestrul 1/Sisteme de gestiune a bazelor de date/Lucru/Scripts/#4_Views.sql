/* 4. Virtual tables (views) */

// Sales informations
CREATE VIEW SalesView AS
SELECT s.sale_id, c.first_name AS customer_first_name, c.last_name AS customer_last_name,
       ca.model_name AS car_model, ca.price AS car_price, s.sale_date
FROM Sales s
JOIN Customers c ON s.customer_id = c.customer_id
JOIN Cars ca ON s.car_id = ca.car_id;

-- Return the view
SELECT * FROM SalesView;

// High value cars
CREATE VIEW HighValueCars AS
SELECT car_id, model_name, price
FROM Cars
WHERE price > 40000.00;

-- Return the view
SELECT * FROM HighValueCars;

// Cars by manufacturer
CREATE VIEW CarsByManufacturer AS
SELECT m.manufacturer_name, c.model_name, c.year, c.price
FROM Cars c
JOIN Manufacturers m ON c.manufacturer_id = m.manufacturer_id;

-- Return the view
SELECT * FROM CarsByManufacturer;

// Cars with very high mileage
CREATE VIEW HighMileageCars AS
SELECT model_name, mileage
FROM Cars
WHERE mileage > 180000;

-- Return the view
SELECT * FROM HighMileageCars;

// Remove all the views
DROP VIEW SalesView;
DROP VIEW HighValueCars;
DROP VIEW CarsByManufacturer;
DROP VIEW HighMileageCars;