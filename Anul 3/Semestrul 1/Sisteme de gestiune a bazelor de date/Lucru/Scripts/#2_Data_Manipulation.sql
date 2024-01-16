/* 2. Data manipulation language */

// Insert Manufacturers records
INSERT INTO Manufacturers (manufacturer_id, manufacturer_name, manufacturer_country)
VALUES (1, 'Toyota', 'Japonia');

INSERT INTO Manufacturers (manufacturer_id, manufacturer_name, manufacturer_country)
VALUES (2, 'Honda', 'Japonia');

INSERT INTO Manufacturers (manufacturer_id, manufacturer_name, manufacturer_country)
VALUES (3, 'Mazda', 'Japonia');

INSERT INTO Manufacturers (manufacturer_id, manufacturer_name, manufacturer_country)
VALUES (4, 'Dacia', 'Romania');

INSERT INTO Manufacturers (manufacturer_id, manufacturer_name, manufacturer_country)
VALUES (5, 'Alfa Romeo', 'Italia');

INSERT INTO Manufacturers (manufacturer_id, manufacturer_name, manufacturer_country)
VALUES (6, 'Volkswagen', 'Germania');

INSERT INTO Manufacturers (manufacturer_id, manufacturer_name, manufacturer_country)
VALUES (7, 'De Tomaso', 'Italia');

INSERT INTO Manufacturers (manufacturer_id, manufacturer_name, manufacturer_country)
VALUES (8, 'Volvo', 'Suedia');

// Insert Car models records
INSERT INTO Cars (car_id, manufacturer_id, model_name, year, price, color, mileage, fuel_type)
VALUES (1, 1, 'GR Supra', 2023, 65000.00, 'Rosu Perfomance', 0, 'Benzina');

INSERT INTO Cars (car_id, manufacturer_id, model_name, year, price, color, mileage, fuel_type)
VALUES (2, 2, 'Civic Type-R', 2023, 50000.00, 'Championship White', 0, 'Benzina');

INSERT INTO Cars (car_id, manufacturer_id, model_name, year, price, color, mileage, fuel_type)
VALUES (3, 3, 'MX-5', 2023, 29000.00, 'Soul Red', 3000.00, 'Benzina');

INSERT INTO Cars (car_id, manufacturer_id, model_name, year, price, color, mileage, fuel_type)
VALUES (4, 4, 'Logan', 2021, 12000.00, 'Alb', 15000.00, 'Diesel');

INSERT INTO Cars (car_id, manufacturer_id, model_name, year, price, color, mileage, fuel_type)
VALUES (5, 2, 'e', 2023, 40000.00, 'Charge Yellow', 0, 'Eletric');

INSERT INTO Cars (car_id, manufacturer_id, model_name, year, price, color, mileage, fuel_type)
VALUES (6, 5, 'Duetto Spider 1750', 1967, 48000.00, 'Rosu perlat', 29000.00, 'Benzina');

INSERT INTO Cars (car_id, manufacturer_id, model_name, year, price, color, mileage, fuel_type)
VALUES (7, 6, 'Corrado VR6', 1992, 25000.00, 'Rosu perlat', 220000.00, 'Benzina');

INSERT INTO Cars (car_id, manufacturer_id, model_name, year, price, color, mileage, fuel_type)
VALUES (8, 2, 'Civic Si', 1992, 8500.00, 'Albastru perlat', 240000.00, 'Benzina');

INSERT INTO Cars (car_id, manufacturer_id, model_name, year, price, color, mileage, fuel_type)
VALUES (9, 7, 'Pantera GT5-S', 1986, 210000.00, 'Rosu perlat', 46000.00, 'Benzina');

INSERT INTO Cars (car_id, manufacturer_id, model_name, year, price, color, mileage, fuel_type)
VALUES (10, 8, 'P1800', 1967, 35000.00, 'Rosu perlat', 100000.00, 'Benzina');

INSERT INTO Cars (car_id, manufacturer_id, model_name, year, price, color, mileage, fuel_type)
VALUES (11, 5, 'Montreal', 1967, 71000.00, 'Verde perlat', 81000.00, 'Benzina');


// Insert Customers records
INSERT INTO Customers (customer_id, first_name, last_name, email, phone_number, citizenship_id)
VALUES (1, 'Laurentiu', 'Faraon', 'laurentiu31faraon@icloud.com', '0744422415', 1);

