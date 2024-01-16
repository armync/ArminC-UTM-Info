SELECT last_name, job_id, salary
FROM employees
WHERE job_id = (SELECT job_id
                FROM employees
                WHERE last_name = 'Sullivan')
AND salary > (SELECT salary
                FROM employees
                WHERE last_name = 'Sullivan');