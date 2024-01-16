SET SERVEROUTPUT ON;
DECLARE
    v_lname VARCHAR2(20);
BEGIN
    SELECT 
        LAST_NAME INTO v_lname
    FROM 
        EMPLOYEES
    WHERE 
        EMPLOYEE_ID = 100;
DBMS_OUTPUT.PUT_LINE('The last name of the employee is '||v_lname);
END;
/