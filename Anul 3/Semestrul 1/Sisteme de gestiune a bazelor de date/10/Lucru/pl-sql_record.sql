DECLARE
    TYPE t_rec IS RECORD
    (
        v_first_name employees.first_name%type,
        v_sal number(8),
        v_hire_date employees.hire_date%type
    );
    v_myrec t_rec;
    
    
BEGIN
    SELECT first_name, salary, hire_date INTO v_myrec
    FROM employees WHERE employee_id = 100;
    
    DBMS_OUTPUT.PUT_LINE('First Name:
    '||v_myrec.v_first_name ||'Salary:
    '||v_myrec.v_sal ||'Hire Date:
    '||v_myrec.v_hire_date);

END;