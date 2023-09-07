WITH needed AS (SELECT query_name, rating / position AS quality, IF(rating < 3, 1, 0) AS poor
                  FROM Queries)
SELECT query_name,
       ROUND(      AVG(quality),         2) AS quality,
       ROUND(100 * SUM(poor) / COUNT(*), 2) AS poor_query_percentage
  FROM needed
 GROUP BY query_name
