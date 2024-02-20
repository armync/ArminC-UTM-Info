/* 3. Multiple SELECT queries */

-- Comparison Operators

// Return cars priced between 35.000 and 100.000 euros
SELECT * FROM Cars WHERE price BETWEEN 35000.00 AND 100000.00;

// Return cars priced below 15.000 euros
SELECT * FROM Cars WHERE price < 15000.00;

// Return luxury cars, priced aboce 100.000 euros
SELECT * FROM Cars WHERE price > 100000.00;

// Return cars older than year 1990
SELECT * FROM Cars WHERE year < 1990;

// Return cars made between 1990 and 2010
SELECT * FROM Cars WHERE year BETWEEN 1990 AND 2010;

-- Joins

// Return sales information
SELECT s.sale_id, c.first_name, c.last_name, s.sale_date, s.sale_price, s.car_id
FROM Sales s
JOIN Customers c ON s.customer_id = c.customer_id;

// Return all of Alfa Romeo manufacturer cars
SELECT c.* 
FROM Cars c
JOIN Manufacturers m ON c.manufacturer_id = m.manufacturer_id
WHERE m.manufacturer_name = 'Alfa Romeo';

// Return the cars with their associated customers
SELECT 
    c.car_id,
    c.model_name AS car_model,
    m.manufacturer_name,
    c.year,
    c.price,
    s.sale_date,
    s.sale_price,
    cu.first_name AS customer_first_name,
    cu.last_name AS customer_last_name
FROM 
    Cars c
INNER JOIN Manufacturers m ON c.manufacturer_id = m.manufacturer_id
INNER JOIN Sales s ON c.car_id = s.car_id
INNER JOIN Customers cu ON s.customer_id = cu.customer_id;

-- Group Functions and Conditions

// Calculate the average absolute sales price
SELECT AVG(sale_price) AS average_sale_price FROM Sales;

// Count the number of sales of Consultant vanzari employees
SELECT e.employee_id, COUNT(s.sale_id) AS total_sales
FROM Sales s
JOIN Employees e ON s.employee_id = e.employee_id
WHERE e.position = 'Consultant vanzari'
GROUP BY e.employee_id;

// Return the min and max sale price
SELECT MAX(sale_price) AS max_sale_price, MIN(sale_price) AS min_sale_price
FROM Sales;

// Return cars sold in 2023
SELECT * FROM Sales WHERE EXTRACT(YEAR FROM sale_date) = 2023;

// Return the number of sold cars per month in 2023
SELECT EXTRACT(MONTH FROM sale_date) AS sales_month, COUNT(*) AS total_sales
FROM Sales
WHERE EXTRACT(YEAR FROM sale_date) = 2023
GROUP BY EXTRACT(MONTH FROM sale_date)
ORDER BY sales_month;

-- Character Functions

// Return the first 3 characters from the manufacturers name
SELECT SUBSTR(manufacturer_name, 1, 3) AS first_three_chars FROM Manufacturers;

// Concatenation of customers first and last name
SELECT first_name || ' ' || last_name AS full_name FROM Customers;

-- Date and time Functions
// Conversion the employee hire date from DATE type to a char string
SELECT
    hire_date AS original_date,
    TO_CHAR(hire_date, 'DD-MON-YYYY HH:MI:SS AM') AS formatted_date
FROM
    Employees;

// Calculate the employees years passed since date of employment
SELECT first_name, last_name, hire_date, (SYSDATE - hire_date)/365 AS years_hired
FROM Employees;

// Calculate the total rental price based on number of days rented
SELECT 
    rental_id,
    (end_date - start_date) AS total_days,
    rental_price_per_day,
    ((end_date - start_date) * rental_price_per_day) AS total_rental_price
FROM Rentals;

-- Conversion Functions

// Converts the shown showroom price of euros into local ron currency 
SELECT car_id, model_name, price, price * 4.97 AS price_in_ron FROM Cars;

// Convertts the car models to lower letters
SELECT LOWER(model_name) AS lower_model_name FROM Cars;

-- CASE Expressions

// Show the cars estimate internal class ranking system
SELECT model_name,
       CASE
           WHEN year < 1990 AND price > 20000 THEN 
               CASE
                   WHEN price BETWEEN 20000 AND 40000 THEN 'Collectible Classic - Mid'
                   ELSE 'Collectible Classic - High'
               END
           WHEN price < 20000 THEN 'Low Range'
           WHEN price BETWEEN 20000 AND 40000 THEN 'Mid Range'
           ELSE 'High Range'
       END AS price_category
FROM Cars;

// Get the customer citizenship type
SELECT 
    customer_id,
    first_name,
    last_name,
    email,
    phone_number,
    CASE 
        WHEN citizenship_id = 1 THEN 'Local - Romania'
        WHEN citizenship_id = 2 THEN 'Cetatean UE'
        WHEN citizenship_id = 3 THEN 'International'
        WHEN citizenship_id = 4 THEN 'Tara embargo'
        ELSE 'Necunoscut'
    END AS citizenship_status
FROM 
    Customers;
    
-- Subqueries (Nested Queries)

// Return premium customers who purchased cars priced above the absolute average sale price
SELECT first_name, last_name
FROM Customers
WHERE customer_id IN (
    SELECT DISTINCT customer_id
    FROM Sales
    WHERE sale_price > (SELECT AVG(sale_price) FROM Sales)
);

-- Set Operators

// Return the customers and employees
(SELECT first_name || ' ' || last_name AS name, 'Employee' AS type FROM Employees)
UNION
(SELECT first_name || ' ' || last_name AS name, 'Customer' AS type FROM Customers);

// Return employees that are customers too
SELECT first_name, last_name FROM Employees
INTERSECT
SELECT first_name, last_name FROM Customers;

// Find registered customers who never made a purchase
SELECT first_name, last_name FROM Customers
MINUS
SELECT c.first_name, c.last_name FROM Customers c
JOIN Sales s ON c.customer_id = s.customer_id;