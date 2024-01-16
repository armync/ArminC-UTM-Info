select department_id, department_name,
        (select count(*)
        from employees e
        where e.department_id = d.department_id) as emp_count
from departments d;