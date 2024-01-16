DECLARE
    v_total SIMPLE_INTEGER := 0;
BEGIN
    FOR i IN 1..10 LOOP
        v_total := v_total + i;
        DBMS_OUTPUT.PUT_LINE
        ('Total is: '|| v_total);
        CONTINUE WHEN i > 5;
        v_total := v_total + i;
        DBMS_OUTPUT.PUT_LINE
        ('Out of Loop Total is:
        '|| v_total);
    END LOOP;
END;
/