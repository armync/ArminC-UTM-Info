/* 8. Functions */

// Toggle the output from database management system (DBMS)
SET SERVEROUTPUT ON;
SET SERVEROUTPUT OFF;

// Return the total sales sum per customer
CREATE OR REPLACE FUNCTION CalculateTotalSales(p_customer_id NUMBER) RETURN NUMBER IS
    v_total_sales NUMBER := 0;
BEGIN
    SELECT SUM(sale_price)
    INTO v_total_sales
    FROM Sales
    WHERE customer_id = p_customer_id;

    RETURN NVL(v_total_sales, 0);
END CalculateTotalSales;
/

// Return the current status of the car
CREATE OR REPLACE FUNCTION GetCarStatus(p_car_id NUMBER) RETURN VARCHAR2 IS
    v_status VARCHAR2(50);
BEGIN
    BEGIN
        SELECT 'vanduta' INTO v_status
        FROM Sales
        WHERE car_id = p_car_id;
    EXCEPTION
        WHEN NO_DATA_FOUND THEN
            BEGIN
                SELECT 'inchiriata' INTO v_status
                FROM Rentals
                WHERE car_id = p_car_id
                  AND start_date <= SYSDATE
                  AND end_date >= SYSDATE;
            EXCEPTION
                WHEN NO_DATA_FOUND THEN
                    v_status := 'disponibila';
            END;
    END;

    RETURN v_status;
END GetCarStatus;
/

// Executing block for customer total sales
DECLARE
    v_customer_id NUMBER := 5; -- ID client
    v_total_sales NUMBER;
BEGIN
    v_total_sales := CalculateTotalSales(v_customer_id);
    DBMS_OUTPUT.PUT_LINE('Suma totala depusa de catre clientul cu ID-ul ' || v_customer_id || ' este: ' || v_total_sales || ' euro.');
END;
/

// Executing block for car status
DECLARE
    v_car_id NUMBER := 4; -- ID masina
    v_car_status VARCHAR2(50);
BEGIN
    v_car_status := GetCarStatus(v_car_id);
    DBMS_OUTPUT.PUT_LINE('Masina cu ID-ul ' || v_car_id || ' este ' || v_car_status);
END;
/

// Remove the functions
DROP FUNCTION CalculateTotalSales;
DROP FUNCTION GetCarStatus;
