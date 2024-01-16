SELECT department_id, employee_id, salary
FROM EMPLOYEES E
WHERE salary =
            (SELECT MAX(DISTINCT salary)
            FROM EMPLOYEES
            WHERE e.department_id = department_id);