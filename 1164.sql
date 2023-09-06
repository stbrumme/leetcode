WITH latest AS (SELECT product_id, MAX(change_date) AS change_date
                  FROM Products
                 WHERE change_date <= '2019-08-16'
                 GROUP BY product_id),
     uniq   AS (SELECT DISTINCT product_id
                  FROM Products)
SELECT u.product_id, COALESCE((SELECT p.new_price
                                 FROM Products p
                                WHERE p.product_id = u.product_id
                                  AND p.change_date = l.change_date),
                               10) AS price
  FROM uniq u LEFT JOIN latest l ON u.product_id = l.product_id
