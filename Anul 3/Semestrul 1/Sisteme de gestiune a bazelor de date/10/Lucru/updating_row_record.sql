DECLARE
    v_employee_number number:= 124;
    v_emp_rec employees%ROWTYPE;
BEGIN
    SELECT * INTO v_emp_rec FROM retired_emps
    WHERE empno = v_employee_number;
    v_emp_rec.leavedate:= CURRENT_DATE;
    
    UPDATE retired_emps SET ROW = v_emp_rec WHERE
    empno=v_employee_number;
END;
/
SELECT * FROM retired_emps;