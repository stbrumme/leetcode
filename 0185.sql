SELECT d.name AS `Department`, e.name AS `Employee`, salary AS `Salary`
  FROM Employee e, Department d
 WHERE e.departmentId = d.id
   AND 3 > (SELECT COUNT(DISTINCT e2.salary)
              FROM Employee e2
             WHERE e2.salary > e.salary
               AND e2.departmentId = e.departmentId)
