SELECT d.name AS `Department`, e.name AS `Employee`, e.salary
  FROM Employee e, Department d
 WHERE e.departmentId = d.id
   AND (departmentId, salary) IN (SELECT departmentId, MAX(salary)
                                    FROM Employee
                                   GROUP BY departmentId)
