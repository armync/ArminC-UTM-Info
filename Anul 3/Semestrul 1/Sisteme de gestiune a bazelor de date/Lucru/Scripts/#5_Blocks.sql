/* 5. PL/SQL (Procedural Language for SQL) - Blocks */

// Toggle the output from database management system (DBMS)
SET SERVEROUTPUT ON;
SET SERVEROUTPUT OFF;

// Required steps per customer are shown (IF)
DECLARE
    v_steps_message VARCHAR2(500);
BEGIN
    FOR cust_rec IN (SELECT * FROM Customers)
    LOOP
        IF cust_rec.citizenship_id = 1 THEN  /* Local (Romania) */
            v_steps_message := 'Se va aplica demersul standard.';
        ELSIF cust_rec.citizenship_id = 2 THEN  /* Cetatean UE */
            v_steps_message := 'Cateva documente aditionale vor fi necesare.';
        ELSIF cust_rec.citizenship_id = 3 THEN /* International */
            v_steps_message := 'Este necesar un numar ridicat de acte.';
        ELSIF cust_rec.citizenship_id = 4 THEN  /* Tara sunb embargo */
            v_steps_message := 'Atentie! client din tara sub embargo. Verificarea amanuntita a procedurilor este necesara.';
        ELSE
            v_steps_message := 'Nu exista date.';
        END IF;

        DBMS_OUTPUT.PUT_LINE('ID client: ' || cust_rec.customer_id || ', Procedura: ' || v_steps_message);
    END LOOP;
END;
/

// Apply vouchers based on number of cars bought by coustomers (CASE)
DECLARE
    v_discount_percentage NUMBER;
BEGIN
    FOR cust_rec IN (SELECT customer_id, first_name, last_name FROM Customers)
    LOOP
        SELECT COUNT(DISTINCT s.car_id)
        INTO v_discount_percentage
        FROM Sales s
        WHERE s.customer_id = cust_rec.customer_id;

        CASE 
            WHEN v_discount_percentage = 1 THEN
                v_discount_percentage := 5;  /* 5% discount pentru o masina deja cumparata */
            WHEN v_discount_percentage >= 2 THEN
                v_discount_percentage := 10; /* 10% discount pentru doua masini deja cumparate */
            ELSE
                v_discount_percentage := 0;
        END CASE;

        DBMS_OUTPUT.PUT_LINE('ID client: ' || cust_rec.customer_id || ', Nume: ' || cust_rec.first_name || ' ' || cust_rec.last_name || ', Procent voucher: ' || v_discount_percentage || '%');
    END LOOP;
END;
/

// Calculate the absolute inventory price of all cars (LOOP)
DECLARE
    v_total_price NUMBER := 0;
BEGIN
    FOR car_rec IN (SELECT * FROM Cars)
    LOOP
        v_total_price := v_total_price + car_rec.price;
    END LOOP;

    DBMS_OUTPUT.PUT_LINE('Pret total inventar masini: ' || v_total_price);
END;
/

// Show available cars under 25.000 euros, check the sold cars and current rented ones (Nested LOOP)
DECLARE
    v_status VARCHAR2(100);
BEGIN
    FOR car_rec IN (SELECT car_id, model_name FROM Cars WHERE price < 25000) LOOP
        v_status := 'Disponibila';
        FOR sale_rec IN (SELECT car_id FROM Sales WHERE car_id = car_rec.car_id) LOOP
            v_status := 'Vanduta';
        END LOOP;
        DBMS_OUTPUT.PUT_LINE('ID masina: ' || car_rec.car_id || ', Model: ' || car_rec.model_name || ', Stare: ' || v_status);
    END LOOP;

    FOR rental_rec IN (
        SELECT r.car_id, c.model_name
        FROM Rentals r
        JOIN Cars c ON r.car_id = c.car_id
        WHERE r.end_date >= SYSDATE  /* verifica data inchiriere */
    ) LOOP
        DBMS_OUTPUT.PUT_LINE('ID masina inchiriata: ' || rental_rec.car_id || ', Model: ' || rental_rec.model_name);
    END LOOP;
END;
/