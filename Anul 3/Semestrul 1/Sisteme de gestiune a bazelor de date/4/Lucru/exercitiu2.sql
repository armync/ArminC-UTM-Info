/*
SELECT last_name, job_id, salary AS Sal
FROM employees;
*/

/*
SELECT *
FROM job_grades;
*/

/*
SELECT employee_id, last_name
sal x 12 ANNUAL SALARY
FROM employees;

-- The EMPLOYEES table does not contain a column called sal. The column is called
SALARY.
-- The multiplication operator is *, not x as shown in line 2.
-- The ANNUAL SALARY alias cannot include spaces. The alias should read
ANNUAL_SALARY or should be enclosed within double quotation marks.
-- A comma is missing after the LAST_NAME column. */

/*
DESCRIBE departments
SELECT *
FROM departments;
*/

/*
DESCRIBE employees
SELECT employee_id, last_name, job_id, hire_date StartDate
FROM employees;
*/

/*
SELECT DISTINCT job_id
FROM employees;
*/

/*
SELECT employee_id "Emp #", last_name "Employee",
job_id "Job", hire_date "Hire Date"
FROM employees;
*/

/*
SELECT last_name||', '||job_id "Employee and Title"
FROM employees;
*/

/*
SELECT employee_id || ',' || first_name || ',' || last_name
|| ',' || email || ',' || phone_number || ','|| job_id
|| ',' || manager_id || ',' || hire_date || ','
|| salary || ',' || commission_pct || ',' ||
department_id
THE_OUTPUT
FROM employees;
*/