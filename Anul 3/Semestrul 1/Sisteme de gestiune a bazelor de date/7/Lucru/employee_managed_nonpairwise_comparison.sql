SELECT employee_id, manager_id, department_id
FROM employees
WHERE manager_id IN (SELECT manager_id
                    FROM employees
                    WHERE employee_id IN (174,141))
AND department_id IN (SELECT department_id
                    FROM employees
                    WHERE employee_id IN (174,141))
AND employee_id NOT IN (174,141);