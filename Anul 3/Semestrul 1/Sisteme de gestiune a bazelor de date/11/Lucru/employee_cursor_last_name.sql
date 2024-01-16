DECLARE
  CURSOR empcursor (pdept NUMBER) IS SELECT * FROM employees WHERE department_id=pdept;
  emprecord employees%ROWTYPE;
BEGIN
  OPEN empcursor(10);
  LOOP
    FETCH empcursor INTO emprecord;
    EXIT WHEN empcursor%NOTFOUND;
    DBMS_OUTPUT.PUT_LINE(emprecord.last_name);
  END LOOP;
  IF empcursor%ISOPEN THEN CLOSE empcursor; END IF;

  OPEN empcursor(20);
  LOOP
    FETCH empcursor INTO emprecord;
    EXIT WHEN empcursor%NOTFOUND;
    DBMS_OUTPUT.PUT_LINE(emprecord.last_name);
  END LOOP;
END;