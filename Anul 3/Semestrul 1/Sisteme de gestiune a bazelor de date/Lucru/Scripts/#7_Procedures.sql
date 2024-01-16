/* 7. Packages with complex procedures */

// Sell and rent package specification
CREATE OR REPLACE PACKAGE CarDealershipPackage AS

    PROCEDURE SellCar(
        p_car_id NUMBER, 
        p_customer_id NUMBER, 
        p_employee_id NUMBER,
        p_sale_price NUMBER
    );
    
    PROCEDURE RentCar(
        p_car_id NUMBER, 
        p_customer_id NUMBER, 
        p_employee_id NUMBER, 
        p_start_date DATE, 
        p_end_date DATE, 
        p_rental_price_per_day NUMBER
    );
    
END CarDealershipPackage;
/

// Create Sales Sequence
CREATE SEQUENCE Sales_SEQ
START WITH 1
INCREMENT BY 1
NOCACHE
NOCYCLE;

// Create Rental Sequence
CREATE SEQUENCE Rentals_SEQ
START WITH 1
INCREMENT BY 1
NOCACHE
NOCYCLE;

// Sell and rent package body
CREATE OR REPLACE PACKAGE BODY CarDealershipPackage AS
    
    -- Selling
    PROCEDURE SellCar(
        p_car_id NUMBER, 
        p_customer_id NUMBER, 
        p_employee_id NUMBER, 
        p_sale_price NUMBER
    ) IS
        v_sale_count NUMBER;
        v_rent_count NUMBER;
    BEGIN
        SELECT COUNT(*) INTO v_sale_count -- verificare unicitate vanzare
        FROM Sales
        WHERE car_id = p_car_id;
        
        SELECT COUNT(*) INTO v_rent_count -- verificare suplimentara existenta inchiriere
        FROM Rentals
        WHERE car_id = p_car_id;

        IF v_sale_count > 0 THEN
            DBMS_OUTPUT.PUT_LINE('Masina cu ID-ul ' || p_car_id || ' a fost deja vanduta.');
        ELSIF v_rent_count > 0 THEN
            DBMS_OUTPUT.PUT_LINE('Masina cu ID-ul ' || p_car_id || ' este deja inchiriata.');
        ELSE
            INSERT INTO Sales(sale_id, car_id, customer_id, employee_id, sale_date, sale_price)
            VALUES(Sales_SEQ.NEXTVAL, p_car_id, p_customer_id, p_employee_id, SYSDATE, p_sale_price);
        
            DBMS_OUTPUT.PUT_LINE('Masina cu ID-ul ' || p_car_id || ' a fost vanduta clientului cu ID-ul ' || p_customer_id || ' de catre angajatul cu ID-ul ' || p_employee_id);
        END IF;
        
    EXCEPTION
        WHEN OTHERS THEN
            DBMS_OUTPUT.PUT_LINE('Posibila eroare intampinata la vanzarea masinii. Incearca din nou.');
    END SellCar;

    -- Renting
    PROCEDURE RentCar(
        p_car_id NUMBER, 
        p_customer_id NUMBER, 
        p_employee_id NUMBER, 
        p_start_date DATE, 
        p_end_date DATE, 
        p_rental_price_per_day NUMBER
    ) IS
        v_sale_count NUMBER;
        v_rent_count NUMBER;
    BEGIN
        
        SELECT COUNT(*) INTO v_rent_count -- verificare unicitate inchiriere
        FROM Rentals
        WHERE car_id = p_car_id;
        
        SELECT COUNT(*) INTO v_sale_count -- verificare suplimentara existenta vanzare
        FROM Sales
        WHERE car_id = p_car_id;

        IF v_rent_count > 0 THEN
            DBMS_OUTPUT.PUT_LINE('Masina cu ID-ul ' || p_car_id || ' este deja inchiriata.');
        ELSIF v_sale_count > 0 THEN
            DBMS_OUTPUT.PUT_LINE('Masina cu ID-ul ' || p_car_id || ' a fost deja vanduta.');
        ELSE
            INSERT INTO Rentals(rental_id, car_id, customer_id, employee_id, start_date, end_date, rental_price_per_day)
            VALUES(Rentals_SEQ.NEXTVAL, p_car_id, p_customer_id, p_employee_id, p_start_date, p_end_date, p_rental_price_per_day);
            
            DBMS_OUTPUT.PUT_LINE('Masina cu ID-ul ' || p_car_id || ' a fost inchiriata clientului cu ID-ul ' || p_customer_id || ' de catre angajatul cu ID-ul ' || p_employee_id || ' incepand cu data de ' || TO_CHAR(p_start_date, 'DD-MON-YYYY') || ' pana la ' || TO_CHAR(p_end_date, 'DD-MON-YYYY'));
        END IF;
        
    EXCEPTION
        WHEN OTHERS THEN
            DBMS_OUTPUT.PUT_LINE('Introdu din nou pana la finalizare.');
    END RentCar;

END CarDealershipPackage;
/

// Executing block
DECLARE
    v_car_id NUMBER := 5; -- ID masina
    v_customer_id NUMBER := 2; -- ID client
    v_employee_id NUMBER := 1; -- ID angajat
    v_sale_price NUMBER := 39000; -- *Pret vanzare
    v_start_date DATE := SYSDATE; -- **Data inceput inchiriere
    v_end_date DATE := SYSDATE + 7; -- **Data finalizare inchiriere
    v_rental_price_per_day NUMBER := 80; -- **Pret inchirierere pe zi
BEGIN
    -- Car selling
    CarDealershipPackage.SellCar(v_car_id, v_customer_id, v_employee_id, v_sale_price);
    
    
    -- Car renting
    -- CarDealershipPackage.RentCar(v_car_id, v_customer_id, v_employee_id, v_start_date, v_end_date, v_rental_price_per_day);
    
    COMMIT;
EXCEPTION
    WHEN OTHERS THEN
        DBMS_OUTPUT.PUT_LINE('Eroare: ' || SQLCODE || ' - ' || SQLERRM);
        ROLLBACK;
END;
/

// Reset the sequences
ALTER SEQUENCE Sales_SEQ RESTART;
ALTER SEQUENCE Rentals_SEQ RESTART;

// Remove the packages
DROP PACKAGE BODY CarDealershipPackage;
DROP PACKAGE CarDealershipPackage;

// Remove the sequences
DROP SEQUENCE Sales_SEQ;
DROP SEQUENCE Rentals_SEQ;