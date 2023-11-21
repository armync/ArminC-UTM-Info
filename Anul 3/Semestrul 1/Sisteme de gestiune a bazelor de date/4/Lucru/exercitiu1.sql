/* SELECT *
FROM employees
WHERE job_id LIKE '%CLERK'
AND hire_date > '01-JAN-05'
*/ 

/*
SELECT e.last_name, j.job_title, e.salary, e.commission_pct
FROM employees e
JOIN jobs j ON e.job_id = j.job_id
WHERE e.commission_pct > 0
ORDER BY e.salary DESC;
*/

/*
SELECT 'The salary of ' || first_name || ' after a 10% raise is ' || ROUND(salary * 1.10) AS projected_raise
FROM employees
WHERE commission_pct IS NULL
AND salary IS NOT NULL
*/

/*
SELECT last_name,
TRUNC(MONTHS_BETWEEN(SYSDATE, hire_date) / 12) YEARS,
TRUNC(MOD(MONTHS_BETWEEN(SYSDATE, hire_date), 12))
MONTHS
FROM employees
ORDER BY years DESC, MONTHS desc;
*/

/*
SELECT last_name
FROM employees
WHERE SUBSTR(last_name, 1,1) IN ('K', 'L', 'M');
*/

/*
SELECT last_name, salary,
decode(commission_pct, NULL, 'No', 'Yes') commission
FROM employees;
*/

/*
-- input example: 1800
SELECT d.department_name, d.location_id, e.last_name, e.job_id,
e.salary
FROM employees e JOIN departments d
ON e.department_id = d.department_id
AND d.location_id = &location_id;
*/

/*
SELECT COUNT(*)
FROM employees
WHERE last_name LIKE '%n';
--or
SELECT COUNT(*)
FROM employees
WHERE SUBSTR(last_name, -1) = 'n';
*/

/*
SELECT d.department_id, d.department_name,
d.location_id, COUNT(e.employee_id)
FROM employees e RIGHT OUTER JOIN departments d
ON e.department_id = d.department_id
GROUP BY d.department_id, d.department_name, d.location_id;
*/

/*
SELECT DISTINCT job_id
FROM employees
WHERE department_id IN (10, 20);
*/

/*
SELECT e.job_id, count(e.job_id) FREQUENCY
FROM employees e JOIN departments d
ON e.department_id = d.department_id
WHERE d.department_name IN ('Administration', 'Executive')
GROUP BY e.job_id
ORDER BY FREQUENCY DESC;
*/

/*
SELECT last_name, hire_date
FROM employees
WHERE TO_CHAR(hire_date, 'DD') < 16;
*/

/*
SELECT last_name, salary, TRUNC(salary, -3)/1000 Thousands
FROM employees;
*/

/*
SELECT e.last_name, m.last_name manager, m.salary,
j.grade_level
FROM employees e JOIN employees m
ON e.manager_id = m.employee_id
JOIN job_grades j
ON m.salary BETWEEN j.lowest_sal AND j.highest_sal
AND m.salary > 15000;
*/

/*
SELECT d.department_id, d.department_name,
count(e1.employee_id) employees,
NVL(TO_CHAR(AVG(e1.salary), '99999.99'), 'No average' )
avg_sal,
e2.last_name, e2.salary, e2.job_id
FROM departments d RIGHT OUTER JOIN employees e1
ON d.department_id = e1.department_id
RIGHT OUTER JOIN employees e2
ON d.department_id = e2.department_id
GROUP BY d.department_id, d.department_name, e2.last_name,
e2.salary,
e2.job_id
ORDER BY d.department_id, employees;
*/

/*
SELECT department_id, MIN(salary)
FROM employees
GROUP BY department_id
HAVING AVG(salary) = (SELECT MAX(AVG(salary))
FROM employees
GROUP BY department_id);
*/

/*
SELECT *
FROM departments
WHERE department_id NOT IN(SELECT department_id
FROM employees
WHERE job_id = 'SA_REP'
AND department_id IS NOT NULL);
*/

/*
-- fewer than three employees
SELECT d.department_id, d.department_name, COUNT(*)
FROM departments d JOIN employees e
ON d.department_id = e.department_id
GROUP BY d.department_id, d.department_name
HAVING COUNT(*) < 3;
*/

/*
-- highest number of employees
SELECT d.department_id, d.department_name, COUNT(*)
FROM departments d JOIN employees e
ON d.department_id = e.department_id
GROUP BY d.department_id, d.department_name
HAVING COUNT(*) = (SELECT MAX(COUNT(*))
FROM employees
GROUP BY department_id);
*/

/*
-- lowest number of employees
SELECT d.department_id, d.department_name, COUNT(*)
FROM departments d JOIN employees e
ON d.department_id = e.department_id
GROUP BY d.department_id, d.department_name
HAVING COUNT(*) = (SELECT MIN(COUNT(*))
FROM employees
GROUP BY department_id);
*/

/*
SELECT e.employee_id, e.last_name, e.department_id, e.salary,
AVG(s.salary)
FROM employees e JOIN employees s
ON e.department_id = s.department_id
GROUP BY e.employee_id, e.last_name, e.department_id,
e.salary;
*/

/*
SELECT last_name, TO_CHAR(hire_date, 'Month DD') BIRTHDAY
FROM employees
ORDER BY TO_CHAR(hire_date, 'DDD');
*/