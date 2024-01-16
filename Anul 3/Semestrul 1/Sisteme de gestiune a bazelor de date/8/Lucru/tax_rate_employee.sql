SELECT last_name, salary,
        DECODE (TRUNC(salary/2000, 0),
                            0, 0.00,
                            1, 0.09,
                            2, 0.20,
                            3, 0.30,
                            4, 0.40,
                            5, 0.42,
                            6, 0.44,
                               0.45) TAX_RATE
FROM employees
WHERE department_id = 80;
                    