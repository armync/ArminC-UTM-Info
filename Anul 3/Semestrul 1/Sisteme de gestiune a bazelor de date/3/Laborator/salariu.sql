SELECT department_id, job_id, MIN(salary), MAX(salary), AVG(salary)
FROM employees
GROUP BY department_id, job_id