WITH req   AS (SELECT requester_id AS id, COUNT(*) AS num
                 FROM RequestAccepted
                GROUP BY requester_id),
     acc   AS (SELECT accepter_id AS id, COUNT(*) AS num
                 FROM RequestAccepted
                GROUP BY accepter_id),
     total AS (SELECT id, num -- emulate FULL OUTER JOIN
                 FROM req
                UNION ALL
               SELECT id, num
                 FROM acc)
SELECT id, SUM(num) AS num
  FROM total
 GROUP BY ID
 ORDER BY SUM(num) DESC
 LIMIT 1
