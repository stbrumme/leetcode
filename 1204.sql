SELECT q1.person_name
  FROM Queue q1
 WHERE 1000 >= (SELECT SUM(weight) FROM Queue q2 WHERE q2.turn <= q1.turn)
 ORDER BY turn DESC
 LIMIT 1
