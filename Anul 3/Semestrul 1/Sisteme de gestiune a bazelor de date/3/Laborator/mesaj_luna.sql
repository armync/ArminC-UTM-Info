SELECT first_name, last_name, hire_date,
    CASE
        WHEN TO_CHAR(hire_date, 'MM') = '01' THEN 'Ianuarie'
        WHEN TO_CHAR(hire_date, 'MM') = '02' THEN 'Februarie'
        WHEN TO_CHAR(hire_date, 'MM') = '03' THEN 'Martie'
        WHEN TO_CHAR(hire_date, 'MM') = '04' THEN 'Aprilie'
        WHEN TO_CHAR(hire_date, 'MM') = '05' THEN 'Mai'
        WHEN TO_CHAR(hire_date, 'MM') = '06' THEN 'Iunie'
        WHEN TO_CHAR(hire_date, 'MM') = '07' THEN 'Iulie'
        WHEN TO_CHAR(hire_date, 'MM') = '08' THEN 'August'
        WHEN TO_CHAR(hire_date, 'MM') = '09' THEN 'Septembrie'
        WHEN TO_CHAR(hire_date, 'MM') = '10' THEN 'Octombrie'
        WHEN TO_CHAR(hire_date, 'MM') = '11' THEN 'Noiembrie'
        WHEN TO_CHAR(hire_date, 'MM') = '12' THEN 'Decembrie'
        ELSE 'Luna necunoscuta'
    END AS month_message
FROM employees;
