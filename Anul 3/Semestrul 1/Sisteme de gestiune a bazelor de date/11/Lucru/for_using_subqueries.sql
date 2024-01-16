BEGIN
  FOR emp_record IN (SELECT employee_id, last_name FROM employees WHERE department_id = 30)
  LOOP
    DBMS_OUTPUT.PUT_LINE(emp_record.employee_id || ' ' || emp_record.last_name);
  END LOOP;
END;
/