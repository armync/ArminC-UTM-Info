DECLARE
TYPE dept_table_type
IS
    TABLE OF departments%ROWTYPE INDEX BY VARCHAR2(20);
    dept_table dept_table_type;
BEGIN
    SELECT * INTO dept_table(1) FROM departments
    WHERE department_id = 10;
    DBMS_OUTPUT.PUT_LINE(dept_table(1).department_id || ' ' ||
    dept_table(1).department_name || ' ' ||
    dept_table(1).manager_id);
END;
/
