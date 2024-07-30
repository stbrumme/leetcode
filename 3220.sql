SELECT transaction_date, SUM(amount * MOD(amount, 2)) AS odd_sum, SUM(amount * (1 - MOD(amount, 2))) AS even_sum
  FROM transactions
 GROUP BY transaction_date
 ORDER BY transaction_date
