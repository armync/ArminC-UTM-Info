DECLARE
    v_val NUMBER :=0;
BEGIN
    WHILE v_val < 11 LOOP
        dbms_output.put_line(v_val);
        v_val:=v_val+1;
    END LOOP;
END;