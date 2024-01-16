CREATE OR REPLACE VIEW dept_sum_vu
    (name, minsal, maxsal, avgsal)
AS 
SELECT d.department_name, MIN(e.salary),
       MAX(e.salary), AVG(e.salary)
FROM employees e JOIN departments d
USING (department_id)
GROUP BY d.department_name;