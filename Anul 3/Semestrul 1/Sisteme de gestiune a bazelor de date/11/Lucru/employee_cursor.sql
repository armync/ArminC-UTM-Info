DECLARE
    CURSOR empcursor IS SELECT * FROM employees;
    emprecord employees%ROWTYPE;
BEGIN
    OPEN empcursor;
    LOOP
        FETCH empcursor into emprecord;
        EXIT WHEN empcursor%NOTFOUND;
        DBMS_OUTPUT.PUT_LINE(emprecord.last_name);
    END LOOP;
    CLOSE empcursor;
END;