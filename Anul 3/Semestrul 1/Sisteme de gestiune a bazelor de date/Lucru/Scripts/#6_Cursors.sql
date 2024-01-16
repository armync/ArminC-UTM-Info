/* 6. PL/SQL (Procedural Language for SQL) - Cursors */

// Toggle the output from database management system (DBMS)
SET SERVEROUTPUT ON;
SET SERVEROUTPUT OFF;

// Show the history of the cars catalog (BASIC)
DECLARE
    CURSOR car_cursor IS
        SELECT car_id, model_name, price FROM Cars;
    v_car_id Cars.car_id%TYPE;
    v_model_name Cars.model_name%TYPE;
    v_price Cars.price%TYPE;
BEGIN
    OPEN car_cursor;
    LOOP
        FETCH car_cursor INTO v_car_id, v_model_name, v_price;
        EXIT WHEN car_cursor%NOTFOUND;
        DBMS_OUTPUT.PUT_LINE('ID masina: ' || v_car_id || ', Model: ' || v_model_name || ', Pret: ' || v_price);
    END LOOP;
    CLOSE car_cursor;
END;
/

// Show the employee (by id) sale details (PARAMETERS)
DECLARE
    v_position Employees.position%TYPE;
    
    CURSOR sales_cursor(p_employee_id NUMBER) IS
        SELECT sale_id, car_id, sale_date
        FROM Sales
        WHERE employee_id = p_employee_id;
    
    v_sale_id Sales.sale_id%TYPE;
    v_car_id Sales.car_id%TYPE;
    v_sale_date Sales.sale_date%TYPE;
    
    v_employee_id NUMBER := 1; /* ID angajat */
BEGIN
    SELECT position INTO v_position
    FROM Employees
    WHERE employee_id = v_employee_id;
    
    IF v_position = 'Consultant vanzari' THEN
        OPEN sales_cursor(v_employee_id);
        
        LOOP
            FETCH sales_cursor INTO v_sale_id, v_car_id, v_sale_date;
            EXIT WHEN sales_cursor%NOTFOUND;
            DBMS_OUTPUT.PUT_LINE('ID vanzare: ' || v_sale_id || ', ID masina: ' || v_car_id || ', Data vanzare: ' || v_sale_date);
        END LOOP;
        
        CLOSE sales_cursor;
        
    ELSE
        DBMS_OUTPUT.PUT_LINE('Atentie! Angajatul cu ID-ul ' || v_employee_id || ' nu are rolul de consultant vanzari.');
    END IF;
EXCEPTION
    WHEN NO_DATA_FOUND THEN
        DBMS_OUTPUT.PUT_LINE('Eroare! Nu am putut gasi angajatul cu ID-ul ' || v_employee_id || '.');
END;
/

// Show the rentals (by customer id) details (PARAMETERS)
DECLARE
    CURSOR rental_cursor(p_customer_id NUMBER) IS
        SELECT rental_id, car_id, start_date, end_date FROM Rentals WHERE customer_id = p_customer_id;
    v_rental_id Rentals.rental_id%TYPE;
    v_car_id Rentals.car_id%TYPE;
    v_start_date Rentals.start_date%TYPE;
    v_end_date Rentals.end_date%TYPE;
BEGIN
    OPEN rental_cursor(6); /* ID client */
    LOOP
        FETCH rental_cursor INTO v_rental_id, v_car_id, v_start_date, v_end_date;
        EXIT WHEN rental_cursor%NOTFOUND;
        DBMS_OUTPUT.PUT_LINE('ID inchiriere: ' || v_rental_id || ', ID masina: ' || v_car_id || ', Data inceput: ' || v_start_date || ', Data finalizare: ' || v_end_date);
    END LOOP;
    CLOSE rental_cursor;
END;
/