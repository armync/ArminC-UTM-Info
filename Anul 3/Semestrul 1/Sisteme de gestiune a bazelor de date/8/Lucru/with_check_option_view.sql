CREATE OR REPLACE VIEW empvu20
AS SELECT *
    FROM employees
    WHERE department_id = 20
    WITH CHECK OPTION CONSTRAINT empvu20_ck;