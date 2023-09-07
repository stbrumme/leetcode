SELECT m.employee_id,
       m.name,
       COUNT(*) AS reports_count,
       ROUND(AVG(e.age)) AS average_age
  FROM Employees m, Employees e
 WHERE m.employee_id = e.reports_to
 GROUP BY m.employee_id
 ORDER BY m.employee_id
