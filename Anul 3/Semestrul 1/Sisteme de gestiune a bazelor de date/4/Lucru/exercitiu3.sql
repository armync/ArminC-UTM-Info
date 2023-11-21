/*
SELECT last_name, salary
FROM employees
WHERE salary > 12000;
*/

/*
SELECT last_name, department_id
FROM employees
WHERE employee_id = 176;
*/

/*
SELECT last_name, salary
FROM employees
WHERE salary NOT BETWEEN 5000 AND 12000;
*/

/*
SELECT last_name, job_id, hire_date
FROM employees
WHERE last_name IN ('Matos', 'Taylor')
ORDER BY hire_date;
*/

/*
SELECT last_name, department_id
FROM employees
WHERE department_id IN (20, 50)
ORDER BY last_name ASC;
*/

/*
SELECT last_name, department_id
FROM employees
WHERE department_id IN (20, 50)
ORDER BY last_name ASC;
*/

/*
SELECT last_name "Employee", salary "Monthly Salary"
FROM employees
WHERE salary BETWEEN 5000 AND 12000
AND department_id IN (20, 50);
*/

/*
SELECT last_name, hire_date
FROM employees
WHERE hire_date >= '01-JAN-10' AND hire_date < '01-JAN-11';
*/

/*
SELECT last_name, job_id
FROM employees
WHERE manager_id IS NULL;
*/

/*
SELECT last_name, salary, commission_pct
FROM employees
WHERE commission_pct IS NOT NULL
ORDER BY 2 DESC, 3 DESC;
*/

/*
SELECT last_name, salary
FROM employees
WHERE salary > &sal_amt;
*/

/*
SELECT employee_id, last_name, salary, department_id
FROM employees
WHERE manager_id = &mgr_num
ORDER BY &order_col;
*/

/*
SELECT last_name
FROM employees
WHERE last_name LIKE '__a%';
*/

/*
SELECT last_name
FROM employees
WHERE last_name LIKE '%a%'
AND last_name LIKE '%e%';
*/

/*
SELECT last_name, job_id, salary
FROM employees
WHERE job_id IN ('SA_REP', 'ST_CLERK')
AND salary NOT IN (2500, 3500, 7000);
*/

/*
SELECT last_name "Employee", salary "Monthly Salary",
commission_pct
FROM employees
WHERE commission_pct = .20;
*/