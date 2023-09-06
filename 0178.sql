WITH s AS (SELECT score
             FROM Scores)
SELECT score, 1 + (SELECT COUNT(DISTINCT score)
                     FROM s
                    WHERE score > Scores.score) AS `rank` -- avoid name collision with rank keyword
  FROM Scores
 ORDER BY `rank`
