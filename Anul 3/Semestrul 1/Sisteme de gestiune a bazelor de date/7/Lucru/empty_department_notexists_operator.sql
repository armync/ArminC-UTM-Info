SELECT department_id, department_name
FROM departments d
WHERE NOT EXISTS (SELECT NULL
                    FROM employees
                    WHERE department_id = d.department_id);