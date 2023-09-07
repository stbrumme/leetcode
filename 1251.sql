WITH combined AS (SELECT u.product_id, u.units, u.units * p.price AS total
                    FROM Prices p, UnitsSold u
                   WHERE u.product_id = p.product_id
                     AND u.purchase_date BETWEEN p.start_date AND p.end_date)
SELECT product_id, ROUND(SUM(total) / SUM(units), 2) AS average_price
  FROM combined
 GROUP BY product_id
