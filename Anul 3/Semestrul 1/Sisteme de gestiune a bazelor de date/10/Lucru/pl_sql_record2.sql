DECLARE
    TYPE t_rec IS RECORD
    (
        v_sal number(8),
        v_minsal number(8) default 1000,
        v_hire_date employees.hire_date%type,
        v_rec1 employees%rowtype
    );
    v_myrec t_rec;
    
    
BEGIN
    v_myrec.v_sal := v_myrec.v_minsal + 500;
    v_myrec.v_hire_date := sysdate;
    SELECT * INTO v_myrec.v_rec1
    FROM employees WHERE employee_id = 100;
    
    DBMS_OUTPUT.PUT_LINE(v_myrec.v_rec1.last_name || ' ' ||
    v_myrec.v_hire_date ||' '|| v_myrec.v_sal);
END;