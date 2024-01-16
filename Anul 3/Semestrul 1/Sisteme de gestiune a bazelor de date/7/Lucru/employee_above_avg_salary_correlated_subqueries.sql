SELECT last_name, salary, department_id
FROM employees outer_table
WHERE salary >
                (SELECT AVG(salary)
                    FROM employees inner_table
                    WHERE inner_table.department_id =
                    outer_table.department_id);