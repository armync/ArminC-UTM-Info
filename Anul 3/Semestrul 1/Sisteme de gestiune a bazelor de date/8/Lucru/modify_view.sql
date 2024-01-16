CREATE OR REPLACE VIEW empvu80
    (id_number, name, sal, department_id)
AS SELECT employee_id, first_name || ' '
          || last_name, salary, department_id
    FROM employees
    WHERE department_id = 80;