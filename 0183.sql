SELECT name AS `Customers`
  FROM Customers
 WHERE id NOT IN (SELECT DISTINCT customerId
                    FROM orders)
