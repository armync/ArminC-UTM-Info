SET SERVEROUTPUT ON

DECLARE
    v_name VARCHAR2(20);
BEGIN
    SELECT
        first_name
    INTO v_name
    FROM
        employees
    WHERE
        employee_id = 100;
        
    DBMS_OUTPUT.PUT_LINE(v_name);
END;