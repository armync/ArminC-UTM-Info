SELECT employee_id, manager_id, department_id
FROM employees
WHERE (manager_id, department_id) IN (SELECT manager_id, department_id
                                        FROM employees
                                        WHERE employee_id IN (174,199))
AND employee_id NOT IN (174,199);