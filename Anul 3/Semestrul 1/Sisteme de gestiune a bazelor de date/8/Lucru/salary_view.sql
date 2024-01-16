CREATE OR REPLACE VIEW salary AS
    SELECT
        employee_id,
        last_name,
        job_id,
        salary
    FROM 
        employees
    WHERE
        department_id = 80
        AND salary > 8000;

SELECT
    employee_id,
    last_name,
    job_id,
    salary
FROM salary;