SELECT
    last_name,
    job_id,
    salary,
CASE
    WHEN job_id='AD_PRES' THEN
    salary * 2
    WHEN job_id='AD_VP' and last_name='Kochar' then
    salary * 1.5
    ELSE
    salary *.5
END AS raise_or_not
FROM
    employees;