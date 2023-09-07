SELECT *
  FROM (SELECT u.name AS results
          FROM Users u, MovieRating r
         WHERE u.user_id = r.user_id
         GROUP BY u.user_id
         ORDER BY COUNT(*) DESC, u.name
         LIMIT 1) s1
 UNION ALL
SELECT *
  FROM (SELECT m.title AS results
          FROM Movies m, MovieRating r
         WHERE m.movie_id = r.movie_id
           AND r.created_at BETWEEN '2020-02-01' AND '2020-02-29'
         GROUP BY m.movie_id
         ORDER BY AVG(r.rating) DESC, m.title
         LIMIT 1) s2
