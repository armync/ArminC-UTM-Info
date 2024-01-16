DECLARE
    v_myage NUMBER := 31;
BEGIN
    IF v_myage < 11
    THEN DBMS_OUTPUT.PUT_LINE('I am a child');
    ELSIF v_myage < 20 THEN
    DBMS_OUTPUT.PUT_LINE('I am young');
    ELSIF v_myage < 30 THEN
    DBMS_OUTPUT.PUT_LINE('I am in my twenties');
    ELSIF v_myage < 40 THEN
    DBMS_OUTPUT.PUT_LINE('I am in my thirties');
    ELSE
        DBMS_OUTPUT.PUT_LINE('I am always young');
    END IF;
END;
/