DECLARE
  CURSOR c_emp_cursor IS
  SELECT employee_id, salary FROM employees
  WHERE department_id = 30;
BEGIN
  FOR emp_record IN c_emp_cursor
  LOOP
    dbms_output.put_line(emp_record.employee_id ||' ' ||emp_record.salary);
    UPDATE employees
    SET salary = 5000
    WHERE employee_id = emp_record.employee_id;
  END LOOP;
END;
/
SELECT employee_id, salary FROM employees
WHERE department_id = 30;