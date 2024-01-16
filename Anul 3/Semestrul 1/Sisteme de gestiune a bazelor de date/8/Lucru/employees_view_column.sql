SET SERVEROUTPUT ON;

CREATE VIEW salvu50 AS
SELECT employee_id AS ID_NUMBER, last_name, first_name, salary*12 AS ANN_SALARY
FROM employees
WHERE department_id = 50;

SELECT *
FROM salvu50;