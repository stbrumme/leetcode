SELECT employee_id
  FROM (SELECT employee_id
          FROM Employees
         WHERE employee_id NOT IN (SELECT employee_id
                                     FROM Salaries)
         UNION ALL
        SELECT employee_id
          FROM Salaries
         WHERE employee_id NOT IN (SELECT employee_id
                                     FROM Employees)
       ) s
 ORDER BY employee_id
