DECLARE
    v_myage NUMBER := 10;
BEGIN
    IF v_myage < 11
    THEN
        DBMS_OUTPUT.PUT_LINE('I am a child');
    END IF;
END;
/