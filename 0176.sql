SELECT MAX(salary) AS SecondHighestSalary -- MAX return NULL if empty
  FROM (SELECT salary
          FROM Employee
         GROUP BY salary
         ORDER BY salary DESC
         LIMIT 1, 1) s
