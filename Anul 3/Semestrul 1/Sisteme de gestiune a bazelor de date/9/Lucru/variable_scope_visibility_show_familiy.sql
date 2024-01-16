DECLARE
    v_father_name VARCHAR2(20):='Patrick';
    v_date_of_birth DATE:='20-Apr-1972';
BEGIN
    DECLARE
        v_child_name VARCHAR2(20):='Mike';
        v_child_date_of_birth DATE:='12-Dec-2002';
    BEGIN
        DBMS_OUTPUT.PUT_LINE('Father''s name: '||v_father_name);
        DBMS_OUTPUT.PUT_LINE('Date of birth: '||v_date_of_birth);
        DBMS_OUTPUT.PUT_LINE('Child''s name: '||v_child_name);
    END;
    DBMS_OUTPUT.PUT_LINE('Date of birth: '||v_date_of_birth);
END;
/