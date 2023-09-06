WITH first AS (SELECT customer_id, MIN(order_date) AS order_date
                 FROM Delivery
                GROUP BY customer_id),
     imm   AS (SELECT 1
                 FROM Delivery
                WHERE (customer_id, order_date) IN (SELECT * FROM first)
                  AND order_date = customer_pref_delivery_date)
SELECT ROUND(100 * (SELECT COUNT(*) FROM imm) / (SELECT COUNT(*) FROM first), 2) AS immediate_percentage
