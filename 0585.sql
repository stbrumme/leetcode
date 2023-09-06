WITH uniq AS (SELECT lat, lon
                FROM Insurance
               GROUP BY lat, lon
              HAVING COUNT(*) = 1),
     same AS (SELECT tiv_2015
                FROM Insurance
               GROUP BY tiv_2015
              HAVING COUNT(*) > 1)
SELECT ROUND(SUM(tiv_2016), 2) AS tiv_2016
  FROM Insurance i, uniq u, same s
 WHERE i.tiv_2015 = s.tiv_2015
   AND i.lat = u.lat
   AND i.lon = u.lon
