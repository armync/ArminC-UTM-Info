DECLARE
  CURSOR c_emp_cursor IS
    SELECT employee_id, last_name 
    FROM employees
    WHERE department_id = 30;
  v_emp_record c_emp_cursor%ROWTYPE;
BEGIN
  OPEN c_emp_cursor;
  LOOP
    FETCH c_emp_cursor INTO v_emp_record;
    EXIT WHEN c_emp_cursor%NOTFOUND;
    DBMS_OUTPUT.PUT_LINE(v_emp_record.employee_id ||' ' ||v_emp_record.last_name);
  END LOOP;
  CLOSE c_emp_cursor;
END;