DECLARE
  CURSOR cur_depts IS
    SELECT department_id, department_name FROM departments;
  v_department_id departments.department_id%TYPE;
  v_department_name departments.department_name%TYPE;
BEGIN
  OPEN cur_depts;
  LOOP
    FETCH cur_depts INTO v_department_id, v_department_name;
    EXIT WHEN cur_depts%NOTFOUND;
    DBMS_OUTPUT.PUT_LINE(v_department_id||' '||v_department_name);
  END LOOP;
  CLOSE cur_depts;
END;