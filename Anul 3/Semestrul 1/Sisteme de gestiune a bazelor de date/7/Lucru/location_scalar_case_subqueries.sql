SELECT employee_id, last_name,
    (CASE
    WHEN department_id =
            (SELECT department_id
            FROM departments
            WHERE location_id = 1800)
        THEN 'Canada' ELSE 'USA' END) location
FROM employees;