INSERT INTO Customers (customer_id, first_name, last_name, email, phone_number, citizenship_id)
VALUES (2, 'Nicu', 'Racleta', 'nicu_racleta213@gmail.com', '0744898929', 1);

INSERT INTO Customers (customer_id, first_name, last_name, email, phone_number, citizenship_id)
VALUES (3, 'Gigel', 'Potrivitu', 'potrivitugigel4@yahoo.com', '0727333412', 1);

INSERT INTO Customers (customer_id, first_name, last_name, email, phone_number, citizenship_id)
VALUES (4, 'Vasile', 'Vitrina', 'vasile.vitrina002@gmail.com', '0725312462', 1);

INSERT INTO Customers (customer_id, first_name, last_name, email, phone_number, citizenship_id)
VALUES (5, 'Ira', 'Constantin', 'irarconstantin101@gmail.com', '0762522860', 1);

INSERT INTO Customers (customer_id, first_name, last_name, email, phone_number, citizenship_id)
VALUES (6, 'Alexander', 'Michael', 'michaelalexander92@gmail.com', '12025550115 ', 3);

INSERT INTO Customers (customer_id, first_name, last_name, email, phone_number, citizenship_id)
VALUES (7, 'Isabella', 'Lucia', 'lucia._isabella2@gmail.com', '39062741324  ', 2);

// Insert Employees records
INSERT INTO Employees (employee_id, first_name, last_name, position, hire_date)
VALUES (1, 'Alexandru', 'Andrei', 'Consultant vanzari', TO_DATE('2021-06-12', 'YYYY-MM-DD'));

INSERT INTO Employees (employee_id, first_name, last_name, position, hire_date)
VALUES (2, 'Jean', 'Paun', 'Tehnician auto', TO_DATE('2018-03-18', 'YYYY-MM-DD'));

INSERT INTO Employees (employee_id, first_name, last_name, position, hire_date)
VALUES (3, 'Mihai', 'Radu', 'Manager vanzari', TO_DATE('2016-12-11', 'YYYY-MM-DD'));

INSERT INTO Employees (employee_id, first_name, last_name, position, hire_date)
VALUES (4, 'Irina', 'Preda', 'Specialist financiar', TO_DATE('2022-05-01', 'YYYY-MM-DD'));

INSERT INTO Employees (employee_id, first_name, last_name, position, hire_date)
VALUES (5, 'Neagu', 'Istrate', 'Consultant vanzari', TO_DATE('2022-05-01', 'YYYY-MM-DD'));

// Insert Sales records
INSERT INTO Sales (sale_id, car_id, customer_id, employee_id, sale_date, sale_price)
VALUES (1, 4, 2, 5, TO_DATE('2023-08-01', 'YYYY-MM-DD'), 11500.00);

INSERT INTO Sales (sale_id, car_id, customer_id, employee_id, sale_date, sale_price)
VALUES (2, 7, 5, 1, TO_DATE('2023-11-27', 'YYYY-MM-DD'), 24800.00);

// Insert Rentals records
INSERT INTO Rentals (rental_id, car_id, customer_id, employee_id, start_date, end_date, rental_price_per_day)
VALUES (1, 2, 1, 1, TO_DATE('2023-12-28', 'YYYY-MM-DD'), TO_DATE('2024-01-03', 'YYYY-MM-DD'), 75.00);

INSERT INTO Rentals (rental_id, car_id, customer_id, employee_id, start_date, end_date, rental_price_per_day)
VALUES (2, 11, 6, 3, TO_DATE('2024-01-10', 'YYYY-MM-DD'), TO_DATE('2024-01-18', 'YYYY-MM-DD'), 100.00);

// Update car price
UPDATE Cars
SET price = 27000.00
WHERE car_id = 3;

// Update employee position column
UPDATE Employees
SET position = 'Director general'
WHERE employee_id = 4;

// Remove a customer
DELETE FROM Customers
WHERE customer_id = 4;

// Remove all records from the tables
DELETE FROM Rentals;
DELETE FROM Sales;
DELETE FROM Cars;
DELETE FROM Customers;
DELETE FROM Employees;
DELETE FROM Manufacturers;