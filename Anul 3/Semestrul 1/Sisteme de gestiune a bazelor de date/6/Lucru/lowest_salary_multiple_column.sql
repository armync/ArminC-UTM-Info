SELECT first_name, department_id, salary
FROM employees
WHERE (salary, department_id) IN
    (SELECT min(salary), department_id
    FROM employees
    GROUP BY department_id)
ORDER by department_id;