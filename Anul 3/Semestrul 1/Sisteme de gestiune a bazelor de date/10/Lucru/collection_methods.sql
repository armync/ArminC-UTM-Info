DECLARE
    TYPE email_table IS TABLE OF
        employees.email%TYPE
        INDEX BY PLS_INTEGER;
        email_list email_table;
    BEGIN
    email_list(100) := 'SKING';
    email_list(105) := 'DAUSTIN';
    email_list(110) := 'JCHEN';
    DBMS_OUTPUT.PUT_LINE('The number of elements in the list' ||
    email_list.COUNT);
    DBMS_OUTPUT.PUT_LINE('The first index in the list '|| email_list.FIRST);
    DBMS_OUTPUT.PUT_LINE('The last index in the list ' || email_list.LAST);
END;
/
