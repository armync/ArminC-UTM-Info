/*
SELECT ROUND(MAX(salary),0) "Maximum",
ROUND(MIN(salary),0) "Minimum",
ROUND(SUM(salary),0) "Sum",
ROUND(AVG(salary),0) "Average"
FROM employees;
*/

/*
SELECT job_id, ROUND(MAX(salary),0) "Maximum",
ROUND(MIN(salary),0) "Minimum",
ROUND(SUM(salary),0) "Sum",
ROUND(AVG(salary),0) "Average"
FROM employees
GROUP BY job_id;
*/

/*
SELECT job_id, COUNT(*)
FROM employees
GROUP BY job_id;
*/

/*
SELECT job_id, COUNT(*)
FROM employees
WHERE job_id = '&job_title'
GROUP BY job_id;
*/

/*
SELECT COUNT(DISTINCT manager_id) "Number of Managers"
FROM employees;
*/

/*
SELECT MAX(salary) - MIN(salary) DIFFERENCE
FROM employees;
*/

/*
SELECT manager_id, MIN(salary)
FROM employees
WHERE manager_id IS NOT NULL
GROUP BY manager_id
HAVING MIN(salary) > 6000
ORDER BY MIN(salary) DESC;
*/

/*
SELECT COUNT(*) total,
SUM(DECODE(TO_CHAR(hire_date, 'YYYY'),2009,1,0))"2009",
SUM(DECODE(TO_CHAR(hire_date, 'YYYY'),2010,1,0))"2010",
SUM(DECODE(TO_CHAR(hire_date, 'YYYY'),2011,1,0))"2011",
SUM(DECODE(TO_CHAR(hire_date, 'YYYY'),2012,1,0))"2012"
FROM employees;
*/

/*
SELECT job_id "Job",
SUM(DECODE(department_id , 20, salary)) "Dept 20",
SUM(DECODE(department_id , 50, salary)) "Dept 50",
SUM(DECODE(department_id , 80, salary)) "Dept 80",
SUM(DECODE(department_id , 90, salary)) "Dept 90",
SUM(salary) "Total"
FROM employees
GROUP BY job_id;
*/