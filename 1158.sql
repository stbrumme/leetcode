WITH bought2019 AS (SELECT *
                      FROM Orders
                     WHERE YEAR(order_date) = 2019)
SELECT u.user_id AS buyer_id, u.join_date, COUNT(order_id) AS orders_in_2019
  FROM Users u LEFT JOIN bought2019 b ON u.user_id = b.buyer_id
 GROUP BY u.user_id
