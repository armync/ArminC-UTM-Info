WITH DPT_SALARY AS (
    SELECT e.employee_id, e.first_name, e.last_name, e.salary, d.department_id
    FROM employees e
    JOIN departments d ON e.department_id = d.department_id
    WHERE d.department_id = 80 AND e.salary > 7500
)
SELECT * FROM DPT_SALARY;