DECLARE
    v_emp_hiredate employees.hire_date%TYPE;
    v_emp_salary employees.salary%TYPE;
BEGIN
   SELECT hire_date, salary
   INTO v_emp_hiredate, v_emp_salary
   FROM employees
   WHERE employee_id = 100;
   DBMS_OUTPUT.PUT_LINE ('Hire date is :'|| v_emp_hiredate);
   DBMS_OUTPUT.PUT_LINE ('Salary is :'|| v_emp_salary);
END;
/