SELECT stock_name, SUM(IF(operation = 'Sell', +price, -price)) AS capital_gain_loss
  FROM Stocks
 GROUP BY stock_name
