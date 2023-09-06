SELECT name
  FROM Employee m
 WHERE 5 <= (SELECT COUNT(*)
               FROM Employee e
              WHERE e.managerId = m.id)
