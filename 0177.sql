CREATE FUNCTION getNthHighestSalary(N INT) RETURNS INT
BEGIN
  SET N = N - 1; -- LIMIT is off-by-one
  RETURN (
      # Write your MySQL query statement below.
      WITH uniq AS (SELECT DISTINCT salary
                      FROM Employee)
      SELECT MAX(salary)
        FROM (SELECT salary
                FROM uniq
               ORDER BY salary DESC
               LIMIT N, 1
             ) s
  );
END
