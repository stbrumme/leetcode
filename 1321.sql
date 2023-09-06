WITH days AS (SELECT visited_on, SUM(amount) AS amount
                FROM Customer
               GROUP BY visited_on),
     week AS (SELECT d1.visited_on, SUM(d2.amount) AS amount, ROUND(SUM(d2.amount) / 7, 2) AS average_amount
                FROM days d1, days d2
               WHERE d1.visited_on >= d2.visited_on
                 AND d1.visited_on <= DATE_ADD(d2.visited_on, INTERVAL 6 DAY)
               GROUP BY d1.visited_on)
SELECT visited_on, amount, average_amount
  FROM week
 WHERE 6 <= DATEDIFF(visited_on, (SELECT MIN(visited_on) FROM days))
