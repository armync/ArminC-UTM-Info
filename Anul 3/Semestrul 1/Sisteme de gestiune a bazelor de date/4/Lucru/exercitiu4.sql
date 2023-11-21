/*
SELECT sysdate "Date"
FROM dual;
*/

/*
SELECT employee_id, last_name, salary,
ROUND(salary * 1.155, 0) "New Salary"
FROM employees;
*/

/*
SELECT employee_id, last_name, salary,
ROUND(salary * 1.155, 0) "New Salary"
FROM employees;
*/

/*
SELECT employee_id, last_name, salary,
ROUND(salary * 1.155, 0) "New Salary",
ROUND(salary * 1.155, 0) - salary "Increase"
FROM employees;
*/

/*
SELECT INITCAP(last_name) "Name",
LENGTH(last_name) "Length"
FROM employees
WHERE last_name LIKE 'M%'
OR last_name LIKE 'A%'
ORDER BY last_name;
*/

/*
SELECT INITCAP(last_name) "Name",
LENGTH(last_name) "Length"
FROM employees
WHERE last_name LIKE '&start_letter%'
ORDER BY last_name;
*/

/*
SELECT INITCAP(last_name) "Name",
LENGTH(last_name) "Length"
FROM employees
WHERE last_name LIKE UPPER('&start_letter%' )
ORDER BY last_name;
*/

/*
SELECT last_name, ROUND(MONTHS_BETWEEN(
SYSDATE, hire_date)) MONTHS_WORKED
FROM employees
ORDER BY months_worked;
*/

/*
SELECT last_name,
LPAD(salary, 15, '$') SALARY
FROM employees;
*/

/*
SELECT last_name,
rpad(' ', (salary/1000)+1, '*')
SALARIES_IN_ASTERISK
FROM employees
ORDER BY salary DESC;
*/

/*
SELECT last_name, trunc((SYSDATE-hire_date)/7) AS TENURE
FROM employees
WHERE department_id = 90
ORDER BY TENURE DESC;
*/