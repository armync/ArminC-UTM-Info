DECLARE
    v_countryid locations.country_id%TYPE := 'CA';
    v_loc_id locations.location_id%TYPE;
    v_counter NUMBER(2) :=1;
    v_new_city locations.city%TYPE := 'Montreal';
BEGIN
    SELECT MAX(location_id) into v_loc_id FROM locations
    WHERE country_id = v_countryid;
    LOOP
        INSERT INTO locations(location_id, city, country_id)
        VALUES((v_loc_id + v_counter), v_new_city, v_countryid);
        v_counter := v_counter + 1;
        EXIT WHEN v_counter > 3;
    END LOOP;
    DBMS_OUTPUT.PUT_LINE(v_counter-1||' rows added.');
    END;
    /