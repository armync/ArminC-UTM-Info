select last_name, first_name, salary*12+300*12 "Yearly salary", to_char(sysdate, 'DD-MON-YYYY HH24:MI:SS') "Current date"
from employees
order by "Yearly salary" DESC
offset 1 rows fetch next 1 rows only