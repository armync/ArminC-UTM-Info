SELECT employee_id, last_name, job_id, department_id
FROM employees outer
WHERE EXISTS ( SELECT NULL
                FROM employees
                WHERE manager_id =
                        outer.employee_id);