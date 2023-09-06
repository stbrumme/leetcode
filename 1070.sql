WITH initial AS (SELECT product_id, MIN(year) AS year
                   FROM Sales
                  GROUP BY product_id)
SELECT s.product_id, s.year AS first_year, s.quantity, s.price
  FROM Sales s, initial i
 WHERE s.product_id = i.product_id
   AND s.year = i.year
