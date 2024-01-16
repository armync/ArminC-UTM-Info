WITH CNT_DEPT AS (
    SELECT department_id,
           COUNT(*) AS NUM_EMP
    FROM EMPLOYEES
    GROUP BY department_id
)
SELECT employee_id,
       SALARY / NUM_EMP AS AVG_SALARY
FROM EMPLOYEES E
JOIN CNT_DEPT C ON (E.department_id = C.department_id);
