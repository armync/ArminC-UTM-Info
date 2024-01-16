SELECT last_name, hire_date
FROM employees
WHERE hire_date > (SELECT hire_date
                  FROM employees
                  WHERE last_name = 'Davies');
