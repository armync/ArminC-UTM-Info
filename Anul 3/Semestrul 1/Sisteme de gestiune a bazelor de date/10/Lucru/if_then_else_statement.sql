DECLARE
    v_myage NUMBER := 31;
BEGIN
    IF v_myage < 11
    THEN
        DBMS_OUTPUT.PUT_LINE('I am a child');
    ELSE
        DBMS_OUTPUT.PUT_LINE('I am not a child');
    END IF;
END;
/