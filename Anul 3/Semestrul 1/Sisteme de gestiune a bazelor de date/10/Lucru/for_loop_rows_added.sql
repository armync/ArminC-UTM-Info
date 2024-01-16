DECLARE
    v_countryid locations.country_id%TYPE := 'CA';
    v_loc_id locations.location_id%TYPE;
    v_new_city locations.city%TYPE := 'Montreal';
BEGIN
    SELECT MAX(location_id) INTO v_loc_id FROM locations
    WHERE country_id = v_countryid;
    FOR i IN  1..3 LOOP
        INSERT INTO locations(location_id, city, country_id)
        VALUES((v_loc_id + i), v_new_city, v_countryid);
    END LOOP;
END;
/