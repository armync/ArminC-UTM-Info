SELECT first_name
FROM employees
WHERE SUBSTR(first_name, 3, 1) = 'a'