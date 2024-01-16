DECLARE
    v_countryid locations.country_id%TYPE := 'CA';
    v_loc_id locations.location_id%TYPE;
    v_new_city locations.city%TYPE := 'Montreal';
    v_counter NUMBER := 1;
BEGIN
    SELECT MAX(location_id) INTO v_loc_id FROM locations
    WHERE country_id = v_countryid;
    WHILE v_counter <= 3 LOOP
        INSERT INTO locations(location_id, city, country_id)
        VALUES((v_loc_id + v_counter), v_new_city, v_countryid);
        v_counter := v_counter + 1;
    END LOOP;
    DBMS_OUTPUT.PUT_LINE(v_counter-1||' rows added.');
 END;
/