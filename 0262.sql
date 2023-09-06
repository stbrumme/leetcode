WITH ban   AS (SELECT users_id AS id
                 FROM Users
                WHERE banned = 'Yes'),
     days  AS (SELECT DISTINCT request_at
                 FROM Trips
                WHERE request_at BETWEEN '2013-10-01' AND '2013-10-03'),
     tours AS (SELECT *
                 FROM Trips
                WHERE client_id NOT IN (SELECT id FROM ban)
                  AND driver_id NOT IN (SELECT id FROM ban)
                  AND request_at IN (SELECT request_at FROM days)),
     completed AS (SELECT request_at, COUNT(*) AS num
                     FROM tours
                    WHERE status = 'completed'
                    GROUP BY request_at),
     cancelled AS (SELECT request_at, COUNT(*) AS num
                     FROM tours
                    WHERE status != 'completed'
                    GROUP BY request_at)
SELECT d.request_at AS `Day`,
       ROUND(COALESCE(ca.num / (ca.num + COALESCE(co.num, 0)), 0), 2) AS `Cancellation Rate`
  FROM days d LEFT JOIN completed co ON (d.request_at = co.request_at)
              LEFT JOIN cancelled ca ON (d.request_at = ca.request_at)
 WHERE ca.num IS NOT NULL OR co.num IS NOT NULL
