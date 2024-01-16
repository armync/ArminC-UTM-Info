/* 8. Triggers */

// Check the validity of date (set date not older than current day)
CREATE OR REPLACE TRIGGER CheckRentDateTrigger
BEFORE INSERT ON Rentals
FOR EACH ROW
BEGIN
    IF :new.start_date < SYSDATE THEN
        RAISE_APPLICATION_ERROR(-20001, 'Data invalida, incearca din nou. Data introdusa este in trecut.');
    END IF;
END;
/

// Check if the employee position is valid for sales
CREATE OR REPLACE TRIGGER CheckEmployeePositionTrigger_Sales
BEFORE INSERT ON Sales
FOR EACH ROW
DECLARE
    v_position VARCHAR2(50);
BEGIN
    SELECT position INTO v_position
    FROM Employees
    WHERE employee_id = :new.employee_id;

    IF v_position NOT IN ('Consultant vanzari', 'Manager vanzari') THEN
        RAISE_APPLICATION_ERROR(-20002, 'Angajat cu post de lucru invalid pentru finalizare vanzare.');
    END IF;
END;
/

// Check if the employee position is valid for renting
CREATE OR REPLACE TRIGGER CheckEmployeePositionTrigger_Rentals
BEFORE INSERT ON Rentals
FOR EACH ROW
DECLARE
    v_position VARCHAR2(50);
BEGIN
    SELECT position INTO v_position
    FROM Employees
    WHERE employee_id = :new.employee_id;

    IF v_position NOT IN ('Consultant vanzari', 'Manager vanzari') THEN
        RAISE_APPLICATION_ERROR(-20003, 'Angajat cu post de lucru invalid pentru finalizare inchiriere.');
    END IF;
END;
/

// Remove the triggers
DROP TRIGGER CheckRentDateTrigger;
DROP TRIGGER CheckEmployeePositionTrigger_Sales;
DROP TRIGGER CheckEmployeePositionTrigger_Rentals;
