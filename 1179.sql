SELECT d1.id,
       (SELECT SUM(d2.revenue) FROM Department d2 WHERE d1.id = d2.id AND d2.month = "Jan") AS Jan_Revenue,
       (SELECT SUM(d2.revenue) FROM Department d2 WHERE d1.id = d2.id AND d2.month = "Feb") AS Feb_Revenue,
       (SELECT SUM(d2.revenue) FROM Department d2 WHERE d1.id = d2.id AND d2.month = "Mar") AS Mar_Revenue,
       (SELECT SUM(d2.revenue) FROM Department d2 WHERE d1.id = d2.id AND d2.month = "Apr") AS Apr_Revenue,
       (SELECT SUM(d2.revenue) FROM Department d2 WHERE d1.id = d2.id AND d2.month = "May") AS May_Revenue,
       (SELECT SUM(d2.revenue) FROM Department d2 WHERE d1.id = d2.id AND d2.month = "Jun") AS Jun_Revenue,
       (SELECT SUM(d2.revenue) FROM Department d2 WHERE d1.id = d2.id AND d2.month = "Jul") AS Jul_Revenue,
       (SELECT SUM(d2.revenue) FROM Department d2 WHERE d1.id = d2.id AND d2.month = "Aug") AS Aug_Revenue,
       (SELECT SUM(d2.revenue) FROM Department d2 WHERE d1.id = d2.id AND d2.month = "Sep") AS Sep_Revenue,
       (SELECT SUM(d2.revenue) FROM Department d2 WHERE d1.id = d2.id AND d2.month = "Oct") AS Oct_Revenue,
       (SELECT SUM(d2.revenue) FROM Department d2 WHERE d1.id = d2.id AND d2.month = "Nov") AS Nov_Revenue,
       (SELECT SUM(d2.revenue) FROM Department d2 WHERE d1.id = d2.id AND d2.month = "Dec") AS Dec_Revenue
  FROM (SELECT DISTINCT id FROM Department) d1
