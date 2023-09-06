WITH hundred AS (SELECT id
                   FROM Stadium
                  WHERE people >= 100)
SELECT DISTINCT s.id, visit_date, people
  FROM Stadium s, hundred h1, hundred h2
 WHERE s.people >= 100
   AND (   (s.id = h1.id + 1 AND s.id = h2.id + 2)
        OR (s.id = h1.id + 1 AND s.id = h2.id - 1)
        OR (s.id = h1.id - 2 AND s.id = h2.id - 1))
 ORDER BY visit_date
